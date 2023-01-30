Python中的迭代、列表生成式、生成器、迭代器

- 定义

  - 迭代：通过for循环来遍历列表、元组、字符串、集合等等，这种遍历就叫迭代

  ```python
  # 列表
  a = [1,2,3]
  for i in a:
      print(i)
  # 元组
  b = (1,2,3)
  for i in b:
      print(i)
  # 字符串
  c = 'abc'
  for i in c:
      print(i)
  # 集合
  d = {'1','2','3'}
  for i in d:
      print(i)
  ```

  - 列表生成式：通过很简短的方式生成一个很长的列表，这种方式就被成为列表生成式

  ```python
  # 想要生成[1,2,3,4,5,6,7,8,9,10]
  c = list(range(1, 11))
  
  # 想要生成[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  c = [x * x for x in range(1, 11)]
  ```

  - 生成器：根据算法不断推算出列表的后续元素，这种方式就是生成器

  ```python
  # 列表[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  c = (x * x for x in range(1, 11))
  # 通过迭代(遍历)、next()函数实现查看
  ```
  - 迭代器：迭代器是一个可以记住遍历的位置的对象，生成器也是特殊的迭代器

  ```python
  a = [1,2,3,4,5,6,7,8,9,10]
  c = iter(a)
  print(next(c)) # 输出 1
  print(next(c)) # 输出 2
  print(next(c)) # 输出 3
  ```

- 优劣

  - 列表：列表元素少的时候，运行速度快、占用内存少、编写简单，一旦元素多了，运行速度慢、占用内存多，并且是一次性生成整个列表
  - 生成器：元素多还是少，运行速度都快、占用内存都少，原因就是生成器并不是一次性生成整个列表，而是不断推算出后续的元素，从而节省大量的空间。

  ```python
  import sys
  import time
  
  def _list(n):
      l1 = [list(range(n)) for i in range(n)]
      print("list Memory size:",sys.getsizeof(l1))
      del l1
  
  def _generator(n):
      ge = (tuple(range(n)) for i in range(n))
      print("generator Memory size:",sys.getsizeof(ge))
      del ge
  
  start_time = time.time()
  l = _list(1000)
  end_time = time.time()
  print("list Spend:",end_time - start_time)
  
  
  start_time = time.time()
  g = _generator(1000)
  end_time = time.time()
  print("generator Spend:",end_time - start_time)
  ---------------
  list Memory size: 9024
  list Spend: 0.048397064208984375
  generator Memory size: 120
  generator Spend: 0.0
  ```

  分析一下，列表是将0-999都生成后放进一个列表里面了(一次性生成)，所以用得时间比较多。
  而生成器只是封装了算法，每次调用在去调用算法，这样做就可以做到节省内存了。

  而且list的内存占用了9024，generator才120，将近75倍的差距。

- 应用场景

  - 列表

  > 应用场景1
  >
  > 需要生成少量元素的时候，就可以用列表。

  ```python
  # 生成0，200之间的偶数列表
  # 第一种 for
  a = []
  for i in range(0,201):
  if i % 2 == 0:
          a.append(i)
  print(a)
  # 第二种 列表生成式
  a = [i for i in range(0,201) if i % 2 == 0]
  print(a)
  ```
  >应用场景2
  >
  >需要列表中指定的某个元素

  ```python
  a = [i for i in range(0,201) if i % 2 == 0]
  print(a[5])
  ```

  - 生成器

  > 应用场景1
  >
  > 需要生成大量元素的时候，就需要用到生成器。

  ```python
  # 生成0，90000之间的偶数列表
  a = (i for i in range(0,201) if i % 2 == 0)
  # 这样就设置好了一个生成器
  # 可以通过多个next(a)的方式来查看多个元素
  # 也可以通过for循环的方式查看
  for i in a:
      print(i)
  ```
  > 应用场景2
  >
  > 斐波那契数列
  >
  > f(0) = 0，f(1) = 1，f(2) = f(0)+ f(1)……f(n)=f(n-1)+f(n-2)、f(n+1)  =  f(n) + f(n+1)

  ```python
  def fibonacci(n):
      a, b, counter = 0, 1, 0 # a充当的是f(n) b充当的是f(n+1)
      while True:
          if (counter > n): 
              return
          yield a
          a, b = b, a + b
          counter += 1
          
  f = fibonacci(int(input()))
  
  for i in f:
      print(i)
  ```

  - 迭代器

  > 应用场景
  >
  > 如果数列的数据规模巨大
  >
  > 数列有规律，但是依靠列表推导式描述不出来
  >
  > ------
  >
  > 斐波那契数列
  >
  > f(0) = 0，f(1) = 1，f(2) = f(0)+ f(1)……f(n)=f(n-1)+f(n-2)、f(n+1)  =  f(n) + f(n+1)

  ```python
  class FibIterator(object):
      def __init__(self, n):
          self.a = 0
          self.b = 1
          self.i = 0
          self.n = n
  
      def __next__(self):# 返回下一个迭代器对象
          if self.i < self.n:
              self.a, self.b = self.b,self.a + self.b
              self.i += 1
              return self.a
          else:
              raise StopIteration
  
      def __iter__(self):# 返回一个特殊的迭代器对象
          return self
  
  fib = FibIterator(20)
  li = list(fib)
  print(li)
  ```

  

- 生成器的原理：

  - 生成器(generator)能够迭代的关键是它有一个next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常。

  - 带有 yield 的函数不再是一个普通函数，而是一个生成器generator。可用next()调用生成器对象来取值。next 两种方式 t.\__next__() | next(t)。可用for 循环获取返回值（每执行一次，取生成器里面一个值）（基本上不会用`next()`来获取下一个返回值，而是直接使用`for`循环来迭代）。

  - yield相当于 return 返回一个值，并且记住这个返回的位置，下次迭代时，代码从yield的下一条语句开始执行。

```python
# 生成器创建1
a = (i for i in range(0,201) if i % 2 == 0)
# 生成器创建2
def two(n):
    for i in range(0,n+1):
        if i % 2 == 0:
            yield i
a = two(200)
# 等同于
a = [i for i in range(0,201) if i % 2 == 0] # 生成列表
b = iter(a) # 创建迭代器对象

# 生成器运行
# 设下生成器的公式 x=x+1
>>> next(生成器) # x = 0
1 # x =  0 + 1 = 1
>>> next(生成器) # x = 1
2 # x = 1 + 1 = 2
…… # 依次循环+1

# 或者说
while True:
    try:
        next(生成器)
    except StopIteration:
        break
```

