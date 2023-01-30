# python 进程、线程

> 进程讲通信
> 线程讲同步

### 进程池(高计算的常见，没有IO(没有文件操作\没有数据库操作\没有网络操作\没有input))

> ## CPU个数\*2 <font color='red'>></font> 进程数  <font color='red'>></font> CPU个数\*1

### 线程池(一般根据IO的比例定制)

> ## 线程数 <font color='red'><=</font> CPU个数\*5

## 进程与线程

### 进程(Process)

> Windows系统中的一个基本概念，它包含着一个运行程序所需要的资源。一个正在运行的应用程序在操作系统中被视为一个进程，**进程可以包括一个或多个线程**。

### 线程(Thread)

> 是**进程中的基本执行单元**，是操作系统分配CPU时间的基本单位，一个进程可以包含若干个线程，在进程入口执行的**第一个线程被视为这个进程的主线程**

## 异步、同步、阻塞、非阻塞

### 异步 `Asynchronous`

> 当一个异步过程调用发出后，调用者在**没有得到结果之前，就可以继续执行后续操作**

### 同步 `Synchronous`

> 就是发出一个功能调用时，在**没有得到结果之前，该调用就<font size=5>不</font>返回或继续执行后续操作**

### 阻塞 `Blocking`

> 调用结果返回之前，当前线程会被挂起

### 非阻塞 `Nonblocking`

> 不能立刻得到结果之前，该调用不会阻塞当前线程

### 同步阻塞

> 调用一个函数需要等待这个函数的执行结果，并且在执行这个函数的过程中CPU不工作

```python
input('>>>>')
```

### 同步不阻塞

> 调用一个函数需要等待这个函数的执行结果，并且在执行这个函数的过程中CPU工作

```python
ret = eval('1+2+3-4')
```

### 异步非阻塞

> 调用一个幻术不需要等待这个函数的执行结果，并且在执行这个函数的过程中CPU工作

### 异步阻塞

> 调用一个幻术不需要等待这个函数的执行结果，并且在执行这个函数的过程中CPU不工作

# 进程的学习

### Python 处理进程模块-multiprocessing[莫提per赛沈]

#### 异步非阻塞

> 不管运行结果，继续运行

```python
from multiprocessing import Process
import os

def func(name, age):
    print(name, age)
    print(os.getpid(), os.getppid())

if __name__ == '__main__':
    print("mian>>>", os.getpid(), os.getppid())
    p = Process(target=func, args=('alex1', '123'))
    p.start() 
    print('继续')
    p = Process(target=func, args=('alex2', '123'))
    p.start()
```

### 同步阻塞

> 等待运行结果，再继续运行

```python
from multiprocessing import Process
import os

def func(name, age):
    print(name, age)
    print(os.getpid(), os.getppid())

if __name__ == '__main__':
    print("mian>>>", os.getpid(), os.getppid())
    p = Process(target=func, args=('alex1', '123'))
    p.start()
    p.join()
    print('继续')
    p = Process(target=func, args=('alex2', '123'))
    p.start()
```

### 开进程的另一种方法

> 用面向对象的方法来开进程

```python
import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, a):
        self.a = a
        super().__init__()

    def run(self):
        time.sleep(1)
        print(f"{self.a} ===> parent pid: {os.getppid()} pid: {os.getpid()}")

if __name__ == '__main__':
    print('-->', os.getpid())
    for i in range(10):
        p = MyProcess(i)
        p.start()
```

### 结束进程须知

#### `terminate`方法

```python
p.terminate()  # 强制结束子进程
```

> 结束进程需要一点时间

```python
import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, a):
        self.a = a
        super().__init__()

    def run(self):
        time.sleep(1)
        print(f"{self.a} ===> parent pid: {os.getppid()} pid: {os.getpid()}")


if __name__ == '__main__':
    print('-->', os.getpid())
    p = MyProcess(1)
    p.start()
    print(p.name)
    print(p.is_alive())  # 子进程是否存活
    p.terminate()  # 强制结束子进程
    print(p.is_alive())
    time.sleep(0.01)
    print(p.is_alive())


--> 35620
MyProcess-1
True # 运行p.terminate()之前，子进程存活
True # 运行p.terminate()之后，不等待，子进程依旧存活
False # 等待0.01秒后，子进程死亡
```

### 守护进程

> 守护进程会等待主进程的代码执行结束之后再执行结束，而不是等待整个主进程结束

```python
import os
import time
from multiprocessing import Process


def func1():
    while True:
        print('守护')
        time.sleep(1)


def func2():
    for i in range(10):
        print(f'{i + 1}我还在！')
        time.sleep(1)


if __name__ == '__main__':
    print('-->', os.getpid())
    p1 = Process(target=func1)
    p1.daemon = True
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    time.sleep(2)
    print('主进程结束')
```

