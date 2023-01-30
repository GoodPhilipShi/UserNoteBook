# MAC 打包

> 在打包之前，要先在对适配、修改好的代码进行push上传
>
> 原因: 打包签名之后就会导致所有文件都会被签名(文件字节变大、但是通过`git diff`进行比较，代码并没有被修改)
>
> ps. 2023时公证脚本需要重新编写(之前的工具已经被弃用)

## 一、事先需要签名的文件

- **[这个比较重要, 部分可被检测出来] `Arduino`**[已签名打包上传，大概率不会有变动也就不需要签名]
  - `Arduino\arduino-builder\arduino-builder`
  - `Arduino\arduino-builder\ctags`
  - `Arduino\hardware\tools\avr`
    - 里面的大部分文件(主要还是程序主体、库文件)
  - `Arduino\hardware\tools\maixduino`
    - 里面的大部分文件(主要还是程序主体、库文件)
  - `Arduino\hardware\tools\mpython`
    - 里面的大部分文件(主要还是程序主体、库文件)
  - `Arduino\hardware\tools\nRF5`
    - 里面的大部分文件(主要还是程序主体、库文件)
- **[不签名可被检测出来] `compat`**
  - `compat\Python3.6.5.zip`[大概率后期，还会重新编译185版本的Python，到时候还需要签名]
    - 需要先解压，再签名
      - 可以先不签名，然后再公证，等待公证结果，再根据公证结果编写签名列表进行批量签名
  - `compat\Lib.zip`[后续只要添加一个扩展，基本就需要签名]
  - `compat\node-pty-prebuilt-multiarch`
  - `compat\serialport`


### 【Arduino】通过`python setup.py`进行下载tools-dxx-1.0.tar.gz和arduino-builder.tar.gz

> 将最后一条语句禁止掉
> 删除hardware\tools文件夹
> 记住下载后，请手动解压tools.tar.gz并重命名为tools
> 最后手动删除下载下来的那两个压缩包

当然也是进行处理的，仅做了解(万一脚本存在问题)


## 二、最后

通过下述命令可以一条龙打包服务

```python
python buildpack.py
```

如果在上述命令运行中，如果打包报错，可以在修改错误之后通过下述命令继续打包签名公证

```
npm run pack
sh compat/pack/mac-notarization.sh ./scratch/Mind+-1.7.2-202206281900.dmg
```

## 三、疑难收集

### 分类: 签名阶段

#### 1. electron-builder > signing(进度): 'xxx../MacOS/Mind+': code object is not signed at all

>  错误详情:

```
  • signing         file=scratch/mac/Mind+.app identityName=Developer ID Application: Shanghai Zhiwei Robotics Co Ltd (7ALKBE5TF4) identityHash=E2119AFE2DDDDADD30B23A3DD3EBC8BCD4C1CDA5 provisioningProfile=none
	failedTask=build stackTrace=Error: Command failed: codesign --sign E2119AFE2DDDDADD30B23A3DD3EBC8BCD4C1CDA5 --force --timestamp --options runtime/Users/dfrobot/Desktop/xxx/testMindPlus/scratch/mac/Mind+.app/Contents/MacOS/Mind+: code object is not signed at all
In subcomponent: /Users/dfrobot/Desktop/xxx/testMindPlus/scratch/mac/Mind+.app/Contents/favicon.icns
```

解决方法: 

```
codesign --force --verify --verbose --deep --options=runtime --timestamp -fs "Developer ID Application: Shanghai Zhiwei Robotics Co Ltd (7ALKBE5TF4)" ./scratch/mac/Mind+.app/Contents/favicon.icns
```

#### 2. electron-builder > signing(进度): Operation not permitted

>  错误详情:

```
• signing         file=scratch/mac/Mind+.app identityName=Developer ID Application: Shanghai Zhiwei Robotics Co Ltd (7ALKBE5TF4) identityHash=E2119AFE2DDDDADD30B23A3DD3EBC8BCD4C1CDA5 provisioningProfile=none
..........commend: codesign xxxxxxx/MacOS/Mind+: Operation not permitted
```

解决方法: 

> 不要使用`sudo codesign`对`MacOS\Mind+`签名

#### 3. electron-builder > signing(进度):  A timestamp was expected but was not found.

>  错误详情: 只要出现了报错中timestamp

解决方法: 

> 重新打包

### 分类: 公证阶段

#### 1. 上传失败: Upload Id is

>  错误详情:

```
####### Notarization Script / dmgNotarization start #######
公证时间比较长，请耐心等待...
step1: checking /Users/dfrobot/Desktop/xxx/mindPlus/scratch/Mind+-1.7.2-202207281900.dmg
step2: uploading /Users/dfrobot/Desktop/xxx/mindPlus/scratch/Mind+-1.7.2-202207281900.dmg ...
Password:
The software asset has already been uploaded. The upload ID is 
No success no uploaded, unknown error
sudo: a password is required
####### Notarization Script / dmgNotarization failed #######
```

解决方法: 

> 等上一段时间之后再重新进行公证

#### 2. 公证结果: The signature of the binary is invalid.(凡是包含signature)

```
{
  "logFormatVersion": 1,
  "jobId": "adf250ca-ee72-446d-94de-31bfe3ef3523",
  "status": "Invalid",
  "statusSummary": "Archive contains critical validation errors",
  "statusCode": 4000,
  "archiveFilename": "Mind+-1.7.2-202206281900.dmg",
  "uploadDate": "2022-07-27T09:51:58Z",
  "sha256": "7c63a7d82c51ff6b91e74481b8f4deb512f8563a9bf63a02c51c920c389e78df",
  "ticketContents": null,
  "issues": [
    {
      "severity": "error",
      "code": null,
      "path": "Mind+-1.7.2-202206281900.dmg/Mind+.app/Contents/openNetNetWorkr.applescript",
      "message": "The signature of the binary is invalid.",
      "docUrl": null,
      "architecture": "x86_64"
    }
  ]
}
```

(99%可行)解决方法: 

> ① 运行下述代码直接进行签名，然后继续git上传
>
> ② 在打包的过程中签名, 方法为: 在pack.py中添加下述代码

```
codesign --force --verify --verbose --deep --options=runtime --timestamp -fs "Developer ID Application: Shanghai Zhiwei Robotics Co Ltd (7ALKBE5TF4)" 待签名的文件路径
```

(1%可行)解决方法: 

> Mind+.app/Contents/Mind+: The signature of the binary is invalid.
>
> 极大可能是**Arduino的工具包存在签名问题**

