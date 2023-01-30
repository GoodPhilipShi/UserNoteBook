> 这里使用的库是`easywebdav`
>
> python3在使用时需要将`basestring`替换成`str`
>
> 位置：`Lib\site-packages\easywebdav\client.py`

# `EasyWebDAV`: Python中的WebDAV 客户端

## 特征

- 基本认证
- 创建目录，删除目录和文件
- 上载和下载文件
- 目录清单
- 支持客户端SSL证书

## 安装

使用distribute进行安装

```python
easy_install easywebdav
```

使用pip进行安装

```python
pip install easywebdav
```

## 快速开始

```python
import easywebdav
# 首先创建一个客户端对象。用户名和密码(如果不需要身份验证，可以省略密码)。
webdav = easywebdav.connect('webdav.your-domain.com', username='myuser', password='mypass')
# 一些操作:
webdav.mkdir('some_dir') # 创建目录
webdav.rmdir('another_dir') # 删除目录
webdav.download('remote/path/to/file', 'local/target/file') # 下载
webdav.upload('local/path/to/file', 'remote/target/file') # 上传
```

### 创建客户端对象

#### 语法

```python
easywebdav.connect(host, port=0, auth=None, username=None, password=None, protocol='http', path="/")
```

| 参数     | 含义                       | 是否可省略         |
| -------- | -------------------------- | ------------------ |
| host     | `WebDav`服务器地址 or 域名 | 不可省略           |
| port     | `WebDav`服务器端口         | 可省略，默认`0`    |
| `auth`   | 编辑者or上传者             | 可省略，默认`None` |
| username | 用户名                     | 可省略，默认`None` |
| password | 密码                       | 可省略，默认`None` |
| protocol | 协议头？                   | 可省略，默认`http` |
| path     | 存储路径                   | 可省略，默认`/`    |

#### 实例

```python
webdav = easywebdav.connect('dav.box.com',username='1183417329@qq.com',password='123456', protocol='https', path="/dav/博客上传/")
```

### 创建目录

#### 语法

```python
mkdir(path, safe=False)
```

| 参数 | 含义       | 是否可省略          |
| ---- | ---------- | ------------------- |
| path | 文件夹名称 | 不可省略            |
| safe |            | 可省略，默认`False` |

#### 实例

> 文件夹会创建在`webdav`对象时填写的path下

```python
webdav.mkdir('some_dir')
```

### 删除目录

> 也可以删除文件

#### 语法

```python
rmdir(path, safe=False)
```

| 参数 | 含义       | 是否可省略          |
| ---- | ---------- | ------------------- |
| path | 文件夹名称 | 不可省略            |
| safe |            | 可省略，默认`False` |

### 上传文件

> 再次提醒，python3在使用时需要将`basestring`替换成`str`

#### 语法

```python
upload(local_path_or_fileobj, remote_path)
```

| 参数                    | 含义                                                     | 是否可省略 |
| ----------------------- | -------------------------------------------------------- | ---------- |
| `local_path_or_fileobj` | 本地路径 or 文件内容(二进制)                             | 不可省略   |
| `remote_path·`          | 远程路径(在`WebDav`服务器上的存储位置) or 文件名(带后缀) | 不可省略   |

#### 实例

```python
# 方法一：提交路径
file_path = 'D:/vscode/vscode-python/flaskblog/static/upload/icon/1604283946.jpg'
webdav.upload(file_path, '路径.jpg')
# 方法二：提交文件
file = open('D:/vscode/vscode-python/flaskblog/static/upload/icon/1604283946.jpg','rb')
webdav.upload(file, '文件.jpg')
```

### 遍历文件

#### 语法

```python
ls(path=None)
```

| 参数 | 含义     | 是否可省略 |
| ---- | -------- | ---------- |
| path | 位置路径 | 可省略     |

#### 实例

