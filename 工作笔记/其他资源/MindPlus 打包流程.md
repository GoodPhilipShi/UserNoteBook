# MindPlus 打包流程

> 当前仓库情况
>
> 1. 已拉仓库(包括子仓库在内的代码、功能)
> 2. 已安装相应的MindPlus环境

通过**Python绿色包**进行分类

1. 全新Python绿色包
2. 全新Python增量包

## 全新Python绿色包

### 通常什么情况下才会走这个流程

1. Python版本更新
2. pinpong库更新

### 步骤

1. 拉取仓库的更新

   1. 代码更新
   2. 依赖库更新

2. 拉取子仓库的更新

   1. Arduino子仓库的更新

      1. 代码更新
      2. 固件更新
      3. 工具更新
      4. static子仓库更新

   2. compat子仓库的更新

      1. 代码更新

      2. 获取云端资源(如果本身就是要更新这些资源的话，则不需要走这一步)

         ```shell
         python update-resources.py
         ```

3. 更新**compat云端资源**

   1. 更新Python

      1. 构建Python绿色包(32/64位)

         > 内容如下:
         >
         1. 纯Python绿色包(无其他库)

         2. 获取Python库

            1. 如果是**Python版本**更新, 则获取当前MindPlus所内置的积木所对应的Python库
            2. 如果只是**pinpong库**更新的话, 就只需要更新绿色包里面的pinpong库

            > ps. 如果存在除了**pinpong库**外的其他库更新的话, 则需要更新增量包
            >
            > > 详细步骤请参考 #全新Python增量包

      2. **Python绿色包**测试过后, 上传至云端(**download3服务器**  - `/var/www/html/MindPlus/Python/resource/window/`)

   2. 更新**行空板的增量包** --> 进行本地更新(由MindPlus软件向行空板进行Python库更新)

      1. 将需要推送的Python包(`.whl`文件)上传至云端(**download3服务器**  - `/var/www/html/MindPlus/Python/resource/ssh/unihiker/`)

         > 目前只有pinpong库需要

      2. 修改`update-resources.py`里面的配置信息

         ```diff
           file_list = [
               {
                   "requesturl": 'window/', 'localdir': '',
                   "filelist": [
                       'Python3.8.5-32.zip', 'Python3.8.5-64.zip',
                       #'Lib.zip', # 增量包，180 RC1.0升级Python版本，暂时没有Lib
                   ],
               },
               {
                   "requesturl": 'ssh/unihiker/', 'localdir': 'ssh\\unihiker\\',
                   'filelist': [
                       'pinpong-0.4.9-py3-none-any.whl'# 行空板的增量包
         +             'xxx.whl'# 在这个位置进行修改、添加
                   ]
               }
           ]; 
         ```

4. 兼容处理\替换资源

   1. 在 MindPlus本地仓库路径下, 运行`python setup.py`

5. 打包

   1. 修改`compat\pack\aftersign.js `文件

      ```diff
        exports.default = async function(context) {
            console.log("afterSign ..........", path.resolve('./'));
            // 打运行exe
      -     // await runCMD("python ./compat/pack/pack.py");
      +     await runCMD("python ./compat/pack/pack.py");
            // 用 签名文件 打安装包exe
      -     await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
      +     // await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
            // 需要修改 签名文件夹地址
      -     await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
      +     // await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
            console.log("afterSign end ..........");
        }
      ```

   2. 在 MindPlus本地仓库路径下, 运行`python buildpack.py`

      > --------------  以上为测试包 -----------------

   3. 测试完成、没有问题后并确定需要发布后，将测试包交由上海(李亮)进行文件签名

   4. 签名完成，将签名后的压缩包解压到桌面

   5. 修改`compat\pack\aftersign.js `文件

      ```diff
        exports.default = async function(context) {
            console.log("afterSign ..........", path.resolve('./'));
            // 打运行exe
      -     await runCMD("python ./compat/pack/pack.py");
      +     // await runCMD("python ./compat/pack/pack.py");
            // 用 签名文件 打安装包exe
      -     // await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
      +    await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
            // 需要修改 签名文件夹地址
      -     // await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
      +     await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
            // 例子: await runCMD("cp <桌面路径>/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
            console.log("afterSign end ..........");
        }
      ```



## 全新Python增量包

