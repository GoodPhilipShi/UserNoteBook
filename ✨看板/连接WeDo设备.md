
# 连接EV3设备成功

![[Pasted image 20230112141004.png]]

# 模拟Scratch连接

```javascript
new WebSocket("wss://device-manager.scratch.mit.edu:20110/scratch/ble").close()
var ws = new WebSocket("ws://127.0.0.1:20111/scratch/ble")
ws.onmessage = (v)=> {
    console.log(v.data)
    let d = JSON.parse(v.data)
    try {
        if(d.method === "didDiscoverPeripheral"){
            ws.send(JSON.stringify({"jsonrpc":"2.0","method":"connect","params":{"peripheralId":d.params.peripheralId},"id":1}))
        }
    }catch {}
}

ws.onopen = () => {
    ws.send(JSON.stringify({"jsonrpc":"2.0","method":"discover","params":{"filters":[{"services":["00001523-1212-efde-1523-785feabcd123"]}],"optionalServices":["00004f0e-1212-efde-1523-785feabcd123"]},"id":0}))
}
```