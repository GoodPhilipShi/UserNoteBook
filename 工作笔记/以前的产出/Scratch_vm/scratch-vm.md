# Scratch-VM

## 了解积木

### 积木类型

> 当前为 scratch-vm 原生积木类型

| 类型        | 描述                                 | 示意图(以`Mind+`为主)                                        |
| ----------- | ------------------------------------ | ------------------------------------------------------------ |
| BOOLEAN     | 六边形、布尔类型                     | ![image-20210709083042437](工作笔记/以前的产出/Scratch_vm/images/image-20210709083042437.png) |
| BUTTON      | 用于某些特殊操作的按钮(不是实际积木) | ![image-20210709083134734](工作笔记/以前的产出/Scratch_vm/images/image-20210709083134734.png) |
| COMMAND     | 命令方块                             | ![image-20210709083255517](工作笔记/以前的产出/Scratch_vm/images/image-20210709083255517.png) |
| CONDITIONAL |                                      |                                                              |
| EVENT       | 帽子形状                             | ![image-20210709091935999](工作笔记/以前的产出/Scratch_vm/images/image-20210709091935999.png) |
| HAT         | 帽子形状                             | ![image-20210709091057981](工作笔记/以前的产出/Scratch_vm/images/image-20210709091057981.png) |
| LOOP        |                                      | ![image-20210709091122686](工作笔记/以前的产出/Scratch_vm/images/image-20210709091122686.png) |
| REPORTER    | 椭圆形状                             | ![image-20210709091134215](工作笔记/以前的产出/Scratch_vm/images/image-20210709091134215.png) |

> Mind+ 新加的积木类型

| 类型    | 描述 | 示意图(以`Mind+`为主) |
| ------- | ---- | --------------------- |
| SPECIAL |      |                       |
| TEXT    |      |                       |

### 数据类型

> 当前为 scratch-vm 原生数据类型

| 类型    | 描述         | 示意图(以`Mind+`为主)                                        |
| ------- | ------------ | ------------------------------------------------------------ |
| ANGLE   | 角度选择器   | ![image-20210709113018231](工作笔记/以前的产出/Scratch_vm/images/image-20210709113018231.png) |
| BOOLEAN | 布尔选择器   | ![image-20210709093148154](工作笔记/以前的产出/Scratch_vm/images/image-20210709093148154.png) |
| COLOR   | 颜色选择器   |                                                              |
| NUMBER  | 数值选择器   | ![image-20210709092842990](工作笔记/以前的产出/Scratch_vm/images/image-20210709092842990.png) |
| STRING  | 字符串选择器 | ![image-20210709093014364](工作笔记/以前的产出/Scratch_vm/images/image-20210709093014364.png) |
| MATRIX  | 矩阵选择器   | ![image-20210712112753950](工作笔记/以前的产出/Scratch_vm/images/image-20210712112753950.png) |
| NOTE    | 音符选择器   | ![image-20210712103921201](工作笔记/以前的产出/Scratch_vm/images/image-20210712103921201.png) |
| IMAGE   | 内嵌图像     |                                                              |

> Mind+ 新加的数据类型

