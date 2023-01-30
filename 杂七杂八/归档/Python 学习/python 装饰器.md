### property

> 内置装饰器函数，只在面向对象中使用
> 将方法伪装成属性，条件是方法就不能接受其他参数

#### 为什么要用property

将一个类的函数定义成特性以后，对象再去使用的时候`obj.name`,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式**遵循了统一访问的原则**

#### 对对象的修改

> 一个静态属性`property`本质就是实现了`get`，`set`，`delete`三种方法

```python
class Person:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name + '哈哈笑'
    @name.setter
    def name(self,new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        del self.__name

tiger = Person('泰哥')
print(tiger.name)
tiger.name = '全班'
print(tiger.name)
del name
# 这样就可以实现对对象的修改
```

> 重点：必须是使用`@property`装饰器的方法①，并且`@name.setter`和`@name.deleter`的`name`必须和方法①名称相同，以及`@name.setter`和`@name.deleter`下的方法的名称也必须和方法①相同