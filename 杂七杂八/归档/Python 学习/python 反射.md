# Python 反射

> 反射的函数：`setattr`, `hasattr`，`getattr`，`delattr`

## 反射的基础妙用

```python
class Teacher:
    dic = {"1":"show_student","2":"show_teacher"}
    def show_student(self):
        print("students")
    def show_teacher(self):
        print("teacher")

alex = Teacher()
for k in Teacher.dic:
    print(k)
key = input("请输入")
if hasattr(alex,Teacher.dic[key]):
    func = getattr(alex,Teacher.dic[key])
    func()
```

## isinstance和issubclass

> isinstance(obj,cls)检查是否obj是否是类 cls 的对象 ===> 是否为实例化类

```python
class Foo(object):pass
obj = Foo()
isinstance(obj, Foo)
```

> issubclass(sub, super)检查sub类是否是 super 类的派生类 ===> 是否为子类

```python
class Foo(object):pass
class Bar(Foo):pass
issubclass(Bar, Foo)
```

## eval

> eval('print("哈喽")') 效果等于 print("哈喽")
>
> 可是有安全隐患，但是加上反射就解决了安全隐患

```python
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
a = A()
a.name = 'alex'
a.age = 63
setattr(a,"name","233")
eval("print(a.name)") # 有安全隐患,由于命令是字符串，那代表无法直接运行代码、运行代码也是接收来的
ret = getattr(a,'name')
print(ret)             # 这样就解决了安全隐患
```

## `__str__`和`__repr__`

> 改变对象的字符串显示`__str__`,`__repr__`
>
> 并且如果`print(a)`没有`__str__`,则输出`__repr__`的结果(即`__repr__`是`__str__`的备胎)

```python
class A:
    def __str__(self):
        return "this is str"

    def __repr__(self):
        return "this is repr"


a = A()
print(a)
print("%s" % a)
print(repr(a))
print("%r" % a)

# this is str
# this is str
# this is repr
# this is repr
```

## `__len__`

```python
class A:
	def __init__(self,name):
		self.name = name
		self.student = []

	def __len__(self):
		return len(self.student)
a = A("哈哈")
a.student.append('李强1')
a.student.append('李强2') # a.student = ['李强1','李强2']
print(len(a))
```

## `__del__`

> 析构方法，当对象在内存中被释放时，自动触发执行。
>
> 注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。

## `__call__`

> 对象后面加括号，触发执行。
>
> 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()

```python
class A:
	def __call__(self):
        print("嘿嘿")
a = A()
a()
```

## `__getitem__`、 `__setitem__`和`__delitem__`

```python
class A:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __getitem__(self, item):
        if hasattr(self, item):
            return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

f = A('er', 2, 'er')
print(f['name']) # er
f['heihei'] = '嘿嘿'
print(f.__dict__) # {'name': 'er', 'age': 2, 'sex': 'er', 'heihei': '嘿嘿'}
print(f.heihei, f['heihei']) # 嘿嘿 嘿嘿
del f.heihei
print(f.__dict__) # {'name': 'er', 'age': 2, 'sex': 'er'}
```

## `__new__`

```python
class Singleton:
    def __new__(cls, *args, **kw): # 由于在调用时self对象并不存在，所以可以用cls
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

one = Singleton()
two = Singleton()

two.a = 3
print(one.a)  # 3
# one和two完全相同,可以用id(), ==, is检测
print(id(one))  # 29097904
print(id(two))  # 29097904
print(one == two)  # True
print(one is two)  # True
```

### 设计模式-单例模式

> 1. 一个类 始终只有一个实例
> 2. 当你第一次实例化这个类的时候，就创建一个实例化的对象
> 3. 当你再次实例化的时候，就会使用之前创建的对象进行修改
>

```python
class A:
    __instance = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kw):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(A)
        return cls.__instance

a = A('er', 2)
print(a.name)  # er
print(a.__dict__)
b = A('san', 3)
print(a == b)  # True
print(a.name, b.name)  # san san
```

## `__hash__`

> 定义hash方法

```python
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __hash__(self):
        return hash(str(self.a)+str(self.b))
a = A()
print(hash(a))
```

## `__eq__`

> 可自定义`==`判断条件

```python
class A:
    def __init__(self,name):
        self.name = name
    def __eq__(self,other):
        if self.name = self.name:
            return True
        else:
            return False
a = A("one")
b = A("one")
print(a == b)
# 如果没有设置__eq__方法
# a == b 判断的是 a的地址 与 b的地址进行比较 ====>>>>> False
# 设置了__eq__方法
# a == b 根据自定义来进行判断，判断的是 a的name 与 b的name进行比较 ====>>>>> True
```

