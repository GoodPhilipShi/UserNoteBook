- 系统架构: amd64
- 适配版本: ~~V1.7.2 RC1.0~~ V1.7.2RC2.0

> UOS的`gedit`(UI版文本编辑器)是`deepin-editor`

# 搭建环境

| 名称     | 版本       | 目标版本     |
| ------ | -------- | -------- |
| Git    | v2.20.1  | 无        |
| NPM    | v5.8.0   | v8.3.1   |
| Node   | v10.21.0 | v16.14.0 |
| Python | v2.7.16  | v3.*     |

## 安装

### 1. 更新软件列表

```shell
sudo apt-get update
```

### 2. 开始安装

```shell
sudo apt-get install npm git
```

> 后面重新安装的时候，不晓得咋个NPM有问题了

### 3. 手动安装NPM

```shell
wget https://nodejs.org/dist/v16.14.2/node-v16.14.2-linux-x64.tar.xz
tar -xvJf node-v16.14.2-linux-x64.tar.xz
cd node-v16.14.2-linux-x64
sudo cp ./bin/* /usr/bin/ -rf
sudo cp ./include/* /usr/include/ -rf
sudo cp ./lib/* /usr/lib/ -rf
sudo cp ./share/* /usr/share/ -rf
```

## 升级Node\NPM

### 1. 安装N

```shell
sudo npm i -g n
```

### 2. 切换至node最新稳定版本

```shell
sudo n stable
```

## 配置Git

### 1. 生成.ssh

```shell
ssh-keygen
```

### 2. 注册

```shell
deepin-editor /home/uos/.ssh/id_rsa.pub
```

