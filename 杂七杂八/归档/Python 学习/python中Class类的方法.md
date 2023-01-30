## Python中Class类的方法

常见的方法是：实例方法、类方法、静态方法

> 不同，场景？？？？？

- 定义
  - 实例方法：也成为普通方法，默认有个self参数
  - 类方法：默认有个 cls 参数，并且需要装饰器@classmethod修饰
  - 静态方法：参数可有可无，并且需要装饰器@staticmethod修饰

  ```python
  class abc():
      def a(self):
          print("这个就是实例方法")
      
      @classmethod
      def b(cls):
          print("这个就是类方法")
          
      @staticmethod
      def c():
          print("这个就是静态方法")       
  ```

- 调用

  - 实例方法：实例对象可以调用
  - 类方法：实例对象和类对象都可以调用
  - 静态方法：实例对象和类对象都可以调用

  ```python
  abc.a() # 报错 TypeError:a() missing 1 required positional argument: 'self'
  abc.b() # 输出 这个就是类方法
  abc.c() # 输出 这个就是静态方法
  
  c = abc()
  c.a() # 输出 这个就是实例方法
  c.b() # 输出 这个就是类方法
  c.c() # 输出 这个就是静态方法
  ```

- 应用场景

  - 类方法

  > 当我们需要和类直接进行交互，而不需要和实例进行交互时，类方法是最好的选择。类方法与实例方法类似，但是传递的不是类的实例，而是类本身，第一个参数是cls。我们可以用类的实例调用类方法，也可以直接用类名来调用。

  > 应用场景1
  >
  > 假设我有一个学生类和一个班级类，想要实现的功能为：
  >
  > 执行班级人数增加的操作、获得班级的总人数；
  >
  > 学生类继承自班级类，每实例化一个学生，班级人数都能增加；
  > 最后，我想定义一些学生，获得班级中的总人数。

  ```python
  # 不使用类方法
  class ClassTest(object):
      __num = 0
  
      def addNum(self):
          self.__num += 1
  
      def getNum(self):
          return self.__num
          
  class Student(ClassTest):
      def __init__(self):
          self.name = ''
  
  ClassTest = ClassTest()
  a = Student()
  ClassTest.addNum()
  b = Student()
  ClassTest.addNum()
  print(ClassTest.getNum())
  ```
  ```python
  # 使用类方法
  class ClassTest(object):
      __num = 0
      @classmethod
      def addNum(cls):
          cls.__num += 1
    
      @classmethod
      def getNum(cls):
          return cls.__num
            
  class Student(ClassTest):
      def __init__(self):
          self.name = ''
          ClassTest.addNum()
            
  a = Student()
  b = Student()
  print(ClassTest.getNum())
  ```

  可以看得出来不用类方法获取学生人数，就必须实例化ClassTest类，并且每实例化一位学生，就要单独调用一次实例化ClassTest类的addNum方法，就很繁琐且拥挤。而使用类方式获取学生人数，既不用实例化ClassTest类，也不用每实例化一位学生，单独调用一次addNum方法。

  > 应用场景2
  >
  > 全部商品打8折

  ```python
  # 不使用类方法
  class Goods:
      __discount = 1
      def __init__(self,name,price):
          self.name = name
          self.__price = price
          
      @property
      def price(self):
          return self.__price*self.__discount
  
      def change_discount(self,new_discount):
          self.__discount = new_discount
  
  apple = Goods('苹果',10)
  apple.change_discount(0.8)
  print(apple.price)
  
  banana = Goods('香蕉',20)
  apple.change_discount(0.8)
  print(banana.price)
  --------------------
  8.0
  16.0
  ```

  ```python
  # 使用类方法
  class Goods:
      __discount = 1
      def __init__(self,name,price):
          self.name = name
          self.__price = price
          
      @property
      def price(self):
          return self.__price*self.__discount
      
      @classmethod
      def change_discount(cls,new_discount):
          cls.__discount = new_discount
  
  apple = Goods('苹果',10)
  apple.change_discount(0.8)
  print(apple.price)
  
  banana = Goods('香蕉',20)
  print(banana.price)
  ------------------
  8.0
  16.0
  ```

  很明显，不使用类方法进行打折运算，每个实例化的商品都要调用一次change_discount实例方法，修改的是实例变量，而使用类方法则可以一次到位，修改的是类变量。

  - 静态方法

  > 静态方法类似普通方法，参数里面不用self。这些方法和类相关，但是又不需要类和实例中的任何信息、属性等等。如果把这些方法写到类外面，这样就把和类相关的代码分散到类外，使得之后对于代码的理解和维护都是巨大的障碍。而静态方法就是用来解决这一类问题的。

  > 应用场景1
  >
  > 通常，有一些与类有关的功能，但不需要类或任何实例来完成某些工作。也许诸如设置环境变量，更改另一个类的属性等之类的东西。在这种情况下，我们也可以使用一个函数，但是这样做也会传播相互关联的代码，这可能会在以后引起维护问题。
  >
  > 参考：https://www.pythoncentral.io/difference-between-staticmethod-and-classmethod-in-python/

  ```python
  # 不使用静态方法
  IND = 'ON'
   
  def checkind():
      return (IND == 'ON')
   
  class Kls(object):
      def __init__(self,data):
          self.data = data
   
      def do_reset(self):
          if checkind():
              print('Reset done for:', self.data)
      
      def set_db(self):
          if checkind():
              self.db = 'new db connection'
              print('DB connection made for:',self.data)
   
  ik1 = Kls(12)
  ik1.do_reset()
  ik1.set_db()
  ```

  ```python
  # 使用静态方法
  IND = 'ON'
   
  class Kls(object):
      def __init__(self, data):
          self.data = data
   
      @staticmethod
      def checkind():
          return (IND == 'ON')
   
      def do_reset(self):
          if self.checkind():
              print('Reset done for:', self.data)
   
      def set_db(self):
          if self.checkind():
              self.db = 'New db connection'
          print('DB connection made for: ', self.data)
   
  ik1 = Kls(12)
  ik1.do_reset()
  ik1.set_db()
  ```
  ```python
  import json
  
  # def readfile():
  #     with open("vscode-python\员工工资记录表.txt","r") as f:
  #         st = f.read()
  #         f.close()
  #     return st
  
  # def saveflie(pe,m):
  #     st = readfile()
  #     try:
  #         i = json.loads(st)
  #     except BaseException:
  #         i = {}
  #     i[pe] = m
  #     with open("vscode-python\员工工资记录表.txt","wb+") as f:
  #         st = json.dumps(i)
  #         sb = bytes(st,"utf-8")
  #         f.write(sb)
  #         f.close()
  
  class moneys(object):
      __me = 0
  
      @staticmethod
      def readfile():
          with open("vscode-python\员工工资记录表.txt","r") as f:
              st = f.read()
              f.close()
          return st
  
      @staticmethod
      def saveflie(pe,m):
          st = moneys.readfile()
          try:
              i = json.loads(st)
          except BaseException:
              i = {}
          i[pe] = m
          with open("vscode-python\员工工资记录表.txt","wb+") as f:
              st = json.dumps(i)
              sb = bytes(st,"utf-8")
              f.write(sb)
              f.close()
  
      # 设置单个员工工资-实例方法
      def __init__(self,pe,m):
          self.pe = pe
          self.money = m
          # saveflie(pe,m) # 不使用静态
          moneys.saveflie(pe,m) # 使用静态
  
      # 全体加工资-类方法
      @classmethod
      def addmoney(cls,m):
          cls.__me = m
          
      def getmoney(self):
          return self.money + self.__me
      
  
  als = moneys("all",0) # 全体员工
  yg1 = moneys("yg1",1000)
  yg2 = moneys("yg2",2000)
  yg3 = moneys("yg3",3000)
  
  print("员工1原本工资为%d"%yg1.getmoney())
  
  # 今年生意好，临时加工资，分红
  als.addmoney(1000)
  print("员工1现在工资为%d"%yg1.getmoney())
  # 第二年，没有分红
  als.addmoney(0)
  
  # 员工1升职了，工资涨了1000
  yg1 = moneys("yg1",2000)
  print("员工1原本工资为%d"%yg1.getmoney())
  
  # 某天，老板想看看员工们额工资
  # print(readfile())
  print(yg1.readfile())
  ```

### 补充-属性方法[python 装饰器](C:\Users\Alex\Desktop\学习\python 装饰器.md)