# linux x86_64 打包

> 很简单，就分三部分: 搭建环境、适配、打包

## 搭建环境

搭建环境也分三部分: 安装程序、搭建仓库、测试环境是否搭建完毕

### 安装程序

| 软件     | 软件版本              | 注释                                                         |
| -------- | --------------------- | ------------------------------------------------------------ |
| git      | 无                    | 没有指定的，只要能够拉取仓库即可                             |
| npm/node | 长期支持版本(16.14.2) | 如果不需要编译`Serialport`、`node-pty`，这样就可以了         |
| python   | 这个指定了要Python3   | 通过`update-alternatives`进行Python版本管理<br />`sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1`<br />`sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2` |

### 搭建Mind+仓库

> 由于仓库过大，所以将仓库分成了两个

| Git仓库链接                              | 注释                |
| ---------------------------------------- | ------------------- |
| https://gitee.com/dfrobotcd/mindPlus2020 | 172以前的源代码仓库 |
| https://gitee.com/dfrobotcd/mindPlus.git |                     |

> 如无意外, 以后适配都是用新的仓库进行
>
> 命令如下:

```shell
git clone -b {mindPlusVersion} git@gitee.com:dfrobotcd/mindPlus.git {mindPath}  --recursive
```

> 例如: 我想要克隆一个**V1.7.2-RC2.0**分支的仓库到桌面的TEST文件夹(**~/Desktop/TEST**)中

```
git clone -b V1.7.2-RC2.0 git@gitee.com:dfrobotcd/mindPlus.git ~/Desktop/TEST  --recursive
```

> 然后就是查看子仓库是否与预计不一样

| 子仓库                         | 版本                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| `Arduino`                      | 与Mind+的大版本基本持平<br />例如：`Mind+@V1.7.2-RC2.0`, 那么`Arduino@V1.7.2`<br />`Mind+@V1.7.2-RC1.0`, 那么`Arduino@V1.7.2` |
| `static`<br />`Arduino\static` | 与Arduino的大版本基本持平<br />例如：当前系统为linux amd64(x86_64)，并且`Arduino@V1.7.2`, 那么`static@linux-amd64-V1.7.2` |
| `compat`                       | 是什么系统就是什么分支<br />例如: 当前系统为linux系统，那么分支就是linux |

> ps. 大部分情况下，`static`不存在可以拉取的分支，需要自己去编译SDK

#### 编译SDK

1. 下载并解压编译工具

   ```shell
   cd Arduino
   python setup.py
   ```

2. 开始编译

   ```shell
   cd Arduino/compile
   python office  --build --includes -b 主板ID
   ```

   or

   ```shell
   python build.py
   ```

### 测试环境是否搭建完毕

> 测试前，则需要先安装依赖库
>
> 如下三个路径需要安装依赖库
>
> `mindPlus`
>
> `mindPlus\otherModules\scratch-l10n`
>
> `mindPlus\otherModules\scratch-vm`

#### 安装依赖库

```shell
# mindPlus
cd ./
npm install

# mindPlus\otherModules\scratch-l10n
cd ./otherModules/scratch-l10n
npm install

# mindPlus\otherModules\scratch-vm
cd ./otherModules/scratch-vm
npm install
```

> 在安装依赖完成后
>
> 编译一下翻译(**scratch-l10n**)
> 

#### 编译翻译

```shell
cd ./otherModules/scratch-l10n
npm run build
```

> 一切准备就绪, 开始测试环境

#### 运行开发版Mind+

```shell
python build.py && python buildvm.py
```

> 有问题就先记录下来，基本上问题都是大小写问题

## 适配

### 测试

1. 测试上传模式(AC/MP)

   > AC: 每个主板, 在每个模块分类选择一个模块，然后再从模块中选出一个积木拼在一起进行编译、烧录测试
   >
   > MP: 测试固件烧录

2. 测试实时模式

   > 基础JS: 每个分类选择一个积木运行
   >
   > 主板JS: 先测试固件烧录、然后测试主板控制积木
   >
   > 小模块JS: 每个模块选择一个积木运行

3. 测试Python模式

   > 每个模块选择一个，然后运行

### 初次修复

将测试中出现的问题修复完成就可以了

### 再次修复xN

在初次修复完成后，打包交测，出现的BUG就修复

## 打包

> 除了最后的打包外也会进行多次打包(交测->修复BUG)

```shell
python buildpack.py
```

