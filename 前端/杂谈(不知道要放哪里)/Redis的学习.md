# Redis的学习

## Redis的入门概述

### Redis是什么？

> #### <font size='5' color='red'>Re</font>mote <font size='5' color='red'>Di</font>ctionary <font size='5' color='red'>S</font>erver --- 远程(Remote)字典(Dictionary)服务器(Server)

完全开源免费的、用C语言编写的，遵从BSD协议，的一个高性能的(Key/Value)分布式内存数据库，基于内存运行并持久化的NoSQL数据库，是当下最热门的NoSQL数据库之一，也被人们成为数据结构化服务器。

Redis 与其他 Key-Value 缓存产品有以下三个特点：

- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用
- Redis不仅仅支持简单的Key-Value类型的数据，同时还提供list、set、zset、hash等数据结构的存储
- Redis支持数据的备份，即master-slave模式的数据备份

## Redis的安装

### [ linux ] Redis的安装

**下载redis.tar.gz后将它放到我们的`/opt`目录下**

![image-20210115161946061](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15 16:30:11.png)

**/opt目录下进行解压，解压命令：`tar -zxvf redis.tar.gz`**

![20210115162047](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15 16:29:51.png)

**解压完成后，出现文件：redis**

![image-20210115162636027](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15 16:29:14.png)

**进入解压目录，命令：`cd redis`，在redis目录下执行make命令，进行编译**

![images-20210115163246](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:33.png)

**编译完成后，移动到`/usr/loacl/redis`，继续执行make install命令进行安装**

![Snipaste_2021-01-15_17-33-02](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:52.png)

**查看默认安装目录：`/usr/local/bin`**

![image-20210115173609472](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:30.png)

> | 名称            | 含义              |
> | --------------- | ----------------- |
> | redis-server    | redis服务器       |
> | redis-cli       | redis命令行客户端 |
> | redis-benchmark | redis性能测试工具 |
> | redis-check-aof | AOF文件修复工具   |
> | redis-check-rdb | RDB文件检索工具   |

**将配置文件复制到`/etc/`目录**

![Snipaste_2021-01-15_17-43-37](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:28.png)

### [ linux ]Redis的配置文件

> 目前Redis的配置文件在`/etc/redis`目录下
>
> 命令：`vi /etc/redis` 必要时，可以添加`sudo`

![image-20210115175518532](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:26.png)

#### **Redis核心配置选项**

**绑定IP：如果需要远程访问，可以将此行注释，或绑定一个真实IP**

> bind 127.0.0.1

![image-20210115180037707](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:24.png)

**端口，默认为6379**

> port 6379

![image-20210115180107389](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:22.png)

**是否以守护进程运行**

- 如果以守护进程运行，则不会在命令行阻塞，类似于服务
- 如果以非守护进程运行，则当前终端被阻塞
- 设置为yes表达守护进程，设置为no表示非守护进程
- 推荐设置为yes

> daemonize yes

![image-20210115180152613](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:20.png)

**数据文件**

> dbfilename dump.rdb

![image-20210115180436773](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:19.png)

**数据文件存储路径**

> dir /var/lib/redis

![image-20210115180501977](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:16.png)

**日志文件**

> logfile /var/log/redis/redis-server.log

![image-20210115180524232](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:14.png)

**数据库，默认有6个**

> database 16

![image-20210115180552916](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:13.png)

**主从复制，类似与双机备份**

> 5.0版本之前：slaveof
>
> 5.0版本之后：replicaof

![image-20210115180838224](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:12:11.png)

## Redis的服务器端和客户端命令

### 服务器端

**服务器端的命令**

> redis-server

**可以使用help查看帮助文档**

> redis-server --help

**推荐使用服务的方式管理redis服务**

**启动**

> sudo service redis start

**停止**

> sudo service redis stop

**重启**

> sudo service redis restart

**更多命令**

> ps -ef|grep redis 查看redis服务器进程
>
> sudo kill -9 pid 杀死redis服务器
>
> sudo redis-server /etc/redis/redis.conf 指定加载的配置文件

### 客户端

**客户端的命令**

> redis-cli

**可以使用help查看帮助文档**

> redis-cli --help

**连接redis**

> redis-cli

![Snipaste_2021-01-15_18-23-49](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:24:26.png)

**运行测试命令**

> ping

![Snipaste_2021-01-15_18-24-57](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:25:19.png)

**切换数据库**

**数据库没有名称，默认有16个，通过0-15来标识，连接redis默认选择第一个数据库**

> select n

![Snipaste_2021-01-15_18-27-31](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:27:58.png)

