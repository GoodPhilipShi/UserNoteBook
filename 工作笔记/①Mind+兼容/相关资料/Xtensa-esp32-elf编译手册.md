> 例子来源于: [GitHub - espressif/crosstool-NG: crosstool-NG with support for Xtensa](https://github.com/espressif/crosstool-ng)

## 1. 克隆crosstool-NG

```
git clone -b xtensa-1.22.x git://github.com/jcmvbkbc/crosstool-NG.git crosstool-NG-xtensa-1.22.x
```

## 安装依赖 texinfo(主要是为了makeinfo) help2man

> [安装texinfo的原因](https://blog.csdn.net/cw616729/article/details/107179809)

```
sudo apt-get install texinfo help2man
```

## 安装依赖 libtool(libtool >= 1.5.26)

最好就是libtool v1.5.26

> [libtool源代码](http://ftp.gnu.org/gnu/libtool/)

- 卸载libtool

```
sudo apt-get remove libtool
```

- 编译并安装

```
./configure && make && sudo make install
```

## 编译crosstool-NG

```
# 源代码使用
./bootstrap && ./configure --prefix=`pwd` && make && make install
# 注册到电脑，然后使用
./bootstrap && ./configure && make && sudo make install
```
> 我这里用的是第一种方法
> ps. 一定要安装，这样程序运行所需要的依赖资源就可以放到正确的位置上去

## 切换打包编译的配置

> 这一步很重要

```
./ct-ng xtensa-esp32-elf
```

## 安装打包依赖(手动) or 自动安装打包依赖

> 推荐自动安装打包依赖 + 手动安装打包依赖
> 即先`./ct-ng build`，然后查看`build.log`查看编译日志
> 然后再去下载相应的包放在`[ct-ng程序路径]/.build/tarballs`即

- 目前的话，会下载失败的包，我已放在我工作电脑的F盘/MindPlus兼容/MindPlus_Esp编译器兼容/crosstool-NG的依赖(也可以通过我的电脑IP进行访问我的分享网盘)

> 以下就是我在打包安装依赖时遇到的几个无法通过自动安装打包依赖完成下载的包

| 包            | 下载地址                                                     |
| ------------- | ------------------------------------------------------------ |
| isl.tar.bz2   | [Index of /pub/gcc/infrastructure](https://gcc.gnu.org/pub/gcc/infrastructure/) |
| expat.tar.bz2 | [Expat XML Parser download \| SourceForge.net](https://sourceforge.net/projects/expat) |
| newlib.tar.gz | [newlib ftp directory](https://sourceware.org/ftp/newlib/index.html) |

## 最后，在打包的结尾可能会出现以下问题

> [ERROR]  >>  Build failed in step 'Installing cross-gdb'

我的解决方法是禁用gdb调试，即将`.config`中的`CT_DEBUG_gdb=y`修改从`CT_DEBUG_gdb=n`

ps: 来自于[cross-gdb build fails · Issue #254 · pfalcon/esp-open-sdk · GitHub](https://github.com/pfalcon/esp-open-sdk/issues/254#issuecomment-747782394)
