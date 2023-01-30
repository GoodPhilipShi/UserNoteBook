哈士奇无法拍照成功
> 串口数据接收不完整

# 测试不变的内容

## 小DEMO

```js
const SerialPort = require("serialport")

const delay = ms => new Promise((resolve, reject) => setTimeout(resolve, ms))
let buffer = []

sp = new SerialPort('/dev/ttyUSB0', {
    baudRate: 3000000,
    highWaterMark: 1024 * 1024, // 1M
})

sp.on("open", async event => {
    const options = {
        dtr: false,
        rts: false,
    };
    await delay(300);
    sp.set(options, async () => {
        console.log("串口打开成功")
        await delay(5000);
        sp.write([85, 170, 17, 0, 49, 65], (err) => {
            if (err) {
                console.log('Error on write: ', err.message);
            }
        });
    });
});

sp.on("data", data => {
    buffer = buffer.concat(JSON.parse(JSON.stringify(data)).data);
    console.log("len==", buffer.length)
});
```

## 测试环境

1. 纯NodeJs环境
2. 纯Mind+环境(NodeJs+Electron)

# 测试开始

## 测试：提升SerialPort版本 -> 10.0.1

### 搭建DEMO环境

```shell
mkdir xx
cd xx
npm init
# 一路回车
touch index.js
# 将DEMO写入index.js文件中
yarn add SerialPort@10.0.1
```

### 运行与结果

```shell
node index.js
```

```
....
len== 230400
```

### 将SerialPort复制到mindPlus/build/static

```shell
rm -rf ../mindPlus/build/static
cp node_modules/serialport ../mindPlus/build/static
```

### 编译bindings.node文件

> 让这个SerialPort适配electron

#### 安装依赖库

```shell
yarn install
```

#### 安装electorn-rebuild

```shell
cd ../../
yarn add electorn-rebuild
```

#### 开始编译

> mindPlus/build/static/serialport/node_modules/@serialport/bindings

```shell
cd build/static/serialport/node_modules/@serialport/bindings
../../../../../../node_modules/.bin/electron-rebuild
```

> 编译失败

```
....
For more information, rerun with the DEBUG environment variable set to "electron-rebuild".

Error: `make` failed with exit code: 2
......
```

## 测试: 降低SerialPort版本 -> 10.0.0

> 同上

## 测试: SerialPort版本不变 -> 10.0.0 并且 升级electron版本至最新

> 同上

### 升级electron版本

> 前提：NodeJs也要很新(不一定要最新, 我用的是16.14.2[长期支持版本])

```shell
yarn add electron
```

> 当前版本: electron@18.1.0

### 开始编译

> mindPlus/build/static/serialport/node_modules/@serialport/bindings

```shell
cd build/static/serialport/node_modules/@serialport/bindings
../../../../../../node_modules/.bin/electron-rebuild
```

> 编译成功

### 运行mindplus

```
[7630:0425/154147.990627:FATAL:setuid_sandbox_host.cc(158)] The SUID sandbox helper binary was found, but is not configured correctly. Rather than run without sandboxing I'm aborting now. You need to make sure that /home/uos/Desktop/mindPlus/node_modules/electron/dist/chrome-sandbox is owned by root and has mode 4755.
/home/uos/Desktop/mindPlus/node_modules/electron/dist/electron exited with signal SIGTRAP
```

> [这里](https://blog.csdn.net/qq_33154343/article/details/106387381)说是Linux内核问题

## 测试: 降低SerialPort版本 -> 9.0.0 并且 electron 恢复 -> 4.2.12

> 同上上一样

## 测试: 查看通过依赖对象的Node进行修改

> [SerialPort支持的Node版本](https://serialport.io/docs/guide-platform-support#last-known-versions-for-unsupported-versions-of-nodejs)
> [Electron支持的Node版本](https://github.com/electron/releases#releases)
> 决定切换成SerialPort@9、NodeJs@10.11.0

> 同上

### electorn-rebuild编译

```shell
yargs parser supports a minimum Node.js version of 12. Read our version support policy: https://github.com/yargs/yargs-parser#supported-nodejs-versions
```

> 所以 NodeJs@12.22.12

> 编译成功

### 运行mindplus

> 依旧接收不完整


# 附录

## 曾认为是NODE_VERSION的问题，尝试NodeJs@10.11.0去运行小DEMO

> 接收完整 230400
