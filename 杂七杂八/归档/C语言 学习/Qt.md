# 基础

## 按钮

### 创建一个按钮

```c++
// 创建一个单纯按钮
QPushButton *btn = new QPushButton;
// 创建一个绑定到某一层窗口的按钮
QPushButton *btn = new QPushButton("直接绑定的按钮", this);
```

### 以顶层方式弹出窗口

```c++
btn->show()
```

### 将按钮添加到某一层窗口

```c++
btn->setParent(this);
```

### 修改按钮描述

```c++
btn->setText("新的按钮");
```

### 移动按钮

```c++
btn->move(100,100);
```

### 调整大小

```c++
btn->resize(50,50);
```

### 例子

> 例如: 在  MainWindow 这一层上添加一个按钮

```c++
MainWindow::MainWindow(QWidget *parent):QMainWindow(parent)
{
    QPushButton *btn = new QPushButton;
    btn->setText("新的按钮");
    btn->setParent(this);
    btn->move(100,100);
    btn->resize(50,50);
}
```

## 窗口

### 窗口命名

```c++
setWindowTitle("第一个窗口");
```

### 设置窗口大小

```c++
resize(600, 400);
```

### 设置固定窗口大小

```c++
setFixedSize(600,400);
```

### 例子

> 例如: 设置  MainWindow 这一层窗口名为”第一个窗口“， 设置窗口大小为600x400

```c++
MainWindow::MainWindow(QWidget *parent):QMainWindow(parent)
{
    setWindowTitle("第一个窗口");
    resize(600, 400);
    setFixedSize(600,400);
}
```

## 重写

> 例如重写QPushButton

### 在头文件(Header Files)中创建MyPushButton.h
```c++
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QPushButton>

class MyPushButton : public QPushButton
{

 Q_OBJECT
public:

 MainWindow(QWidget *parent = nullptr);

 ~MainWindow();

private:

 Ui::MainWindow *ui;

};

#endif // MAINWINDOW_H
```

### 在源文件(Source Files)中创建MyPushButton.cpp
