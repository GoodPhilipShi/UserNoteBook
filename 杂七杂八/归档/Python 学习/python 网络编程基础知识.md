## 软件开发的架构

### C/S架构

> C/S即：Client与Server ，中文意思：客户端与服务器端架构，这种架构也是从用户层面（也可以是物理层面）来划分的。
>
> 这里的客户端一般泛指客户端应用程序EXE，程序需要先安装后，才能运行在用户的电脑上，对用户的电脑操作系统环境依赖较大。

![img](https://gitee.com/acg-q/pic-go-images/raw/master/20201126172823.png)

### B/S架构

> B/S即：Browser与Server,中文意思：浏览器端与服务器端架构，这种架构是从用户层面来划分的。
>
> Browser浏览器，其实也是一种Client客户端，只是这个客户端不需要大家去安装什么应用程序，只需在浏览器上通过HTTP请求服务器端相关的资源（网页资源），客户端Browser浏览器就能进行增删改查。

![img](https://gitee.com/acg-q/pic-go-images/raw/master/20201126172857.png)

### OSI5层协议

![image-20201126091355787](https://gitee.com/acg-q/pic-go-images/raw/master/20201126091356.png)

![image-20201126091859301](https://gitee.com/acg-q/pic-go-images/raw/master/20201126091859.png)

![image-20201126094023297](https://gitee.com/acg-q/pic-go-images/raw/master/20201126094023.png)

![image-20201126100541681](https://gitee.com/acg-q/pic-go-images/raw/master/20201126100541.png)

### TCP协议

![img](https://gitee.com/acg-q/pic-go-images/raw/master/20201126173253.png)

#### TCP握手

![image-20201126172657754](https://gitee.com/acg-q/pic-go-images/raw/master/20201126172658.png)

> TCP是因特网中的传输层协议，使用三次握手协议建立连接。当主动方发出SYN连接请求后，等待对方回答`SYN+ACK`，并最终对对方的 `SYN` 执行 `ACK` 确认。这种建立连接的方法可以防止产生错误的连接。
> TCP三次握手的过程如下：
> 客户端发送`SYN（SEQ=x）`报文给服务器端，进入`SYN_SEND`状态。
> 服务器端收到`SYN`报文，回应一个`SYN （SEQ=y）ACK(ACK=x+1）`报文，进入`SYN_RECV`状态。
> 客户端收到服务器端的`SYN`报文，回应一个`ACK(ACK=y+1）`报文，进入`Established`状态。
> 三次握手完成，TCP客户端和服务器端成功地建立连接，可以开始传输数据了。

#### TCP四次挥手

![image-20201126173518153](https://gitee.com/acg-q/pic-go-images/raw/master/20201126173518.png)

> 建立一个连接需要三次握手，而终止一个连接要经过四次握手，这是由TCP的半关闭（half-close）造成的。
> (1) 某个应用进程首先调用close，称该端执行“主动关闭”（active close）。该端的TCP于是发送一个FIN分节，表示数据发送完毕。
> (2) 接收到这个FIN的对端执行 “被动关闭”（passive close），这个FIN由TCP确认。
> 注意：FIN的接收也作为一个文件结束符（end-of-file）传递给接收端应用进程，放在已排队等候该应用进程接收的任何其他数据之后，因为，FIN的接收意味着接收端应用进程在相应连接上再无额外数据可接收。
> (3) 一段时间后，接收到这个文件结束符的应用进程将调用close关闭它的套接字。这导致它的TCP也发送一个FIN。
> (4) 接收这个最终FIN的原发送端TCP（即执行主动关闭的那一端）确认这个FIN。
> 既然每个方向都需要一个FIN和一个ACK，因此通常需要4个分节。
> 注意：
> (1) “通常”是指，某些情况下，步骤1的FIN随数据一起发送，另外，步骤2和步骤3发送的分节都出自执行被动关闭那一端，有可能被合并成一个分节。
> (2) 在步骤2与步骤3之间，从执行被动关闭一端到执行主动关闭一端流动数据是可能的，这称为“半关闭”（half-close）。
> (3) 当一个Unix进程无论自愿地（调用exit或从main函数返回）还是非自愿地（收到一个终止本进程的信号）终止时，所有打开的描述符都被关闭，这也导致仍然打开的任何TCP连接上也发出一个FIN。
> 无论是客户还是服务器，任何一端都可以执行主动关闭。通常情况是，客户执行主动关闭，但是某些协议，例如，HTTP/1.0却由服务器执行主动关闭。

## SOCKET运用

### `TCP`基础运用

#### 服务端

```python
import socket
HOST = '127.0.0.1'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind((HOST, PORT))
    f.listen()
    conn, addr = f.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

#### 客户端

```python
import socket

HOST = '127.0.0.1'
PORT = 10086

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
```

### `UDP`基础运用

#### 服务端

```python
import socket
HOST = '127.0.0.1'
PORT = 10086
f = socket.socket(type = socket.SOCK_DGRAM)
f.bind((HOST,PORT))
while True:
    msg,addr = f.recvfrom(1024)
    print(msg.decode('utf-8'))
    msg = input('>>>>')
    f.sendto(msg.encode('utf-8'),addr)
```

#### 客户端

```python
import socket
HOST = '127.0.0.1'
PORT = 10086
with socket.socket(type = socket.SOCK_DGRAM) as f:
    while True:
        msg = input('>>>>')
        if msg.upper() == 'Q': break
        f.sendto(msg.encode('utf-8'), (HOST, PORT))
        msg = f.recv(1024).decode('utf-8')
        if msg.upper() == 'Q':break
        print(msg)
```

### 传输文件

> 1. `recv(1024)`并不代表一定可以收到1024个字节，而是最多收到1024个字节
> 2. 两条连续发送的数据一定要避免粘包问题
> 3. 先发送数据的长度，再发送数据
>    1. 发送的数据相关的内容组成`json`：先发送`json`的长度，再发送`json`，`json`中存了接下来要发送的数据长度,再发数据

#### 服务端

```python
import json
import socket

HOST = '127.0.0.1'
PORT = 9876
key = b'asd'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind((HOST, PORT))
    f.listen()
    conn, addr = f.accept()
        with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        data = json.loads(data.decode('utf-8'))
        filesize = data['filesize']
        while filesize > 0:
            data = conn.recv(1024)
            filesize -= len(data)
            print(data)
        conn.sendall(b"success!")
```

#### 客户端

```python
import json
import os
import socket

HOST = '127.0.0.1'
PORT = 9876
filename = 'text.txt'
KEY = b'asd'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    filesize = os.path.getsize(filename)
    ret = {'filesize': filesize}
    s.send(json.dumps(ret).encode('utf-8'))
    with open(filename, 'rb') as f:
        while filesize > 0:
            content = f.read(1024)
            filesize -= len(content)
            s.send(content)
    content = s.recv(1024)
    print(content)
```

### 验证合法-不使用`hmac`模块

> 第一步，生成随机字符串，并发送到客户端
> 第二步，客户端将接收到的字符串通过HASH算法的`sha1`进行加密，再用密钥(KEY)进行更新，最后再进行加密并返回服务端
> 第三步，服务端进行和客户端相同的操作，并将结果和接收到的数据进行对比
> 第四步，相同则合法，不相同则非法

#### 服务端

```python
import hashlib
import os
import socket

HOST = '127.0.0.1'
PORT = 9876
key = b'asd' # 密钥

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind((HOST, PORT))
    f.listen()
    conn, addr = f.accept()
    rand = os.urandom(32)
    conn.send(rand)
    sha = hashlib.sha1(rand)
    sha.update(key)
    res = sha.hexdigest()
    res_c = conn.recv(1024).decode('utf-8')
    if res_c == res:
        print('合法')
        conn.send(b'hello world!')
    else:
        print('非法')
```

#### 客户端

```python
import hashlib
import socket

HOST = '127.0.0.1'
PORT = 9876
filename = 'text.txt'
KEY = b'asd' # 密钥

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    rand = s.recv(32)
    sha = hashlib.sha1(rand)
    sha.update(KEY)
    res = sha.hexdigest()
    s.send(res.encode('utf-8'))
    content = s.recv(1024)
    print(content)
```

### 验证合法-使用`hmac`模块

> **原理相同**
>
> 将
>
> ```python
> sha = hashlib.sha1(rand)
> sha.update(key)
> ```
> 替换成
>
> ```python
> res = hmac.new(key, rand)
> ```

#### 服务端

```python
import os
import socket
import hmac

HOST = '127.0.0.1'
PORT = 9876
key = b'asd'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind((HOST, PORT))
    f.listen()
    conn, addr = f.accept()
    rand = os.urandom(32)
    conn.send(rand)
    # ----------修改项--------- #
    res = hmac.new(key, rand)
    # ------------------------ #
    res = res.hexdigest()
    res_c = conn.recv(1024).decode('utf-8')
    if res_c == res:
        print('合法')
        conn.send(b'hello world!')
    else:
        print('非法')
```

#### 客户端

```python
import socket
import hmac

HOST = '127.0.0.1'
PORT = 9876
filename = 'text.txt'
KEY = b'asd'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    rand = s.recv(32)
    # ----------修改项--------- #
    res = hmac.new(KEY, rand)
    # ------------------------ #
    res = res.hexdigest()
    s.send(res.encode('utf-8'))
    content = s.recv(1024)
    print(content)
```

## `SOCKETSERVER` 服务器并发

### 服务端

```python
import time
import socketserver
HOST = '127.0.0.1'
PORT = 10086
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionRefusedError:
                break

server = socketserver.ThreadingTCPServer((HOST,PORT),Myserver)
server.serve_forever()
```

### 客户端

```python
import socket
HOST = '127.0.0.1'
PORT = 10086

with socket.socket() as f:
    f.connect((HOST, PORT))
    while True:
        f.send(b'socketserver')
        content = f.recv(1024).decode('utf-8')
        print(content)
```

## 多进程与SOCKET

> 通过多进程实现`socketserver`可以同时接受多个客户端的请求

### 服务端

```python
import socket
from multiprocessing import Process

def main(conn):
    while True:
        ret = conn.recv(1024).decode('utf-8')
        conn.send(ret.upper().encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    HOST = '127.0.0.1'
    POPT = 10086
    f = socket.socket()
    f.bind((HOST, POPT))
    f.listen()
    while True:
        conn, addr = f.accept()
        Process(target=main, args=(conn,)).start()
    f.close()
```

### 客户端

```python
import socket
import time

HOST = '127.0.0.1'
POPT = 10086
f = socket.socket()
f.connect((HOST, POPT))
while True:
    f.send('hello world! 你好 世界！'.encode('utf-8'))
    time.sleep(1)
    msg = f.recv(1024).decode('utf-8')
    print(msg)
f.close()
```

## 扩展

### 请聊聊进程队列的特点和实现原理？

#### 特点

- 进程之间的通信
- 数据安全
- 先进先出

#### 实现原理

- 基于管道 + 锁
- 管道 基于文件级别的socket + pickle实现

### 数据安全or不安全

| 状态                          | 安危       |
| ----------------------------- | ---------- |
| 同步                          | 绝对安全   |
| 异步                          | 可能不安全 |
| 异步+‘运算赋值 or bool表达式’ | 不安全     |
| 异步+’列表单加单减‘           | 安全       |
| 异步+’列表多加单减‘           | 不安全     |
| 异步+’列表单加多减‘           | 不安全     |
| 异步+’列表多加多减‘           | 不安全     |

> 是否数据共享，是同步还是异步 数据共享并异步才有肯可能不安全
> += -= *= /= 赋值 = 计算之后 数据不安全
> if while 条件 这两个判断是由多线程完成的 数据不安全