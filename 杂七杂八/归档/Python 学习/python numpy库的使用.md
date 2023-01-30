python numpy库的使用

> https://www.numpy.org.cn/

- 创建数组：
  - numpy.**empty**():numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：

    ```python
    numpy.empty(shape, dtype = float, order = 'C')
    ```

    | 参数  | 描述                                                         |
    | :---- | :----------------------------------------------------------- |
    | shape | 数组形状                                                     |
    | dtype | 数据类型，可选                                               |
    | order | 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

    ```python
    import numpy as np 
    x = np.empty([3,2], dtype = int)
    print (x)
    -------------
    [[1 0]
     [8 0]
     [0 0]] # 注意 − 数组元素为随机值，因为它们未初始化。
    ```
    
  - numpy.**zeros**()：创建指定大小的数组，数组元素以 0 来填充：

    ```python
    numpy.zeros(shape, dtype = float, order = 'C')
    ```

    | 参数  | 描述                                                |
    | :---- | :-------------------------------------------------- |
    | shape | 数组形状                                            |
    | dtype | 数据类型，可选                                      |
    | order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |

    ```python
    import numpy as np
     
    # 默认为浮点数
    x = np.zeros(5) 
    print(x) # 输出 [0. 0. 0. 0. 0.]
     
    # 设置类型为整数
    y = np.zeros((5,), dtype = np.int) 
    print(y) # 输出 [0 0 0 0 0]
     
    # 自定义类型
    z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
    print(z)
    ------------
    [[(0, 0) (0, 0)]
     [(0, 0) (0, 0)]]
    ```
    
  - numpy.**ones**()：创建指定形状的数组，数组元素以 1 来填充：
  
    ```python
    numpy.ones(shape, dtype = None, order = 'C')
    ```
  
    | 参数  | 描述                                                |
    | :---- | :-------------------------------------------------- |
    | shape | 数组形状                                            |
    | dtype | 数据类型，可选                                      |
    | order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |
  
    ```python
    import numpy as np
     
    # 默认为浮点数
    x = np.ones(5) 
    print(x) # 输出 [1. 1. 1. 1. 1.]
     
    # 自定义类型
    x = np.ones([2,2], dtype = int)
    print(x)
    -----------------------
    [[1 1]
     [1 1]]
    ```
  
  - numpy.**asarray**()：numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个。
  
    ```python
    numpy.asarray(a, dtype = None, order = None)
    ```
  
    | 参数  | 描述                                                         |
    | :---- | :----------------------------------------------------------- |
    | a     | 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组 |
    | dtype | 数据类型，可选                                               |
    | order | 可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |
  
    ```python
    import numpy as np 
     
    x =  [1,2,3] 
    a = np.asarray(x)  
    print (a) # 输出 [1  2  3]
    ```
  

