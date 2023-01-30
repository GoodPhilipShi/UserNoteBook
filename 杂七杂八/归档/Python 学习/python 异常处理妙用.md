### Try---Except

> 仅意会，不可运行

```python
if "c://a.txt": # 文件是否存在
	if  e盘空间大于 a.txt的大小(文件长度):
    	if 文件复制到一半IO断流了:
            停止复制，输出IO流出问题！
        else:
            复制 C://a.txt 到 D://a.txt
    else:
        print("e盘空间不够放a.txt!")
else:
    print("a.txt文件不存在！")
            
```

> 写的就很麻烦，而且长
>
> 最重要的是将运行代码和异常代码写在一起了

```python
try:
    复制 C://a.txt 到 D://a.txt
except:
    print("文件无法复制")
```

Try---Except---Finally

> Finally 异常与否，都要运行

With

> With 不是用来取代Try---Except---Finally结构的，只是作为补充，方柏霓我们在文件管理、网络通讯时的开发

Trackback模块

- 使用Trackback模块打印异常信息

  ```python
  #coding=utf-8
  import trackback
  try:
      print("strp1")
      num = 1 / 0
  except:
      traceback.print_exc()
  ##########将异常信息输出到指定的文件中###########
  #coding=utf-8
  import trackback
  try:
      print("strp1")
      num = 1 / 0
  except:
      with open("log.txt","a") as f:
      	traceback.print_exc(file = f)
  ```
  

自定义异常类

```python
#coding=utf-8
# 测试自定义异常
class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return self.errorInfo + "年龄错误！应该在1-150之间"
    
############测试代码#############
if __name__:"__main__": # 如果为true,则模块是作为独立文件运行，可以执行测试代码
    age = int(input("输入一个年龄："))
    if age < 1 or age > 150:
        raise AgeError()
    else:
        print("正常的年龄：",age)
```

文本和二进制文件

| 名称                              | 说明                                           |
| --------------------------------- | ---------------------------------------------- |
| IO模块                            | 文件流的输入输出操作  input output             |
| OS模块                            | 基本操作系统功能，包括文件操作                 |
| glob模块                          | 查找符合特定功能规则的文件路径名               |
| fnmatch模块                       | 使用模式来匹配文件路径名                       |
| fileinput模块                     | 处理多个输入文件                               |
| failecmp模块                      | 用于文件的比较                                 |
| cvs模块                           | 用于csv文件的处理                              |
| pickle和cPickle                   | 用于序列化和反序列化                           |
| xml包                             | 用于XML数据处理                                |
| bz2、gzip、zipfile、zlib、tarfile | 用于处理压缩和解压缩文件（分别对应不同的算法） |

enumerate方法

```python
a = ["你","是","猪"]
b = enumerate(a)
print(b) # 输出 <enumerate object at 0x0000012B64923E08>
print(list(b)) # 输出 [(0, '你'), (1, '是'), (2, '猪')]
c = [ temp + " #" +str(index) for index,temp in enumerate(a)]
print(c) # 输出 ['你 #0', '是 #1', '猪 #2']
```

