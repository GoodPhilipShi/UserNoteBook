### 源码

0. [OpenOCD For openocd.org](https://www.openocd.org/pages/getting-openocd.html)
   
   > 官网上的信息

1. [OpenOCD For Github](https://github.com/openocd-org/openocd)
   
   > 只有最新版本的代码

2. [OpenOCD For sourceforge](https://sourceforge.net/projects/openocd/files/openocd/)
   
   > 拥有多个版本的源代码

### 编译方法

1. [openocd编译安装](https://blog.csdn.net/task_struct/article/details/113094980)
2. [OpenOCD安装与使用（JTAG调试）](https://www.cnblogs.com/ImagineMiracle-wxn/p/Riscv-OpenOCD_And_JTAG.html)
3. [Linux 环境下从源码编译 OpenOCD](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.0/api-guides/jtag-debugging/building-openocd-linux.html)
4. [OpenOCD安装与使用（JTAG调试）](https://www.bbsmax.com/A/Vx5MDGgvJN/)

# 编译V0.10.0

## 下载并解压源代码

[OpenOCD - Open On-Chip Debugger V0.10.0 from SourceForge.net](https://sourceforge.net/projects/openocd/files/openocd/0.10.0/openocd-0.10.0.zip/download)

> 使用`归档管理器`解压`openocd-0.10.0.zip`到桌面

## 创建用于存放打包的文件夹

```shell
cd ~/Desktop
mkdir openocd-build
```

## 生成Makefile文件

> 一开始, 未指定参数

```shell
./configure --prefix=`pwd`/../openocd-build
```

> 加加加...

```shell
./configure --prefix=`pwd`/../openocd-build --enable-cmsis-dap --enable-sysfsgpio --enable-usb-blaster-2 --enable-openjtag --enable-ftdi
```

```shell
OpenOCD configuration summary
--------------------------------------------------
MPSSE mode of FTDI based devices        yes
ST-Link JTAG Programmer                 yes (auto)
TI ICDI JTAG Programmer                 yes (auto)
Keil ULINK JTAG Programmer              yes (auto)
Altera USB-Blaster II Compatible        yes
Versaloon-Link JTAG Programmer          yes (auto)
OSBDM (JTAG only) Programmer            yes (auto)
eStick/opendous JTAG Programmer         yes (auto)
Andes JTAG Programmer                   yes (auto)
USBProg JTAG Programmer                 no
Raisonance RLink JTAG Programmer        no
Olimex ARM-JTAG-EW Programmer           no
CMSIS-DAP Compliant Debugger            yes
Altera USB-Blaster Compatible           yes (auto)
ASIX Presto Adapter                     yes (auto)
OpenJTAG Adapter                        yes
SEGGER J-Link Programmer                yes (auto)
```

```shell
./configure --prefix=`pwd`/../openocd-build --enable-cmsis-dap --enable-cmsis-dap-v2 --enable-sysfsgpio --enable-usb-blaster-2 --enable-openjtag --enable-ftdi --enable-usbprog --enable-rlink --enable-armjtagew
```

```shell
OpenOCD configuration summary
--------------------------------------------------
MPSSE mode of FTDI based devices        yes
ST-Link JTAG Programmer                 yes (auto)
TI ICDI JTAG Programmer                 yes (auto)
Keil ULINK JTAG Programmer              yes (auto)
Altera USB-Blaster II Compatible        yes
Versaloon-Link JTAG Programmer          yes (auto)
OSBDM (JTAG only) Programmer            yes (auto)
eStick/opendous JTAG Programmer         yes (auto)
Andes JTAG Programmer                   yes (auto)
USBProg JTAG Programmer                 yes
Raisonance RLink JTAG Programmer        yes
Olimex ARM-JTAG-EW Programmer           yes
CMSIS-DAP Compliant Debugger            yes
Altera USB-Blaster Compatible           yes (auto)
ASIX Presto Adapter                     yes (auto)
OpenJTAG Adapter                        yes
SEGGER J-Link Programmer                yes (auto)
```

## 开始编译

> 以8线程(同时进行8个编译命令)进行编译

```shell
make -j8
```

### 遇到的报错

#### ①报错代码: `[-Werror=implicit-fallthrough=]`

```shell
src/svf/svf.c: In function ‘svf_read_command_from_file’:
src/svf/svf.c:663:7: error: this statement may fall through [-Werror=implicit-fallthrough=]
     i = -1;
     ~~^~~~
src/svf/svf.c:664:4: note: here
    case '\r':
    ^~~~
src/svf/svf.c:667:8: error: this statement may fall through [-Werror=implicit-fallthrough=]
     if (!cmd_pos)
        ^
src/svf/svf.c:669:4: note: here
    default:
    ^~~~~~~
```

> 解决方法: 忽略该错误继续编译即可

```shell
make -j8 CFLAGS='-Wno-implicit-fallthrough'
```

#### ②报错代码: `[-Werror=tautological-compare]`

```text
src/target/arm_disassembler.c: In function ‘evaluate_misc_instr’:
src/target/arm_disassembler.c:1499:30: error: bitwise comparison always evaluates to false [-Werror=tautological-compare]
   if (((opcode & 0x00600000) == 0x00100000) && (x == 0)) {
                              ^~
src/target/arm_disassembler.c:1521:29: error: bitwise comparison always evaluates to false [-Werror=tautological-compare]
   if ((opcode & 0x00600000) == 0x00300000) {
                             ^~
src/target/arm_disassembler.c:1542:30: error: bitwise comparison always evaluates to false [-Werror=tautological-compare]
   if (((opcode & 0x00600000) == 0x00100000) && (x == 1)) {
                              ^~
```

> 解决方法: 然后将报错的三个位置进行修改(`==`改成`-`)

##### 修改1

```shell
vim src/target/arm_disassembler.c +1499
```

```diff
-   if (((opcode & 0x00600000) == 0x00100000) && (x == 0)) {
+   if (((opcode & 0x00600000) - 0x00100000) && (x == 0)) {
```

```shell
:wq
```

##### 修改2

```shell
vim src/target/arm_disassembler.c +1521
```

```diff
-   if ((opcode & 0x00600000) == 0x00300000) {
+   if ((opcode & 0x00600000) - 0x00300000) {
```

```shell
:wq
```

##### 修改3

```shell
vim src/target/arm_disassembler.c +1542
```

```diff
-   if (((opcode & 0x00600000) == 0x00100000) && (x == 1)) {
+   if (((opcode & 0x00600000) - 0x00100000) && (x == 1)) {
```

```shell
:wq
```

#### ③报错3: `[-Werror=format-overflow=]`

```shell
src/target/nds32_cmd.c: In function ‘jim_nds32_bulk_read’:
src/target/nds32_cmd.c:824:21: error: ‘sprintf’ writing a terminating nul past the end of the destination [-Werror=format-overflow=]
   sprintf(data_str, "0x%08" PRIx32 " ", data[i]);
                     ^~~~~~~
src/target/nds32_cmd.c:824:38: note: format string is defined here
   sprintf(data_str, "0x%08" PRIx32 " ", data[i]);
                                      ^
src/target/nds32_cmd.c:824:3: note: ‘sprintf’ output 12 bytes into a destination of size 11
   sprintf(data_str, "0x%08" PRIx32 " ", data[i]);
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

> 解决方法: 忽略该错误继续编译即可

```shell
make -j8 CFLAGS='-Wno-implicit-fallthrough -Wno-format-overflow'
```

## 安装到`openocd-build`

```shell
make install
```
