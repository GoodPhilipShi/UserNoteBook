import re
import csv
import time
import json
import os
from pygtrans import Translate, ApiKeyTranslate

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# # 翻译次数
# translateCount = 0
# # 每20次翻译，暂停2秒
# sleepCount = 20
# sleep = 2

systemPath = os.path.dirname(os.path.abspath(__file__))
resourcesPath = os.path.abspath(os.path.join(systemPath, "./control.yaml"))

# 配置信息
options = {
    # 是否支持相对路径
    "relative": False,
    # 是否为使用API翻译
    "translateApi": False,
    # 每翻译多少次暂停一次
    "translateNum": 0,
    # 翻译一次暂停多久
    "translateSleep": 0,
    # 翻译倾向
    "translateTo": 'zh-CN',
    "extract": {
        "menu": {
            "extractType": "",
            "expression": ""
        },
        "info": {
            "extractType": "",
            "expression": ""
        }
    }
}

translateCount = 0

def __readToContent(filePath):
    with open(filePath, mode="r", encoding="utf-8") as f:
        return f.read()

def __writeToContent(filePath, content):
    with open(filePath, mode="w", encoding="utf-8") as f:
        f.write(content)

def generateDefaultConfigurationInformation(path):
    """AI is creating summary for generateDefaultConfigurationInformation
    生成默认配置信息
    Args:
        path ([str]): 配置文件路径
    """    


    defulateConfig = "# 任务设置" + \
    "# 支持相对路径、绝对路径、插件吗名称(需要先设置Obsidian的plugins文件夹路径)" + \
    "Tasks: \n" + \
    "Setting:" + \
    "  # 路径设置" + \
    "  pluginsPath:" + \
    "    - # 支持多个路径" + \
    "  # 翻译设置" + \
    "  translate:" + \
    "    Api: # 可以不填写" + \
    "    Interval: # 每翻译多少次暂停一次" + \
    "      num: 20" + \
    "      sleep: 2 # 单位为秒" + \
    "      to: zh-CN # 更多目标语言 https://pygtrans.readthedocs.io/zh_CN/latest/langs.html\n" + \
    "extract:" + \
    "  translateManifest:" + \
    "    expression:" + \
    "      - description" + \
    "    type: json" + \
    "  translateMenu:" + \
    "    expression:" + \
    "      - \'text: \"(.*?)\"\'" + \
    "      - setName\\(\"(.*?)\"\\)" + \
    "      - setDesc\\(\"(.*?)\"\\)" + \
    "    type: regular"
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(defulateConfig)

def isPathOk(path):
    """AI is creating summary for isPathOk

    Args:
        path ([str]): 待判断的路径

    Returns:
        [bool]: 路径是否存在
    """
    return os.path.exists(path)