### 通常什么情况下才会走这个流程

1. 除pinpong库外的其他库**更新**
2. **添加**除pinpong库外的其他库
3. 当然，pinpong库更新后，也需要在这里进行添加

### 步骤

1. 拉取仓库的更新

   1. 代码更新
   2. 依赖库更新

2. 拉取子仓库的更新

   1. Arduino子仓库的更新

      1. 代码更新
      2. 固件更新
      3. 工具更新
      4. static子仓库更新

   2. compat子仓库的更新

      1. 代码更新

      2. 获取云端资源(如果本身就是要更新这些资源的话，则不需要走这一步)

         ```shell
         python update-resources.py
         ```

3. 更新**compat云端资源**

   1. 更新Python增量包`Lib.zip`

      > 压缩包内容如下:

      ```
      X:\XXX\LIB
      ├─site-packages
      │  └─这里放不需要做32、64版本判断的Python库
      ├─site-packages-32
      │  └─这里放64版本的Python库
      └─site-packages-64
         └─这里放32版本的Python库
      ```

      > 获取Python库方法:

      1. 在纯Python文件夹里面运行`python.exe -m pip install <Python 库的名称>`
      2. 从`纯Python文件夹里面\Lib\site-packages`里面将Python库提取出来
      3. 然后放到`Lib.zip`解压后的文件夹`Lib`里面
      4. 然后再压缩成`Lib.zip`

      > **Python增量包**测试过后, 上传至云端(**download3服务器**  - `/var/www/html/MindPlus/Python/resource/window/`)

   2. 更新**行空板的增量包** --> 进行本地更新(由MindPlus软件向行空板进行Python库更新)

      1. 将需要推送的Python包(`.whl`文件)上传至云端(**download3服务器**  - `/var/www/html/MindPlus/Python/resource/ssh/unihiker/`)

         > 目前只有pinpong库需要

      2. 修改`update-resources.py`里面的配置信息

         ```diff
           file_list = [
               {
                   "requesturl": 'window/', 'localdir': '',
                   "filelist": [
                       'Python3.8.5-32.zip', 'Python3.8.5-64.zip',
                       #'Lib.zip', # 增量包，180 RC1.0升级Python版本，暂时没有Lib
                   ],
               },
               {
                   "requesturl": 'ssh/unihiker/', 'localdir': 'ssh\\unihiker\\',
                   'filelist': [
                       'pinpong-0.4.9-py3-none-any.whl'# 行空板的增量包
         +             'xxx.whl'# 在这个位置进行修改、添加
                   ]
               }
           ]; 
         ```

4. 兼容处理\替换资源

   1. 在 MindPlus本地仓库路径下, 运行`python setup.py`

5. 打包

   1. 修改`compat\pack\aftersign.js `文件

      ```diff
        exports.default = async function(context) {
            console.log("afterSign ..........", path.resolve('./'));
            // 打运行exe
      -     // await runCMD("python ./compat/pack/pack.py");
      +     await runCMD("python ./compat/pack/pack.py");
            // 用 签名文件 打安装包exe
      -     await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
      +     // await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
            // 需要修改 签名文件夹地址
      -     await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
      +     // await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
            console.log("afterSign end ..........");
        }
      ```

   2. 在 MindPlus本地仓库路径下, 运行`python buildpack.py`

      > --------------  以上为测试包 -----------------

   3. 测试完成、没有问题后并确定需要发布后，将测试包交由上海(李亮)进行文件签名

   4. 签名完成，将签名后的压缩包解压到桌面

   5. 修改`compat\pack\aftersign.js `文件

      ```diff
        exports.default = async function(context) {
            console.log("afterSign ..........", path.resolve('./'));
            // 打运行exe
      -     await runCMD("python ./compat/pack/pack.py");
      +     // await runCMD("python ./compat/pack/pack.py");
            // 用 签名文件 打安装包exe
      -     // await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
      +    await runCMD("rm ./scratch/win-ia32-unpacked/* -rf");
            // 需要修改 签名文件夹地址
      -     // await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
      +     await runCMD("cp C:/Users/11834/Desktop/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
            // 例子: await runCMD("cp <桌面路径>/win-ia32-unpacked/* ./scratch/win-ia32-unpacked/ -rf");
            console.log("afterSign end ..........");
        }
      ```
