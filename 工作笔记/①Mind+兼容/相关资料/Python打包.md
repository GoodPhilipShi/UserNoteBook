# Python打包

# 编译步骤

## 1. 下载源码

[Python-3.6.5.tar.xz](https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz)

## 2. 下载libreadline-dev

>为了防止**python**交互模式下按**方向键**出现`^[[A ^[[B ^[[C ^[[D`

```shell
sudo apt-get install libreadline-dev
```


## 3. 创建用于存放打包的文件夹

```shell
cd ~/Desktop
mkdir Python-3.6.5-build
```

## 4. 生成Makefile文件

```shell
# ./configure --prefix=`pwd`/../Python-3.6.5-build --enable-optimizations

./configure --prefix=`pwd`/../Python-3.6.5-build
```

> 启用`--enable-optimizations`，估计需要翻墙才行(?)
> 其中的错误: `[[SSL: EE_KEY_TOO_SMALL] ee key too small`(密钥太短了....emm)

## 5. 编译

```
make -j8
```

## 6. 安装

```
make install
```