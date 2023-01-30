# Node-red 自定义节点的修改

## Modbus 通用节点

### xx/down xx/up 的 deveui 的修改

- [x] deveui 的修改

> [!tip] 寻求辉哥的协助

```javascript
/**
 * 生成deveui
 * @param {string} agreement 协议 RTU、TCP
 * @param {string} port 设备端口 /dev/ttyUSB0、/dev/ttyS0、/dev/ttyACM
 * @param {string} address 地址 0x50
 * @returns deveui uint64字符串
 */
const generateDeveui = (agreement, port, address) => {
    let buff = new Array(20)
    buff[12] = 'M'.codePointAt(0)
    buff[13] = agreement.slice(0, 1).toUpperCase().codePointAt(0)
    buff[14] = /tty(.)/g.exec(port)[1].codePointAt(0)
    buff[15] = Number(/tty.*(\d{1,})/g.exec(port)[1])
    buff[16] = Number(address)
    buff[17] = 0
    buff[18] = 0
    buff[19] = 0

    let deveui = buff.map((v, i) => {
        if (i < 12) return ""
        v = v.toString(16)
        if (v.length === 1) {
            return "0" + v
        }
        return v
    }).join("")

    return deveui
}
```

### xx/down 发送数据的修改

 - [x] `band` 改为 `baud`

```diff
	- band: `${n.baudrate} ${n.databits}${n.parity}${n.stopbits}`,
	+ baud: `${n.baudrate} ${n.databits}${n.parity}${n.stopbits}`,
```

 - [x] `addr` 应该直接直接使用整形

```diff
- addr: n.address
+ addr: Number(n.address)
```

 - [x] `size` 填写发送数据 (`cmd`) 的长度

```diff
- size: 0,
+ size: n.content.length,
 cmd: n.content
```

### xx/up 接收数据的修改

- [x] `data` 需要进行 base64 编码

```diff
+ try {
+     payload.hasOwnProperty("rxpk") && payload.rxpk.constructor === Array && (payload.rxpk = payload.rxpk.map((v) => v.hasOwnProperty("data") ? { ...v, data: this.btoa(v.data) } : v))
+ } catch (e) { }
  msg.payload = payload;
```

## UI

### 修改名称后, 节点没有改变

- [x] 已修改

```diff
- label: "通用发送",
+ label: function() {
+     return this.name||"通用发送";
+ },
```

### 添加一个输入框：数据处理脚本

> [!note]
> 允许用户使用 js 脚本进行数据的处理
> 使用 `eval` 函数实现

- [x] modbus 通用节点
- [x] lorawan 通用节点
- [x] 其他 input 节点 (发送节点)

> [!tip]
> 其余节点采用内置的数据处理脚本
> > 后续由辉哥提供相应的js脚本



```html
<script type="text/html" data-template-name="名称">
	<div class="form-row">
        <label for="node-input-decodeText"><i class="fa fa-tag"></i> 数据处理脚本</label>
        // 注意！这里的ID不要与要保存的名称相同
        // 存到decodeText里面(node-input-decodeText)
        // 那么ID就不要是node-input-decodeText
        <div style="height: 250px; min-height:150px;" class="node-text-editor" id="node-input-decode"></div>
    </div>
</script>

<script type="text/javascript">
    RED.nodes.registerType("名称",{
        defaults: {
            decodeText: { value: "内置" },
        },
        oneditprepare: function() {
            this.editor = RED.editor.createEditor({
                id: 'node-input-decode',
                mode: 'ace/mode/javascript',
                value: this.decodeText
            });
        },
        oneditsave: function () {
            this.decodeText = this.editor.getValue();
            this.editor.destroy();
            delete this.editor;
        },
        oneditcancel: function () {
            this.editor.destroy();
            delete this.editor;
        },
    });
</script>
```

```js
if(decode &&decode.includes("Decode")){
    try{
        eval(decode)
        if(typeof payload === 'string'){
            msg.payload = Decode(payload)
        }else{
            msg.payload = Decode(JSON.stringify(payload))
        }
    }catch(e){
        msg.payload = payload;
    }
}else{
    msg.payload = payload;
}
```

### `data-template-name` 的修改

- [x] `pt100 input` 改为 `pt100 meter`
- [x] `smogmeter input` 改为 `somg meter`

### 删除 Lorawan\\modbus 字样

> [!tip] 后续通过ICON来表示节点的分属