## 数据操作

### string

**String类型**

> 字符集类型是Redis最为基础的数据存储类型，它在Redis中是二进制安全的，这边意味着该类型可以接受任何格式的数据，如JPEG图像数据或JSON对象描述信息等。在Redis中字符串类型的Value最多可以容纳的数据长度是512M。

#### 保存

> 如果设置额键不存在则为添加，如果设置的键已经存在则修改

- 设置键值

  > set key value

- 例1：设置键为name值为itcast的数据

  > set name itcast

  ![image-20210115183629359](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:36:45.png)

- 设置键值及过期时间，以秒为单位

  > setex key seconds value
  
- 例2：设置键为aa值为5，过期时间为3秒的数据
  
  > setex aa 3 5
  
  ![image-20210115184028093](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:40:32.png)
  
- 设置多个键值

  > mset key1 value1 key2 value2……

- 例3：设置键为‘a1’值为‘Python’、键为‘a2’值为‘java’

  > mset a1 python a2 java

  ![image-20210115184412662](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:44:32.png)

- 追加值

  > append key value

- 例4：向键为‘a1’中追加值’haha‘

  > append a1 haha

  ![image-20210115184704133](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:47:08.png)

#### 获取

- 根据键获取值，如果不存在此键则返回nll

  > get key

- 例5：获取键‘name’的值

  > get ‘name’

  ![image-20210115185004792](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:51:38.png)

- 根据多个键获取多个值

  > mget key1 key2

- 例6：获取键为a1、a2的值

  > mget a1 a2

  ![image-20210115185127063](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:51:35.png)

#### 删除

> 详见`键命令`

### 键命令

- 查找键，参数支持正则表达式

  > keys pattern

- 例1：查看所有键

  > keys *

  ![image-20210115185351815](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:53:57.png)

- 例2：查看名称中包含a的键

  > keys 'a*'
  
  ![image-20210115185513306](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:55:16.png)
  
  ![image-20210115185553112](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-15_18:55:56.png)
  
- 判断键是否存在，如果存在返回1，不存在返回0

  > exists key

- 例3：判断键a1是否存在

  > exists a1

  ![image-20210118085733011](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:01:10.png)

- 查看键对应的value的类型

  > type key

- 例4：查看键a的值类型，为redis支持的五种类型中的一种

  > type a

  ![image-20210118090059856](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:01:16.png)

- 删除键及对应的值

  > del key1，key2

- 例5：删除键a

  ![image-20210118090417945](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:04:24.png)

- 设置过期时间，以秒为单位

- 如果没有指定过期时间则一直存在，知道使用del移除

  > expire key seconds

- 例6：设置键a的过期时间为5秒

  ![image-20210118090713336](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:07:18.png)

- 查看有效时间，以秒为单位

  > ttl key

- 查看键a1的有效时间

  > ttl a1

  ![image-20210118091002306](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:10:28.png)

### hash

> ## hash类型
>
> - hash用于存储对象，对象的结构为属性、值
> - 值的类型为string

#### 添加、修改

- 设置单个属性

  > hset key fileId value

- 例1：设置键user的属性name为liuji

  > hset user name liuji

  ![image-20210118091629502](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:21:36.png)

- 设置 多个属性

  > hmset key fileId1 value1 fileId2 value2

- 例子2：设置键user的属性name为liuji，属性age为18

  > hmset user name liuji age 18

  ![image-20210118092023956](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:21:32.png)

#### 获取

- 获取指定键所有的属性

  > hkeys key

- 例3：获取键user的所有属性

  ![image-20210118092352648](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:25:13.png)

- 获取一个属性的值

  > hget key fieId

- 例4：获取键user属性name的值

  > hget user name

  ![image-20210118092649775](../../AppData/Roaming/Typora/typora-user-images/image-20210118092649775.png)

- 获取多个属性的值

  > hmget key fieId1 fieId2

- 例5：获取键user属性name的值和属性age 的值

  > hmget user name age

  ![image-20210118092852937](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:29:22.png)

-  获取所有属性的值

  > hvals key

- 例6：获取键user所有属性的值

  > hvals user

  ![image-20210118093136331](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:31:40.png)

#### 删除

- 删除整个hash键及值，使用del命令

- 删除属性，属性对应的值会被一起删除

  > hdel key fieId1 fieId2

- 例7：删除键user的属性age

  > hdel user age

  ![image-20210118093647435](https://gitee.com/acg-q/pic-go-images/raw/master//2021-01-18_09:36:53.png)

### list

> https://www.bilibili.com/video/BV1Pt411Q7qQ?p=7

### set

### zset