Zlib库--- 与 gzip 兼容的压缩

> 参考zlib文档：https://docs.python.org/zh-cn/3/library/zlib.html
>
> 参考gzip文档：https://docs.python.org/zh-cn/3/library/gzip.html

- zlib与gzip常用函数对比

> 由于二者都是压缩字节，所以在压缩前要将字符串、文本内容等等转换成字节
>
> 方法1：x = **bytes**(s, 'utf-8')  s是待转换的字符串、文本内容等等  x就是转换后的字节
>
> 方法2：x = b'字符串'  在字符串前面添加b，就表示b后面的字符串是字节类型的，但是无法转换中文

| Zilb                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| zlib.**compress**(data, level=-1)                            | 压缩 *data* 中的字节，返回含有已压缩内容的 bytes 对象。参数 *level* 为整数，可取值为 `0` 到 `9` 或 `-1`，用于指定压缩等级。`1` 表示最快速度和最低压缩率，`9` 表示最慢速度和最高压缩率。`0`  表示不压缩。参数默认值为 `-1`。Z_DEFAULT_COMPRESSION 是速度和压缩率之间的平衡 (一般相当于设压缩等级为 6)。 |
| zlib.**decompress**(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE) | 解压 data 中的字节，返回含有已解压内容的 bytes 对象。参数 wbits 取决于 data 的格式，具体参见下边的说明。bufsize 为输出缓冲区的起始大小。 |

| Gzip                                                    | 描述                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| gzip.**compress**(data, compresslevel=9, *, mtime=None) | 压缩 data，返回一个包含压缩数据的 bytes 对象。 compresslevel 和 mtime 的含义与上文中 GzipFile 构造器的相同。 |
| gzip.**decompress**(data)                               | 解压缩 data，返回一个包含未压缩数据的 bytes 对象。           |

- 使用方法：

  - Zlib：

  ```python
  # 压缩
  import zlib
  # 第一种方法
  a = b'hello' # 无法转换中文
  b = zlib.compress(a)
  print(b) # 输出 b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'
  
  # 第二种方法
  c = '中文'
  d = bytes(c,'utf-8')
  e = zlib.compress(d)
  print(e) # 输出 b'x\x9c{\xb2c\xed\xb3i\xed\x00\x10\x0f\x04M'
  
  # 解压缩
  f = zlib.decompress(b)
  print(f) # 输出 b'hello'
  
  g = zlib.decompress(e)
  print(g) # 输出 b'\xe4\xb8\xad\xe6\x96\x87'
  h = str(g,'utf-8') # 还需要将字节转换成字符串
  print(h) # 输出 中文
  ```

  - Gzip:

  ```python
  # 压缩
  import gzip
  # 第一种方法
  a = b'hello' # 无法转换中文
  b = gzip.compress(a)
  print(b) # 输出 b'\x1f\x8b\x08\x00\x8f\xf2k_\x02\xff\xcbH\xcd\xc9\xc9\x07\x00\x86\xa6\x106\x05\x00\x00\x00'
  
  # 第二种方法
  c = '中文'
  d = bytes(c,'utf-8')
  e = gzip.compress(d)
  print(e) # 输出 b'\x1f\x8b\x08\x00\x8f\xf2k_\x02\xff{\xb2c\xed\xb3i\xed\x007\xed\tZ\x06\x00\x00\x00'
  
  # 解压缩
  f = gzip.decompress(b)
  print(f) # 输出 b'hello'
  
  g = gzip.decompress(e)
  print(g) # 输出 b'\xe4\xb8\xad\xe6\x96\x87'
  h = str(g,'utf-8') # 还需要将字节转换成字符串
  print(h) # 输出 中文
  ```

- 压缩等级：

  - Zlib：

  ```python
  import zlib
  
  a = b'This is the original text.' * 1024
  
  template1 = '{:^15}  {:^5}'
  template2 = '{:^15}  {:^15}'
  print(template1.format('压缩级别', '压缩大小'))
  print(template2.format('-' * 15, '-' * 15))
  
  for i in range(0, 10):
      data = zlib.compress(a, i)  # 设置压缩级别进行压缩
      print(template2.format(i, len(data)))
  -----------------------------------------
       压缩级别        压缩大小
  ---------------  ---------------
         0              26635
         1               215
         2               215
         3               215
         4               118
         5               118
         6               118
         7               118
         8               118
         9               118
  ```

  可以看出从4开始压缩大小就差不多了，所以推荐4-6的压缩级别，级别越高，压缩越慢

  - Gzip：

  ```python
  import gzip
  
  a = b'This is the original text.' * 1024
  
  template1 = '{:^15}  {:^5}'
  template2 = '{:^15}  {:^15}'
  print(template1.format('压缩级别', '压缩大小'))
  print(template2.format('-' * 15, '-' * 15))
  
  for i in range(0, 10):
      data = gzip.compress(a, i)  # 设置压缩级别进行压缩
      print(template2.format(i, len(data)))
  -----------------------------------------
       压缩级别        压缩大小
  ---------------  ---------------
         0              26647
         1               227
         2               227
         3               227
         4               130
         5               130
         6               130
         7               130
         8               130
         9               130
  ```

  从这里可以看出gzip的压缩能力比不上zlib


- 压缩文件：

  > 这里就要提到：os.path.getsize(filepath) 获取文件大小
  
  ```python
  # 生成待压缩文件
  a = '你好 世界！Hello World！\n'*1024
  b = bytes(a,'utf-8')
  f = open("vscode-python\待压缩.txt","wb") # wb wb+ rb rb+ + rw b具体应用场景
  f.write(b)
  f.close()
  ```
  
  
  - Zlib：
  
  ```python
  import os
  import zlib
  path1 = 'vscode-python\待压缩.txt'
  path2 = 'vscode-python\zlib压缩.txt'
  print("原始文件大小:",os.path.getsize(path1))
  a = open(path1,'rb')
  b = a.read()
  c = zlib.compress(b,5)
  d = open(path2,'wb')
  d.write(c)
  d.close()
  a.close()
  print("压缩文件大小:",os.path.getsize(path2))
  ------------------------------------------
  原始文件大小: 31744
  压缩文件大小: 142
  ```
  
  - Gzip:
  
  ```python
  import os
  import gzip
  path1 = 'vscode-python\待压缩.txt'
  path2 = 'vscode-python\gzip压缩.txt'
  print("原始文件大小:",os.path.getsize(path1))
  a = open(path1,'rb')
  b = a.read()
  c = gzip.compress(b,5)
  d = open(path2,'wb')
  d.write(c)
  d.close()
  a.close()
  print("压缩文件大小:",os.path.getsize(path2))
  ------------------------------------------
  原始文件大小: 31744
  压缩文件大小: 154
  ```
  
  再次证明了在同样的条件下，gzip比不上zlib。
  
  