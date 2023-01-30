# 系统环境

- 系统名称: 统信(UOS)
- 系统架构: arm64
- 系统版本: 

# 问题

## 解决无法启动 OpenOCD

**过程如下:**

> 方向: 缺少什么就安装什么

### ① 运行 `./openocd`

```
./openocd: error while loading shared libraries: libusb-0.1.so.4: cannot open shared object file: No such file or directory
```

> 缺少 libusb-0.1.so.4

解决方法:

- 安装 libusb-0.1.4 `sudo apt-get install libusb-0.1.4`

  ```
  正在读取软件包列表... 完成
  正在分析软件包的依赖关系树
  正在读取状态信息... 完成
  注意，根据正则表达式 'libusb-0.1.4' 选中了 'libusb-0.1-4'
  下列软件包是自动安装的并且现在不需要了：
    deepin-pw-check fbterm imageworsener libheif1 liblqr-1-0 libmaxminddb0 libqtermwidget5-0 libsmi2ldbl
    libutempter0 libutf8proc2 libwireshark-data libwireshark11 libwiretap8 libwscodecs2 libwsutil9
    qtermwidget5-data squashfs-tools x11-apps x11-session-utils xbitmaps xinit
  使用'sudo apt autoremove'来卸载它(它们)。
  下列【新】软件包将被安装：
    libusb-0.1-4
  升级了 0 个软件包，新安装了 1 个软件包，要卸载 0 个软件包，有 196 个软件包未被升级。
  需要下载 21.5 kB 的归档。
  解压缩后会消耗 59.4 kB 的额外空间。
  获取:1 https://professional-packages.chinauos.com/desktop-professional eagle/main arm64 libusb-0.1-4 arm64 2:0.1.12-32 [21.5 kB]
  已下载 21.5 kB，耗时 1秒 (28.7 kB/s)
  正在选中未选择的软件包 libusb-0.1-4:arm64。
  (正在读取数据库 ... 系统当前共安装有 217799 个文件和目录。)
  准备解压 .../libusb-0.1-4_2%3a0.1.12-32_arm64.deb  ...
  正在解压 libusb-0.1-4:arm64 (2:0.1.12-32) ...
  正在设置 libusb-0.1-4:arm64 (2:0.1.12-32) ...
  正在处理用于 libc-bin (2.28.14-1+dde) 的触发器 ...
  ```

### ② [BUG] 运行 `./openocd`

```
 ./openocd: error while loading shared libraries: libftdi1.so.2: cannot open shared object file: No such file or directory
```

> 缺少 libftdi1.so.2

解决方法:

- 安装 libftdi `sudo apt-get install libftdi1`

  ```
  正在读取软件包列表... 完成
  正在分析软件包的依赖关系树
  正在读取状态信息... 完成
  下列软件包是自动安装的并且现在不需要了：
    deepin-pw-check fbterm imageworsener libheif1 liblqr-1-0 libmaxminddb0 libqtermwidget5-0 libsmi2ldbl
    libutempter0 libutf8proc2 libwireshark-data libwireshark11 libwiretap8 libwscodecs2 libwsutil9
    qtermwidget5-data squashfs-tools x11-apps x11-session-utils xbitmaps xinit
  使用'sudo apt autoremove'来卸载它(它们)。
  下列【新】软件包将被安装：
    libftdi1
  升级了 0 个软件包，新安装了 1 个软件包，要卸载 0 个软件包，有 196 个软件包未被升级。
  需要下载 17.0 kB 的归档。
  解压缩后会消耗 47.1 kB 的额外空间。
  获取:1 https://professional-packages.chinauos.com/desktop-professional eagle/main arm64 libftdi1 arm64 0.20-4 [17.0 kB]
  已下载 17.0 kB，耗时 6秒 (3,055 B/s)
  正在选中未选择的软件包 libftdi1:arm64。
  (正在读取数据库 ... 系统当前共安装有 217806 个文件和目录。)
  准备解压 .../libftdi1_0.20-4_arm64.deb  ...
  正在解压 libftdi1:arm64 (0.20-4) ...
  正在设置 libftdi1:arm64 (0.20-4) ...
  正在处理用于 libc-bin (2.28.14-1+dde) 的触发器 ...
  ```
  > 也就无法成功解决

### ③ 切换 libftdi1 版本 libftdi1 -> libftdi1-2