def loadConfigurationInformation(path):
    """AI is creating summary for loadConfigurationInformation
    加载配置信息
    Args:
        path ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(path, mode="r", encoding="utf-8") as f:
        return load(f.read(), Loader=Loader)

def checkoutConfig(config):
    global options
    
    try:
        print(f"[2][1] 正在检测Obsidian的Plugins路径")
        if type(config["Setting"]["pluginsPath"]) == str:
            if not isPathOk(config["Setting"]["pluginsPath"]):
                print("[2] Obsidian的Plugins路径不存在, 不支持相对路径")
                options["relative"] = False
            else:
                print("[2] Obsidian的Plugins路径存在, 支持相对路径")
                options["relative"] = True
                options["relativePath"] = config["Setting"]["pluginsPath"]
        elif type(config["Setting"]["pluginsPath"]) == list:
            pathLen= len(config["Setting"]["pluginsPath"])
            if pathLen == 1:
                if not isPathOk(config["Setting"]["pluginsPath"][0]):
                    print("[2] Obsidian的Plugins路径不存在, 不支持相对路径")
                    options["relative"] = False
                else:
                    print("[2] Obsidian的Plugins路径存在, 支持相对路径")
                    options["relative"] = True
                    options["relativePath"] = config["Setting"]["pluginsPath"][0]
            else:
                print("[2] Obsidian的Plugins路径为空或者多条路径, 不支持相对路径")
                options["relative"] = False
        else:
            print("[2] Obsidian的Plugins路径为空, 不支持相对路径")
            options["relative"] = False
        
        print(f"[2][2] 正在检测Obsidian的translate配置")
        if config["Setting"]["translate"]["Api"] == None or config["Setting"]["translate"]["Api"].strip() == "":
            print(f"[3] 启动免费翻译器")
            options["translateApi"] = False
        else:
            print(f"[3] 启动API翻译器")
            options["translateApi"] = config["Setting"]["translate"]["Api"].strip()
        
        if config["Setting"]["translate"]['domain'] == None or config["Setting"]["translate"]['domain'].strip() == "":
            options['translateDomain'] = 'com'
        else:
            options['translateDomain'] = config["Setting"]["translate"]['domain']

        if int(config["Setting"]["translate"]["Interval"]["num"]) != 0 and int(config["Setting"]["translate"]["Interval"]["sleep"]) != 0:
            print(f'[3] 每{config["Setting"]["translate"]["Interval"]["num"]}次暂停{config["Setting"]["translate"]["Interval"]["sleep"]}秒')
            options["translateNum"] = int(config["Setting"]["translate"]["Interval"]["num"])
            options["translateSleep"] = int(config["Setting"]["translate"]["Interval"]["sleep"])
        else:
            print(f"[3] 没有设置次数, 即无限制 [不推荐]")
            options["translateNum"] = 0
            options["translateSleep"] = 0
            
        if config["Setting"]["translate"]["Interval"]["to"]:
            print(f'[3] 翻译至 {config["Setting"]["translate"]["Interval"]["to"]}')
            options["translateTo"] = config["Setting"]["translate"]["Interval"]["to"]
        else:
            print(f"[3] 没有翻译倾向, 默认: zh-CN")
            options["translateTo"] = 'zh-CN'

        print(f"[2][3] 正在加载字符提取规则")
        if config["extract"]["translateMenu"]["type"] == "regular":
            print(f"[4] 翻译目标: 菜单 提取规则类型: 正则")
            options["extract"]["menu"]["extractType"] = "regular"
            options["extract"]["menu"]["expression"] = config["extract"]["translateMenu"]["expression"]
        elif config["extract"]["translateMenu"]["type"] == "json":
            print(f"[4] 翻译目标: 菜单 提取规则类型: JSON")
            options["extract"]["menu"]["extractType"] = "json"
            options["extract"]["menu"]["expression"] = config["extract"]["translateMenu"]["expression"]
        else:
            print(f'[4] 翻译目标: 菜单 提取规则类型: {config["extract"]["translateMenu"]["type"]} 暂不支持')
            return False
        
        if config["extract"]["translateManifest"]["type"] == "regular":
            print(f"[4] 翻译目标: 插件信息 提取规则类型: 正则")
            options["extract"]["info"]["extractType"] = "regular"
            options["extract"]["info"]["expression"] = config["extract"]["translateManifest"]["expression"]
        elif config["extract"]["translateManifest"]["type"] == "json":
            print(f"[4] 翻译目标: 插件信息 提取规则类型: JSON")
            options["extract"]["info"]["extractType"] = "json"
            options["extract"]["info"]["expression"] = config["extract"]["translateManifest"]["expression"]
        else:
            print(f'[4] 翻译目标: 插件信息 提取规则类型: {options["extract"]["translateManifest"]["type"]} 暂不支持')
            return False
        
        return True
    except BaseException as err:
        print(f"[2] ---------- 配置存在异常 ----------\n异常原因:{err}")
        return False

def createTranslationClient():
    """AI is creating summary for createTranslationClient
    创建翻译客户端
    """    
    global client
    if(options['translateApi']):
        client = ApiKeyTranslate(target=options['translateTo'], api_key=options['translateApi'])
    else:
        client = Translate(target=options['translateTo'], domain=options['translateDomain'])

def translation(tasks, mold, remarks=None):
    global translateCount
    if mold == "menu":
        file = "main.js"
    elif mold == "json":
        file = "manifest.json"
    else:
        return

    if options["extract"][mold]["extractType"] == "regular":
        print(f"[{remarks}][1] 创建正则对象")
        regObjs = options["extract"][mold]["expression"]

        if type(tasks) == list:
            for task in tasks:
                if isPathOk(task):
                    path = task
                elif options["relative"] and isPathOk(os.path.join(options["relativePath"], task)):
                    path = os.path.join(options["relativePath"], task)
                
                fileName = os.path.join(path, file)
                content = __readToContent(fileName)
                __writeToContent(f"{fileName}.bak", content)
                print(f"[{remarks}][2] 翻译运行中")
                translateCount = 0
                result = translateForRegular(regObjs, content)
                __writeToContent(fileName, result)

        else:
            if isPathOk(tasks):
                path = tasks
            elif options["relative"] and isPathOk(os.path.join(options["relativePath"], tasks)):
                path = os.path.join(options["relativePath"], task)

            fileName = os.path.join(path, file)
            content = __readToContent(fileName)
            __writeToContent(f"{fileName}.bak", content)
            print(f"[{remarks}][2] 翻译运行中")
            translateCount = 0
            result = translateForRegular(regObjs, content)
            __writeToContent(fileName, result)

    elif options["extract"][mold]["extractType"] == "json":
        print(f"[{remarks}][1] 创建JSONPath")
        jsonPaths = options["extract"][mold]["expression"]

        if type(tasks) == list:
            for task in tasks:
                if isPathOk(task):
                    path = task
                elif options["relative"] and isPathOk(os.path.join(options["relativePath"], task)):
                    path = os.path.join(options["relativePath"], task)
                
                fileName = os.path.join(path, file)
                content = __readToContent(fileName)
                __writeToContent(f"{fileName}.bak", content)
                print(f"[{remarks}][2] 翻译运行中")
                translateCount = 0
                result = translateForJson(jsonPaths, content)
                __writeToContent(fileName, result)
        else:
            if isPathOk(tasks):
                path = task
                content = __readToContent(tasks)
            elif options["relative"] and isPathOk(os.path.join(options["relativePath"], tasks)):
                path = os.path.join(options["relativePath"], task)
                content = __readToContent(os.path.join(options["relativePath"], tasks))

            fileName = os.path.join(path, file)
            content = __readToContent(fileName)
            __writeToContent(f"{fileName}.bak", content)
            print(f"[{remarks}][2] 翻译运行中")
            translateCount = 0
            result = translateForJson(jsonPaths, content)
            __writeToContent(fileName, result)

    else:
        print(f'[{remarks}][1] 异常类型 {options["extract"][mold]["extractType"]} 跳过')

def translateForRegular(regObjs:list, toBeTranslatedForText):
    global translateCount
    content = toBeTranslatedForText
    print(regObjs)
    for regular in regObjs:
        regularObj = re.compile(regular)
        for toBeTranslatedIterator in regularObj.finditer(toBeTranslatedForText):
            translateCount += 1
            toBeTranslated = toBeTranslatedIterator.group()
            print(f"# ====== 获取Google翻译[{regular}] ====== 开始")
            print(f"获取到值: {toBeTranslated}")
            print("正在搜索", end='')
            translation = client.translate(toBeTranslated)
            print("-->", translation)
            if translation == "Null":
                print("翻译失败")
            else:
                result = translation.translatedText
                print("\b"* 8 + ' ' * 8, end='\n', flush=True)
                print(f"\r翻译结果: {result}", end='\n', flush=True)
                print(f"# ====== 获取Google翻译 ====== 结束\n\n")
                origin = re.sub("(\(.*\))", toBeTranslated, regular)
                result = re.sub("(\(.*\))", result, regular)
                content = re.sub(origin, result, content)

                if translateCount%options["translateNum"] == 0:
                    print(f'达到{translateCount}个翻译，等待{options["translateSleep"]}秒')
                    time.sleep(options["translateSleep"])

    return content

def translateForJson(jsonPaths:list, toBeTranslatedForJson):
    global translateCount
    dit = json.loads(toBeTranslatedForJson)
    for value in jsonPaths:
        translateCount += 1
        toBeTranslated = dit.get(value)
        print(f"# ====== 获取Google翻译 ====== 开始")
        print(f"获取到值: {toBeTranslated}")
        print("正在搜索", end='')
        translation = client.translate(toBeTranslated)
        result = translation.translatedText
        print("\b"* 8 + ' ' * 8, end='\n', flush=True)
        print(f"\r翻译结果: {result}", end='\n', flush=True)
        print(f"# ====== 获取Google翻译 ====== 结束\n\n")
        dit[value] = result
        if translateCount%options["translateNum"] == 0:
            print(f'达到{translateCount}个翻译，等待{options["translateSleep"]}秒')
            time.sleep(options["translateSleep"])
    return json.dumps(dit, ensure_ascii=False, indent=4)

def main():
    # [1] 加载配置项
    print(f"[1] 加载配置项: {resourcesPath}")
    if not isPathOk(resourcesPath):
        print(f"[ERROR] 配置文件不存在...开始生成")
        generateDefaultConfigurationInformation(resourcesPath)
        exit()
    config = loadConfigurationInformation(resourcesPath)
    tasks = config["Tasks"]
    print(f"[2] 检测配置项的有效项")
    if not checkoutConfig(config):
        print(f"[ERROR] 配置文件异常...开始生成")
        generateDefaultConfigurationInformation(resourcesPath)
        exit()
    print(f"[3] 创建翻译客户端")
    createTranslationClient()
    print(f"[4] 开始翻译菜单")
    translation(tasks, "menu", 4)

    print(f"[5] 开始翻译插件信息")
    translation(tasks, "info", 5)

if __name__ == "__main__":
    main()