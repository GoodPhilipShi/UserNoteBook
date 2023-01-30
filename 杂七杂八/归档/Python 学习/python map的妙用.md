- 生成A-Z的字母列表

  ```python
  # 利用 chr 可以将 ASCII码 转义
  # A 的 ASCII码 是 65，Z 的 ASCII码 是 90
  a = list(map(chr,range(65,91)))
  print(a) # 输出 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  ```

- 批量将字符串转换整数

  ```python
  a = ['1','2','3']
  print(list(map(int,a))) # 输出 [1, 2, 3]
  ```

- 批量函数

  ```python
  def two(n):
      return n**2
  a = [1, 2, 3]
  print(list(map(two,a))) # 输出 [1, 4, 9]
  ```

  

