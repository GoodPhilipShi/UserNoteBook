PySide2等同于PyQt5

> [官方文档](https://doc.qt.io/qtforpython)
>
> 运行不成功，暂时不学

## PySide2、PyQt5 简介

PySide2、PyQt5 都是基于著名的 Qt 库。

Qt库里面有非常强大的图形界面开发库，但是Qt库是C++语言开发的，PySide2、PyQt5可以让我们通过Python语言使用Qt。

但是 PySide2、PyQt5 这两者有什么区别呢？

可以形象地这样说： PySide2 是Qt的 `亲儿子` ， PyQt5 是Qt还没有亲儿子之前的收的 `义子` （Riverbank Computing这个公司开发的）。

那为什么 PyQt5 这个义子 反而比 PySide2 这个亲儿子更出名呢？

原因很简单：PySide2 这亲儿子最近（2018年7月）才出生。

但是亲儿子毕竟是亲儿子，Qt准备大力培养，PySide2 或许更有前途。

已经在使用 PyQt5 的朋友不要皱眉， 两个库的使用 对程序员来说，差别很小：它们的调用接口几乎一模一样。

如果你的程序是PyQt5开发的，通常只要略作修改，比如把导入的名字从 PyQt5 换成 PySide2 就行了。反之亦然。

> 注意：必须先具备Python基础知识，才可以学习本教程。还没有Python基础的朋友，可以直接学习本网站的Python基础教程。

## 安装 PySide2

很简单，直接执行

```py
pip install pyside2
```

即可下载安装。

这个库比较大，大概有100M左右，大家耐心等待。

有的朋友，网络比较慢，可以指定国内的安装源，下载安装。

比如，使用豆瓣源下载安装：

```
pip install pyside2 -i https://pypi.douban.com/simple/
```

建议：如果你的程序要发布给客户使用，建议使用32位的Python解释器，这样打包发布的exe程序可以兼容32位的Windows

注意：

Qt 官方网站声明了： `Windows上 Python 3.8.0` 调用 Qt 5.14 ， 会有问题。

有类似下面这样的导入错误

```
ImportError: Dll load failed while importing shiboken2: 找不到指定的程序
```

所以， `就是不能用 Python 3.8.0` ，请使用3.8.1或者以后的版本， Python 3.7 也可以。

## 安装PyQt5

如果你选择PyQt5，直接执行

```py
pip install pyqt5-tools
```

即可同时安装 PyQt5 和 一些重要的工具，比如 Qt designer。

现在我们要开发一个程序，让用户输入一段文本包含：员工姓名、薪资、年龄。

格式如下：

```py
薛蟠     4560 25
薛蝌     4460 25
薛宝钗   35776 23
薛宝琴   14346 18
王夫人   43360 45
王熙凤   24460 25
王子腾   55660 45
王仁     15034 65
尤二姐   5324 24
贾芹     5663 25
贾兰     13443 35
贾芸     4522 25
尤三姐   5905 22
贾珍     54603 35
```

该程序可以把薪资在 2万 以上、以下的人员名单分别打印出来。

当然我们可以像以前一样，开发命令行程序（准确的说应该叫字符终端程序，因为UI是字符终端），让用户在字符终端输入。

### 图形界面

```python
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)

window.show()

app.exec_()
```

`QApplication` 提供了整个图形界面程序的底层管理功能，比如：

初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…

对 QApplication 细节比较感兴趣的话，可以[点击这里参考官方网站](https://doc.qt.io/qt-5/qapplication.html)

既然QApplication要做如此重要的初始化操作，所以，我们必须在任何界面控件对象创建前，先创建它。

QMainWindow、QPlainTextEdit、QPushButton 是3个控件类，分别对应界面的主窗口、文本框、按钮

他们都是控件基类对象QWidget的子类。

要在界面上 `创建一个控件` ，就需要在程序代码中 `创建` 这个 `控件对应类` 的一个 `实例对象`。



在 Qt 系统中，控件（widget）是 `层层嵌套` 的，除了最顶层的控件，其他的控件都有父控件。

QPlainTextEdit、QPushButton 实例化时，都有一个参数window，如下

```python
QPlainTextEdit(window)
QPushButton('统计', window)
```

就是指定它的父控件对象 是 window 对应的QMainWindow 主窗口。

而 实例化 QMainWindow 主窗口时，却没有指定 父控件， 因为它就是最上层的控件了。



控件对象的 move 方法决定了这个控件显示的位置。

比如

`window.move(300, 310)` 就决定了 主窗口的 左上角坐标在 `相对屏幕的左上角` 的X横坐标300像素, Y纵坐标310像素这个位置。

`textEdit.move(10,25)` 就决定了文本框的 左上角坐标在 `相对父窗口的左上角` 的X横坐标10像素, Y纵坐标25像素这个位置。



控件对象的 resize 方法决定了这个控件显示的大小。

比如

`window.resize(500, 400)` 就决定了 主窗口的 宽度为500像素，高度为400像素。

`textEdit.resize(300,350)` 就决定了文本框的 宽度为300像素，高度为350像素。



放在主窗口的控件，要能全部显示在界面上， 必须加上下面这行代码

```python
window.show()
```

最后 ，通过下面这行代码

```python
app.exec_()
```

进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。

## 界面动作处理 (signal 和 slot)



[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=3)

接下来，我们要实现具体的统计功能：

当用户点击 **统计** 按钮时， 从界面控件 QPlainTextEdit 里面获取 用户输入的字符串内容，进行处理。

首先第一个问题： 用户点击了 **统计** 按钮，怎么通知程序？ 因为只有程序被通知了这个点击，才能做出相应的处理。

在 Qt 系统中， 当界面上一个控件被操作时，比如 被点击、被输入文本、被鼠标拖拽等， 就会发出 `信号` ，英文叫 `signal` 。就是表明一个事件（比如被点击、被输入文本）发生了。

我们可以预先在代码中指定 处理这个 signal 的函数，这个处理 signal 的函数 叫做 `slot` 。

比如，我们可以像下面这样定义一个函数

```python
def handleCalc():
    print('统计按钮被点击了')
```

然后， 指定 如果 发生了button 按钮被点击 的事情，需要让 `handleCalc` 来处理，像这样

```python
button.clicked.connect(handleCalc)
```

用QT的术语来解释上面这行代码，就是：把 button 被 点击（clicked） 的信号（signal）， 连接（connect）到了 handleCalc 这样的一个 slot上

大白话就是：让 handleCalc 来 处理 button 被 点击的操作。



但是上面这行代码运行后，只能在字符窗口 打印出 `统计按钮被点击了` ， 还不能处理分析任务。

要处理分析任务，我们还得从 textEdit 对应的 文本框中 获取用户输入的文本，并且分析薪资范围，最终弹出对话框显示统计结果。

我们修改后，代码如下

```python
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

def handleCalc():
    info = textEdit.toPlainText()

    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name,salary,age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                '统计结果',
                f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                )

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)
button.clicked.connect(handleCalc)

window.show()

app.exec_()
```

## 封装到类中

上面的代码把控件对应的变量名全部作为全局变量。

如果要设计稍微复杂一些的程序，就会出现太多的控件对应的变量名。

而且这样也不利于 代码的模块化。

所以，我们通常应该把 一个窗口和其包含的控件，对应的代码 全部封装到类中，如下所示

```python
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)


    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
```

```python
# 输入并运行成功归并排序的程序。
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst)/2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)
    return merged

data_list = [6,202,100,301,38,8,1]
print(merge_sort(data_list))
# 输入并运行成功判断天数的程序
import datetime
dtstr = '20181206'
dt = datetime.datetime.strptime(dtstr,"%Y%m%d")
another_dtstr=dtstr[:4]+"0101"
another_dt = datetime.datetime.strptime(another_dtstr,"%Y%m%d")
print(int((dt-another_dt).days)+1)
# 输入并运行成功计算函数的程序
x = float(input())
a = 2
b = -45
c = 13
y = a*x**2+b*x+c
print(x,y)
# 输入并运行成功打印三角形的程序
n=int(input())
for i in range(n):
    line = " "*(n-1-i)+"@"*(2*i+1)
    print(line)
```

