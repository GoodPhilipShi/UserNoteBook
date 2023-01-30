# C++语言的学习

## 🌐你好，世界

```c++
#include <iostream>
int main() {
    std::cout << "你好，世界" << std::endl;
    return 0;
}
```

## 变量

### 定义变量的方法

```c++
类型名 变量名 变量值;
```

## 常量

### 定义常量的方法

- `#define` 宏常量，直接定义常量
- `const` 修饰变量，将变量变成常量

```c++
#define 常量名 常量值;
const 类型名 变量名 变量值;
```

## 数据类型

### 整型

| 整型分类  | 含义     |
| --------- | -------- |
| short     | 短整型   |
| int       | 整型     |
| long      | 长整型   |
| long long | 长长整型 |

### 实型

| 实型分类 | 含义   |
| -------- | ------ |
| float    | 单精度 |
| double   | 双精度 |

### 字符型

```c++
char a = '1';
```

- `0-31`控制字符
- `32-126`打印字符

### 字符串型

- C语言`char 变量名[] = "字符串值";`
- C++语言 `string 变量名 = "字符串值";`

### 布尔类型

- `bool 变量名 = true;`

## 数据的输入输出

- `cin >> 变量;`
- `cout << 输出内容 << endl`

## 运算符

### 算术运算符

| 运算符 | 术语       | 示例  |
| ------ | ---------- | ----- |
| `+`    | 正号       | `+1`  |
| `-`    | 负号       | `-1`  |
| `+`    | 加         | `1+1` |
| `-`    | 减         | `1-1` |
| `*`    | 乘         | `1*1` |
| `/`    | 除         | `1/1` |
| `%`    | 取模(取余) | `1%1` |
| `i++`  | 后置递增   | `1++` |
| `++i`  | 前置递增   | `++1` |
| `i--`  | 后置递减   | `1--` |
| `--i`  | 前置递减   | `--1` |

### 赋值运算符

| 运算符 | 术语   | 示例                |
| ------ | ------ | ------------------- |
| `=`    | 赋值   | `a=1;`              |
| `+=`   | 加等于 | `a+=1;` ==> `a=a+1` |
| `-=`   | 减等于 | `a-=1;` ==> `a=a-1` |
| `*=`   | 乘等于 | `a*=1;` ==> `a=a*1` |
| `/=`   | 除等于 | `a/=1;` ==> `a=a/1` |
| `%=`   | 模等于 | `a%=1;` ==> `a=a%1` |

### 比较运算符

| 运算符 | 术语     | 示例     |
| ------ | -------- | -------- |
| `==`   | 相等于   | `a == b` |
| `!=`   | 不等于   | `a != b` |
| `<`    | 小于     | `a < b`  |
| `>`    | 大于     | `a > b`  |
| `<=`   | 小于等于 | `a <= b` |
| `>=`   | 大于等于 | `a >= b` |

### 逻辑运算符

| 运算符 | 术语 | 示例     |                |
| ------ | ---- | -------- | -------------- |
| `!`    | 非   | `!a`     | 假非真，真非假 |
| `&&`   | 与   | `a && b` | 有假假，无假真 |
| `||`   | 或   | `a || b` | 有真真，无真假 |

## 程序流程结构

基本结构：`顺序结构`，`选择结构`，`循环结构`

### 选择结构

#### `if`语句

```c++
void main() {
    if(条件表达式){
        //条件成立
    }else {
        //条件不成立
    }
}
```

#### 三目运算符

```c++
条件？条件成立表达式:条件不成立;
```

#### `switch`语句

```c++
switch(表达式){
    case 结果1: 执行语句1;break;
    case 结果2: 执行语句2;break;
    default 执行语句;break;
}
```

### 循环结构

#### `while`循环语句

```c++
while(循环条件){
    循环条件成立;
}
```

#### `do…while`循环语句

```c++
do{
    第一次运行和循环条件成立;
}while(循环条件);
```

#### `for`循环语句

```c++
for(表达式;条件表达式;递增表达式){
    条件成立;
}
```

> `条件表达式`必须写的，其余的为可选项。

### 跳转语句

