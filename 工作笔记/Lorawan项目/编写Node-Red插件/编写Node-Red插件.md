官网: [Node-RED](https://nodered.org/)

# 安装 Node-Red

## 本地安装 Node-Red

> [!tip] linux

```shell
sudo npm install -g --unsafe-perm node-red
```
> [!tip] windows

[Running on Windows : Node-RED](https://nodered.org/docs/getting-started/windows)
```shell
npm install -g node-red
```
> [!tip] 安装 Node. js Windows 构建工具 (写插件时必须的？应该吧)
>
> > Node-RED 或已安装节点使用的许多 Node.js 模块都有二进制组件，这些组件在 Windows 上工作之前需要编译。要使 npm 能够在 Windows 平台上编译二进制文件

```shell
npm install --global --production windows-build-tools
```
## 运行 Node-Red

```shell
node-red
```

## 安装参考插件 -node-red-node-serialport

![[Pasted image 20221115152926.png]]

![[Pasted image 20221115153021.png]]

![[Pasted image 20221115153043.png]]

> [!tip] 新增的节点在”网络“分类下

![[Pasted image 20221115153153.png]]

> [!tip] 插件存放路径
> C:\Users\<用户名>\.node-red\node_modules\node-red-node-serialport

![[Pasted image 20221115153341.png]]

# Node-Red 插件

> [!tip] 学习地址: [Creating Nodes : Node-RED](https://nodered.org/docs/creating-nodes/)

## package.json

在常规 `package.json` 文件中，自行添加 `node-red`

```json
{
	name: ""
	....
	"node-red": {
		"nodes": {
			// 运行时模块包含哪些节点文件
			"lower-case": "lower-case.js"
		}
	}
}
```

## 节点.js

> [!note]
> 1. 启动时、加载节点时，运行这个函数方法
> 2. 最外层只存在一个输入参数 `RED`
> 3. 如果需要调用 node 库，记得要在 `package,json` 的 `dependencies` 里面添加上去
>
> > 使用 `yarn add` 或者 `npm i -s` 就可以自动添加上去

```javascript
module.exports = function(RED) {
	// LowerCaseNode --> 节点构造函数
    function LowerCaseNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            msg.payload = msg.payload.toLowerCase();
            node.send(msg);
        });
    }
    // 将上面的函数 LowerCaseNode 绑定到 lower-case(这是一个KEY),
    RED.nodes.registerType("lower-case",LowerCaseNode);
}
```

### 节点构造函数

这个函数，第一步就是调用函数来初始化

```javascript
RED.nodes.createNode(this,config)
```

```javascript
function LowerCaseNode(config) {
    RED.nodes.createNode(this,config);
    var node = this;
    // 上面的就是默认操作，获取
    node.on('input', function(msg) {
        msg.payload = msg.payload.toLowerCase();
        node.send(msg);
    });
}
```

#### 接收消息

> [!tip] 监听 `input` 事件

|  |参数|描述|描述|
|----| ---- | ------------------------ | ---------------------------------------------------------------------------------- |
|  |msg|接收到的消息|  |
|  |send| 用于发送消息的函数       |  |
|  | done | 函数，程序运行结束的函数 |程序完成时，要记得调用 `done()`，这样的话就可以在早期版本的 Node-Red（<1.0）中使用|

```javascript
this.on('input', function(msg, send, done){
	//此调用被包装在“done”存在的检查中
	if(done) done()
})
```

##### 处理错误信息

```javascript
this.on('input', function(msg, send, done) {
	// err 代指错误信息
    if (err) {
        if (done) {
	        // 在Node-RED 1.0及以上版本，要这样用
            done(err);
        } else {
            // 在以前的版本中，要这样用
            node.error(err, msg);
        }
    }
});
```

#### 发送消息

> [!tip] 兼容 Node-Red 0. x 版本

```javascript
send = send || function() { node.send.apply(node,arguments) }
```

>[!note]
> 发送的内容格式为 `{payload: "hi"}`
> 如果发送的内容为 null，则 `send(msg)` 不会发送任何消息

```javascript
this.on('input', function(msg, send, done) {
    send = send || function() { node.send.apply(node,arguments) }

    msg.payload = "hi";
    send(msg);

    if (done) {
        done();
    }
});
```

##### 多输出和多信息

```javascript
this.send([ msg1 , msg2 ])
this.send([ [msgA1 , msgA2 , msgA3] , msg2 ]);
```

#### 关闭事件监听

```javascript
this.on('close', function() {
    // tidy up any state
});
```

> [!note] 
> 如果关闭时，需要异步工作来完成整理，那么就要这样写
> 
> `doSomethingWithACallback` 就是你要处理的事，然后记得添加回调参数
> 
> `doSomethingWithACallback` 只是一个代指

```javascript
this.on('close', function(done) {
    doSomethingWithACallback(function() {
        done();
    });
});
```

> [!note]
> 如果是在 Node-Red 0.17 版本上运行的话
> 
> `removed` 接收节点是否因已删除而关闭，或者只是重新启动，如果没有被禁用的话
> 
> `done`
>
> > 在 Node-Red 0.17 之前，如果不调用，就会一直卡在这里
> > 
> > 之后的版本，如果不调用，等待 15 秒，就会触发超时错误，程序继续运行

```javascript
this.on('close', function(removed, done) {
    if (removed) {
        // This node has been disabled/deleted
    } else {
        // This node is being restarted
    }
    done();
});
```

### 打印日志函数

```javascript
this.log("Something happened");
this.warn("Something happened you should know about");
this.error("Oh no, something bad happened");

// Node-RED 0.17 之后添加的打印日志函数
this.trace("Log some internal detail not needed for normal operation");
this.debug("Log something more details for debugging the node's behaviour");
```

### 设置节点状态

> [Node status : Node-RED](https://nodered.org/docs/creating-nodes/status)

```javascript
this.status({fill:"red",shape:"ring",text:"disconnected"});
```

### 定义配置节点

[[#配置节点(全解)]]

## 节点.html

```
<script type="text/javascript">
    RED.nodes.registerType('lower-case',{
        category: 'function',
        color: '#a6bbcf',
        defaults: {
            name: {value:""}
        },
        inputs:1,
        outputs:1,
        icon: "file.png",
        label: function() {
            return this.name||"lower-case";
        }
    });
</script>

<script type="text/html" data-template-name="lower-case">
    <div class="form-row">
        <label for="node-input-name"><i class="fa fa-tag"></i> Name</label>
        <input type="text" id="node-input-name" placeholder="Name">
    </div>
</script>

<script type="text/html" data-help-name="lower-case">
    <p>A simple node that converts the message payloads into all lower-case characters</p>
</script>
```

> [!note]
>节点的 HTML 文件提供以下内容:
>- 定义节点
>- 编辑模板
>- 帮助文本
>
> > 注意: 以上三个部分都需要包裹在 `<script>`

### 定义节点

使用 `RED.nodes.registerType` 继续注册节点类型以及定义

> 如果不定义，则会使用默认配置信息

```
<script type="text/javascript">
    RED.nodes.registerType(类型,{定义});
</script>
```

#### 节点定义

[节点定义](https://nodered.org/docs/creating-nodes/node-html#node-definition)

节点定义包含有关 编辑 器。它是具有以下属性的对象：

| 节点定义 KEY | 类型         | 描述                                                                                                                |
| ----------- | ------------ | ------------------------------------------------------------------------------------------------------------------- |
| category    | 字符串       | 节点所在的类别                                                                                                |
| defaults    | 对象         | 默认值, 保存值, [节点属性](https://nodered.org/docs/creating-nodes/properties), 相关绑定 node-input-\<propertyname> |
| credentials | 对象         | defaults 类似, 不过限制类型 [节点凭据](https://nodered.org/docs/creating-nodes/credentials)                         |
| inputs      | 数字         | 是否输入 (0/1)                                                                                                       |
| outputs     | 数字         | 是否输出、输出条目 (0/1,2,3...)                                                                                      |
| color       | 字符串       | hex 值，[背景颜色](https://nodered.org/docs/creating-nodes/appearance#background-colour)                             |
| label       | 字符串\|函数 | 要在工作区中使用的 [标签](https://nodered.org/docs/creating-nodes/appearance#label)。                                |
| icon        | 字符串       | [图标](https://nodered.org/docs/creating-nodes/appearance#icon)                                                     |
| align       | 字符串       | 图标和标签的 [对齐方式](https://nodered.org/docs/creating-nodes/appearance#alignment)                                |

> [!tip]
只列出了部分

### 编辑模板

```
<script type="text/html" data-template-name="node-type">
    <div class="form-row">
        <label for="node-input-name"><i class="fa fa-tag"></i> Name</label>
        <input type="text" id="node-input-name" placeholder="Name">
    </div>
    <div class="form-tips"><b>Tip:</b> This is here to help.</div>
</script>
```

> [!note] 注意事项
> 1. 必须包裹在<script></script>里面
> 2. \<script>必须存在 `type` 和 `data-template-name` 这两个属性

> [!tip]
> 编辑对话框通常由一系列的行组成
> 每行包含其他属性的标签和输入

```
<div class="form-row">
    <label for="node-input-name"><i class="fa fa-tag"></i> Name</label>
    <input type="text" id="node-input-name" placeholder="Name">
</div>
```

> [!note]
> - 通过 `form-row` 来规定行
> - 行里面包括<input\/>(值)、<label\/>(标签)
> 	- 在其中可以使用<i\/> +`Font Awesome Icons` 实现图标显示功能 or 内置 ICON or 节点文件夹中的图片
> - 其中 id\for 必须统一，并且值的只能是 `node-input-<propertyname>`(节点)、`node-config-input-<property-name>`([[#定义配置节点]])
> - 值可以是 <input\/>、<select\/>
> 	- <input\/> 可以是 字符串 (text)、数字 (number)、布尔值 (checkbox)
> 	- <select\/>

#### Node-Red 提供的标准的 UI 小部件

##### 按钮

[按钮](https://nodered.org/docs/creating-nodes/edit-dialog#buttons)

##### 输入框

> [!tip]
> 可以使用常规的<input\/>
> 也可以使用 `TypedInput` 参数实现更多样化的<input\/>

[输入](https://nodered.org/docs/creating-nodes/edit-dialog#inputs)

##### 多行文本编辑器

使用方法也很简单

> [!tip]
> 1. 创建占位符 (?)
> 	1. class 必须是 `node-text-editor`
> 	2. 需要设置高度 height
> 	~~~html
> 	<div style="height: 250px; min-height:150px;" class="node-text-editor" id="node-input-example-editor"></div>
> 	~~~
> 2. 在节点. js 里面需要使用函数进行初始化 `RED.editor.createEditor`

```javascript
this.editor = RED.editor.createEditor({
   id: 'node-input-example-editor',
   mode: 'ace/mode/text',
   value: this.exampleText
});
```

> [!tip]
> 并且还需要添加
>  
>  `oneditsave` 获取值
>  
>  `oneditcancel` 确保编辑器已被删除

```javascript
oneditsave: function() {
    this.exampleText = this.editor.getValue();
    this.editor.destroy();
    delete this.editor;
},
oneditcancel: function() {
    this.editor.destroy();
    delete this.editor;
},
```

> [!TiP] 我估计是放在这里

```javascript
   onxxx: function() {
      this.editor = RED.editor.createEditor({
	   id: 'node-input-example-editor',
	   mode: 'ace/mode/text',
	   value: this.exampleText,
	  })
   },
   oneditsave: function() {
     this.exampleText = this.editor.getValue();
     this.editor.destroy();
     delete this.editor;
   },
   oneditcancel: function() {
       this.editor.destroy();
       delete this.editor;
   },
});
```

### 帮助文本

```javascript
<script type="text/html" data-help-name="node-type">
   <p>Some useful help text to introduce the node.</p>
   <h3>Outputs</h3>
       <dl class="message-properties">
       <dt>payload
           <span class="property-type">string | buffer</span>
       </dt>
   <h3>Details</h3>
   <p>Some more information about the node.</p>
</script>
```

>[!TIP] [[#帮助样式指南(全解)]]

## 在 Node-RED 中测试您的节点

要在本地测试节点模块，可以使用 `npm install <folder>` 命令。这允许在本地目录中开发节点，并且在开发过程中将其链接到本地 Node-red 安装目录中

在 Mac OS 或 Linux 上，如果您的节点位于 `~/dev/node-red-contrib-example-lower-case`

```shell
cd ~/.node-red
npm install ~/dev/node-red-contrib-example-lower-case
```

在 Windows 上，您可以执行以下操作

```shell
cd C:\Users\my_name\.node_red
npm install C:\Users\my_name\Documents\GitHub\node-red-contrib-example-lower-case
```

>[!TIP] 记得重启启动 node-red

### 单元测试 (未能明白)

Node-Red 提供了 `node-red-node-test-helper` 插件用于单元测试

> [!note]
> 1. 在节点文件夹中添加一个 test 文件夹
> 2. 并在 test 文件夹中创建 节点名称 _spec.js

> [!tip] test/lower-case_spec.js

```javascript
var helper = require("node-red-node-test-helper");
var lowerNode = require("../lower-case.js");

describe('lower-case Node', function () {

  afterEach(function () {
    helper.unload();
  });

  it('should be loaded', function (done) {
    var flow = [{ id: "n1", type: "lower-case", name: "test name" }];
    helper.load(lowerNode, flow, function () {
      var n1 = helper.getNode("n1");
      n1.should.have.property('name', 'test name');
      done();
    });
  });

  it('should make payload lower case', function (done) {
    var flow = [{ id: "n1", type: "lower-case", name: "test name",wires:[["n2"]] },
    { id: "n2", type: "helper" }];
    helper.load(lowerNode, flow, function () {
      var n2 = helper.getNode("n2");
      var n1 = helper.getNode("n1");
      n2.on("input", function (msg) {
        msg.should.have.property('payload', 'uppercase');
        done();
      });
      n1.receive({ payload: "UpperCase" });
    });
  });
});
```

## 【todo】存储上下文

## 节点状态 (全解)

> [!TIP] 在 [[#设置节点状态|节点.js\设置节点状态]] 中有简单的了解

[节点状态](https://nodered.org/docs/creating-nodes/status)

## 配置节点 (全解)

>[!TIP] 在 [[#定义配置节点|节点.js\定义配置节点]] 中有简单的了解

[定义配置节点](https://nodered.org/docs/creating-nodes/config-nodes)

## 帮助样式指南 (全解)

>[!tip] 在 [[#帮助文本|节点.html\帮助文本]] 中有简单的了解

[帮助样式指南](https://nodered.org/docs/creating-nodes/help-style-guide)