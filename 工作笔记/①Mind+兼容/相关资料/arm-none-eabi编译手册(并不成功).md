# ① 克隆 crosstool-NG

```
git clone https://github.com/crosstool-ng/crosstool-ng.git crosstool-NG-1.24.0
```

> 不用重命名项目名称为`crosstool-NG-1.24.0`

# ② [可能] 安装依赖 texinfo(主要是为了 makeinfo) help2man

> 因为之前编译`Xtensa-esp32-elf`时安装了的
>
> [安装 texinfo 的原因](https://blog.csdn.net/cw616729/article/details/107179809)

```
sudo apt-get install texinfo help2man
```

# ③ [可能] 安装依赖 libtool(libtool >= 1.5.26)

最好就是 libtool v1.5.26

> [libtool 源代码](http://ftp.gnu.org/gnu/libtool/)

- 卸载 libtool

```
sudo apt-get remove libtool
```

- 编译并安装

```
./configure && make && sudo make install
```

# ④ 编译 crosstool-NG

```
# 源代码使用
./bootstrap && ./configure --prefix=`pwd` && make && make install
# 注册到电脑，然后使用
./bootstrap && ./configure && make && sudo make install
```

> 我这里用的是第一种方法
> ps. 一定要安装，这样程序运行所需要的依赖资源就可以放到正确的位置上去

# ⑤ 切换打包编译的配置

```
./ct-ng arm-unknown-eabi
```

# ⑥ 更改交叉编译器内部 GCC 版本配置、交叉编译器名称(部分名称)

> 打开`.config`

```diff
- CT_THREADS="unknown"
+ CT_THREADS="none"
  ...
- CT_GCC_VERSION="8.3.0"
+ CT_GCC_VERSION="10.2.0"
```

> 最新版(2022年8月16日，版本(当前发布): crosstool-ng-1.25.0), 以上的修改就可以不用管了

```diff
- CT_TARGET_VENDOR="unknown"
+ CT_TARGET_VENDOR="none"
```

# ⑦ 安装打包依赖(手动) or 自动安装打包依赖

> 推荐自动安装打包依赖 + 手动安装打包依赖
> 即先`./ct-ng build`，然后查看`build.log`查看编译日志
> 然后再去下载相应的包放在`[ct-ng程序路径]/.build/tarballs`即可

- 目前的话，会下载失败的包，我已放在我工作电脑的 F 盘/MindPlus 兼容/MindPlus_Esp 编译器兼容/crosstool-NG 的依赖(也可以通过我的电脑 IP 进行访问我的分享网盘)

> 以下就是我在打包安装依赖时遇到的几个无法通过自动安装打包依赖完成下载的包

| 包            | 下载地址                                                                               |
| ------------- | -------------------------------------------------------------------------------------- |
| isl.tar.bz2   | [Index of /pub/gcc/infrastructure](https://gcc.gnu.org/pub/gcc/infrastructure/)        |
| expat.tar.bz2 | [Expat XML Parser download \| SourceForge.net](https://sourceforge.net/projects/expat) |
| newlib.tar.gz | [newlib ftp directory](https://sourceware.org/ftp/newlib/index.html)                   |

# ⑧ 最后还需要添加一些库

> 添加原因: 缺少的话就会报错 `cannot find -lc_name`等等类似的错误
>
> 添加相应的\*\_nano.a
>

> 来源于: [yotta_osx_installer/prerequisites/gcc-arm-none-eabi-4_9-2015q3/arm-none-eabi/lib at master · ARMmbed/yotta_osx_installer · GitHub](https://github.com/ARMmbed/yotta_osx_installer/tree/master/prerequisites/gcc-arm-none-eabi-4_9-2015q3/arm-none-eabi/lib)

| 包名              |
| ----------------- |
| libc_nano.a       |
| libg_nano.a       |
| librdimon_nano.a  |
| libstdc++\_nano.a |
| libsupc++\_nano.a |