#### `break`语句

**作用**：跳出当前循环

#### `continue`语句

**作用**：进入下一次循环

#### `goto`语句

**作用**：无条件跳转

```c++
a: printf("goto语句到此一游");
printf("goto");
goto a;
```

## 数组

### 一维数组

#### 定义一维数组的方法：

- `数据类型 数组名[数组长度];`
- `数据类型 数组名[数组长度] = {值1,值2};`
- `数据类型 数组名[] = {值1,值2,值3};`

### 二维数组

#### 定义二维数组的方法：

- `数据类型 数据名[行数][列数];`
- `数据类型 数据名[行数][列数] = {{数据1，数据2}};`
- `数据类型 数组名[行数][列数] = {数据1，数据2};`
- `数据类型 数组名[][列数] = {数据1，数据2};`

## 函数

**作用**：将一段经常使用的代码封装，减少重复代码

```c++
返回值类型 函数名(参数列表);
返回值类型 函数名(参数列表) {
    函数体语句;
    return 表达式;
}
```

#### 函数的分文件编写

函数分文件编写一般有4个步骤：

- 创建后缀名为`.h`的头文件
- 创建后缀名为`.cpp`的源文件
- 在头文件中写函数的声明
- 在源文件中写函数的定义

##### `.h`头文件

```c++
// swap.h
void swap(int,int);
```

##### `.cpp`源文件

```c++
// swap.cpp
#include "swap.h"
void swap(int num1,int num2){
    int zhong;
    std::printf("原先num1=%d num2=%d\n",num1,num2);
    zhong = num1;
    num1 = num2;
    num2 = zhong;
    std::printf("现在num1=%d num2=%d",num1,num2);
}
```

##### `main.cpp`主文件

```c++
// main.cpp
#include <iostream>
#include "swap.h"
int main() {
    swap(5,10);
    return 0;
}
```

## 指针

### 定义指针

```c++
类型名 *变量名;
```

### 使用指针

```c++
*指针
```

### 指针所占的内存大小

- 在32位系统下占用4字节
- 在64位系统下占用8字节

### 空指针和野指针

- **空指针：**指针变量指向内存中编号为0的空间

  **用途：**初始化指针变量

  **注意：**空指针指向的内存是不可访问的

- **野指针：**指针变量指向非法的内存空间

  **注意：**在程序中野指针是错误

### `const`修饰指针

- 修饰指针 常量指针

  特点：指针的指向可以改变，但是指针指向的值不可以改变

  ```c++
  int a=5;
  const int *p = &int;
  ```

  - `p = 5;`✅
  - `*p = 5;`❎

- 修饰常量  指针常量

  特点：指针指向的值可以改变，但是指针的指向不可以改变

  ```c++
  int * const p = &a;
  ```

  - `p = 5;`❎
  - `*p = 5;`✅

- 修饰常量和指针

  特点：指针的指向不可以改变，指针指向的值也不可以改变

  ```c++
  const int * const p = &a;
  ```

  - `p=5;`❎
  - `*p=5;`❎

### 指针和数组

通过指针访问数组

```c++
int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
int *p = arr;
for (int i = 0; i < sizeof(arr) / sizeof(int); i++) {
    std::cout << *p++ << std::endl;
}
```

### 指针和函数

传递指针，才能改变实参

### 指针、数组、函数

案例描述：封装一个函数，利用冒泡排序，实现对整型数组的升序排序

```c++
#include <iostream>
void paixu(int *,int);
void paixu(int *arr, int len) {
    int zhong = 0;
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                zhong = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = zhong;
            }
        }
    }
}

int main() {
    int arr[10] = {4, 6, 9, 3, 1, 2, 10, 8, 7, 5};
    int *p = arr;
    int len = sizeof(arr) / sizeof(arr[0]);
    paixu(arr, len);
    std::printf("---------------------\n");
    for (int i = 0; i < sizeof(arr) / sizeof(int); i++) {
        std::cout << *p++ << std::endl;
    }

    return 0;
}

```

## 结构体

结构体属于用户自定义的数据类型，允许用户存储不同的数据类型

### 结构体定义和使用

