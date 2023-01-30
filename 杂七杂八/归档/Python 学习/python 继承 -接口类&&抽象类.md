### 规范子类

> 接口类：Python原生不支持
>
> 抽象类：Python原生支持的

```python
from abc import abstractmethod,ABCMeta

class Payment(metaclass=ABCMeta):# metaclass 元类 默认为type
    @abstractmethod
    def pay(self):pass# 规范要求实现pay方法
# 规范：可以称之为抽象类或接口类

class Weipay(Payment):
    def pay(self):
        print('使用微信支付')

class Alipay(Payment):
    def fuq(self):
        print('使用支付包')

W = Weipay()# 实例化Weipay
A = Alipay()# 实例化Alipay
# 报错 Can't instantiate abstract class Alipay with abstract methods pay
# 大致上的意思就是 没有实现pay方法
```

> 接口类 默认多继承 ，接口类中的方法都必须不能实现
>
> 抽象类 不支持多继承，抽象类中方法可以有一些代码的实现

### 接口类

```python
from abc import abstractmethod,ABCMeta
class Swim_Animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):pass

class Walk_Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):pass

class Fly_Animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(Self):pass
# 规范
class Tiger(Walk_Animal,Swim_Animal):
    def walk():pass
    def swmin():pass
class OldYing(Fly_Animal,Walk_Animal):pass
```

> #### 接口类 刚好满足接口隔离原则(客户端不应该依赖它不需要的接口。一个类对另一个类的依赖应该建立在最小的接口上。) 面向对象的思想 规范

### 抽象类

```python
import abc
class File(metaclass=abc.ABCMeta): #同一类事物:文件
    @abc.abstractmethod
    def click(self):
        pass

class Text(File): #文件的形态之一:文本文件
    def click(self):
        print('open file')

class ExeFile(File): #文件的形态之二:可执行文件
    def click(self):
        print('execute file')
```

> 抽象类：规范
>
> 一般情况下 单继承 能实现的功能都是一样的，所以在弗雷中可以有一些简单的基础实现
>
> 多继承的情况 由于功能比较复杂，所以不容易抽象出相同的功能的具体实现写在父类中

### 总结

> 抽象类还是接口类：面向对象的开发规范  所有接口类均不可实例化
>
> 从Java出发讲解：
>
> Java里的所有类型的继承都是单继承，所以抽象类完美的解决考虑单继承需求中的规范问题
> 但是对于多继承的需求，由于Java本身语法的不支持，所以创建了接口Interface这个概念类解决多继承的问题
>
> 从Python出发讲解：
>
> Python中没有接口类：python中自带多继承，所以我们直接用class来实现了接口类
> python中支持抽象类：一般情况下 单继承 不能实例化，且可以实现python代码
>
> 至于python中接口类和抽象类的问题：都是一种规范，python不支持接口类