### Process类的一些其他方法、属性

#### name

> 进程名称

```python
p.name()
```

#### pid

> 进程id

#### ident

> 进程id

#### daemon

> 设置守护进程

```python
p1.daemon = True # 开启
p1.daemon = False # 关闭
```

#### tetminate方法

> 结束进程

#### isalive方法

> 进程是否存活

### 进程与进程之间数据隔离

> 内存空间是不能共享的，当然执意要共享还是有方法的

#### 通过multiprocessing 中的Manager进行跨进程数据共享

> 仅做了解

### 进程之间通信(IPC)-Inter Process Communication

#### 基于文件

> 同一台机器上的多进程之间通信

> 基于Socket的文件级别的通信来完成数据传输

#### 基于网络

> 同一台机器或者多台机器之间的多进程间的通信

##### 第三方工具(消息中间)

> `memcache`、`redis`、`rabbitmq`、`kafka`

### 生产者消费者模型

> 生产者消费者模式就是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。这个阻塞队列就是用来给生产者和消费者解耦的。

```python
from multiprocessing import Process, Queue
import time
import random


def consumer(q, d):  # 消费者:通常取到数据之后还要进行某些操作
    while True:
        food = q.get()
        print(food)
        if not food: break
        print(f'{d} 吃了 {food}')


def producer(q, r, p):  # 生产者：通常在放数据之前需要先通过某些代码来获取数据
    for i in range(10):
        print(f'{r} 制作了 {p}{i + 1}号')
        time.sleep(random.random())
        q.put(f'{p}{i + 1}号')


if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer, args=(q, '🐖'))
    p1 = Process(target=producer, args=(q, '工人1', '饼干'))
    p2 = Process(target=producer, args=(q, '工人2', '香蕉'))
    c1.start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)
```

# 线程的学习

> 数据共享，效率高开销小，可以被多个CPU调度(是CPU调度的最小单位)，数据不安全，由操作系统负责调度
>
> 在CPython解析器下，GIL锁(全局解释器锁)导致了用一个进程中的多个线程不能利用多核

## Python  线程模块-threading[踹顶]

```python
import threading
def pain():
	print("start")
	print("end")
def thread():
	thread1 = threading.Thread(target=pain)
	thread1.start()
	thread1.join()
if __name__ == '__main__':
	thread()
```

### threading的用法

#### Thread

```python
Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

| 参数   | 表示                          |
| ------ | ----------------------------- |
| group  | 为以后的ThreadGroup类预留     |
| target | 被执行的对象，由run()方法执行 |
| args   | target对象使用的参数          |
| daemon | 是否为守护进程                |

#### start()

> 每个thread 对象都只能被调用1次start()

#### run()

> 如果创建Thread的子类，重写该方法。负责执行target参数传来的可执行对象。

#### join()

> 阻塞线程直到结束

#### ident()

> 获取进程ID

#### current_thread()

> 获取当前所在的线程的对象 current_thread().ident通过ident可以获取线程id

### 🔒线程锁

#### ❌线程锁-互斥锁

> ### +=，-=，*=，/=，if，while 数据<font size='5' color='red'>不安全🚫</font>，需要加线程锁
>
> ### append，pop，strip 数据<font size='5' color='red'>安全❤</font>，可加可不加
>
> - #### 但是加了赋值操作[b = a.strip()]数据不安全

```python
from threading import Thread,Lock
import time

list = []

def append():
    for i in range(500000):
        list.append(1)

def pop(lock):
    for i in range(500000):
        with lock:
            if not list: time.sleep(1E-7)
            list.pop()

t_1 = []
lock = Lock()
for i in range(10):
    t1=Thread(target=append)
    t1.start()
    t2=Thread(target=pop,args=(lock,))
    t2.start()
    t_1.append(t1)
    t_1.append(t2)

for t in t_1:
    t.join()
print(list)
```

#### ⭕线程锁-递归锁

> 获取多少次钥匙，就要还回去多少次钥匙，不然就会卡住

```python
from threading import Thread, RLock

def func(i, lock):
    lock.acquire()
    lock.acquire()
    print(i, ":start")
    lock.release()
    lock.release()
    print(i, ":end")

lock = RLock()
for i in range(5):
    Thread(target=func, args=(i, lock)).start()
```

#### 🔑线程锁的应用-单例模式

> ### 线程安全

```python
from threading import Lock
import time

class A:
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.0001)
                cls.__instance = super(A, cls).__new__(cls)
        return cls.__instance