```c++
struct 结构体名 {
    结构体成员列表;
}
```

通过结构体创建变量的三种方法：

- `struct 结构体名 变量名;`
- `struct 结构体名 变量名 = {值1,值2};`
- 定义结构体时顺便创建变量

#### 总结

- 定义结构体时`struct`不可省略
- 声明(创建)变量时可以省略`struct`
- 通过`变量名.结构体成员名`进行访问

### 结构体数组

**作用：**将自定义的结构体放到数组中方便维护

**语法：**`struct 结构体 数组名[元素个数]={{},{},{},{},{}}`

```c++
#include <iostream>
using namespace std;
struct Stu {
    string name;
    int age;
    string sex;
};
int main() {
    struct Stu stus[] = {
            {"张三", 3, "男"},
            {"李四", 4, "男"}
    };
    int length = sizeof(stus) / sizeof(stus[0]);
    for (int i = 0; i < length; i++) {
        printf("姓名：%s 年龄：%d 性别：%s\n", stus[i].name.c_str(), stus[i].age, stus[i].sex.c_str());
    };
    return 0;
};
```

### 结构体指针

- 利用操作符`->`可以通过结构体指针访问结构体属性

```c++
#include <iostream>
using namespace std;
struct Stu {
    string name;
    int age;
    string sex;
};
int main() {
    struct Stu stu = {"张三", 3, "男"};
    struct Stu *p = &stu;
    printf("姓名：%s 年龄：%d 性别：%s\n", p -> name.c_str(), p -> age, p->sex.c_str());
    return 0;
};
```

### 结构体嵌套结构体

```c++
#include <iostream>
using namespace std;
struct Stu {
    string name;
    int age;
    string sex;
};
struct Teacher {
    string name;
    int age;
    string sex;
    struct Stu stu;
};
int main() {
    struct Teacher t = {"李四", 4, "男", {"张三", 3, "男"}};
    printf("老师的名字：%s\t老师的年龄：%d\t\t老师的性别：%s\n"
           "老师教授的学生的姓名：%s\t老师教授的学生的年龄：%d"
           "\t\t老师教授的学生的姓名：%s\n", t.name.c_str(), 
           t.age, t.sex.c_str(),t.stu.name.c_str(), 
           t.stu.age, t.stu.sex.c_str());
    return 0;
};
```

### 结构体与`const`

- 将函数中的形参改成指针，可以减少内存空间，而且不会产生副本
- 加入`const`，可以防止误操作

```c++
#include <iostream>
using namespace std;
struct Stu {
    string name;
    int age;
    string sex;
};
struct Teacher {
    string name;
    int age;
    string sex;
    struct Stu stu;
};
void printT(const Teacher *t);
void printT(const Teacher *t) {
     printf("老师的名字：%s\t老师的年龄：%d\t\t老师的性别：%s\n"
           "老师教授的学生的姓名：%s\t老师教授的学生的年龄：%d"
           "\t\t老师教授的学生的姓名：%s\n", 
            t->name.c_str(), t->age, t->sex.c_str(),
            t->stu.name.c_str(), t->stu.age, t->stu.sex.c_str());
}
int main() {
    struct Teacher t = {"李四", 4, "男", {"张三", 3, "男"}};
    printT(&t);
    return 0;
};
```

## 内存分区模型

C++程序在执行时，将内存大方向划分为4个区域

- **代码区**：存放函数体的二进制代码，由操作系统进行管理的
- **全局区**：存放全局变量和静态变量以及常量
- **栈区**：由编译器自动分配释放，存放函数的参数值、局部变量等
- **堆区**：由程序员分配和释放，若程序员不释放，程序结束时由操作系统回收

**内存四区的意义：**不同的区域存放的数据，赋予不同的生命周期，给我们更大的灵活编程

### `new`操作符

C++中使用`new`开辟一个新的空间

```c++
new int a;
```

`new`返回的时该数据类型的指针

```c++
int *p = new int a;
```

假如想要释放

```c++
delete p;
```

## 引用

```c++
int a = 10;// 类型名 本名 = 值;
int &b = a;//引用 类型名(与上面相同) &别名 = 本名;
b = 20;//这是赋值
```

