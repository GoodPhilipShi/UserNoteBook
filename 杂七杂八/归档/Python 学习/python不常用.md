### Print 输出

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 **end=""**：

### 字符串

使用三引号('''或""")可以指定一个多行字符串。

```python
paragraph = """这是一个段落，
可以由多行组成"""
```

### Set集合

妙用：去重

使用set()将列表、元组转换成集合，就可以去重，再转换回去即可。

### Python算术运算符

| 运算符 | 描述                        | 实例                                |
| ------ | --------------------------- | ----------------------------------- |
| //     | 取整除 - 向下取接近商的整数 | >>> 9//2<br/>4<br/>>>> -9//2<br/>-5 |

### Python数据类型转换

| 运算符 | 描述                        |
| ------ | --------------------------- |
| str(x) | 将对象 x 转换为字符串  |
| repr(x) | 将对象 x 转换为表达式字符串 |
| frozenset(s) | 转换为不可变集合 |
| ord(x) | 将一个字符转换为它的整数值 |
| hex(x) | 将一个整数转换为一个十六进制字符串 |
| oct(x) | 将一个整数转换为一个八进制字符串 |

### Python赋值运算符

| 运算符 | 描述                                                         | 实例                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| :=     | 海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符** | if (n := len(a)) > 10:<br/>    print(f"List is too long ({n} elements, expected <= 10)") |

```python
# 不使用海象运算符
n = len(a)
if n > 10:
    print(f"List is to long({n} elements, expected <= 10)")

# 使用海象运算符
if (n:=len(a)) > 10:
    print(f"List is to long({n} elements, expected <= 10)")
    
# 节省赋值给中间变量的步骤
```

### Python位运算符

按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：

下表中变量 a 为 60，b 为 13二进制格式如下：

| 运算符 | 描述                                                         | 实例                                                         |
| :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| &      | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100                 |
| \|     | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                |
| ^      | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                 |
| ~      | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
| <<     | 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                 |
| >>     | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 |                                                              |

### 数学函数

| 函数                                                         | 返回值 ( 描述 )                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| abs(x)                                                       | 返回数字的绝对值，如abs(-10) 返回 10                         |
| ceil(x)                                                      | 返回数字的上入整数，如math.ceil(4.1) 返回 5                  |
| cmp(x, y)                                                    | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃，使用 (x>y)-(x<y) 替换**。 |
| exp(x)                                                       | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
| fabs(x)                                                      | 返回数字的绝对值，如math.fabs(-10) 返回10.0                  |
| floor(x)                                                     | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
| log(x)                                                       | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0            |
| log10(x)                                                     | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
| max(x1, x2,...)                                              | 返回给定参数的最大值，参数可以为序列。                       |
| min(x1, x2,...)                                              | 返回给定参数的最小值，参数可以为序列。                       |
| modf(x)                                                      | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
| pow(x, y)                                                    | x**y 运算后的值。                                            |
| round(x [,n\])](https://www.runoob.com/python3/python3-func-number-round.html) | 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。**其实准确的说是保留值将保留到离上一位更近的一端。** |
| sqrt(x)                                                      | 返回数字x的平方根。                                          |

### Python转义字符

在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：

| 转义字符    | 描述                                                         |
| :---------- | :----------------------------------------------------------- |
| \(在行尾时) | 续行符                                                       |
| \\          | 反斜杠符号                                                   |
| \'          | 单引号                                                       |
| \"          | 双引号                                                       |
| \a          | 响铃                                                         |
| \b          | 退格(Backspace)                                              |
| \000        | 空                                                           |
| \n          | 换行                                                         |
| \v          | 纵向制表符                                                   |
| \t          | 横向制表符                                                   |
| \r          | 回车                                                         |
| \f          | 换页                                                         |
| \oyy        | 八进制数，**yy** 代表的字符，例如：**\o12** 代表换行，其中 o 是字母，不是数字 0。 |
| \xyy        | 十六进制数，yy代表的字符，例如：\x0a代表换行                 |
| \other      | 其它的字符以普通格式输出                                     |

### python字符串格式化符号

| 符  号 | 描述                                 |
| :----- | :----------------------------------- |
| %c     | 格式化字符及其ASCII码                |
| %s     | 格式化字符串                         |
| %d     | 格式化整数                           |
| %u     | 格式化无符号整型                     |
| %o     | 格式化无符号八进制数                 |
| %x     | 格式化无符号十六进制数               |
| %X     | 格式化无符号十六进制数（大写）       |
| %f     | 格式化浮点数字，可指定小数点后的精度 |
| %e     | 用科学计数法格式化浮点数             |
| %E     | 作用同%e，用科学计数法格式化浮点数   |
| %g     | %f和%e的简写                         |
| %G     | %f 和 %E 的简写                      |
| %p     | 用十六进制数格式化变量的地址         |

### 格式化操作符辅助指令

| 符号  | 功能                                                         |
| :---- | :----------------------------------------------------------- |
| *     | 定义宽度或者小数点精度                                       |
| -     | 用做左对齐                                                   |
| +     | 在正数前面显示加号( + )                                      |
| <sp>  | 在正数前面显示空格                                           |
| #     | 在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X') |
| 0     | 显示的数字前面填充'0'而不是默认的空格                        |
| %     | '%%'输出一个单一的'%'                                        |
| (var) | 映射变量(字典参数)                                           |
| m.n.  | m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)        |

### Python 内置函数

|                                                              | 内置函数                                                     |                                                              |                                                              |                                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ |
| abs()  绝对值                                                | divmod()  商和余数                                           | input()  输入                                                | open()  打开文件                                             | staticmethod()  函数的静态方法                               |
| all() 所有元素是否都为 TRUE                                  | [enumerate()](https://www.runoob.com/python/python-func-enumerate.html) | [int()](https://www.runoob.com/python/python-func-int.html)  | [ord()](https://www.runoob.com/python/python-func-ord.html)  | [str()](https://www.runoob.com/python/python-func-str.html)  |
| [any()](https://www.runoob.com/python/python-func-any.html)  | [eval()](https://www.runoob.com/python/python-func-eval.html) | [isinstance()](https://www.runoob.com/python/python-func-isinstance.html) | [pow()](https://www.runoob.com/python/func-number-pow.html)  | [sum()](https://www.runoob.com/python/python-func-sum.html)  |
| [basestring()](https://www.runoob.com/python/python-func-basestring.html) | [execfile()](https://www.runoob.com/python/python-func-execfile.html) | [issubclass()](https://www.runoob.com/python/python-func-issubclass.html) | [print()](https://www.runoob.com/python/python-func-print.html) | [super()](https://www.runoob.com/python/python-func-super.html) |
| [bin()](https://www.runoob.com/python/python-func-bin.html)  | [file()](https://www.runoob.com/python/python-func-file.html) | [iter()](https://www.runoob.com/python/python-func-iter.html) | [property()](https://www.runoob.com/python/python-func-property.html) | [tuple()](https://www.runoob.com/python/att-tuple-tuple.html) |
| [bool()](https://www.runoob.com/python/python-func-bool.html) | [filter()](https://www.runoob.com/python/python-func-filter.html) | [len()](https://www.runoob.com/python/att-string-len.html)   | [range()](https://www.runoob.com/python/python-func-range.html) | [type()](https://www.runoob.com/python/python-func-type.html) |
| [bytearray()](https://www.runoob.com/python/python-func-bytearray.html) | [float()](https://www.runoob.com/python/python-func-float.html) | [list()](https://www.runoob.com/python/att-list-list.html)   | [raw_input()](https://www.runoob.com/python/python-func-raw_input.html) | [unichr()](https://www.runoob.com/python/python-func-unichr.html) |
| [callable()](https://www.runoob.com/python/python-func-callable.html) | [format()](https://www.runoob.com/python/att-string-format.html) | [locals()](https://www.runoob.com/python/python-func-locals.html) | [reduce()](https://www.runoob.com/python/python-func-reduce.html) | unicode()                                                    |
| [chr()](https://www.runoob.com/python/python-func-chr.html)  | [frozenset()](https://www.runoob.com/python/python-func-frozenset.html) | [long()](https://www.runoob.com/python/python-func-long.html) | [reload()](https://www.runoob.com/python/python-func-reload.html) | [vars()](https://www.runoob.com/python/python-func-vars.html) |
| [classmethod()](https://www.runoob.com/python/python-func-classmethod.html) | [getattr()](https://www.runoob.com/python/python-func-getattr.html) | [map()](https://www.runoob.com/python/python-func-map.html)  | [repr()](https://www.runoob.com/python/python-func-repr.html) | [xrange()](https://www.runoob.com/python/python-func-xrange.html) |
| [cmp()](https://www.runoob.com/python/func-number-cmp.html)  | [globals()](https://www.runoob.com/python/python-func-globals.html) | [max()](https://www.runoob.com/python/func-number-max.html)  | [reverse()](https://www.runoob.com/python/att-list-reverse.html) | [zip()](https://www.runoob.com/python/python-func-zip.html)  |
| [compile()](https://www.runoob.com/python/python-func-compile.html) | [hasattr()](https://www.runoob.com/python/python-func-hasattr.html) | [memoryview()](https://www.runoob.com/python/python-func-memoryview.html) | [round()](https://www.runoob.com/python/func-number-round.html) | [__import__()](https://www.runoob.com/python/python-func-__import__.html) |
| [complex()](https://www.runoob.com/python/python-func-complex.html) | [hash()](https://www.runoob.com/python/python-func-hash.html) | [min()](https://www.runoob.com/python/func-number-min.html)  | [set()](https://www.runoob.com/python/python-func-set.html)  |                                                              |
| [delattr()](https://www.runoob.com/python/python-func-delattr.html) | [help()](https://www.runoob.com/python/python-func-help.html) | [next()](https://www.runoob.com/python/python-func-next.html) | [setattr()](https://www.runoob.com/python/python-func-setattr.html) |                                                              |
| [dict()](https://www.runoob.com/python/python-func-dict.html) | [hex()](https://www.runoob.com/python/python-func-hex.html)  | object()                                                     | [slice()](https://www.runoob.com/python/python-func-slice.html) |                                                              |
| [dir()](https://www.runoob.com/python/python-func-dir.html)  | [id()](https://www.runoob.com/python/python-func-id.html)    | [oct()](https://www.runoob.com/python/python-func-oct.html)  | [sorted()](https://www.runoob.com/python/python-func-sorted.html) |                                                              |

### 获取文件名

```python
def get_file_name(url, headers):
    filename = ''
    if 'Content-Disposition' in headers and headers['Content-Disposition']:
        disposition_split = headers['Content-Disposition'].split(';')
        if len(disposition_split) > 1:
            if disposition_split[1].strip().lower().startswith('filename='):
                file_name = disposition_split[1].split('=')
                if len(file_name) > 1:
                    filename = unquote(file_name[1])
    if not filename and os.path.basename(url):
        filename = os.path.basename(url).split("?")[0]
    if not filename:
        return time.time()
    return filename
```