> 然后就是复制到 `Gitee -> 设置 -> SSH公钥`
> 
> 快捷: [SSH公钥 - Gitee.com](https://gitee.com/profile/sshkeys)

### 3. 配置用户邮箱、用户名称

```shell
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## 配置Python默认版本

> [Linux下切换Python版本的几种方法 - Feyn - 博客园](https://www.cnblogs.com/feynxd/p/11367806.html)
> 
> ### 我决定采用update-alternatives 切换版本

### 建立python的组,并添加Python2和Python3的可选项

> 建立一组候选项

```shell
sudo update-alternatives --install <链接> <名称> <路径> <优先级>
```

```shell
# 添加Python2可选项，优先级为1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
# 添加Python3可选项，优先级为2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
```

### 番外1: 切换python组的配置

> 配置<名称>组中的可选项，并选择使用其中哪一个

```shell
sudo update-alternatives --config <名称>
```

```shell
sudo update-alternatives --config python
```

### 番外2: 删除python组的某个可选项

> 从<名称>中去掉<路径>选项

```shell
sudo update-alternatives --remove <名称> <路径>
```

```shell
sudo update-alternatives --remove python /usr/bin/python2.7
```

## 开始拉取MindPlus

### 运行全自动脚本

```
python Automatic\ Clone\ For\ mindPlus.py
```

> ✔环境搭建完毕😁

# 适配

## `scacth-vm`编译

### 错误①: 文件大小写

> 错误详情: ModuleNotFoundError: Module not found: Error: Can't resolve '../../modules/bos0063' in '/home/uos/Desktop/mindPlus/otherModules/scratch-vm/src/blocks/sensor'

#### 1. 查看实际上是否存在`bos0063`

> 查看目标: /home/uos/Desktop/mindPlus/otherModules/scratch-vm/src/modules/bos0063
> 目标文件名称，例如`bos0063.js`
> 存在，但文件名称是`BOS0063.js`

#### 2. 查找文件并修改代码

```shell
grep -nr "../../modules/bos0063"
# src/blocks/sensor/scratch3_BOS0063.js:12:import BOS0063 from '../../modules/bos0063'
vim otherModules/scratch-vm/src/blocks/sensor/scratch3_BOS0063.js +12
# '../../modules/bos0063' --> '../../modules/BOS0063'
```

## `gui`编译

### 错误①: 文件大小写

> 错误详情: Module not found: Error: Can't resolve './sensor/huskylens' in '/home/uos/Desktop/mindPlus/src/lib/block-generator/MicroPython'

#### 1. 查看实际上是否存在`huskylens`

> 查看目标: /home/uos/Desktop/mindPlus/src/lib/block-generator/MicroPython/sensor/huskylens
> 目标文件名称，例如`huskylens.js`
> 存在，但文件名称是`huskyLens.js`

#### 2. 查找文件并修改代码

```shell
grep -nr "./sensor/huskylens"
# lib/block-generator/MicroPython/index.js:92:    huskylens: () => import("./sensor/huskylens"),
vim src/lib/block-generator/MicroPython/index.js +92
# huskylens: () => import("./sensor/huskylens"), --> huskylens: () => import("./sensor/huskyLens"),
```

## SDK编译

### 第一步: 进行全部SDK编译

```shell
cd Arduino/compile
# 方法1
python build.py
# 方法2 每个主板编译一次
python ofile.py --build --includes -b uno
```

### 第二步: 将编译失败的SDK进行修复

```shell
python ofile.py --build --includes -b microbit
python ofile.py --build --includes -b microbitV2
python ofile.py --build --includes -b uno
```

#### 修复①: 编译`UNO`的SDK

> 部分错误代码: `/home/uos/Desktop/mindPlus/Arduino/compile/tmp/arduino_build_oo/libraries/DFRobot_pinpongBread/DFRobot_pinpongBread.cpp.o (symbol from plugin): In function "mpu":`
> 
> 想法: 将可以编译的先编译完成

1. 屏蔽`DFRobot_pinpongBread`
   
   > 路径: `Arduino/libraries/DFRobot_pinpongBread/config.json`
   
   ```diff
   - "uno": true,
   + "uno": false,
   ```

2. 编译
   
   ```shell
   python ofile.py --build --includes -b uno
   ```

3. 单独编译`DFRobot_pinpongBread`
   
   ```diff
   + "uno": true,
   - "uno": false,
   ```
   
   ```shell
   python ofile.py --build --includes -b uno -l DFRobot_pinpongBread.h
   ```

#### 修复②: 编译`microbit`的SDK

## `npm run electron` 运行

> 查看各个模式基础UI是否正常

| 模式       | 查看内容          |
| -------- | ------------- |
| 实时模式     | 打开是否正常、UI是否正常 |
| 上传模式     | 打开是否正常、UI是否正常 |
| Python模式 | 解压Python，并运行  |

## 测Python

#### 错误①

> 具体代码: `/home/uos/Documents/mindplus-py/environment/Python3.6.5-64/bin/python: /lib/x86_64-linux-gnu/libm.so.6: version 'GLIBC_2.29' not found (required by /home/uos/Documents/mindplus-py/environment/Python3.6.5-64/bin/python)`
> 
> 参考地址: [wkhtmltopdf: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.27' not found (required by wkhtmltopd_maintain 的博客-CSDN博客](https://blog.csdn.net/u012999810/article/details/88999081)

1. 查看该系统支持的GLIBC_ 版本
   
   ```shell
   strings /lib/x86_64-linux-gnu/libm.so.6 | grep GLIBC_
   ```
   
   ```
   GLIBC_2.2.5
   GLIBC_2.4
   GLIBC_2.15
   GLIBC_2.18
   GLIBC_2.23
   GLIBC_2.24
   GLIBC_2.25
   GLIBC_2.26
   GLIBC_2.27
   GLIBC_2.28
   GLIBC_PRIVATE
   ```

2. 思考: 系统本身就存在`Python 3.7.3`, 那么就不可能说我运行不了`Python 3.6.5`

3. 查看一下: `compat`是不是分支没有切换
   
   > 估计原因是: [不是很确定]之前编译的`Python 3.6.5`是在`Ubuntu`上编译的所以相关的库比较领先于现在的`UOS`

4. 重新编译一份`Python 3.6.5`
   
   1. 下载源代码
      
      > 源代码发布地址: [Python Release Python 3.6.5 | Python.org](https://www.python.org/downloads/release/python-365/)
      > 
      > [源码下载](https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz)
   
   2. 创建 `Python-3.6.5-build` 文件夹
   
   3. 开始编译
      
      ```shell
      ./configure --prefix=`pwd`/../Python-3.6.5-build
      make && make install
      ```
      
      > 编译好的代码就在 `Python-3.6.5-build`文件夹
      > 
      > 最后就是打包替换原 `Python3.6.5_linux_x86_64.zip`

> ps: 上述编译存在错误
> 
> 新的打包文档: [[Python打包]]

##### 后续将已经支持的库添加到Python包当中

```shell
opencv-python==4.5.5.64
siot==0.1.0
xlrd==2.0.1
xlwt==1.3.0
schedule==1.1.0
requests==2.27.1
PyAutoGUI==0.9.53
pygame==2.0.1
unihiker==0.0.22
jedi==0.18.1
```

安装方法如下:

```shell
cd  ~/Deskt/Python-3.6.5-build
./bin/python -m pip install ***(代指库的名称)
```

难点有:

1. unihiker库
   
   > 下载时遇到: `Running setup.py install for pyaudio ... error`
   
   ```shell
   sudo apt-get install python3-pyaudio
   ```
   
   > 安装完成后，只是本地Python可以使用`pyaudio`了，而你安装依旧报错
   > 
   > 那么，则需要将本地的`pyaudio`复制到Python包里面去
   
   1. 进入本地Python的`site-packages`
      
      ```shell
      cd /usr/lib/python3/dist-packages/
      ```
   
   2. 复制`pyaudio`到Python包当中
      
      ```shell
      cp ./PyAudio-0.2.11.egg-info ~/Deskt/Python-3.6.5-build/lib/python3.6/site-packages
      cp ./pyaudio.py ~/Deskt/Python-3.6.5-build/lib/python3.6/site-packages
      ```
   
   > 然后
   
   > ps. 我的这个方法并不是所有包都可以这样操作, 就目前而言tkinter就不行

#### 错误②

> 具体代码: `Unhandled Exception TypeError: Cannot read property 'trim' of undefined
>     at alertDialog (custom-dialog.js?2464:22)
>     at SelectSerial.handleSelectChange (select-serial.jsx?565d:617)`

1. 搜索代码: `gui.dialog.serialDriverInstalling`
   
   ```shell
   cd otherModules/scratch-l10n/editor
   grep -nr "gui.dialog.serialDriverInstalling"
   ```
   
   > 没找到，猜测：1. 仓库并没有上传翻译文件2. id 错误了
   > 
   > 然后就询问了一下涛哥

2. 结果: `id错误`
   
   > 修改英文、中文翻译的ID
   
   ```diff
   - "gui.dialog.serialDriverInstallin": "串口驱动安装中...",
   + "gui.dialog.serialDriverInstalling": "串口驱动安装中...",
   ```

## 测上传

[V1.7.2RC2.0测试表格](../③Mind+测试/Mind+测试.md)

### Micro:bit

> 当前程序运行至 `microbitBurner.js`
> 
> 功能: `burnToBoard(port, file) > findUDisk(serialNumber)`
> 
> 找到了磁盘
> 
> 查看了`/sys/class/block/sdb/device/scsi_device`下的文件夹`33:0.0`
> 
> 得到id`3`

```
Command failed: cat /proc/scsi/usb-storage/3
```

> [linux下区分各种SCSI磁盘类型](https://www.icode9.com/content-3-738963.html)

```
sudo find / -name "3" -exec grep -in "Serial Number" {} \;
sudo find / -name "3" -perm 755 -type c,f,p -exec grep -in "Serial Number" {} \;
```

> 还没有到开始正在烧录！！

---

> 后续跟进
> 
> 当前情况: 已经切换成`V1.7.2RC2.0`

1. 错误: 不管是否挂载，直接烧录失败
   
   ![](C:\Users\11834\AppData\Roaming\marktext\images\2022-03-31-16-25-43-image.png)、
   
   > 那么就需要排查是否存在导入库不存在的问题
   
       ![](C:\Users\11834\AppData\Roaming\marktext\images\2022-03-31-16-26-53-image.png)
   
   > 最后排查处一个库的大小写存在问题

### Arduino Leonardo

> 烧录失败, 板子烧毁

### FireBeetle ESP32-E

```shell
esptool.py v4.0-dev
Serial port /dev/ttyUSB0
Connecting......................................

A fatal error occurred: Failed to connect to ESP32: Wrong boot mode detected (0x13)! The chip needs to be in download mode.
For troubleshooting steps visit: https://docs.espressif.com/projects/esptool/en/latest/troubleshooting.html
```

> 根据几位大佬的推测: CH341SER驱动的问题
> 
> > 尝试构建驱动失败
> > 
> > > 已给官方发送邮件， 请求获取最新驱动源码

### Bonson MC1

> 与 [FireBeetle ESP32-E](#FireBeetle ESP32-E) 一个错

### [MicroPython] Telloesp32

> 擦除、烧录后无法自动重启

## 修复①

### Micro:bit

> 路径: `otherModules/scratch-vm/webpack.config.js`

```javascript
  plugins: [
      new CleanWebpackPlugin(),
      new webpack.DefinePlugin({
          'DEF_MAC': `${!!packageJson.build.mac}`,
          'DEF_WIN': `${!!packageJson.build.win}`,
          'DEF_LINUX': `${!!packageJson.build.linux}`,
          'APP_VERSION': `"${packageJson.version}"`,
          'DEF_LINUX_X86_64': `${!!packageJson.build.linux && !!os.arch().match(/x32|x64/i)}`,
+         // 请手动修改
+         'DEF_UOS_X86_64': true
      }),
      // new HardSourceWebpack()
  ]
```

> 修复烧录前的判断: 是否已挂载成功

```diff
  if (DEF_LINUX) {
      setTimeout(
      this.runtime.childProcess.exec('df -h', (err, stdout, stderr) => {
          if (err) {
              this.emit('message', `${err.toString()}\n`);
              return reject(err);
          }
          let dfinfo = [];
          stdout.toString().split('\n').map((item) => {
              item = item.split(/ +/g);
              let fileSys = item[0].split('/').pop();
              let mountPoint = item.pop();
              if ((/MICROBIT|MATRIXBIT/g.test(mountPoint) && this.name === 'microbit') ||
                  (/MINI/g.test(mountPoint) && this.name === 'calliope')) {
                  dfinfo.push({ mp: mountPoint, fs: fileSys })
              }
          })
          let promises = dfinfo.map((item) => {
              return new Promise(resolve => {
-                   fs.readdir(path.join(`/sys/class/block`, item.fs, 'device/scsi_device'), (err, data) => {
-                       if (err) return resolve();
-                       let id = data[0][0];
-                       this.runtime.childProcess.exec(`cat ${path.join('/proc/scsi/usb-storage', id)}`, (err, stdout, stderr) => {
-                           if (err) {
-                               this.emit('message', `${err.toString()}\n`);
-                               return resolve();
-                           }
-                           let sn = null;
-                           stdout.toString().split('\n').forEach((line) => {
-                               if (/Serial Number:/g.test(line)) {
-                                   sn = line.replace(/Serial Number: +/g, '');
-                                   return false;
-                               }
-                           })
-                           resolve({ sn: sn, mp: item.mp });
-                       });
-                   })
+                 if(DEF_UOS_X86_64){
+                     this.runtime.childProcess.exec(`cat /proc/mounts`, (err, stdout, stderr) => {
+                         if (err) {
+                             this.emit('message', `${err.toString()}\n`);
+                             return resolve();
+                         }
+                         let sn = false;
+                         if (stdout.toString().indexOf(`${item.fs} ${item.mp} `)!=-1){
+                             sn = true
+                         }
+                         resolve({ sn: sn, mp: item.mp });
+                     });
+                 }else{
                      fs.readdir(path.join(`/sys/class/block`, item.fs, 'device/scsi_device'), (err, data) => {
                          if (err) return resolve();
                          let id = data[0][0];
                          this.runtime.childProcess.exec(`cat ${path.join('/proc/scsi/usb-storage', id)}`, (err, stdout, stderr) => {
                              if (err) {
                                  this.emit('message', `${err.toString()}\n`);
                                  return resolve();
                              }
                              let sn = null;
                              stdout.toString().split('\n').forEach((line) => {
                                  if (/Serial Number:/g.test(line)) {
                                      sn = line.replace(/Serial Number: +/g, '');
                                      return false;
                                  }
                              })
                              resolve({ sn: sn, mp: item.mp });
                          });
                      })
+                 }
              })
          })
          return Promise.all(promises).then(result => {
              if (result.length === 0) return resolve();
              let mp = null;
              result.forEach(item => {
-                 if (!DEF_UOS_X86_64 && item.sn === this.product.serialNumber) {
+                 if (item.sn ||!DEF_UOS_X86_64 && item.sn === this.product.serialNumber) {
                      mp = item.mp;
                      return false;
                  }
              })
              return resolve(mp);
          })
      }), 2000)
  }
```

```diff
  burnToBoard(port, file) {
      if (!this.product.choosedSerial) {
          return Promise.reject('Serialport disconnect\n');
      }
      // 获取磁盘列表 ---> 查找磁盘 ---> 找到磁盘 ---> U盘烧录
      //                        ---> 未找到磁盘 ---> 磁盘未挂载 ---> SWD烧录
      //                                      ---> 设备不存在 ---> 烧录失败
      return this.findUDisk(this.product.serialDeviceId)
          .then((upath) => {
              if (upath) {
                  // 磁盘已经被挂载
                  return this.burnMicrobitByUDisk(file, upath);
              }
              if (this.product.choosedSerial) {
                  // 磁盘存在但未被挂载
-                 return this.burnMicrobitBySWD(file, this.product.serialNumber);
+                 if(!DEF_UOS_X86_64){
+                     // 原因: 
+                     //     1. UOS那边直到V171RC1.0，也并不支持OpenOCD的依赖
+                     //     2. 所以UOSX86就屏蔽这条路
+                     return this.burnMicrobitBySWD(file, this.product.serialNumber);
+                 }else{
+                     return Promise.reject('未挂载, 请在手动插拔进行挂载\n');
+                 }
              }
              // 磁盘不存在
              return Promise.reject('Serialport disconnect\n');
          })
  }
```

### Arduino Leonardo

> UOS适配的`Arduino IDE`也无法烧录`Arduino Leonardo`
> 给予管理员权限后, 板子烧毁

✔处理措施: 屏蔽

### 调整终端UI

#### 全局调整

> 路径: `build/static/vs/vs-overwrite/find-widget.css`

```css
/* uos x86 终端宽度 */
#brace-editor,
/* Python 终端滚动条*/
.xterm-viewport,
/* Python 终端宽度*/
.xterm-screen {
    width: auto!important
}
```

#### 调整Python Xterm终端UI

> 路径: `src/components/python/xterm-wrapper/xterm-wrapper.jsx`

```jsx
  shouldComponentUpdate(nextProps, nextState) {
    if (nextProps.terminalHeight !== this.props.terminalHeight ||
      nextProps.width !== this.props.width ||
      nextProps.dragDisabled !== this.props.dragDisabled ||
      nextProps.locale !== this.props.locale ||
      nextProps.connectShow !== this.props.connectShow ||
      nextProps.remoteName !== this.props.remoteName ||
      nextProps.remoteConnect !== this.props.remoteConnect ||
      nextProps.fontBold !== this.props.fontBold
    ) {
      if (this.term) {
        if (!DEF_LINUX) {
          this.term.resize(parseInt(nextProps.width / 10), parseInt((nextProps.terminalHeight - TerHeaderHeight) / 18));
        } else {
-         this.term.resize(parseInt(nextProps.width / 10), parseInt((nextProps.terminalHeight - TerHeaderHeight) / 20));
+         if(DEF_UOS_X86_64){
+           this.term.resize(parseInt(nextProps.width / 10), parseInt((nextProps.terminalHeight - TerHeaderHeight) / 20));
+         }else{
+           this.term.resize(parseInt(nextProps.width / 10), parseInt((nextProps.terminalHeight - TerHeaderHeight) / 24));
+         }
        }
      }
      return true;
    }
    return false;
  }
```

#### 调整Arduino Xterm终端UI

> 路径: `src/components/arduino/terminal-wrapper/xterm-wrapper.css`

```css
.isUOS_X86_64 {
    width: auto!important;
}
```

> 路径: `src/components/arduino/terminal-wrapper/xterm-wrapper.jsx`

```jsx
  return (
    <div
        className={classNames(
            styles.terminalWrapper,
+           {
+               [styles.isUOS_X86_64]: DEF_UOS_X86_64
+           }
        )}
        style={{ height: terminalHeight, width: width, backgroundColor:   "#060101" }}
    // id='terminal-container'
    >
  )
```

> 路径: `webpack.config.js`

```diff
  new webpack.DefinePlugin({
      'process.env.NODE_ENV': '"' + process.env.NODE_ENV + '"',
      'process.env.DEBUG': Boolean(process.env.DEBUG),
      'process.env.GA_ID': '"' + (process.env.GA_ID || 'UA-146796610-2') + '"',
      'DEF_MAC': `${!!packageJson.build.mac}`,
      'DEF_WIN': `${!!packageJson.build.win}`,
      'DEF_LINUX': `${!!packageJson.build.linux}`,
      'DEF_LINUX_X86_64': `${!!packageJson.build.linux && !!os.arch().match(/x32|x64/i)}`,
      'APP_VERSION': `"${packageJson.version}"`,
      'APP_ISPACKAGED': process.env.NODE_ENV === "production",
+     // 手动修改
+     'DEF_UOS_X86_64': true,
  }),
```

### [已屏蔽] FireBeetle ESP32-E\Boson MC1

> ps. 屏蔽原因: `ubuntu-20.04.3`上也没法烧录

驱动: [GitHub - WCHSoftGroup/ch341ser_linux: USB to serial driver for USB to serial chip ch340, ch341, etc.](https://github.com/WCHSoftGroup/ch341ser_linux)

1. 删除原本的驱动
   
   > 路径: `/usr/lib/modules/4.19.0-amd64-desktop/kernel/drivers/usb/serial/`
   > 
   > > 其他系统: `/usr/lib/modules/$(uname -r)/kernel/drivers/usb/serial/`
   
   ```shell
   cd /usr/lib/modules/$(uname -r)/kernel/drivers/usb/serial/
   sudo rm -rf ch34x.ko
   ```

2. 编译并安装最新驱动
   
   ```shell
   git clone https://github.com/WCHSoftGroup/ch341ser_linux.git
   cd ch341ser_linux/driver
   make && sudo make install
   ```
   
   > 然后重启电脑即可

3. 根据官网上的信息进行判断驱动\设备是否运行正常
   
   1. [驱动] 通过`lsusb`或`dmesg`查看USB VID为[1A86]
      
      ```shell
      $ lsusb
      Bus 002 Device 011: ID 1a86:7522 QinHeng Electronics
      ```
      
      > ✔驱动运行正常
   
   2. [设备]  在/dev 目录下是否存在名为`ttyCH341USBx`的 tty 设备
      
      ```shell
      $ ls -l /dev/ttyCH341USB*
      crw-rw---- 169,0 root  6 4月  11:37 /dev/ttyCH341USB0
      ```
      
      > ✔设备运行正常

4. 测试结果
   
   ```shell
   mkdir test
   cd test
   cat>index.js<<EOF
   const { SerialPort } = require('serialport');
   
   SerialPort.list().then((ports) => {
      ports.forEach(function (port) {
         console.log(port.path)
      })
   })
   EOF
   npm install serialport
   ```
   
   ```shell
   $ node index.js
   ...没有/dev/ttyCH341USB0
   ```
   
   > 测试其他的和`FireBeetle ESP32-E`串口芯片(FireBeetle ESP32 V4.0)
   > 
   > ```shell
   > $ ls -l /dev/ttyCH341USB*
   > crw-rw---- 169,0 root  6 4月  11:37 /dev/ttyCH341USB0
   > ```
   > 
   > 但是，`node index.js`依旧无法列出`/dev/ttyCH341USB0`
   > 
   > ps. 要知道之前的驱动是可以找到`FireBeetle ESP32 V4.0`的串口(`/dev/ttyUSB0`)

5. 最后的处理：给`tech@wch.cn\lzy@wch.cn`(CH341SER驱动官方)发送邮件，寻求解决方法

### Telloesp32

> 目前RMTT MicroPython烧录存在问题(时能烧录成功时烧录失败) --- 没有整理出烧录成功的规律
> 
> ❗❗❗ps. 健哥那边就没得什么问题❗❗❗

## 修复②

> 初次打包，交测后的BUG

### 未内置unihiker库

> [禅道5809](http://test.dfrobot.top:5000/zentao/bug-view-5809.html)
> 
> 原先认为行空板这个扩展就只是为了行空板，所以在原先的Python包里面并没有内置unihiker库

> 下载时遇到: Running setup.py install for pyaudio ... error

```shell
sudo apt-get install python3-pyaudio
```

> 安装完成后，只是本地Python可以使用pyaudio了，而你安装依旧报错
> 
> 那么，则需要将本地的pyaudio复制到Python包里面去

1. 进入本地Python的site-packages
   
   ```shell
   cd /usr/lib/python3/dist-packages/
   ```

2. 复制pyaudio到Python包当中
   
   ```shell
   cp ./PyAudio-0.2.11.egg-info ~/Deskt/Python-3.6.5-build/lib/python3.6/site-packages cp ./pyaudio.py ~/Deskt/Python-3.6.5-build/lib/python3.6/site-packages
   ```

> 然后./bin/python -m pip install unihiker，就可以安装成功了

### 设备无法上传程序，报错无权限

> [禅道5811](http://test.dfrobot.top:5000/zentao/bug-view-5811.html)
> 
> 原先一直认为是`electron-builder`初次打包(会在打包的过程中下载依赖资源)的问题
> 
> 再后来认为是UOS新系统初次安装的问题
> 
> 最后发现是UOS自带的安装包安装程序存在问题(或者说是*UOS自带的安装包安装程序* 对 *electron-builder打的原生deb包* 存在兼容问题)

> 解决方法为: 使用linux命令进行安装`sudo dpkg -i mindplus.deb`

### 掌控上传程序报错

> [禅道5814](http://test.dfrobot.top:5000/zentao/bug-view-5814.html)
> 
> 打包前没有赋予x权限(作为程序运行)，打包后安装就无法运行了

> 给程序添加x权限，然后重新打包就可以了

### 双击sb3打开Mind+，显示内容为空

> [禅道5816](http://test.dfrobot.top:5000/zentao/bug-view-5816.html)
> 
> 原本remote.process.argv中会在[程序名称、sb3文件]中间添加一个`--`， 但是没有生效

> 文件路径: mindPlus\src\lib\usersb3-loader-hoc.jsx

```diff
- if (DEF_WIN || DEF_LINUX){
+ if (DEF_WIN){
+     // 171 2.0增加网页打开本地程序，传递参数前增加了--，双击打开文件的位置后延一位1=>2
      fileUrl = remote.process.argv[2];
+ }
+ if (DEF_LINUX){
+     fileUrl = remote.process.argv[1];
+ }
```

### 新建项目，文件系统的项目中的文件未全部清空

> [禅道5818](http://test.dfrobot.top:5000/zentao/bug-view-5818.html)
> 
> Mind+环境变量设置存在问题

> 原`set NODE_ENV=production`在linux上并没有效果, 所以程序判断当前环境为开发环境(开发环境默认不删除)

> 文件路径:
> 
> package.json

```diff
- "prod": "set NODE_ENV=production&&webpack --target electron-renderer",
+ "prod": "export NODE_ENV=production&&webpack --target electron-renderer",
```

### 不能识别新版掌控

> [禅道5819](http://test.dfrobot.top:5000/zentao/bug-view-5819.html)
> 
> 并没有在Linux和MAC上添加对新掌控版的判断

> 文件路径:
> 
> src/components/select-serial/select-serial.jsx

```diff
  if (DEF_MAC) {
  // 省略
+                     if (port.vendorId === "1a86" && port.productId  === "55d4") {
+                        name = 'CH9102';
+                     }
  // 省略
  }
  if (DEF_LINUX) {
  // 省略
+                     } else if (port.productId === "55d4" && port.vendorId === "1a86" ) {
+                        name = '(CH9102)';
  // 省略
  }
```

### 文件系统右键菜单“另存为”，闪退

> [禅道5821](http://test.dfrobot.top:5000/zentao/bug-view-5821.html)
> 
> 没有设置扩展，就会闪退

> 文件路径:
> 
> src/components/arduino/mpy-file-tree/mpy-file-tree.jsx
> 
> src/components/python/file-tree/file-tree.jsx

```diff
+ let exts = d.title.split(".")
+ exts = exts.length > 1 ? exts.pop() : ""
+ ipcRenderer.send('open-file-dialog', { title: "另存为", exts: [exts], defaultPath: d.title });
- ipcRenderer.send('open-file-dialog', { title: "另存为", exts: [], defaultPath: d.title });
```

### 哈士奇无法获取拍照、截屏

> [禅道5815](http://test.dfrobot.top:5000/zentao/bug-view-5815.html)

> 测试相关信息: [统信系统+amd64-哈士奇问题以及测试](统信系统+amd64-哈士奇问题以及测试.md)
> 
> 结论:
> 
> 1. 虚拟机和真实机上进行串口读取存在差异
>    
>    ```python
>    import serial
>    
>    ser = serial.Serial('/dev/ttyUSB0', 3000000, 8, 'N', 1)
>    ser.rts = False
>    ser.dtr = False
>    
>    print(ser.is_open)
>    
>    ser.write(bytes([0x55,0xAA,0x11,0x00,0x31,0x41,0x30,0x2E,0x35,0x2E,0x31,0x49]))
>    
>    print(ser.readable())
>    
>    data = ser.read(230000)
>    
>    print(len(data))
>    
>    ser.close()
>    ```
> 
> 2. electron@4.2.12运行SerialPort无法获取完整数据

> 屏蔽

## 修改版本号

> ❗ 记得取消webpack的热编译

### 修改version.json

> 路径: compat下面

```diff
  {
-     "version": "1.7.2-202110301900"
+     "version": "1.7.2-202204261730"
  }
```

### 修改version-map.json

> 路径: compat下面

```diff
+ "1.7.2-202204261730": {
+     "description": "1.7.2 RC2.0"
+ }
```

### 修改package.json

```diff
- "version": "1.7.1-202110301900"
+ "version": "1.7.1-202203241730"
```

# 打包

>❗ 记得取消webpack的热编译

```python
python buildpack.py
```

# 番外

## 更新时间

```shell
sudo apt-get install ntpdate
ntpdate -u ntp.aliyun.com
```

```shell
sudo -S hwclock --hctosys
```

## 虚拟机

```cmd
VBoxManage.exe setextradata "UOS_X86" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" "1"
```

## 安装Chrome

```shell
sudo apt-get install google-chrome-stable
```

## 调整无法通过鼠标调整的窗口

### 安装 `wmctrl`

```shell
sudo apt-get install wmctrl
```

### 列出窗口

```shell
wmctrl -l
```

```
0x02000006 -1    N/A 桌面
0x02600006 -1    N/A DDE Dock
0x0600000a  0    N/A 终端
0x06200002  0 uos-PC 百度一下，你就知道 - Google Chrome
```

### 调整窗口大小

> 要根据它的标题调整窗口大小

```shell
wmctrl -r WindowTitleName -e gravity,X,Y,width,height
```

```shell
wmctrl -r Chrome -e 0,0,0,1280,800
```

## [VirtualBox] 配置虚拟机串口

```shell
sudo apt-get install minicom
sudo minicom -s
```

```
 +-----[configuration]------+
 | Filenames and paths      |
 | File transfer protocols  |
 | Serial port setup        |
 | Modem and dialing        |
 | Screen and keyboard      |
 | Save setup as dfl        |
 | Save setup as..          |
 | Exit                     |
 | Exit from Minicom        |
 +--------------------------+
```

> 使用上下键选择 `Serial port setup`，回车

```
 +-----[configuration]------+ 
 | Filenames and paths      | 
 | File transfer protocols  | 
 | Serial port setup        | <-- Enter选中
 | Modem and dialing        | 
 | Screen and keyboard      |
 | Save setup as dfl        |
 | Save setup as..          |
 | Exit                     |
 | Exit from Minicom        |
 +--------------------------+
```

> 此时光标在 `Change which setting?` 后面停留
> 按下“A”更改Serial Device为“/dev/ttyS0”，表示minicom要操作的是串口COM1。
> 然后回车确定

```
 +-----------------------------------------------------------------------+
 | A -    Serial Device      : /dev/modem                                |
 | B - Lockfile Location     : /var/lock                                 |
 | C -   Callin Program      :                                           |
 | D -  Callout Program      :                                           |
 | E -    Bps/Par/Bits       : 115200 8N1                                |
 | F - Hardware Flow Control : Yes                                       |
 | G - Software Flow Control : No                                        |
 |                                                                       |
 |    Change which setting?                                              |
 +-----------------------------------------------------------------------+
```

```
 +-----------------------------------------------------------------------+
 | A -    Serial Device      : /dev/ttyS0                                |
 | B - Lockfile Location     : /var/lock                                 |
 | C -   Callin Program      :                                           |
 | D -  Callout Program      :                                           |
 | E -    Bps/Par/Bits       : 115200 8N1                                |
 | F - Hardware Flow Control : Yes                                       |
 | G - Software Flow Control : No                                        |
 |                                                                       |
 |    Change which setting?                                              |
 +-----------------------------------------------------------------------+
```

> 回车，结束
> 使用上下键选择 `Save setup as df`，回车

```
 +-----[configuration]------+
 | Filenames and paths      |
 | File transfer protocols  |
 | Serial port setup        |
 | Modem and dialing        |
 | Screen and keyboard      |
 | Save setup as dfl        |  <-- Enter选中
 | Save setup as..          |
 | Exit                     |
 | Exit from Minicom        |
 +--------------------------+
```

## 将用户从用户组中删除

> 将用户“uos”从“dialout”组中删除

```shell
sudo gpasswd dialout -d uos
```

## 解压压缩包

```shell
# 解压 tar包
tar -xvf file.tar
# 解压tar.gz
tar -xzvf file.tar.gz
# 解压 tar.bz2
tar -xjvf file.tar.bz2
# 解压 tar.xz
tar -xvJf file.tar.xz
# 解压tar.Z
tar -xZvf file.tar.Z
# 解压rar
unrar e file.rar
# 解压zip
unzip file.zip
```

### 没有tkinter

> ModuleNotFoundError: No module named '_tkinter'

> NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev

```shell
sudo apt-get install python3-tk python3-dev
```

### 绝对不能用统信的安装包安装工具

> 这个安装包属于使用electron-builder打包后的安装包

1. 安装后虽然会运行脚本(我在脚本中添加了一串在桌面创建文件的命令，可以得到结果[桌面上有一个属于root的文件])，但是用户组添加并没有效果
   
   > 在安装包安装工具的详情(输入密码后，在安装包安装工具上会有<显示详细信息>，点击就可以看到安装步骤)里面也没有运行脚本的相关信息

2. 使用`sudo dpkg -i Mindxxx.deb`，就不会存在任何问题

3. 最重要的是，第一次安装包安装工具进行安装，第二次再用命令进行安装，用户组就会添加成功
   
   ```shell
   uos : uos tty lp uucp dialout sudo plugdev users netdev lpadmin scanner sambashare
   ```