```python
ls = webdav.ls()
print(ls)
#--------------
[File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/', size=142678, mtime='Mon, 02 Nov 2020 05:14:55 GMT', ctime='2020-11-02T02:35:19Z', contenttype=''), File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/some_dir/', size=0, mtime='Mon, 02 Nov 2020 04:21:24 GMT', ctime='2020-11-02T04:21:24Z', contenttype=''), File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/some_dir2/', size=0, mtime='Mon, 02 Nov 2020 04:21:52 GMT', ctime='2020-11-02T04:21:52Z', contenttype=''), File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/%e6%96%87%e4%bb%b6.jpg', size=71339, mtime='Mon, 02 Nov 2020 05:14:55 GMT', ctime='2020-11-02T05:14:55Z', contenttype='image/jpeg'), File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/1604283946.jpg', size=71339, mtime='Mon, 02 Nov 2020 05:14:42 GMT', ctime='2020-11-02T05:11:59Z', contenttype='image/jpeg')]
#--------------
print(type(ls))
#--------------
<class 'list'>

# 获取每个文件的名称
from urllib.parse import unquote
for i in ls:
    print(i)
    print(unquote(i.name))
#----仅一部分------
File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/%e6%96%87%e4%bb%b6.jpg', size=71339, mtime='Mon, 02 Nov 2020 05:14:55 GMT', ctime='2020-11-02T05:14:55Z', contenttype='image/jpeg')
/dav/博客上传/文件.jpg
File(name='/dav/%e5%8d%9a%e5%ae%a2%e4%b8%8a%e4%bc%a0/1604283946.jpg', size=71339, mtime='Mon, 02 Nov 2020 05:14:42 GMT', ctime='2020-11-02T05:11:59Z', contenttype='image/jpeg')
/dav/博客上传/1604283946.jpg
```

### 删除文件

#### 语法

```python
delete(file_path)
```

> `file_path`指的是在`webdav`对象时填写的path下的路径

#### 实例

```python
webdav.delete('文件.jpg')
```

### 下载文件

#### 语法

```python
download(remote_path, local_path_or_fileobj)
```

| 参数                    | 含义                                                     | 是否可省略 |
| ----------------------- | -------------------------------------------------------- | ---------- |
| `remote_path·`          | 远程路径(在`WebDav`服务器上的存储位置) or 文件名(带后缀) | 不可省略   |
| `local_path_or_fileobj` | 本地路径                                                 | 不可省略   |

### 获取文件url

#### 语法

```python
_get_url(path)
```

#### 实例

```python
webdav._get_url('文件.jpg')
```



## 客户端对象`API`

该API几乎是不言自明的：

```python
cd(path)
ls(path=None)
exists(remote_path)
mkdir(path, safe=False)
mkdirs(path)
rmdir(path, safe=False)
delete(file_path)
upload(local_path_or_fileobj, remote_path)
download(remote_path, local_path_or_fileobj)
```

## 使用客户端`SSL`证书

```python
webdav = easywebdav.connect('secure.example.net',
                            username='user',
                            password='pass',
                            protocol='https',
                            cert="/path/to/your/certificate.pem")
# Do some stuff:
print(webdav.ls())
```

请注意，有关[请求API](http://docs.python-requests.org/en/latest/api/)的“ cert”参数的所有选项和限制在 此处适用，因为该参数仅通过！

## 开发`EasyWebDAV`

强烈建议使用虚拟环境：

```python
virtualenv --no-site-packages easywebdav_dev
source easywebdav_dev/bin/activate
```

在开发模式下安装库：

```python
EASYWEBDAV_DEV=1 python setup.py develop
```

该命令的第一部分使setup.py除常规依赖项外还安装开发依赖项。

运行测试：

```python
nosetests --with-yanc --nologcapture --nocapture tests
```

使用WebDAV服务器日志运行测试：

```python
WEBDAV_LOGS=1 nosetests --with-yanc --nologcapture --nocapture -v tests
```