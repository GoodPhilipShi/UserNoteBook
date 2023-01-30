import re
import csv
import time
import json
import os
from pygtrans import Translate

client = Translate()

# 翻译次数
translateCount = 0
# 每20次翻译，暂停2秒
sleepCount = 20
sleep = 2

# 创建菜单正则
regularsForMenu = [
    'text: \"(.*?)\"', 
    'setName\(\"(.*?)\"\)',
    'setDesc\(\"(.*?)\"\)'
]

# 插件描述
valuesForManifest = [
    'description'
]
systemPath = os.path.dirname(os.path.abspath(__file__))
resourcesPath = os.path.join(systemPath, "./resources.json")
completePath = os.path.join(systemPath, "./complete.json")

def loadResourcesAndComplete():
    try:
        content = read(resourcesPath)
        ditResources = json.loads(content)
    except:
        ditResources = {}
    
    try:
        content = read(completePath)
        ditComplete = json.loads(content)
    except:
        ditComplete = {}

    saveResourcesAndComplete(
        json.dumps(ditResources, ensure_ascii=False, indent=4),
        json.dumps(ditComplete, ensure_ascii=False, indent=4)
    )

    return ditResources, ditComplete

def saveResourcesAndComplete(resContent, ComContent):
    wrtie(resourcesPath, resContent)
    wrtie(completePath, ComContent)

def read(file):
    with open(file, mode="r", encoding="utf-8") as f:
        return f.read()

def wrtie(file, content):
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(content)

def translatedMenu(content):
    global translateCount
    for regular in regularsForMenu:
        for toBeTranslated in re.findall(re.compile(regular), content):
            translateCount += 1
            # toBeTranslated = re.search(regular, txt)
            # value = toBeTranslated.group(1)
            print(f"# ====== 获取Google翻译[{regular}] ====== 开始")
            print(f"获取到值: {toBeTranslated}")
            print("正在搜索", end='')
            # result = getBaiduTranslate(value)
            # translation = translator.translate(value, dest='zh-CN')
            translation = client.translate(toBeTranslated)
            result = translation.translatedText
            print("\b"* 8 + ' ' * 8, end='\n', flush=True)
            print(f"\r翻译结果: {result}", end='\n', flush=True)
            print(f"# ====== 获取Google翻译 ====== 结束\n\n")
            # ====== 获取百度翻译 ======
            # content = re.sub(regular, value, result)
            content = content.replace(toBeTranslated, result)
            if translateCount%sleepCount == 0:
                print(f"达到{translateCount}个翻译，等待{sleep}秒")
                time.sleep(sleep)
    return content

def translatedManifest(content):
    global translateCount
    dit = json.loads(content)
    for value in valuesForManifest:
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
        if translateCount%sleepCount == 0:
            print(f"达到{translateCount}个翻译，等待{sleep}秒")
            time.sleep(sleep)
    return json.dumps(dit, ensure_ascii=False, indent=4)

def main(plugin):
    global regularsForMenu, valuesForManifest
    # 获取 complete.json 信息
    # 获取 resources.json 信息
    res, com = loadResourcesAndComplete()
    plugins = []
    # if len(res['menu']) > 0: regularsForMenu = res['menu']
    if len(res['manifest']) > 0: valuesForManifest = res['manifest']
    if com.get('plugins'): plugins = com.get('plugins')
    
    print(regularsForMenu)

    if plugin in plugins:
        print(f"已经汉化过了...")
        return

    path = os.path.join(com['pluginsPath'], plugin)

    print(f"# ====== 翻译菜单 ====== 开始")

    fileName = os.path.join(path, "main.js")
    content = read(fileName)

    print("[1] 备份文件")
    # 生成拜访名称
    backName = fileName + ".bak"
    wrtie(backName, content)

    print("[2] 开始翻译")
    content = translatedMenu(content)
    wrtie(fileName, content)

    print(f"# ====== 翻译菜单 ====== 结束\n\n")

    print(f"# ====== 翻译菜单 ====== 开始")

    fileName = os.path.join(path, "manifest.json")
    content = read(fileName)

    print("[1] 备份文件")
    # 生成拜访名称
    backName = fileName + ".bak"
    wrtie(backName, content)

    print("[2] 开始翻译")
    content = translatedManifest(content)
    wrtie(fileName, content)

    print(f"# ====== 翻译菜单 ====== 结束")

    plugins.append(plugin)
    com['plugins'] = plugins

    saveResourcesAndComplete(
        json.dumps(res, ensure_ascii=False, indent=4),
        json.dumps(com, ensure_ascii=False, indent=4)
    )
    
if __name__ == "__main__":
    main("alx-folder-note")