| 类型                   | 描述 | 示意图(以`Mind+`为主)                                        |
| ---------------------- | ---- | ------------------------------------------------------------ |
| COLORPICKER            |      | ![image-20210712092710058](工作笔记/以前的产出/Scratch_vm/images/image-20210712092710058.png) |
| COLORPALETTE           |      | ![image-20210712092747193](工作笔记/以前的产出/Scratch_vm/images/image-20210712092747193.png) |
| SHOWLIGHTS             |      |                                                              |
| RANGE                  |      | ![image-20210712092849465](工作笔记/以前的产出/Scratch_vm/images/image-20210712092849465.png) |
| INFRAREDTEXT           |      | ![image-20210712093013573](工作笔记/以前的产出/Scratch_vm/images/image-20210712093013573.png) |
| OBLOQPARAMETER         |      | ![image-20210712093217285](工作笔记/以前的产出/Scratch_vm/images/image-20210712093217285.png) |
| MQTTPARAMETER          |      | ![image-20210712093405461](工作笔记/以前的产出/Scratch_vm/images/image-20210712093405461.png) |
| OBLOQHTTPPARAMETER     |      | ![image-20210712093540531](工作笔记/以前的产出/Scratch_vm/images/image-20210712093540531.png) |
| SETTINGS               |      | ![image-20210712093921829](工作笔记/以前的产出/Scratch_vm/images/image-20210712093921829.png)<br/>模块的示意图并不固定, 通过配置进行生成 |
| TINYDBPARAMETER        |      | ![image-20210712094616341](工作笔记/以前的产出/Scratch_vm/images/image-20210712094616341.png) |
| ESP32IMGSETTING        |      | ![image-20210712100059778](工作笔记/以前的产出/Scratch_vm/images/image-20210712100059778.png) |
| MPYSHOWIMG             |      | ![image-20210712100951217](工作笔记/以前的产出/Scratch_vm/images/image-20210712100951217.png) |
| OLED2864IMGSETTING     |      | ![image-20210712102032868](工作笔记/以前的产出/Scratch_vm/images/image-20210712102032868.png) |
| ESP32TEXTPREVIEW       |      | ![image-20210712102358995](工作笔记/以前的产出/Scratch_vm/images/image-20210712102358995.png) |
| OLED2864TEXTPREVIEW    |      | ![image-20210712102615617](工作笔记/以前的产出/Scratch_vm/images/image-20210712102615617.png) |
| PIANO                  |      | ![image-20210712103004656](工作笔记/以前的产出/Scratch_vm/images/image-20210712103004656.png) |
| STMOTORAXIS            |      | ![image-20210712104646932](工作笔记/以前的产出/Scratch_vm/images/image-20210712104646932.png) |
| PICTUREAIUSERCONFIG    |      | ![image-20210712111249503](工作笔记/以前的产出/Scratch_vm/images/image-20210712111249503.png) |
| PICTUREAIIMAGESETTING  |      | ![image-20210712111337873](工作笔记/以前的产出/Scratch_vm/images/image-20210712111337873.png) |
| PICTUREAIDIRSETTING    |      | ![image-20210712111410958](工作笔记/以前的产出/Scratch_vm/images/image-20210712111410958.png) |
| PICTUREAIWEBIMGSETTING |      | ![image-20210712111439853](工作笔记/以前的产出/Scratch_vm/images/image-20210712111439853.png) |
| CAMERALIST             |      | ![image-20210712111536893](工作笔记/以前的产出/Scratch_vm/images/image-20210712111536893.png) |
| TELLOGROUPLIST         |      | ![image-20210712112101599](工作笔记/以前的产出/Scratch_vm/images/image-20210712112101599.png) |
| MATRIXICONS            |      | ![image-20210709133844942](工作笔记/以前的产出/Scratch_vm/images/image-20210709133844942.png) |
| CITYMENU               |      | ![image-20210712113338894](工作笔记/以前的产出/Scratch_vm/images/image-20210712113338894.png) |
| CONTENTINPUT           |      | ![image-20210712113019246](工作笔记/以前的产出/Scratch_vm/images/image-20210712113019246.png) |
| NUMBERDROPDOWN         |      | ![image-20210712114007246](工作笔记/以前的产出/Scratch_vm/images/image-20210712114007246.png)<br/>左 |
| TEXTDROPDOWN           |      | ![image-20210712114007246](工作笔记/以前的产出/Scratch_vm/images/image-20210712114007246.png)<br/>右 |

## 创建模块

### 添加模块: 创建模块文件

> 文件命名规则如下:
>
> 1. 文件名称不限，只要文件名称符合Windows要求即可
> 2. 为了保证后期阅读、理解性, 文件名应当保持为scratch3_xx

> 在`src\blocks\`创建js文件, 文件名称: scratch3_Text
>
> > src\blocks\scratch3_Text.js

### 添加模块: 导入模块必备文件

> 1. `const BlockType = require("../extension-support/block-type");`
> 2. `const ArgumentType = require("../extension-support/argument-type");`
> 3. 其余的视情况而定

### 添加模块: 创建Class类

> 名称应当保持为Scratch3xx

```javascript
const ArgumentType = require("../../extension-support/argument-type");
const BlockType = require("../../extension-support/block-type");