- 引用必须初始化
- 引用在初始化后，不可以改变

> 引用的本质在C++内部实现是一个指针常量，运行以下代码，你就懂了

```c++
#include <iostream>

void func(int &a){
    a = 100;
}
int main() {
    int a = 10;
    int &b = a;
    b = 20;
    printf("a:%d\n",a);
    printf("b:%d\n",b);

    func(b);
    printf("a:%d\n",a);
    printf("b:%d\n",b);
    return 0;
};
```

## 函数

### 默认参数

> 声明里面有了默认参数，实现里面就不能有，反之，实现里面有了默认参数，声明里面就不要有。

### 占位参数

只写参数类型，不写参数名(即目前无法调用的参数)，调用时必许传(填写)符合参数类型的值

占位参数还可以设置默认值，这样调用时就可以不填那一部分的值

### 函数重载

函数名可以相同，提高复用性

**函数重载满足条件：**

- 同一作用域下
- 函数名称相同
- 函数参数 **类型不同** 或者 **个数不同** 或者 **顺序不同**

注意：

- 引用作为重载条件

  ```c++
  int func(int &a){}
  int func(const int &a){}
  int a = 10;
  func(a);// 调用第一个
  func(10);// 调用第二个
  int &b = a;
  func(b);// 调用第二个
  ```

- 函数重载碰到默认参数

  ```c++
  int func(int a){}
  int func(int a,int b = 10){}
  int func(10);//上面还是下面可以运行(碰到二义性)
  ```

## 类和对象

C++的三大特性：封装、继承、多态

C++认为万物皆对象，对象上有其属性和行为

### 封装

**封装的意义：**

- 将属性和行为作为一个整体，表现生活中的事物
- 将属性和行为加以权限控制

**封装意义①：**

- 在设计类的时候，属性和行为写在一起，表现事物

例如：用封装的方法求⚪的周长

创建类，设置属性，设置行动(函数\方法)

```c++
#include <iostream>

#define PI 3.14

class Circle{
public:
    float r = 4;
    void zhouchang(){
        printf("周长：%g\n",2 * PI * r);
    }

};

int main() {
    Circle c;
    c.r = 9.2;
    c.zhouchang();
    return 0;
};
```

**封装意义②：**类在设计时，可以把属性和行为放在不同的权限下，加以控制

| 权限        | 权限等级 | 权力                         |
| ----------- | -------- | ---------------------------- |
| `public`    | 公共权限 | 类外、类内可以访问           |
| `protected` | 保护权限 | 类内可以访问，类外不可以访问 |
| `private`   | 私有权限 | 类内可以访问，类外不可以访问 |

#### `struct`和`class`区别

在C++中`struct`和`class`的唯一区别在于**默认的访问权限不同**

- `struct`默认权限为**公共**
- `class`默认权限为**私有**

#### 成员属性设置为私有

**优点①：**将所有所有成员属性设置为私有，可以自己控制读写权限

**优点②：**对于写权限，我们可以检测数据的有效性

### 对象的初始化和清理

#### 构造函数和析构函数

- 构造函数：主要作用在于创建对象时为对象的成员属性赋值，构造函数由编译器自动调用，无须手动调用
- 析构函数：主要作用于对象销毁前系统自动调用，执行一些清理工作

##### 构造函数

```c++
类名(){}
```

- 构造函数、没有返回值也不写`void`

- 函数名称于类名相同

- 构造函数可以由参数，因此可以发生重载

- 程序在调用对象是偶会自动调用构造，无需手动调用，而且只会调用一次

  ```c++
  class A{
      A(){
          // 构造函数
          // 函数名与类名相同
      }
  }
  ```

##### 析构函数

```c++
~类名(){}
```

- 析构函数，没有返回值也不写`void`
- 函数名称与类名称相同，在名称前添加上`~`
- 析构函数不可以由参数，因此不可以发生重载
- 程序在对象销毁前会自动调用析构，无需手动调用，而且只会调用一次

  ```c++
  class A{
      ~A(){
          // 构造函数
          // 函数名与类名相同
      }
  }
  ```

