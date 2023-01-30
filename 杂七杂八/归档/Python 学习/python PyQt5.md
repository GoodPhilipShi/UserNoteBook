# 『💡重点学习💡』信号与槽

## 基本概念

> 信号(Signal)和槽(Slot的Qt中的核心机制，主要作用在于对象之间进行通讯

### 信号-Signal

> 当一个控件的状态发送变化时，向外界发出的信息

### 槽-Slot

> 一个执行某些操作的函数/方法

### 总结

> 所有继承自`QWidget`的控件都支持“信号与槽”的机制

## 机制描述

### 手动操作

> 将会控件事件的信号与槽绑定(关联)

### 自动操作

> 当信号发出时，连接的槽函数会自动执行

## 基本使用介绍

### 信号

#### 控件内置的一些信号

- `QPushButton().pressed`
- ``QPushButton().clicked`
- ……

#### 自定义信号

- `pyqtSignal()`

### 槽

- 不同的控件内置的槽函数

- 自定义的函数/方法

### 连接方式

```python
object.信号.connect(槽函数)
```

### 特性

- 一个信号可以连接多个槽函数
- 一个信号也可以连接另外一个信号
- 信号的参数可以是任何Python类型的
- 一个槽可以监听多个信号
- ……

# `PyQt5` 基础控件

## 控件分类

> https://www.bilibili.com/video/BV1UZ4y1p7PA?p=21

### 按钮

##### `QPushButton`

> 点击按钮

##### `QCommandLinkButton`

> 命令连接按钮

##### `QRadioButton`

> 单选按钮

##### `QCheckBox`

> 多选按钮

### 输入控件

#### 纯键盘输入

##### `QLinkEdit`

> 单行输入框-普通文本

##### `QTextEdit`

> 多行输入框-富文本

##### `QPlainTextEdit`

> 多行输入框-普通文本

##### `QKeySequenceEdit`

> 热键采集

#### 步长调节(键盘+鼠标)

##### `QDaleTimeEdit`

> 日期时间调节
>
> #### `QDateEdit`
>
> > 日期调节
>
> #### `QTimeEdit`
>
> > 时间调节

##### `QSpinBox`

> 整型调节

##### `QDoubleSpinBox`

> 浮点型调节

#### 组合框

##### `QComboBox`

> 自定义下拉框
>
> #### `QFontComboBox`
>
> > 限定字体下拉框

#### 滑块

##### `QDial`

> 旋转滑块(旋钮)

##### `QSlider`

> 平移滑块

##### `QScrollBar`

> 滚动条

#### 橡皮筋选中

##### `QRubberBand`

> 橡皮筋框(方框选中)

#### 对话框

##### `QColorDialog`

> 颜色对话框(选择颜色)

##### `QFileDialog`

> 文件对话框(选择文件)

##### `QFontDialog`

> 字体对话框(选择字体)

##### `QInputDialog`

> 输入对话框(用于接收)

#### 日期

##### `QCalendarWidget`

> 日历空间

### 展示控件

##### `QLabel`

> 标签(展示普通文本、数字、富文本、图片、动画)

##### `QLCDNumber`

> 显示数字的LCD灯

##### `QProgressBar`

> 进度条

#### 对话框

##### `QMessageBox`

> 信息对话框

##### `QErrorMessage`

> 错误对话框

##### `QProgressDialog`

> 进度对话框

### 容器控件

##### `QToolBox`

> 承载按钮

##### `QDialogButtonBox`

> 承载对话框的按钮

##### `QGroupBox`

> 分组

##### `QMdiSubWindow`

> #### `QMdiArea和QMdiSubWindow`

### 结构控件

##### `QMainWindow`

> 主控件
>
> #### `QMenuBar`
>
> > 菜单栏
> >
> > #### `QMenu`
> >
> > > 菜单控件
>
> #### `QToolBar`
>
> > 工具栏
> >
> > #### `QToolButton`
> >
> > > 工具按钮
>
> #### `QStatusBar`
>
> > 状态栏

##### `QTabwifget`

> 标签控件
>
> #### `QTabBar`
>
> > 单独标签控件

##### `QStackedWidget`

> 栈结构(?) 多界面

##### `QSplitter`

> 分割窗口

##### `QDockWidget`

> 悬浮窗口

### 滚动控件

#### Qt滚动区域原理(`QAbstractScrollArea`)

##### `QTextBrowser`

> 文本滚动

##### `QScrollArea`

> 滚动区域

##### `QAbstractitemView`

> #### `QColumnView`
>
> > 列视图
>
> #### `QHeaderView`
>
> > 头部视图
>
> #### `QListView`
>
> > > #### `QListWidget`
> > >
> > > > 展示列表中元素
> > >
> > > #### `QUndoView`
> > >
> > > > 是否撤销
>
> #### `QTableView`
>
> > #### `QTableWidget`
> >
> > > 列表视图
>
> #### `QTreeView`
>
> > #### `QTreeWidget`
> >
> > > 树形结构

##### `QMdiarea`

> 子控件组合

##### `QGraphicsView`

> 画图控件

### 辅助控件

##### `QFocusFrame`

> 获取焦点

##### `QSizeGrip`

> 窗口大小控件

##### `QDesktopWidget`

> 桌面信息详情

### 其他

#### 向导/打印

##### `QWizard`

> 向导页
>
> #### `QWizardPage`
>
> > 单独的向导页

##### `QAbstractPrintDialog`

> #### `QPrintDialog`
>
> > 打印对话框

##### `QPrintPreviewDialog`

> 打印预览

##### `QPageSetupDialog`

> 页面设置

#### 欢迎界面

##### `QSplahScreen`

> 欢迎界面

#### 功能性控件

##### `QVideoWidget`

> 视频控件
>
> #### `QCameraViewfinder`
>
> > 相机控件

##### `QWebEngineView`

> 浏览器

# `PyQt5 QObject`的学习

## 🚩`PyQt5`对象的名称和属性

### 设置对象名称、属性和样式

#### `setObjectName`方法

> 设置名称

```python
object.setObjectName("姓名")
```

#### `setProperty`方法

> 设置属性

```python
object.setProperty("属性名称","属性")
```

#### `setStyleSheet`方法

> 设置样式

```python
object.setStyleSheet("样式内容")
# 例子,设置对象的背景颜色为红色
object.setStyleSheet("background-color:red;")
```

### 获取对象名称、属性

#### `objectName`方法

> 获取名称

```python
object.objectName()
```

#### `property`方法

> 获取属性

```python
object.property()
```

## 🚩`PyQt5`对象的父子关系

### 设置父子关系

#### `setParent`方法

> 设置父类对象

```python
object.setParent("父类对象")
```

### 获取对象父对象、子对象

#### `parent`方法

> 获取父类对象

```python
object.parent()
```

#### `children`方法

> 获取所有子类对象

```python
object.children()
```

#### `findChild`方法

> 获取某个指定名称和类型的子对象

```python
object.findChild(类型,"名称")
# 例子，查找名为btn1的QPushButton的子对象
object.findChild(QPushButton,"btn1")
```

#### `findChildren`方法

> 获取类型的所有子对象

```python
object.findChildren(类型)
```

## 🚩`PyQt5`对象的信号处理

### 信号与槽

> `PyQt5`有一个独一无二的信号和槽机制来处理事件。信号和槽用于对象之间的通信。当指定事件发生，一个事件信号会被发射。槽可以被任何Python脚本调用。当和槽连接的信号被发射时，槽会被调用。

#### 🔗连接

> 在`PyQt5`中信号与槽通过connect()方法连接s

```python
object.signal.connect()
```

#### 🔗断开

```python
object.blockSignals(True) # 暂时中断连接
object.blockSignals(False) # 恢复连接
object.disconnect() # 断开连接
```

### 事件

>### 常见事件如下：
>
>键盘事件、鼠标事件、拖放事件、滚轮事件、定时事件、焦点事件、进入和离开事件（光标移入控件或者移出），移动事件（窗口位置变化），
>
>显示和隐藏事件，窗口事件（窗口是否为当前窗口）、以及常见的Qt事件：Socket事件、剪贴板事件、文字改变事件，布局改变事件；

#### `objectNameChanged`事件

> 对象名称改变事件

```python
object.objectNameChanged.connect("方法 or 函数")
```

#### `destroyed`事件

> 对象删除事件

```python
object.destroyed.connect("方法 or 函数")
```

## `PyQt5`对象的类型判断

### `isWidgetType`方法

> 判定是不是控件类型

```python
object.isWidgetType()
```

### `inherits`方法

> 判定是不是继承父类对象

````python
object.inherits("父类对象")
# 例子，这个对象是不是继承QLabel
object.inherits("QLabel")
````

## `PyQt5`对象的删除

### `deletelater`方法

> `deletelater`方法不会立即销毁对象，直到消息循环执行完毕后，等到下一次再删除

## `PyQt5`对象的事件处理-无详细内容

### `childEvent`方法

### `customEvent`方法

### `eventFilte`方法

### `installEventFilter`方法

### `removeEventFilter`方法

### `event`方法

### 事件机制

> 可以看成是对“信号处理”的信号与槽的补充
>
> > 信号与槽机制是对事件机制的高级封装
> > 事件机制更偏底层(远离用户)

## `PyQt5`对象的定时器

### `startTimer`方法

> 开启定时器

```python
object.startTimer(时间，定时器类型) -> 定时器id
# 时间 毫秒类型
# 定时器类型
Qt.PreciseTimer # 精定时器：尽可能保持毫秒准确
Qt.CoarseTimer # 粗定时器：5%的误差间隔
Qt.VeryCoarseTimer # 很粗的定时器：只能到秒级
# 定时器id 定时器的唯一标识
```

### `KillTimer`方法

> 根据定时器id关闭定时器

```python
object.killTimer(定时器id)
```

### `timeEvent`方法

> 定时器执行事件

```python
object.timeEvent("方法 or 函数")
```

# `PyQt5 QWidget`的学习

> https://www.bilibili.com/video/BV1UZ4y1p7PA?p=20

## 🚩`PyQt5`控件的创建

```python
# 无父控件，则为顶层控件
win1 = QWidget()
# 并且需要show方法来展示
win1.show()
# 有父控件，不需要show方法，就可以展示，依托于父控件
win2 = QWidget(win1)
```

## 🚩`PyQt5`控件的大小位置

> X:自左而右
> Y:自上而下

### 获取大小、位置

#### `x`方法

> 获取坐标X
>
> > 有父控件，则x值为相对于父控件的x位置
> > 无父控件，则x值为桌面的x位置

```python
widget.x()
```

#### `y`方法

> 获取坐标Y
>
> > 有父控件，则y值为相对于父控件的y位置
> > 无父控件，则y值为桌面的y位置

```python
widget.y()
```

#### `pos`方法

> x和y的组合

```python
widget.pos()
```

#### `wight`方法

> 控件的宽度

```python
widget.wight()
```

#### `heigh`方法

> 控件的高度

```python
widget.heigh()
```

#### `size`方法

> 控件的大小

```python
widget.size()
```

#### `geometry`方法

> 用户区域相对于父控件的位置和尺寸组合

```python
widget.geometry()
```

#### `rect`方法

> 位置和宽高的组合

```python
widget.rect()
```

#### `frameSize`方法

> 框架大小

```python
widget.frameSize()
```

#### `frameGeometry`方法

> 框架尺寸

```python
widget.frameGeometry()
```

### 设置大小、位置

`move`方法

> 设置的是x和y，也就是pos

```python
widget.move(x,y)
```

`resize`方法

> 设置的是宽高，也就是大小，但不包括窗口框架

```python
widget.resize(width,height)
```

`setGeometry`方法

> 注意：此处参照为用户区域

```python
widget.setGeometry(x_noFrame,y_noFrame,width,height)
```

`adjustSize`方法

>  根据内容自适应
>  

```python
widget.adjustSize()
```

`serFixedSize`方法

> 设置固定尺寸
> 

```python
widget.serFixedSize(width,height)
```

## 🚩`PyQt5`控件的最大和最小尺寸

### 获取最大和最小尺寸

#### `minimumWidth`方法

> 获取最小尺寸的宽度
> 

```python
widget.minimumWidth()
```

#### `minimumHeight`方法

> 获取最小尺寸的高度
> 

```python
widget.minimumHeight()
```

#### `minimumSize`方法

> 获取最小尺寸的大小
> 

```python
widget.minimumSize()
```

#### `maximumWidth`方法

> 获取最大尺寸的宽度
> 

```python
widget.maximumWidth()
```

#### `maximumHeight`方法

> 获取最大尺寸的高度
> 

```python
widget.maximumHeight()
```

#### `maximumSize`方法

> 获取最大尺寸的大小
> 

```python
widget.maximumSize()
```

### 设置最大和最小尺寸

#### `setMinimumWidth`方法

> 设置最小尺寸的宽度
> 

```python
widget.setMinimumWidth(width)
```

#### `setMinimumHeight`方法

> 设置最小尺寸的高度
> 

```python
widget.setMinimumHeight(height)
```

#### `setMinimumSize`方法

> 设置最小尺寸的大小
> 

```python
widget.setMinimumSize(width,height)
```

#### `setMaximumWidth`方法

> 设置最大尺寸的宽度
> 

```python
widget.setMaximumWidth(width)
```

#### `setMaximumHeight`方法

> 设置最大尺寸的高度
> 

```python
widget.setMaximumHeight(height)
```

#### `setMaximumSize`方法

> 设置最大尺寸的大小
> 

```python
widget.setMaximumSize(wigth,height)
```

## 🚩`PyQt5`控件的内容外边框

### 获取内容边距和区域

#### `getContentsMargins`方法

> 获取内容边距

#### `contentsRect`方法

> 获取内容区域

### 设置内容边距

#### `setContentMargins`方法

> 设置内容边距

## 🚩`PyQt5`控件的鼠标相关

### 设置鼠标样式

#### `setCursor`方法

> 设置鼠标样式(状态)

```python
widget.setCursor(鼠标样式)
```

#### 鼠标样式

| 鼠标样式                | 含义           | 示意图                                                       |
| ----------------------- | -------------- | ------------------------------------------------------------ |
| `Qt.CrossCursor`        | 十字形         | ![image-20201204110229790](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112140.png) |
| `Qt.ArrowCursor`        | 箭头型         | ![image-20201204110408385](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112138.png) |
| `Qt.UpArrowCursor`      | 向上箭头       | ![image-20201204110431293](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112137.png) |
| `Qt.IBeamCursor`        | 文本输入       | ![image-20201204110452438](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112135.png) |
| `Qt.WaitCursor`         | 等待           | ![鼠标等待](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112133.gif) |
| `Qt.BusyCursor`         | 繁忙           | ![鼠标繁忙](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112131.gif) |
| `Qt.ForbiddenCursor`    | 禁止           | ![image-20201204111617938](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112129.png) |
| `Qt.PointingHandCursor` | 指向           | ![image-20201204111645469](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112127.png) |
| `Qt.WhatsThisCursor`    | 这是什么       | ![image-20201204111705137](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112124.png) |
| `Qt.SizeVerCursor`      | 垂直拖拽       | ![image-20201204111727704](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112122.png) |
| `Qt.SizeHorCursor`      | 水平拖拽       | ![image-20201204111750463](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112121.png) |
| `Qt.SizeBDiagCursor`    | 对角线调整大小 | ![image-20201204111827194](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112119.png) |
| `Qt.SizeAllCursor`      | 移动对象       | ![image-20201204111853477](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112111.png) |
| `Qt.SplitHCursor`       | 水平拆分条     | ![image-20201204111921987](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112101.png) |
| `Qt.SplitVCursor`       | 垂直拆分条     | ![image-20201204111943363](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112059.png) |
| `Qt.OpenHandCursor`     | 打开           | ![image-20201204112005840](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112056.png) |
| `Qt.ClosedHandCursor`   | 关闭           | ![image-20201204112023374](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112053.png) |
| `Qt.BlankCursor`        | 空白           | ![image-20201204112041369](https://gitee.com/acg-q/pic-go-images/raw/master/20201204112049.png) |

#### 自定义鼠标样式

```python
# 创建鼠标样式
pixmap = QPixmap(文件位置).scaled(widght,height)
# scaled 就是设置鼠标样式的大小
cursor = QCursor(pixmap,x,y)
# x,y就是设置当鼠标的那个位置离开控件时解除鼠标样式
# 设置鼠标样式
widget.setCursor(cursor)
```

### 重置鼠标形状

#### `unsetCursor`方法

```python
widget.unsetCursor()
```

### 获取鼠标

#### `cursor`方法

```python
widget.cursor()
```

## 🚩`PyQt5`控件的事件

### `mouseMoveEvent`事件

> 鼠标移动

### `mouseReleaseEvent`事件

> 鼠标松开

### `mousePressEvent`事件

> 鼠标按下

## 🚩`PyQt5`控件的父子关系

> https://www.bilibili.com/video/BV1UZ4y1p7PA?p=24

### `childAt`方法

> 获取在指定坐标的控件

### `parentWidget`方法

> 获取指定控件的父控件

### `childrenRect`方法

> 所有子控件组成的边界矩形

## 🚩`PyQt5`控件的层级控制

## 🚩`PyQt5`控件的顶层窗口相关

## `PyQt5`控件的交互状态

## `PyQt5`控件的信息提示

## `PyQt5`控件的焦点控制