class Scratch3Text {
    constructor(runtime) {
        this.runtime = runtime;
    }
    static get EXTENSION_ID() {
        return "Text";
    }
    getInfo() {
        return {
            id: Scratch3Text.EXTENSION_ID,
            name: "测试专用",
            blockIconURI: xx,
            menuIconURI: xx,
            blocks: [
               …………
            ]
        }
    }
}
```

#### 添加模块: 添加模块

```javascript
{
    opcode: "text_add",
    text: formatMessage({
        id: '独立、唯一的ID,方便添加翻译',
        defaultMessage: 'Some Blocks',
        description: '测试加法[A] + [B]'
    }),
    arguments: {
        A: {
            type: ArgumentType.NUMBER,
            defaultValue: 800,
        },
        B: {
            type: ArgumentType.NUMBER,
            defaultValue: 800,
        },
    },
}
```

```javascript
text_add(){
  	// 实时模式的话, 就需要写逻辑
  	// 其余模式, 直接留空或者return
		return
}
```

### 添加模块: 暴露接口

> 这一步很重要

```
module.exports = Scratch3Text;
```

---

### 模块文件基本完成

```javascript
const ArgumentType = require("../../extension-support/argument-type");
const BlockType = require("../../extension-support/block-type");

const formatMessage = require("format-message");

class Scratch3Text {
    constructor(runtime) {
        this.runtime = runtime;
    }
    static get EXTENSION_ID() {
        // 模块文件的ID
        return "text";
    }
    getInfo() {
        return {
            id: Scratch3Text.EXTENSION_ID,
            name: formatMessage({
                id: '独立、唯一的ID,方便添加翻译',
                defaultMessage: 'Some Blocks',
                description: '测试专用'
            }),
            blockIconURI: xx,
            menuIconURI: xx,
            blocks: [
                {
                    opcode: "text_add",
                    text: formatMessage({
                        id: '独立、唯一的ID,方便添加翻译',
                        defaultMessage: 'Some Blocks',
                        description: '测试加法[A] + [B]'
                    }),
                    arguments: {
                        A: {
                            type: ArgumentType.NUMBER,
                            defaultValue: 800,
                        },
                        B: {
                            type: ArgumentType.NUMBER,
                            defaultValue: 800,
                        },
                    },
                },
            ],
        };
    }
    text_add() {
        return;
    }
}
module.exports = Scratch3Text;
```

### 将模块添加至`extension-manager`

> 文件路径: src\extension-support\extension-manager.js

```javascript
const builtinExtensions = {
		// 模块文件的ID: () => require("../blocks/scratch3_xx")
  	text: () => require("../blocks/scratch3_Text"),
}
```

> 到了这里, 在Scratch-vm的添加已经完成.
> 而在Mind+(Scratch-gui)中则这只是第一步
>
> 这里需要记住 `模块文件的ID`
> Mind+的`src\lib\libraries\`目录下的`index.js`中添加下述代码

```javascript
import textIconURL from "";

export default [
    {
        name: (
            <FormattedMessage
                defaultMessage="text"
                description="Name for the 'text' extension"
                id="gui.extension.text.name"
            />
        ),
        extensionURL: 'text',// 将 模块文件的ID 填写至此
        iconURL: textIconURL,
        description: (
            <FormattedMessage
                defaultMessage="Play instruments and drums."
                description="Description for the 'text' extension"
                id="gui.extension.text.description"
            />
        ),
        featured: true,
      	// 再根据配置, 添加如下类似的代码:
      	// vortex: {
        //     javascript: false,
        //     cpp: false,
        //     micropython: false
        // },
    },
]
```

> PS. 另外还要记得添加翻译

![image-20210712140805546](工作笔记/以前的产出/Scratch_vm/images/image-20210712140805546.png)

## [Scratch-VM]生成模块(添加文件->显示至GUI上)的逻辑

![加载扩展-基本流程](工作笔记/以前的产出/Scratch_vm/images/加载扩展.png)

### [Scratch-GUI]XML重新渲染

![](工作笔记/以前的产出/Scratch_vm/images/gui-vm-入口.png)



### [Scratch-VM]loadExtensionURL

![](工作笔记/以前的产出/Scratch_vm/images/vm-loadExtensionURL.png)
