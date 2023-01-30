# 🚀 Scratch-Link全手册(Win)

## 搭建Scratch-Link环境

### 步骤①: 安装Visual Studio(社区版即可)

下载地址: [~~下载 Visual Studio Tools - 免费安装 Windows、Mac、Linux~~](https://visualstudio.microsoft.com/zh-hans/downloads/)

> 💥 推荐安装Visual Studio 2019版本
>
> Visual Studio 2022版本没有Windows 10.0.16299 SDK

下载VS2019: [Visual Studio 2019(VS2019)正式版下载-Visual Studio 2019破解版-华军软件园](https://www.onlinedown.net/soft/1226702.htm)

或者 直接百度"VS2019"进行下载即可

#### Ⅰ 双击安装包

![image-20220518141725097](image-20220518141725097.png)

> 点击 **<继续>**
>
> 然后等待下载并安装成功

#### Ⅱ 安装Visual Studio Community 2019

![image-20220518142215586](image-20220518142215586.png)

#### Ⅲ 配置Visual Studio Community 2019

##### Ⅲ.Ⅰ 选择程序<u>主体部分</u>

> 就选择这两个，其他的就不用管，默认的就行

![image-20220518142638768](image-20220518142638768.png)

##### Ⅲ.Ⅱ 选择程序主要<u>组件</u>

> 其余默认，不用管

![安装Windows 10.0.16299 SDK](image-20220518142546884.png)

![安装.NET Framework 4.6.2](image-20220518142718850.png)



#### Ⅳ 设置Visual Studio Community 2019的安装路径

> [!NOTE] 注意事项
> Visual Studio IDE(程序主体) 路径就随便就可以了
>
> 下载缓存, 默认即可。另外, 安装后保存下载缓存(是否勾选都可以，推荐不要勾选) -- 改动之后，会出现严重问题
>
> 共享组件、工具和SDK，同上

![image-20220518143910359](image-20220518143910359.png)

> 然后，点击 **<安装>**

![image-20220518144944103](image-20220518144944103.png)

> 等待即可

### 步骤②: 打开Scratch-Link

#### Ⅰ 打开\克隆Scratch-Link

##### Ⅰ.Ⅰ 打开Scratch-Link

```git
git clone https://github.com/LLK/scratch-link.git
```

> 然后, 使用Visual Studio Community 2019打开Scratch-Link

![image-20220518145143606](image-20220518145143606.png)

![image-20220518145210484](image-20220518145210484.png)

> 然后，点击 **<打开>**

##### Ⅰ.Ⅱ 克隆Scratch-Link

![image-20220518145252339](image-20220518145252339.png)

> 然后，点击 **<克隆>**

### 步骤③: 编译Scratch-Link

>[!TIP] 注意: 记得改WebSocketServer的端口
>修改`scratch-link\Windows\scratch-link\App.cs`的`SDMPort`的值为`20110`

#### Ⅰ 生成图标

> 路径: scratch-link\Windows

```
bash generate-images.sh
```

or

双击 generate-images.sh

> 图标文件会生成到scratch-link\Windows\scratch-link\Resources

#### Ⅱ 开始编译

![image-20220523090843325](image-20220523090843325.png)

![image-20220523090947685](image-20220523090947685.png)

## Scratch-Link打包

### 步骤①: 安装插件打包插件Microsoft Visual Studio Installer Projects

![image-20220518145526493](image-20220518145526493.png)

![image-20220518145413237](image-20220518145413237.png)

> 关闭Visual Studio Community 2019，等待安装Microsoft Visual Studio Installer Projects

![image-20220518145637731](image-20220518145637731.png)



### 步骤②: 编辑打包项目ScratchLinkAppSetup

#### Ⅰ 新建 -> 项目

![devenv_JOIoJw1d3b](devenv_JOIoJw1d3b.png)

#### Ⅱ 创建新项目

![image-20220518170503597](image-20220518170503597.png)

#### Ⅲ 填写项目信息

![image-20220518170746503](image-20220518170746503.png)

然后，点击 **<创建>**

![image-20220518171611298](image-20220518171611298.png)

#### Ⅳ 编辑安装包信息

![image-20220518171715163](image-20220518171715163.png)

![image-20220518171740255](image-20220518171740255.png)

> 下图只是一个示例

![image-20220518171920508](image-20220518171920508.png)

> ps. **Manufacturer** 和 **ProductName**会导致两件事情:
>
> 	1. 默认的安装路径会变成: **C:\Program Files (x86)\成都极趣\安装包**
> 	1. 在应用管理器上会显示程序名为 **安装包**

> pps. 每次重新打安装包，如果需要覆盖安装的话，就要修改**UpgradeCode**

#### Ⅴ 🚩 添加项目输出(每次程序重新打包后打安装包都要于此重新开始)

![image-20220518172150356](image-20220518172150356.png)

![image-20220518172258606](image-20220518172258606.png)

![image-20220518172211220](image-20220518172211220.png)

#### Ⅵ 添加图标文件(这里可以不做，让快捷方法的图片和程序图标保持一致)

![image-20220518172418649](image-20220518172418649.png)

![image-20220518172438759](image-20220518172438759.png)

#### Ⅶ 创建快捷方式

![image-20220519084925394](image-20220519084925394.png)

![image-20220519084954832](image-20220519084954832.png)

![image-20220520093012535](image-20220520093012535.png)

![image-20220518172600120](image-20220518172600120.png)

> 点击 **<Browse>**

![image-20220518172619610](image-20220518172619610.png)

> 选中 **<Application Folder>**, 点击 **<OK>**

![image-20220520093111593](image-20220520093111593.png)

>选中 **<Executable Files(*.exe)>**

![image-20220520093210004](image-20220520093210004.png)



> 选中 **<主输出 from ScratchLink (Action)>**, 点击 **<OK>**

![image-20220520093252791](image-20220520093252791.png)

>点击 **<OK>**

#### Ⅷ 修改安装.NET Framework版本

![image-20220519090825774](image-20220519090825774.png)

> 双击**<Microsoft .NET Framework>**

![image-20220519091021356](image-20220519091021356.png)

![image-20220519091108068](image-20220519091108068.png)

> 如果不清楚程序的**.NET Framework版本**，就可以先选**Any**
>
> 不过目前也是清楚的, 要选**.NET Framework 4.6.2**

#### Ⅸ 打包


![image-20220520094211274](image-20220520094211274.png)

![image-20220520094226608](image-20220520094226608.png)

> ps. 可以通过下图进行切换打包后的路径(以及不同的打包配置，具体详情就不是很清楚)
>
> ![image-20220520094402644](image-20220520094402644.png)

#### Ⅹ 发布(?)

> 如果想要找到安装在哪里

![image-20220520094450236](image-20220520094450236.png)

![image-20220520094528572](image-20220520094528572.png)

> 根据上一步的选择(**Debug** or **Release**), 来判断安装在那个文件夹中

![image-20220520094711282](image-20220520094711282.png)

> **ScratchLinkAppSetup.msi**: 这个才是你的安装包
>
> **setup.exe**: 就是一个调用**ScratchLinkAppSetup.msi**的小程序

## Scratch-Link代码修改

### 去SSL证书校验

> 2022年5月20日 10点00分
>
> 源代码拉取至**第532次cmmits**
>
> >  [fix macOS code signing on CI · LLK/scratch-link@f78273b · GitHub](https://github.com/LLK/scratch-link/commit/f78273b9003bc0272dbcfb8a39a5a1358de89007)
>
> 当前代码已去除SSL证书校验

# 🔥 Scratch-Link全手册(Mac)

## 搭建Scratch-Link环境

### 步骤①: 安装Xcode

> 推荐: 通过**App Store**进行安装

> 由于当前系统为**Mac OS 11.2.1**
> 所以需要下载[Xcode 12.4](https://download.developer.apple.com/Developer_Tools/Xcode_12.4/Xcode_12.4.xip)

### 步骤②: 打开Scratch-Link

#### Ⅰ 打开\克隆Scratch-Link

#### Ⅰ.Ⅰ 打开Scratch-Link

```shell
git clone https://github.com/LLK/scratch-link.git
```

> 然后使用Xcode打开文件

![image-20220520152549791](image-20220520152549791.png)

> 点击**<Open a project or file>**

![image-20220520153444563](image-20220520153444563.png)

> 选中**<macOS>**, 然后点击**<Open>**

#### Ⅰ.Ⅱ 克隆Scratch-Link(待研究，clone了半天就是clone不成功)

![image-20220520152852432](image-20220520152852432.png)

> 点击**<Clone an existing project>**

![image-20220520152945163](image-20220520152945163.png)

> 填入**https://github.com/LLK/scratch-link.git**，然后点击**<Clone>**

![image-20220520153001733](image-20220520153001733.png)

## Scratch-Link打包

### 步骤①: 通过Xcode进行debug调试

> 刚开始的时候会下载依赖库。(如果下载失败，可以考虑一下翻墙[重新打开项目就可以重新下载依赖库])
>
> 依赖库的话就是下图圈中的

![image-20220520160507741](image-20220520160507741.png)

> 点击**<▶️>**

![image-20220520160333454](image-20220520160333454.png)

> 如果运行正常，那么你就成功了99%
>
> 下一步就是打开[ScratchWeb页面(这个需要翻墙)](https://scratch.mit.edu/projects/editor/?tutorial=getStarted)，通过”Lego“扩展库进行测试(随便选一个LEGO库就行了)

![image-20220520162347856](image-20220520162347856.png)

![image-20220520162442837](image-20220520162442837.png)

> 打开**开发者工具**，然后点击**<Start Searching>**

![image-20220520162505247](image-20220520162505247.png)

> 查看开发者工具->**Network**

![image-20220520162749313](image-20220520162749313.png)

> 链接成功，成功100%

### 步骤②: 使用`make`进行打包

> 路径: scratch-link/macOS

```shell
sudo make
```

![image-20220520154927774](image-20220520154927774.png)

#### 下载相应的库

> 路径: scratch-link/macOS/.build/repositories
>


> 可能会卡在第一步，我就将库打包了
>
> 蓝奏云: [ScratchLink打包的依赖打包](https://liuji.lanzouj.com/ivj5u055qk2j)
>
> 下载下来，将压缩包内的所有文件、文件夹都解压到scratch-link/macOS/.build/repositories

#### 生成图片合集Scratch Link.iconset

> 💡 如果卡住\错误了，就继续`sudo make`

![image-20220520155311934](image-20220520155311934.png)

#### 生成图片合集iconTemplate.iconset

> 💡 如果卡住\错误了，就继续`sudo make`

![image-20220520155356080](image-20220520155356080.png)

#### 生成程序Scratch Link.app

> 💡 如果卡住\错误了，就继续`sudo make`

![image-20220520155840146](image-20220520155840146.png)

> Ps. 我打包就`sudo make`三次
>
> 	1. 第一次生成Scratch Link.iconset
> 	2. 第二次生成iconTemplate.iconset
> 	3. 第三次生成Scratch Link.app

### 步骤③: 生成dmg包

> 随便百度一下**生成dmg文件**

https://jingyan.baidu.com/article/4e5b3e1953b991d0901e2480.html

## Scratch-Link代码修改

### 去SSL校验

> 2022年5月20日 10点00分
>
> 源代码拉取至**第532次cmmits**
>
> >  [fix macOS code signing on CI · LLK/scratch-link@f78273b · GitHub](https://github.com/LLK/scratch-link/commit/f78273b9003bc0272dbcfb8a39a5a1358de89007)
>
> 当前代码已去除SSL证书校验

# 💨 疑难杂症方法合集

## 不管怎么卸载都无法修改`共享组件、工具和SDK`

![image-20220520141037828](image-20220520141037828.png)

**解决方法:**

> ❗ 建议在删除前先进行备份

 1. 打开注册表编辑器

 2. 找到 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\VisualStudio`

    > 路径: 计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\VisualStudio

 3. 删除 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\VisualStudio`

 4. 重新启动 **Visual Studio Installer**

