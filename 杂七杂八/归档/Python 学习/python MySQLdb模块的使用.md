> https://blog.csdn.net/kongsuhongbaby/article/details/84948205

- 引入模块

  ```python
  import MySQLdb
  ```

- 连接数据库

  ```python
  # 打开数据库连接
  db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )
  db = MySQLdb.connect(服务器地址, 用户名, 密码, 数据库名, charset='utf8' )
  ```
  - connect()的参数列表如下：
  
    ```python
    host，连接的数据库服务器主机名，默认为本地主机(localhost)。
    user，连接数据库的用户名，默认为当前用户。
    passwd，连接密码，没有默认值。
    db，连接的数据库名，没有默认值。
    conv，将文字映射到Python类型的字典。默认为MySQLdb.converters.conversions
    cursorclass，cursor()使用的种类，默认值为MySQLdb.cursors.Cursor。
    compress，启用协议压缩功能。
    named_pipe，在windows中，与一个命名管道相连接。
    init_command，一旦连接建立，就为数据库服务器指定一条语句来运行。
    read_default_file，使用指定的MySQL配置文件。
    read_default_group，读取的默认组。
    unix_socket，在unix中，连接使用的套接字，默认使用TCP。
    port，指定数据库服务器的连接端口，默认是3306。
    ```

- 获取操作游标===>获取操作权限?

  ```python
  # 使用cursor()方法获取操作游标 
  cursor = db.cursor()
  ```

- 执行SQL语句✦核心

  ```python
  # 使用execute方法执行SQL语句
  cursor.execute("SELECT VERSION()")
  # 使用executemany方法执行多条SQL语句
  ```

  - execute(query,args=None)
    - **函数作用**：执行单条的sql语句，执行成功后返回受影响的行数
    - **参数说明**：
      **query**：要执行的sql语句，字符串类型
      **args**：可选的序列或映射，用于query的参数值。如果args为序列，query中必须使用%s做占位符；如果args为映射，query中必须使用%(key)s做占位符
  - executemany(query,args=None)
    - **函数作用**：批量执行sql语句，比如批量插入数据，执行成功后返回受影响的行数
    - **参数说明**：
      **query**：要执行的sql语句，字符串类型
      **args**：嵌套的序列或映射，用于query的参数值
    - **注意**：
      1.数据库性能瓶颈很大一部份就在于网络IO和磁盘IO，将多个sql语句放在一起，只执行一次IO，可以有效的提升数据库性能。推荐此方法
      2.用executemany()方法一次性批量执行sql语句，固然很好，但是当数据一次传入过多到server端，可能造成server端的buffer溢出，也可能产生一些意想不到的麻烦。所以，合理、分批次使用executemany是个合理的办法

- 获取返回的数据

  - cursor.fetchone():获取游标所在处的一行数据，返回元组，没有返回None
  - cursor.fetchmany(size):接受size行返回结果行。如果size大于返回的结果行的数量，则会返回cursor.arraysize条数据。
  - cursor. fetchall():接收全部的返回结果行。

  ```python
  # 获取所有记录列表
  results = cursor.fetchall()
  # 获取3行数据
  results = cursor.fetchmany(3)
  # 获取一条数据
  result = cursor.fetchone()
  ```

- 断开数据库连接

  ```mysql
  # 先关闭游标
  cursor.close()
  # 提交
  db.commit()
  # 关闭数据库连接
  db.close()
  ```

- 数据库异常

  | 代码 | 内容                                                         | 含义                         |
  | ---- | ------------------------------------------------------------ | ---------------------------- |
  | 1049 | Unknown database 'myemployees1'                              | 没有找到数据库               |
  | 1045 | Access denied for user 'root1'@'localhost' (using password: YES) | 账号或密码错误               |
  | 2005 | Unknown MySQL server host 'sads' (11001)                     | 为找到数据库服务             |
  | 2002 | Can't connect to MySQL server on '127.255.255.255' (10049)   | 无法连接数据库服务器         |
  | 1025 | Error on rename of '.\students\stuinfo' to '.\students\#sql2-773c-7d' (errno: 152) | 删除外键时使用约束名进行删除 |
| 1136     | Column count doesn't match value count at row 1              | 插入的数据与表的列数不符                                     |
| 1075     | Incorrect table definition; there can be only one auto column and it must be defined as a key | 将标识列设置为key，主键或唯一约束即可     |
| 1046     | You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near | 语法错误                                                     |
|          | sql = "UPDATE table SET depart='bbb' WHERE depart='aaa' AND dataname LIKE 'xxx_%'" conn = MySQLdb.connect(host="localhost", user="root", passwd="baidu_cs", db="dataview", charset="utf 8") cur = conn.cursor() cur.execute(sql) | 支持事务的数据库引擎需要commit（可能自动或手动），不支持事务的引擎不需要commit。<br>添加conn.commit() |
|          |||
  
  