python textwrap模块--- 文本自动换行与填充

> [`textwrap`](https://docs.python.org/zh-cn/3.7/library/textwrap.html#module-textwrap) 模块提供了一些快捷函数，以及可以完成所有工作的类 [`TextWrapper`](https://docs.python.org/zh-cn/3.7/library/textwrap.html#textwrap.TextWrapper)。 如果你只是要对一两个文本字符串进行自动换行或填充，快捷函数应该就够用了；否则的话，你应该使用 [`TextWrapper`](https://docs.python.org/zh-cn/3.7/library/textwrap.html#textwrap.TextWrapper) 的实例来提高效率
>
> 参考链接：https://docs.python.org/zh-cn/3.7/library/textwrap.html

- 常用函数

  - textwrap.**wrap**(*text*, *width=70*, ***kwargs*)：对 *text* (字符串) 中的单独段落自动换行以使每行长度最多为 *width* 个字符。 返回由输出行组成的列表，行尾不带换行符。

    ```python
    >>> textwrap.wrap('hello',1)
    ['h','e','l','l','o']
    ```

  - textwrap.**fill**(*text*, *width=70*, ***kwargs*)：对 text 中的单独段落自动换行，并返回一个包含被自动换行段落的单独字符串。 fill() 是以下语句的快捷方式

    ```python
    >>> textwrap.fill('hello',4)
    hell
    o
    ```

  - textwrap.**shorten**(text, width, **kwargs)：折叠并截短给定的 *text* 以符合给定的 *width*。

    ```python
    >>> textwrap.shorten("Hello  world!", width=12)
    Hello world!
    >>> textwrap.shorten("Hello  world!", width=11)
    Hello [...]
    >>> textwrap.shorten("Hello world", width=10, placeholder="...")
    Hello...
    ```

  - textwrap.**dedent**(text)：移除 text 中每一行的任何相同前缀空白符。

    ```python
    >>> s = '''\
    hello
      world
    '''
    >>> repr(s)         # 输出 '    hello\n      world\n    '
    >>> repr(textwrap.dedent(s))  # 输出 'hello\n  world\n'
    ```

    

- 应用场景

  - wrap:

    > 给您一个字符串S和宽度W。您的任务是将字符串包装成一段宽度。
    >
    > 如果将以下字符串作为程序输入：
    >
    > ABCDEFGHIJKLIMNOQRSTUVWXYZ
    >
    > 4
    >
    > 然后，程序的输出应为：
    >
    > ABCD
    >
    > EFGH
    >
    > IJKL
    >
    > IMNO
    >
    > QRST
    >
    > UVWX
    >
    > YZ

    ```python
    import textwrap
    a = input("字符串：")
    b = int(input("宽度："))
    c = textwrap.wrap(a,b)
    for i in c:
        print(i)
    ```

    