##### 构造函数的分类与调用

- 普通构造函数
- 有参构造函数：有参
- 拷贝构造函数：参数为类的对象

```c++
#include <iostream>
using namespace std;
class Cube {
public:
    Cube() {
        printf("这个是普通构造函数\n");
    }
    Cube(int a) {
        printf("这个是参数构造函数\n");
    }
    Cube(Cube &a) {
        printf("这个是拷贝构造函数");
    }
};
int main() {
    // 括号法
    Cube c1; //这个是普通构造函数的调用方法
    Cube c2(10); //这个是参数构造函数的调用方法
    Cube c3(c2); //这个是拷贝构造函数的调用方法
    // 显示法 // 我没有但是无法成功
    Cube c4;//这个是普通构造函数的调用方法
    Cube c5 = Cube(10);//这个是参数构造函数的调用方法
    Cube c6 = Cube(c5);//这个是拷贝构造函数的调用方法
    // 隐式转换法 // 我没有但是无法成功
    Cube c7 = 10;
    Cube p5 = p7;
};
```

#### 深拷贝和浅拷贝

- 浅拷贝：复制指向地址
- 深拷贝：复制赋值

````c++
class Cube {
public:
    int height;
    Cube(Cube &a) {
        printf("这个是拷贝构造函数");
        //height = a.heght;// 浅拷贝
        //height = new int(*a.heght);// 深拷贝
    }
    ~Cube(){
    	printf("这个是析构函数构造函数");
        delete height;// 清理元素
        // 1.如果是浅拷贝的话，height的指向内存 和 a.heght的指向内存相同，即当第一height被清除时，第二height就无法进行清除操作(非法操作)
        // 2.如果是深拷贝的话，height的指向内存 和 a.heght的指向内存不相同，即当第一height被清除时，第二height也可以进行清除操作
    }
};
````

## 继承

> 减少重复的代码

```c++
#include <iostream>
using namespace std;
class Base{
public:
    void see(){
        printf("我是父类");
    }
};
class Cube: public Base{
public:
    void see(){
        printf("我继承了父类");
    }
};
int main() {
    Cube c;
    c.see();
    return 0;
};
```

### 继承的三种方式

- 公共继承`class B:public A`
  - 除了私有的，其他的都可以访问
- 保护继承`class B:protected A`
  - 除了私有的，其他的都可以访问
  - 并且公共权限变成保护权限
- 私有继承`class B:private A`
  - 除了私有的，其他的都可以访问
  - 并且公共权限和保护权限变成私有权限

> `cl /dl reportSingleClassLayout类名 文件名`
>
> 例如：`cl /dl reportSingleClassLayoutAce "test.cpp"`

### 继承中构造函数和析构函数的顺序

继承中 先调用父类的构造函数，在调用子类的构造函数，析构函数的顺序相反

### 继承中的同名成员处理

```c++
#include <iostream>
using namespace std;
class A{
public:
    void hh(){
        printf("哈哈\n");
    }
};
class B:public A{
public:
    void hh(){
        printf("呵呵\n");
    }
};
int main(){
    B b;
    b.hh();
    b.A::hh();
    return 0;
};
```

> 1. 子类对象可以直接访问到子类中同名的成员
> 2. 子类对象加作用域可以访问到父类同名成员
> 3. 当子类与父类拥有同名的成员函数，子类会隐藏父类中同名函数，加作用域可以访问到父类中同名函数

## 多态

多态分两类

- 静态多态：函数重载 和 运算符重载 属于静态多态
- 动态多态：派生类(父类)和虚函数实现运行多态

### 虚函数

在函数前添加`virtual`，该函数就变成虚函数了

## 补充

### 错误：`printf`打印`string`

> Cannot pass object of non-trivial type 'std::string' (aka 'basic_string<char>') through variadic function; call will abort at runtime

原因分析：`printf`属于C语言中的方法，而C语言中无`string`类型

解决方案：所以为了打印`string`类型的变量，必须通过string类对象的成员函数`c_str()`把string对象转换成C中的字符串样式，如下：

```c++
printf("%s\n", edges.c_str());
```

