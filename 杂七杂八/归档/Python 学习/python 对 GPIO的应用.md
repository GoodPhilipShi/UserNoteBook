# python 对 GPIO的应用

> 基于文件sysfs级别的应用

## 📃GPIO命令

> [GPIO的介绍](https://developer.ridgerun.com/wiki/index.php/How_to_use_GPIO_signals)

### 📤导出引脚GPIO配置export

```bash
echo 132 > /sys/class/gpio/export
# 意思：往/sys/class/gpio/export文件中写入132
```

### 📥删除引脚GPIO配置unexport

```bash
echo 132 > /sys/class/gpio/unexport
# 意思：往/sys/class/gpio/unexport文件中写入132
```

### 🔁设置引脚输入输出direction

```bash
echo out > /sys/class/gpio/gpio132/direction # 输出
echo in > /sys/class/gpio/gpio132/direction # 输入
# 意思：往/sys/class/gpio/gpio132/direction文件中写入in/out
```

### ⚡设置引脚高低电平<font color='red'>输出</font>value

> 数字1/0都是字符串类型，不是整数类型

```bash
echo 1 > /sys/class/gpio/gpio132/value # 高电平
echo 0 > /sys/class/gpio/gpio132/value # 低电平
# 意思：往/sys/class/gpio/gpio132/value文件中写入0/1
```

### ⚡获取引脚电平值value

```bash
cat /sys/class/gpio/gpio133/value
# 意思：读取/sys/class/gpio/gpio132/value文件的内容
```

### ✨设置边缘事件edge

> <b><font size='5' color='red'>边缘</font></b>是指信号状态的改变，从低到高（上升沿**rising**）或从高到低（下降沿**falling**）。通常情况下，我们更关心于输入状态的该边而不是输入信号的值。这种状态的该边被称为事件。
>
> <b><font size='5' color='red'>边缘</font></b>事件如下：
>
> - <font size='5' color='red'>rising</font> 上升
>
>   **数字电平从低电平（数字“0”）变为高电平（数字“1”）的那一瞬间叫作上升沿**。 上升沿触发是当信号有上升沿时的开关动作，当电位由低变高而触发输出变化的就叫上升沿触发。也就是当测到的信号电位是从低到高也就是上升时就触发，叫做上升沿触发。
>
> - <font size='5' color='red'>falling</font> 下降
>
>   **数字电平从高电平（数字“1”）变为低电平（数字“0”）的那一瞬间叫作下降沿**。  下降沿触发是当信号有下降沿时的开关动作，当电位由高变低而触发输出变化的就叫下降沿触发。也就是当测到的信号电位是从高到低也就是下降时就触发，叫做下降沿触发
>
> - <font size='5' color='red'>both</font> 变化
>
>   检测到电平变化就触发

```bash
echo rising > /sys/class/gpio/gpio133/edge
# 意思：往/sys/class/gpio/gpio133/edge文件写入rising
```

## 📃Python实现对GPIO操作的方法

> 从Linux版本4.8开始，不再使用GPIO sysfs接口，而是使用GPIO gpiolib 接口

### 方法™①：通过运行命令的方法进行实现

> 运行命令进行实现

#### ✅os.system方法

> **os.system**方法是os模块最基础的方法，其它的方法一般在该方法基础上封装完成。

```python
os.system(cmd)
```

> 执行成功，那么会返回0，表示命令执行成功

> 另外，多条语句执行的方法如下：
>
> 第一种方法是确保工作目录的变更和svn都在子进程中进行，可以使用复合语句（如`os.system('cd path-to-repo && svn ci')`）或多个语句（如`os.system('cd path-to-repo; svn ci')`）。
>
> 第二种方法则是先在父进程中切换工作目录`os.chdir('path-to-repo')`，再利用ps1原理，执行子进程即可`os.system('svn ci')`。
>
> ps1:父进程的环境变量(environment variables)会默认传递到子进程中(工作目录PWD就是环境变量之一)

#### ✅os.popen方法

> 该方法不但执行命令还返回执行后的信息对象

```python
popen(cmd [, mode='r' [, bufsize]])
```

| 参数    |                                                              |
| ------- | ------------------------------------------------------------ |
| cmd     | 运行环境下的命令                                             |
| mod     | 模式权限[只读(r)、写入(w)]，默认r                            |
| bufsize | 指明了文件需要的缓冲大小，0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位），负的bufsize意味着使用系统的默认值，默认使用系统默认缓冲 |

> 返回一个文件描述符号为fd的打开的信息对象

| 方法      | 意思                                        | 例子                     |
| --------- | ------------------------------------------- | ------------------------ |
| read      | 获取命令执行后的全部内容，并返回字符串      | os.popen(‘ls’).read()    |
| readlines | 获取命令执行后的每一行内容，并返回列表      | os.popen(‘ls’).readlines |
| readline  | 获取命令执行后的第一行内容，并返回字符串(?) | os.popen(‘ls’).readline  |

> 以上操作均会产生阻塞

#### ✅subprocess模块（待学习）

> [Subprocess模块文档](https://docs.python.org/3/library/subprocess.html)

```python
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
```

> - args：表示要执行的命令。必须是一个字符串，字符串参数列表。
> - stdin、stdout 和 stderr：子进程的标准输入、输出和错误。其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者 None。subprocess.PIPE 表示为子进程创建新的管道。subprocess.DEVNULL 表示使用 os.devnull。默认使用的是 None，表示什么都不做。另外，stderr 可以合并到 stdout 里一起输出。
> - timeout：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。
> - check：如果该参数设置为 True，并且进程退出状态码不是 0，则弹 出 CalledProcessError 异常。
> - encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。
> - shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。

```python
subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, 
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)
```

> - args：shell命令，可以是字符串或者序列类型（如：list，元组）
> - bufsize：缓冲区大小。当创建标准流的管道对象时使用，默认-1。
>   0：不使用缓冲区
>   1：表示行缓冲，仅当universal_newlines=True时可用，也就是文本模式
>   正数：表示缓冲区大小
>   负数：表示使用系统默认的缓冲区大小。
> - stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
> - preexec_fn：只在 Unix 平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
> - shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
> - cwd：用于设置子进程的当前目录。
> - env：用于指定子进程的环境变量。如果 env = None，子进程的环境变量将从父进程中继承。

```python
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)
```

> 运行*args*描述的命令。等待命令完成，然后返回[`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode)属性。

#### ✅commands模块❗不推荐使用❗

```python
commands.getoutput(cmd)
```

> 执行命令，并返回输出的内容，返回结果为str

```python
commands.getstatusoutput(cmd)
```

> 执行命令，并返回执行的状态和输出的内容，返回结果为int和str。

### 方法™②：通过File方法进行实现

> 对相应的文件进行读取、写入等操作来实现

