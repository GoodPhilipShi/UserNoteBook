## modbus 通用接收 xx/up 修改

屏蔽上次的收到的数据继续转base64

即恢复成收到啥就转发啥

## modbus 通用发送 xx/down 修改

1. cmd~~`去`0x`~~, 并且base64转换

   ```js
   btoa(n.content)
   
   btoa(!!n.contentIsHex ? n.content.split(" ").map((v)=>hex2int(v)) : n.content.split(""))
   ```
   
> [!tip]
> 不太符合要求
   
   ```nodejs
   const hex2int = (hex) =>  {
       var len = hex.length, a = new Array(len), code;
       for (var i = 0; i < len; i++) {
           code = hex.charCodeAt(i);
           if (48<=code && code < 58) {
               code -= 48;
           } else {
               code = (code & 0xdf) - 65 + 10;
           }
           a[i] = code;
       }
       
       return a.reduce(function(acc, c) {
           acc = 16 * acc + c;
           return acc;
       }, 0);
   }
   
   // hex发送 n.content.split(" ").map((v)=>hex2int(v))
   // 文本发送 n.content.split("")
   let buffer = Buffer.from(!!n.contentIsHex ? n.content.split(" ").map((v)=>hex2int(v)) : n.content.split(""))
   ```

2. `size`默认值对应的大小为8字节

   ```js
   !!n.contentIsHex ? n.content.split(" ").length : n.content.replace(/[^u0000-u00ff]/g,"aa").length,
   ```

   ```nodejs
   buffer.length
   ```
   

## modbus 通用发送 xx/down UI修改

1. 在数据一栏添加勾选框`hex发送`

    ~~选择`hex`就可以不用填写`0x`~~

![[Pasted image 20221221130459.png]]

勾选之后(hex发送)，采用正则判断，不同填写`0x`

不勾选(文本发送)

```diff
- content: { value: "11 22 33 44 55 66"},
+ content: { value: "11 22 33 44 55 66", validate: function(v){
+     if(!!this.contentIsHex){
+         return /^((?=\w)[^_]{2} )*(?=\w)[^_]{2}$/.test(v)
+     }
+     return true
+ }},
+ // 这个是选择框的值 初始化
+ contentIsHex: { value: "1" },
+ // 数据的长度 初始化
+ contentLen: {value:""}
```

```diff
  <div class="form-row">
      <label for="node-input-content" ><i class="fa fa-globe"></i> 数据</label>
      <input type="text" id="node-input-content">
+    <input title="HEX发送" type="checkbox" id="node-input-content-checkout" style="position: absolute;width: 16px;margin: 10px 2px;" />
  </div>
```

```js
oneditprepare: {
    this.conetentIsHexElement = document.querySelector("#node-input-content-checkout")
    if (this.contentIsHex) this.conetentIsHexElement.checked = !!this.contentIsHex
}
```

> [!tip]
> 赋予保存选择框的值 `this.contentIsHex`


```js
oneditsave: function () {
   this.contentIsHex = (this.conetentIsHexElement.checked ? 1 : 0).toString()
},
```

> [!warning]
> 如果不符合规则，输入框显示为红色，但是可以保存，保存也生效(错误值也能够保存成功)，但是在部署的时候显示下面的内容

![[Pasted image 20221221132117.png]]

![[Pasted image 20221221132209.png]]

![[Pasted image 20221221131929.png]]

### HEX发送计算个数

```
n.content.split(" ").length
```

### 文本发送计算字节长度

> [!tip]
> 一个英文一字节，一个中文两字节

```
n.content.replace(/[^u0000-u00ff]/g,"aa").length
```

## 烟雾计

能收到数据格式(?)，但是提取有问题

> [!tip]
> 可能是数据格式问题

> 以上废弃

> [!info] 修改内置数据处理脚本

> [!tip] 烟雾计数据处理脚本

```js
function Decode(data) {
    let obj = JSON.parse(data)
    var b = Buffer.from(obj.data, 'base64')
    var s = b.toString('hex');
    return parseInt(s, 16)
}
```

![[msedge_k8Skv7RhbU.png]]

> [!tip] pt100 数据处理脚本


```js
function Decode(data) {
    let obj = JSON.parse(data)
    var b = Buffer.from(obj.data, 'base64')
    var s = b.toString('hex');
    return parseInt(s, 16) / 100.0
}
```

![[Pasted image 20221222100245.png]]

## 单继电路、通用发送(Lorawan)

> [!tip] - [x]  格式待探讨


自己提取图片中的显示为

```json
{
	"applicatrionID": "",
	"devEUI": "",
	"confirmed": "",
	"fPort": "",
	"data": "",// 记得base64编码
	"object": null // 这个是啥？
}
```

采用与[modbus 通用发送 xx/down UI修改](#modbus 通用发送 xx/down UI修改)/[modbus 通用发送 xx/down 修改](#modbus 通用发送 xx/down 修改)同样的处理

1. 添加校验

   ```js
   content: {value: "11 22 33 44 55 66", validate: RED.validators.regex(/^((?=\w)[^_]{2} )*(?=\w)[^_]{2}$/)},
   ```

2. 添加`hex2int`

   ```js
   const hex2int = (hex) =>  {
       var len = hex.length, a = new Array(len), code;
       for (var i = 0; i < len; i++) {
           code = hex.charCodeAt(i);
           if (48<=code && code < 58) {
               code -= 48;
           } else {
               code = (code & 0xdf) - 65 + 10;
           }
           a[i] = code;
       }
       
       return a.reduce(function(acc, c) {
           acc = 16 * acc + c;
           return acc;
       }, 0);
   }
   ```

3. 处理content

   ```js
   let buffer = Buffer.from(n.content.split(" ").map((v)=>hex2int(v)))
   ```

4. 修改数据结构

   ```js
   msg.payload = {
       "applicatrionID": n.application,
       "devEUI": n.deveui,
       "confirmed": n.confirmed == "true" ? true : false,
       "fPort": n.fport,
       "data": buffer.toString("base64"),
       "object": null // 默认为null
   }
   ```

   