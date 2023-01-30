Python Random库的使用

- random库中的函数
  - 基本随机数函数：seed()，random()
  - 扩展随机数函数：randint()，randrange()，uniform()，choice()，shuffle()，getrandbits()

  ![img](https://upload-images.jianshu.io/upload_images/12265479-d8e0e058a2bcddfb.png?imageMogr2/auto-orient/strip|imageView2/2/w/1036/format/webp)
  
  - 函数详情
  
  | 函数                      | 功能                                 | 参数                                          |
  | ------------------------- | ------------------------------------ | --------------------------------------------- |
  | random.seed([x])          | 改变随机数生成器的种子               | x：种子，整型或浮点型都行。默认为当前系统时间 |
  | random.random()           | 返回[0,1)内一个随机浮点数            | null                                          |
  | random.randint(m,n)       | 返回[m,n)中的一个随机整数            | m,n必须是整数                                 |
  | random.randrange(m,n[,k]) | 返回[m,n)中以k为步长的一个随机整数   | m,n,k必须是整数 k默认为1                      |
  | random.getrandbits(k)     | 返回一个可以用k位二进制的整数        | k为整数                                       |
  | random.uniform(m,n)       | 返回[m,n)中的一个随机浮点数          | m,n可以是整型或是浮点型                       |
  | random.choice(seq)        | 返回一个列表、元组或字符串的随机项。 | 字符串、列表或元组                            |
  | random.sample(seq,k)      | 返回k个列表、元组或字符串的随机项。  | 字符串、列表或元组                            |
  | random.shuffle(list)      | 将序列的所有元素随机排序。无返回值   | 列表                                          |
  - 函数使用效果
  
  ```python
  >>> random.seed(10) # 设置种子为10
  >>> random.random() # 生成随机数，但是设置了种子后，随机数就已经固定了
  0.5714025946899135
  >>> random.seed() # 设置种子为当前系统时间
  >>> random.randint(10, 100) # 生成10，100之间的随机整数
  64
  >>> random.randrange(10, 100, 10) # 生成10，100之间步长为10的随机整数，步长简单来说就是间隔
  80
  >>> random.getrandbits(2) # 生成2位二进制的整数 2位二进制：00（0），01（1），10（2），11（3） 也就是说随机范围为 00，01，10，11 随机生成后再转换成整数的过程就这个函数的作用过程
  3
  >>> random.uniform(10, 100) # 生成 10，100之间的随机数
  13.096321648808136
  >>> random.choice([1,2,3,4,5,6,7,8,9]) # 生成列表(元组、字符串)中随机元素
  8 
  >>> s=[1,2,3,4,5,6,7,8,9]
  >>> random.shuffle(s) # 随机排序
  >>> print(s)
  [3, 5, 8, 9, 6, 1, 2, 7, 4] # 顺序已被打乱
  >>> random.sample(s,5) # 从s列表中随机抽取5个
  [8, 4, 7, 3, 2]
  ```
  
- 应用场景

  > 应用场景1
  >
  > 例如，抽奖，手机号码抽奖，评论抽奖
  >
  > 这里就用得到choice()、sample()这两个函数

  ```python
  # 手机号抽奖，抽1位幸运观众
  a = ['114','112','110']
  import random #导入 random随机库
b = random.choice(a)
  print("本期的获奖得主是",b) # 输出 本期的获奖得主是 114
  
  # 彩票抽奖，8位号码
  a = list(range(10))
  print(random.sample(a,8)) # 输出 [4, 0, 9, 1, 7, 2, 3, 5]
  ```
  
  > 应用场景2
  >
  > 洗牌
  >
  > 这里就可以用到 shuffle()函数
  
  ```python
  # 假设一副牌共10张
  import random
  pai = ['1','2','3','4','5','6','7','8','9','0']
  random.shuffle(pai)
  print(pai) # 输出 ['4', '0', '9', '3', '8', '1', '7', '2', '6', '5']
  ```

- random库生成随机数的原理

![图1](https://upload-images.jianshu.io/upload_images/12265479-7c524a3b678118d2.png?imageMogr2/auto-orient/strip|imageView2/2/w/1172/format/webp)
