- Python 访问字符串中的值

  ```python
  var1 = 'Hello World!'
  var2 = "Python Runoob"
  
  print("var1[0]: ", var1[0])
  print("var2[1:5]: ", var2[1:5])
  ---------------------
  var1[0]:  H
  var2[1:5]:  ytho
  ```

- Python 字符串连接

  ```python
  var1 = 'Hello World!'
  print("输出 :- ", var1[:6] + 'Runoob!')
  ```

- Python 三引号

  ```python
  >>> hi = '''hi 
  there'''
  >>> hi   # repr()
  'hi\nthere'
  >>> print(hi)  # str()
  hi 
  there
  ```

- python的字符串内建函数

  - str.count(str, beg=0, end=len(string))：返回 str 在 string 里面出现的次数

    ```python
    >>> a = '999900099'
    >>> a.count('9')
    6
    ```

  - str.center(width[, fillchar])：返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。

    ```python
    >>>str = 'runoob'
    >>> str.center(20, '*')
    '*******runoob*******'
    >>> str.center(20)
    '       runoob       '
    ```

  - string.format()：格式化字符串
  
    ```python
    >>> print("{} {}".format("hello", "world"))    # 不设置指定位置，按默认顺序
    'hello world'
    >>> print("{0} {1}".format("hello", "world"))  # 设置指定位置
    'hello world'
    >>> print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
    'world hello world'
    ```
  
    