解决方法:

- 卸载 libftdi `sudo apt-get uninstall libftdi1`

- 安装 libftdi `sudo apt-get install libftdi1-2`

  ```
  正在读取软件包列表... 完成
  正在分析软件包的依赖关系树
  正在读取状态信息... 完成
  下列软件包是自动安装的并且现在不需要了：
    deepin-pw-check fbterm imageworsener libheif1 liblqr-1-0 libmaxminddb0 libqtermwidget5-0 libsmi2ldbl
    libutempter0 libutf8proc2 libwireshark-data libwireshark11 libwiretap8 libwscodecs2 libwsutil9
    qtermwidget5-data squashfs-tools x11-apps x11-session-utils xbitmaps xinit
  使用'sudo apt autoremove'来卸载它(它们)。
  下列【新】软件包将被安装：
    libftdi1-2
  升级了 0 个软件包，新安装了 1 个软件包，要卸载 0 个软件包，有 196 个软件包未被升级。
  需要下载 27.8 kB 的归档。
  解压缩后会消耗 76.8 kB 的额外空间。
  获取:1 https://professional-packages.chinauos.com/desktop-professional eagle/main arm64 libftdi1-2 arm64 1.4-1+b2 [27.8 kB]
  已下载 27.8 kB，耗时 1秒 (53.3 kB/s)
  正在选中未选择的软件包 libftdi1-2:arm64。
  (正在读取数据库 ... 系统当前共安装有 217813 个文件和目录。)
  准备解压 .../libftdi1-2_1.4-1+b2_arm64.deb  ...
  正在解压 libftdi1-2:arm64 (1.4-1+b2) ...
  正在设置 libftdi1-2:arm64 (1.4-1+b2) ...
  正在处理用于 libc-bin (2.28.14-1+dde) 的触发器 ...
  ```

### ④ [BUG] 运行 `./openocd`

```debug
./openocd: error while loading shared libraries: libhidapi-hidraw.so.0: cannot open shared object file: No such file or directory
```

> 缺少 libhidapi-hidraw.so.0

解决方法:

- 下载[libhidapi-0.11.0-alt1_1.aarch64.rpm](https://altlinux.pkgs.org/sisyphus/classic-aarch64/libhidapi-0.11.0-alt1_1.aarch64.rpm.html)

- 安装 rpm alien fakeroot `sudo apt-get install rpm alien fakeroot`

- 使用 rpm 转换成 deb `sudo alien --to-deb libhidapi-0.11.0-alt1_1.aarch64.rpm --target=arm64`

  ```
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  warning: libhidapi-0.11.0-alt1_1.aarch64.rpm: Header V4 RSA/SHA512 Signature, key ID da2773bb: NOKEY
  libhidapi_0.11.0-1_arm64.deb generated
  ```

- 安装 deb 文件 `sudo dpkg -i libhidapi_0.11.0-1_arm64.deb`

### ⑤ [BUG] 运行 `./openocd`

```
./openocd: error while loading shared libraries: libhidapi-hidraw.so.0: cannot open shared object file: No such file or directory
```

解决方法:

- 卸载 libhidapi `sudo dpkg -r libhidapi`

- 安装 libhidapi `sudo apt install libhidapi-dev`

  > 解决成功

### ✔ 总结正确步骤

1. 安装 libusb
   ```
   sudo apt-get install libusb-0.1.4
   ```
2. 安装 libftdi1
   > 这一步或许可以不用(！？)
   > 只需要下面那一步就可以了
   ```
   sudo apt-get install libftdi1
   ```
3. 安装 libftdi1-2
   ```
   sudo apt-get install libftdi1-2
   ```
   > 上述 2,3 可以用 `sudo apt-get install libftdi1-dev` 进行替代
4. 安装 libhidapi
   ```
   sudo apt install libhidapi-dev
   ```

## 解决 ICNS

> 问题代码: ERR_ELECTRON_BUILDER_CANNOT_EXECUTE
> PS: 不是说时这个代码就一定是这个问题

1. 安装 ruby

   ```
   sudo apt-get install ruby rubygems
   ```

2. 修改源

   ```
   gem sources -a http://mirrors.aliyun.com/rubygems/
   gem sources -a https://gems.ruby-china.com/
   gem sources -r https://rubygems.org/
   ```

3. 安装 FPM
   ```
   sudo gem install fpm
   ```