def func():
    a = A()
    print(a)

for i in range(10):
    Thread(target=func).start()
```

#### 💬互斥锁Lock|递归锁RLock

> ### Lock ❌互斥锁 效率高
>
> ### RLock ⭕递归锁(recursion)锁 效率相对低

#### 🔏死锁现象

> ### ❓产生的原因
>
> #### 多把(互斥|递归)锁 并且在多线程中 交叉使用
>
> ### 🔧解决方法
>
> #### 如果是互斥锁，出现了死锁现象，最快的解决方案是把所有的互斥锁都改成一把递归锁

### 面向对象的方式起线程

```python
from threading import Thread

class MyTread(Thread):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def run(self):
        print(self.ident)
        print(f'{self.a + self.b}')

t = MyTread(1, 2)
t.start()
print(t.ident)
```



# Python 线程(进程)池、流下载

> 从`Python3.2`开始，标准库为我们提供了` concurrent.futures `模块，它提供了 `ThreadPoolExecutor` (线程池)和`ProcessPoolExecutor `(进程池)两个类。

## 线程池的基本使用-实现多线程流下载

> ## `Response.iter_content`
>
> 获取请求的原始响应可以用：`Response.raw`、`Response.iter_content`
>
> 普通情况可以用 r.raw，在初始请求中设置 stream=True,来获取服务器的原始套接字响应
>
> ```python
> url = "http://wx4.sinaimg.cn/large/d030806aly1fq1vn8j0ajj21ho28bduy.jpg"
> r = requests.get(url, stream=True)
> r.raw.read(10)
> 
> #-------------
> b'\xff\xd8\xff\xe1\x13\xe9Exif'
> ```
>
> 当流下载时，用`Response.iter_content`或许更方便些。`requests.get(url)`默认是下载在内存中的，下载完成才存到硬盘上，可以用`Response.iter_content`来边下载边存硬盘
>
> ```python
> url = "http://wx4.sinaimg.cn/large/d030806aly1fq1vn8j0ajj21ho28bduy.jpg"
> 
> rsp = requests.get(url, stream=True)
> with open('1.jpg', 'wb') as f:
>     for i in rsp.iter_content(chunk_size=1024):  # 边下载边存硬盘, chunk_size 可以自由调整为可以更好地适合您的用例的数字
>         f.write(i)
> ```

```python
from concurrent.futures import ThreadPoolExecutor
import requests

# 线程数
num_Thread = 5
# 缓冲大小
content_size = 1024

def prints(url):
    r = requests.get(url,stream=True)
    filename = url.split("/")[-1]
    with open(filename,"wb") as f:
        for data in r.iter_content(content_size):
            f.write(data)


if __name__ == '__main__':
    urls = [
        "url1",
        "url2",
        "url3"
    ]

    with ThreadPoolExecutor(max_workers=num_Thread) as bool:
        bool.map(prints,urls)
```

## 线程池的用法

#### submit

```python
submit(fn, *args, **kwargs)
```

| 参数            | 表示               |
| --------------- | ------------------ |
| fn              | 需要线程执行的函数 |
| *args, **kwargs | 函数所需的参数     |

> 通过 submit 返回的是一个 future 对象，它是一个未来可期的对象，通过它可以获悉线程的状态主线程(或进程)中可以获取某一个线程(进程)执行的状态或者某一个任务执行的状态及返回值

```python
with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容纳数量为5的线程池
    task1 = t.submit(spider, 1)
```

#### wait

```python
wait(fs, timeout=None, return_when=ALL_COMPLETED)
```

| 参数        | 表示                                                         |
| ----------- | ------------------------------------------------------------ |
| fs          | 表示需要执行的序列                                           |
| timeout     | 等待的最大时间，如果超过这个时间即使线程未执行完成也将返回   |
| return_when | 表示wait返回结果的条件，默认为 ALL_COMPLETED 全部执行完成再返回 |

#### as_completed

> 上面(`done()`)虽然也提供了判断任务是否结束的方法，但是不能在主线程中一直判断啊。最好的方法是当某个任务结束了，就给主线程返回结果，而不是一直判断每个任务是否结束。
>
> ThreadPoolExecutorThreadPoolExecutor 中 的 as_completed() 就是这样一个方法，当子线程中的任务执行完后，直接用 result() 获取返回结果

```python
with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for page in range(1, 5):
            obj = t.submit(spider, page)
            obj_list.append(obj)

        for future in as_completed(obj_list):
            data = future.result()
            print(f"main: {data}")
```

#### map

```python
map(fn, *iterables, timeout=None)
```

| 参数      | 表示                                                         |
| --------- | ------------------------------------------------------------ |
| fn        | 需要线程执行的函数                                           |
| iterables | 接受一个可迭代对象                                           |
| timeout   | 第三个参数 timeout 跟 wait() 的 timeout 一样，但由于 map 是返回线程执行的结果，如果 timeout小于线程执行时间会抛异常 TimeoutError |

#### add_done_callback(fn)

| 参数 | 表示               |
| ---- | ------------------ |
| fn   | 需要线程执行的函数 |

```python
import time, random
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def func(a, b):
    print(current_thread().ident, 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(current_thread().ident, 'end', a)
    return a * b

def print_func(ret):
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(max_workers=4)
    for i in range(20):
        ret = tp.submit(func, i, b=i + 1)
        ret.add_done_callback(print_func)
```



# 🏳‍🌈队列

## 🏁队列的用法

### queue

> 查看队列中所有元素

### qsize()

> 返回队列的大小

### empty()

> 如果队列为空，返回True,反之False

### full()

> 如果队列为满，返回True,反之False

### get()

> 取数据

### get_nowait()

> 相当于Queue.get(False)，非阻塞方法

### put()

> 存数据

### join()

>  实际上意味着等到队列为空，再执行别的操作

## 🏁先进先出队列`Queue`

### `Queue(maxsize=5)`

```python
from queue import Queue
q=Queue(maxsize=5)
for i in range(5):
    q.put(i)
print(q.get())
# 0
```

## 🏁后进优先队列`LifoQueue`

### `LifoQueue(maxsize=6)`

```python
from queue import LifoQueue
q=LifoQueue(maxsize=5)
for i in range(5):
    q.put(i)
print(q.get())
# 4
```

## 🏁优先级队列`PriorityQueue`

### `PriorityQueue(maxsize=5)`

```python
from queue import PriorityQueue
q = PriorityQueue(maxsize=5)
q.put((3, '普通用户'))
q.put((2, 'VIP'))
q.put((1, 'SVIP'))
print(q.get())
# (1, 'SVIP')
```

# 🏆守护线程\进程的<font size='7' color='red'>区别</font>

## 守护进程 会随着<font size='6' color='red'>主进程的代码</font>结束而结束

> ### 如果主进程代码结束之后还有其他子进程在运行，守护线程不守护

## 守护线程 随着<font size='6' color='red'>主线程</font>的结束而结束

> ### 如果主线程代码结束之后还有其他子线程在运行，守护线程也守护

## 为什么？

- ## 守护进程和守护线程的结束原理不同

- ### 守护<font size='5' color='red'>进程</font>需要主进程来回收资源

- ### 守护<font size='5' color='red'>线程</font>是随着进程的结束才结束

  - #### 其他子线程 --> 主线程结束 --> 主进程结束 --> 整个进程所有的资源都被回收

# 协程

- ## <font color='red'>协程</font>是操作系统不可见的

- ## <font color='red'>协程</font>本质上就是一条线程 多个任务在一条线程上来回且切换

- ## 利用<font color='red'>协程</font>这个概念实现的内容：来规避IO操作，就达到了我们将一条线程中的IO操作降到最低的目的

## `gevent`

> ## 利用了  `greenlet` 底层模块完成的切换 + 自动规避IO的功能

```python
import time
import gevent
from gevent import monkey
# monkey 可以使导入模块中的io操作也能被识别
monkey.patch_all()

def func():
    print('start func')
    # gevent.sleep(1)
    time.sleep(1)
    print('end func')


g1 = gevent.spawn(func)
g2 = gevent.spawn(func)
g3 = gevent.spawn(func)
g4 = gevent.spawn(func)
# g1.join() # 通过堵塞，实现并发
gevent.joinall([g1, g2, g3, g4])
```

## `asyncio`

> ## 利用了  yield  底层模块完成的切换 + 自动规避IO的功能

### `tornado`-异步的WEB框架

### `yield from`-更好的实现协程

### `send`-更好的实现协程

### `asyncio`模块 基于python原生的协程的概念正式的被成立

### 特殊的在python中提供协程功能的关键字：`aysnc`(标识一个函数时协程函数，await语法必须用在`async`函数中) `await`(写好的`asyncio`中的阻塞方法)

```python
import asyncio


async def func(name):
    print(name, 'start')
    await asyncio.sleep(1)
    print(name, 'end')


loop = asyncio.get_event_loop()
# 单运行
loop.run_until_complete(func())
# 运行+传参 同步
loop.run_until_complete(func('alex'))
# 运行+传参 异步
loop.run_until_complete(asyncio.wait([func('alex'), func('大笔')]))
```

