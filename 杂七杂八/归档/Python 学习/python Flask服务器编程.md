web阶段：

> - Python 基础
>
> - 数据库：MySql redis
>
> - 网页：html+css+js+jquery+bootstrap
>
> - vue：前后分离
>
> web后端：网站
>
> 联合项目：h5+python
>
> h5展示：触发事件 ----> 后端发请求 ----> 后端(处理)
>
> 注册、登录
>
> Flask --> Tornado --> django

### 介绍

Flask 轻量级 灵活

tornado c10k(c:并发  1万的并发量)

digango 重量级

### Flask项目结构介绍

```markdown
-- 项目名:
	|--static (静态) js css
	|--templates (模板)
	|--app.py (运行|启动)
	
web项目:
	mvc:
	model 模型
	view 视图
	controler 控制器
	
python:
	mtv:
	model 模型
	template 模板-->html
	view 视图 起控制作用 python代码

b/s:
borwser 浏览器
server  服务器

c/s:
client 客户端
server 服务器
```

#### WSGI到底是什么?

##### 介绍

`WSGI`全称`Python Web Server Gateway Interface`，指定了web服务器和Python web应用或web框架之间的标准接口，以提高web应用在一系列web服务器间的移植性。

从以上介绍可以看出:

1. WSGI是一套接口标准协议/规范；
2. 通信{作用)区间是Web服务器和Python Web应用程序之间；
3. 目的是制定标准，以保证不同Web服务器可以和不同的Python程序之间相互通信

###  Flask配置与访问

#### 端口号

```python
run(port='端口号')
```

> ip地址，一个端口号对应一个程序

#### ip地址

```python
run(host='ip地址',port='端口号')
```

> (在云服务器上)如果将host设置为:0.0.0.0 外网可以访问
>
> 默认情况下，只能本机访问

#### Debug

> debug返回是布尔类型的值
>
> 默认False，代码发生改变也不会自动加载 适合于开发环境 development
>
> 如果改为True，代码一改变，服务器就会重新加载最新的代码 适合于 production

```python
run(host='ip地址',port='端口号',debug='True')
```

#### 环境

> production--生产(运行)环境
>
> development--开发环境
>
> testing--测试环境

```python
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
```

> 也可以通过修改配置文件

```python
# settings.py
# 文件内容如下:
# 配置文件
ENV = 'development'
DEBUG = True

# app.py
# 文件内容如下:
from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)
```

### 路由的请求和响应

> 浏览器地址栏输入内容：http://127.0.0.1:5000/index -->服务器 --->app --->有没有这个路由--->就会执行路由匹配的函数--->return 'hello world' ---> response -->客户端的浏览器

#### 请求:request

> http协议，request请求

- 请求行
  - 请求地址：http://127.0.0.1:5000/index
  - 请求方法(method)：getpost

- 请求头
  - key:value ---> 键对值

- 请求体

#### 响应:response

- 响应行

  - 状态码

    | 响应码 | 意思                                                         |
    | ------ | ------------------------------------------------------------ |
    | 200    | {成功) 服务器已成功处理了请求。通常，这表示服务器提供了请求的网页。 |
    | 201    | {已创建)  请求成功并且服务器创建了新的资源。               |
    | 202    | {已接受) 服务器已接受请求，但尚未处理。                    |
    | 203    | {非授权信息) 服务器已成功处理了请求，但返回的信息可能来自另一来源。 |
    | 204    | {无内容) 服务器成功处理了请求，但没有返回任何内容。        |
    | 205    | {重置内容)服务器成功处理了请求，但没有返回任何内容。       |
    | 206    | {部分内容) 服务器成功处理了部分 GET 请求。                 |
    | 300    | {多种选择) 针对请求，服务器可执行多种操作。服务器可根据请求者 (user agent) 选择一项操作，或提供操作列表供请求者选择。 |
    | 301    | {永久移动)  请求的网页已永久移动到新位置。服务器返回此响应{对 GET 或 HEAD 请求的响应)时，会自动将请求者转到新位置。 |
    | 302    | {临时移动) 服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。 |
    | 303    | {查看其他位置)请求者应当对不同的位置使用单独的 GET 请求来检索响应时，服务器返回此代码。 |
    | 304    | {未修改)自从上次请求后，请求的网页未修改过。服务器返回此响应时，不会返回网页内容。 |
    | 305    | {使用代理)请求者只能使用代理访问请求的网页。如果服务器返回此响应，还表示请求者应使用代理。 |
    | 307    | {临时重定向) 服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。 |
    | 400    | {错误请求)服务器不理解请求的语法。                         |
    | 401    | {未授权)请求要求身份验证。对于需要登录的网页，服务器可能返回此响应。 |
    | 403    | {禁止)服务器拒绝请求。                                     |
    | 404    | {未找到)服务器找不到请求的网页。                           |
    | 405    | {方法禁用)禁用请求中指定的方法。                           |
    | 406    | {不接受)无法使用请求的内容特性响应请求的网页。             |
    | 407    | {需要代理授权)此状态代码与 401（未授权)类似，但指定请求者应当授权使用代理。 |
    | 408    | {请求超时)  服务器等候请求时发生超时。                     |
    | 409    | {冲突) 服务器在完成请求时发生冲突。服务器必须在响应中包含有关冲突的信息。 |
    | 410    | {已删除) 如果请求的资源已永久删除，服务器就会返回此响应。  |
    | 411    | {需要有效长度)服务器不接受不含有效内容长度标头字段的请求。 |
    | 412    | {未满足前提条件)服务器未满足请求者在请求中设置的其中一个前提条件。 |
    | 413    | {请求实体过大)服务器无法处理请求，因为请求实体过大，超出服务器的处理能力。 |
    | 414    | {请求的 URI 过长)请求的 URI（通常为网址)过长，服务器无法处理。 |
    | 415    | {不支持的媒体类型)请求的格式不受请求页面的支持。           |
    | 416    | {请求范围不符合要求)如果页面无法提供请求的范围，则服务器会返回此状态代码。 |
    | 407    | {未满足期望值)服务器未满足"期望"请求标头字段的要求。       |
    | 500    | {服务器内部错误) 服务器遇到错误，无法完成请求。            |
    | 501    | {尚未实施)服务器不具备完成请求的功能。例如，服务器无法识别请求方法时可能会返回此代码。 |
    | 502    | {错误网关)服务器作为网关或代理，从上游服务器收到无效响应。 |
    | 503    | {服务不可用)服务器目前无法使用{由于超载或停机维护)。通常，这只是暂时状态。 |
    | 504    | {网关超时) 服务器作为网关或代理，但是没有及时从上游服务器收到请求。 |
    | 505    | （HTTP 版本不受支持)服务器不支持请求中所用的 HTTP 协议版本。 |

- 响应头
  
- key:value ---> 键对值
  
- 响应体
  
  - 响应后返回的内容

### Flask的路由和变量规则

#### 路由

```python
192.168.1.10:8080
@app.route('/index')
def index():
    return ''
```

> URL：http://192.168.1.10:8080/index

##### 路由的绑定

```python
def route(self,rule,**options):
    def decorator(f):
        self.add_url_rule(rule,endpoint,f,**options)
        return f
    return decprator
```

> 这个`@app.route`装饰器其实就是将rule字符串跟视图函数进行了绑定，通过add_url_rule()实现的绑定

```python
# 第一种绑定方式，也是最常用的
@app.route('/')
def index():
    return "index page"

@app.route("/hello")
def hello():
    return "Hello World!"
# 第二种绑定方式，不常用，仅做了解
def index():
    return "index page"
app.add_url.rule("/",view_func=index)

def hello():
    return "Hello World!"
app.add_url.rule("/hello",view_func=hello)
```

##### 路由的变量规则

| 变量类型 | 含义                             |
| -------- | -------------------------------- |
| string   | (缺省值)接受任何不包含斜杠的文本 |
| int      | 接受正整数                       |
| float    | 接受浮点数                       |
| path     | 类似于`string`，但可以包含斜杠   |
| uuid     | 接受UUID字符串                   |

```python
# string
@app.route('/getcity/<key>')
def get_city(key):
    return date.get(key)
# int
@app.route('/add/<int:num>')
def add(num):
    print('-->',type(num))
    result = num + 10
    return str(result)
# float
@app.route('/add1/<float:money>')
def add1(money):
    print('==>',type(money))
    return str(money)
# path
@app.route('/index/<path:p>')
def get_path(p):
    print('***>',type(p))
    print(p)
    return p
# uuid
@app.route('/eee/<uuid:p>')
def emmm(p):
    print('*s*s>',type(p))
    return '获取唯一的标识码'
```

##### 唯一的URL/重定向行为

```python
@app.route('/projects/')
def porjects():
    return "this is projects"

@app.route('/about')
def about():
    return "this is about"
```

> `porjects`路由中定义了'/'，无论请求的URL是否带有/，都会执行视图函数，如果请求的是没有'/'的，浏览器就会做一次重定向，帮你在结尾添加'/'
>
> `about`请求路由中如果添加了'/'：http://127.0.0.1/5000/about/ 显示Not Found
>
> 所有的路由搜索规则是自上而下搜索，在写路由的是有定义的路由是惟一的。

#### 视图

##### 返回值：response对象

> flask中你想向前端返回数据，必须是`response`的对象
>
> str                                =\==\==\==\==>  自动转成`response`对象
> dict                              =\==\==\=\=\==>  `JSON`
> response对象             =\==\==\==\==\>  `response`对象
> make_response()      =\==\==\==\==\>   `response`对象
> redirect()                     =\==\==\==\==>  重定向  302码
> render_template()     =\==\==\====>   模板渲染 + 模板
>
> send_file()  				 =\==\==\====>  打开并返回文件内容 自动识别文件类型 Content-Type:text/plan
>
> jsonify()  					 =\==\==\====>  返回标准的JSON文件字符串 Content-Type：application/json

###### 自动转换成`response`的对象

```python
@app.route("/index")
def index():
    return '嘿嘿嘿'
```

###### 返回多个值

```python
@app.route("/index1")
def index1():
    return "index1.html","200 ok",{"name":"haha"}
```

> `"index1.html" `    --->字符串
>
> `"200 ok"`            --->状态码
>
> `{"name":"haha"}`--->请求头
>
> `return`多个值的时候，前两个必须填，而且顺序不能改变

###### make_response

```python
@app.route("/index2")
def index2():
    response = make_response("index1.html",200,{"name":"haha"})
    return response
```

###### Response

```python
@app.route("/index3")
def index3():
    return Response("<h2>嘿嘿</h2>",headers={"name":"haha"})
```

> 可以解析`html`标签
>
> 另外还可以通过`Response.headers["名称"]="值"`来修改请求头

###### 获取属性的方法

```python
Response.content_type ===> 类型
Response.headers      ===> 请求头 
Response.status_code  ===> 状态码 200
Response.status       ===> 200 ok
```

| 类型       | 类型名称    |
| ---------- | ----------- |
| text/html  | HTML格式    |
| text/plain | 纯文本格式  |
| text/xml   | XML格式     |
| image/gif  | gif图片格式 |
| image/jpeg | jpg图片格式 |
| image/png  | png图片格式 |

##### request请求对象

```python
@app.route("/register")
def regis():
    te = render_template("register.html")
    return te
```

> 自动搜索文件夹中的`template`文件夹中的`register.html`

```html
# register.html较为重要的部分信息
<form action="/action" method="get" style=" text-align: center;">
    <p><input type="text" name="username" placeholder="请输入用户名"></p>
    <p><input type="text" name="ddl" placeholder="请输入地址"></p>
    <p><input type="submit" value="提交"></p>
</form>
```

> `form`默认`get`请求，提交必须具有`name`属性和值

```python
@app.route("/action")
def action():
    print(request.full_path) # /action?username=%E5%BC%A0%E4%B8%89&ddl=%E6%9D%8E%E5%9B%9B
    # 解码 /action?username=张三&ddl=李四
    print(request.path) # /action
    print(request.args) # ImmutableMultiDict([('username', '张三'), ('ddl', '李四')]) ==> {'username':'张三','ddl':'李四'}
    print(request.args.get('username'))
    return "注册成功"
```

> 这样写只能接受`get`请求的信息
>
> 想要就是`post`请求就必须添加`methods=['get','post']`参数

```python
@app.route("/action",methods=['GET','POST'])
def action():
    print(request.form) # 如果请求方法是post则需要通过request.form取值
    print(request.form.get('username')) # ImmutableMultiDict([('username', '你好'), ('ddl', '世界')])
    return "注册成功"
```

> request.args ===>` get`请求
>
> request.form===> `post`请求

##### 重定向

```python
users = []
@app.route("/register",methods=['GET','POST'])
def regis():
    if request.method == 'POST':
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        rpwd = request.form.get("rpwd")
        if pwd == rpwd:
            user = {"username":username,"password":pwd}
            users.append(user)
            return redirect("/")# 首页
        else:
            return "两次密码不一致"
    return render_template("register.html")
```

> ` redirect`重定向函数

```python
@app.route("/",endpoint="index")
def index():
    return render_template("index.html")

users = []
@app.route("/register",methods=['GET','POST'])
def regis():
    if request.method == 'POST':
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        rpwd = request.form.get("rpwd")
        if pwd == rpwd:
            user = {"username":username,"password":pwd}
            users.append(user)
            return redirect(url_for("index"))
        else:
            return "两次密码不一致"
    return render_template("register.html")
```

> 通过`url_for("别名、索引名")`函数来获取首页链接，从而达成重定向到首页，常用于大型、复杂的网站。

#### 模板

> 向模版中传递变量值
>
> `render_template("show.html",key=value)`
>
> 1. 控制结构 {% %}
> 2. 变量取值 {{ }}
> 3. 注释 {# #}

##### 基础方法

```python
name = '李强'
age = 18
friends = ['1','2']
dict = {'gift1':1,'gift2':2,'gift3':3}
# -----------------
{{ 变量名key }}
{{ list.0 }} ====> {{ list[0] }}
{{ dict.key }}====> {{ dict.get(key) }}
{{ girl.name }} ===> {{ 对象.属性 }}
```

##### 控制块

###### 判断语句

```python
{% if 条件 %}
{% endif %}

{% if 条件 %}
	条件为Ture
{% else %}
	条件为False
{% endif %}

{% if 条件 %}
	条件成立
{% elif %}
	条件成立
	……
{% endif %}
# -------例子-------
# 在下面
```

###### 循环语句

```python
{% for 变量 in 可迭代的对象 %}
	for 循环执行任务
{% endfor %}
# -------例子-------
{% for item in users %}
<table border="0">
    {% if '4' in item.user %}
        <tr style="color: red;">
            <th>username</th>
            <th>password</th>
        </tr>
    {% else %}
        <tr>
            <th>username</th>
            <th>password</th>
        </tr>
    {% endif %}
    <tr>
        <td>{{ item.user }}</td>
        <td>{{ item.pwd }}</td>
    </tr>
</table>
{% endfor %}
```

> 将for循环语句放置到列表语句中

###### 序号语句

> loop.index           从1开始排序
>
> loop.index0         从0开始排序
>
> loop.revindex      倒数到1
>
> loop.revindex0    倒数到0
>
> loop.first               判断是否为第一，布尔类型
>
> loop.last                判断是否为最后，布尔类型

```python
{% for item in users %}
<ul>
	<li>{{ loop.index }}</li> # 从1开始排序
    <li>{{ loop.index0 }}</li> # 从0开始排序
    <li>{{ loop.revindex }}</li> # 倒数到1
    <li>{{ loop.revindex0 }}</li> # 倒数到0
    <li>{{ item }}</li>
</ul>
{% endfor %}
```

##### 过滤器

> a.过滤器需要传参
>
> ​	{{ 变量名 | 过滤器(*args) }}
>
> b.过滤器不需要传参
>
> ​	{{ 变量名 | 过滤器 }}

| 过滤器      | 含义                                         |
| ----------- | -------------------------------------------- |
| safe        | 渲染时值不转义                               |
| capitialize | 把值的首字母转换成大写，其他子母转换为小写   |
| lower       | 把值转换成小写形式                           |
| upper       | 把值转换成大写形式                           |
| title       | 把值中每个单词的首字母都转换成大写           |
| trim        | 把值的首尾空格去掉                           |
| striptags   | 渲染之前把值中所有的HTML标签都删掉           |
| join        | 拼接多个值为字符串                           |
| replace     | 替换字符串的值                               |
| round       | 默认对数字进行四舍五入，也可以用参数进行控制 |
| int         | 把值转换成整型                               |
| first       | 取第一个元素                                 |
| last        | 取最后一个元素                               |
| length      | 获取列表长度                                 |
| sum         | 列表求和                                     |
| sort        | 列表排序                                     |

##### 自定义过滤器

> 过滤器本质就是 函数

###### 通过Flask模块中的`add_template_filter`方法

```python
def replace_hello(value):
    print("---------",value)
    value = value.replace("hello","")
    print("=========",value)
    return value.strip() # 务必将替换的结果返回

app.add_template_filter(replace_hello,"hello")
```

> a.定义函数，带有参数和返回值
>
> b.添加过滤器`add_template_filter(function,name="")`
>
> c.在模板中使用：{{ 变量 | 自定义过滤器}}

###### 使用装饰器完成

```python
@app.template_filter("listreverse")
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li
```

> a.定义函数，带有参数和返回值
>
> b.通过装饰器完成，`@app.template_filter("过滤器名字")`
>
> c.在模板中使用：{{ 变量 | 自定义过滤器}}

##### 复用

###### 模板继承⭐

> 需要模板继承的情况：
>
> 1. 多个模板具有完全相同的顶部和底部
> 2. 多个模板具有相同的模板内容，但内容不同
> 3. 多个模板具有完全相同的模板内容

**标签**

```python
{% block 名字 %}
{% enblock %}
```

**使用**

```python
{% extends "show.html" %}
{% block title %}
    show1
{% endblock %}
```

> a.定义父模板
>
> b.子模板继承父模板

**步骤如下：**

> **父模板：**
>
> 1.定义一个base.html的模板
>
> 2.分析模板哪些是变化的
>
> ​	对变化的部分用block进行“预留位置”也称作：挖坑
>
> 3.注意：样式和脚本 需要提前预留
>
> ​	{% block mycss%}{% endblock %}
>
> ​	{% block myjs%}{% endblock %}
>
> **子模板使用父模板：**
>
> 1.将父模板继承过来  {% extends "父模板的名称" %}
>
> 2.找到对应的block(坑)填充，每个block都是有名字的

**加载css、js等静态文件的方法**

> url_for('static',filname='css/style.css')

###### include：包含

> 在A,B,C页面都有的共同部分，但是其他页面没有这部分
>
> 这个时候考虑`include`

**步骤**

> a.先定义一个公开模板的部分，xxx.html
>
> b.谁使用则include过来，{% include ‘文件夹/文件名’ %}

###### 宏：macro

> 可以把它看作是jinja2的一个函数，这个函数可以返回一个HTML字符串
>
> 目的：代码可以复用，避免代码冗余

```python
{# 定义宏 #}
{% macro form(action,value="登录",method="POST") %}
    <form action="{{ action }}" method="{{ method }}">
        <p><input type="text" name="username" placeholder="用户名" ></p>
        <p><input type="password" name="password" placeholder="密码"  id=""></p>
        <p><input type="submit" value="{{ value }}"></p>
    </form>
{% endmacro %}

{# 调用宏1 #}
{% form("/") %}

{# 调用宏2 #}
{% import "macro/macro.html" as f %}
{{ f.form('/',value="注册") }}
```

### 附加：声明变量&&总结

```python
{#  全局声明  #}
{% set username="李强" %}
{{ username }}
{#  局部声明  #}
{% with num=1000 %}
    {{ num }}
{% endwith %}
```

```python
变量：{{ 变量 }}

块：
{% if 条件 %}………………{% endif %}
{% for 条件%}………………{% endfor %}
{% block 条件 %}…………{% endblock %}
{% macro 条件 %}…………{% endmacro %}
{% include "" %}………包含
{% import "" %}…………导入宏
{% extends "" %}…………继承
{{ url_for("static",filename="") }}
{{ hongname(xxx) }}

view:视图
@app.route("/",endpoint="",methods=["GET","POST"])
def index():
	return response|""|render_template("xxx.html")

template:模板
	模板的语法
	网页 ---> 模板引擎处理 ---> 模板
	render_template
	{{ 变量 }}

Blueprint:蓝图
```

### 蓝图和视图

> `Blueprint`是一种组织一组相关视图及其他代码的方式。与把视图及其他 代码直接注册到应用的方式不同，蓝图方式是把它们注册到蓝图，然后在工厂函数中 把蓝图注册到应用。
>
> Flaskr 有两个蓝图，一个用于认证功能，另一个用于博客帖子管理。每个蓝图的代码 都在一个单独的模块中。使用博客首先需要认证，因此我们先写`认证蓝图`。

#### 认证蓝图

```python
Flask
	|- apps[python包-蓝图]
		|- __init__.py[初始化文件]
		|- user[蓝图-用户]
            |- model.py[模型文件]
            |- view.py[蓝图-用户中的视图文件]
            |- __init__.py
	|- static[静态资源]
	|- templates[模板]
		|- base.html[基础模板]
		|- user
			|- login.html[用户登录]
			|- register.html[用户注册]
            |- update.html[用户信息修改]
			|- show.html[用户信息展示]
	|- app.py[Flask启动]
	|- settings.py[Flask配置文件]
```

> 创建蓝图
>
> ```python
> user_bp = Blueprint('user', __name__)
> ```
>
> `app/__init__.py`中注册蓝图
>
> ```python
> app.register_blueprint(user_bp)
> ```
>
> `app/__init__.py`中创建app，添加`template_folder`(模板文件夹)以及`static_folder`(静态文件夹)
>
> ```python
> app = Flask(__name__,template_folder="../templates",static_folder="../static")
> ```

#### 数据库

> 数据的持久化

##### Flask-Script

> ```powershell
> pip install flask-script
> ```
>
> Pipenv
>
> ```powershell
> pipenv install flask-script
> ```

**使用里面的`Manager`进行命令得到管理和使用**

```python
from flask_script import Manager
manager = Manager(app=app)
manager.run()
```

**使用命令在终端**

```
python3 app.py runserver
python app.py runserver
```

**自定义命令**

```python
@manager.command
def init():
    print("初始化")
------------终端--------------
(Flask2) D:\vscode\vscode-python\Flask2>python app.py init
初始化
```

##### 安装

###### PyMySQL--建公路

> 连接数据库
>
> ```powershell
> pipenv install PyMySQL
> ```

###### Flask-SQLAlchemy--实现ORM映射

>基于SQLAIchemy，做了提升
>
>使用程序员在开发的时候更方便
>
>```powershell
>pipenv install flask_sqlalchemy
>```

###### SQLAIchemy

> SQLAlchemy 是 Python 中一个通过 ORM 操作数据库的框架

###### Flask-Migrate--发布命令工具

> Flask-Migrate以十分方便的进行数据库的迁移与映射，将我们修改过的ORM模型映射到数据库中
>
> ```powershell
> pipenv install flask-migrate
> ```

##### 配置环境

```python
Flask
    |- apps
        |- __init__.py
        |- user
        	|- __init__.py
            |- models.py[模型文件]
            |- view.py
    |- ext
        |- __init__.py
    |- static
    |- templates
    |- app.py
    |- settings.py[配置文件]
```

###### 1.配置数据库的连接路径[settings.py]

```python
# 配置文件
class Config:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:456789@127.0.0.1:3306/flasklx'

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
```

###### 2.创建包[ext]

```python
------ext/__init__.py文件------
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
------apps/__init__.py文件-----
def create_app():
    …………
	db.init_app(app) # 将db对象与app进行关联
    …………
    return app
```

###### 3.migrate[app.py]

```python
migrate = Migrate(app=app,db=db)# 影响数据库的映射
manager.add_command('db',MigrateCommand)# 命令交给manager
```

###### 4.创建模型[models.py]

```python
# 模型文件
# OPM 类 ---> 表
# 类对象 ---> 表中的一条记录
from datetime import datetime

from ext import db

class User(db.Model):
    # db.Column(类型,约束) 映射表中的列
    '''
    类型：
    db.Integer      int
    db.String(15)   varchar(15)
    db.DateTime     datetime
    '''
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(20),nullable=False)
    phone = db.Column(db.Integer,unique=True)
    rdatetime = db.Column(db.DateTime,default=datetime.now)

    def __str__(self):
        return self.username
```

###### 5.使用命令	

> a.敲黑板……
> 	app.py 中导入 模型文件
>
> ```python
> from apps.user.model import User
> ```
>
> b.在终端使用命令：db
>
> ```python
> # 产生一个文件夹migrations
> python app.py db init
> # 自动产生版本文件
> python app.py db migrate
> # 
> python app.py db upgrade
> # -----------------------------------------
> |- migrations ===> python app.py db init
> 	|- versions 版本文件夹
>  	|- d3c49ec05e99_.py ===> python app.py db migrate
> 
> # 便于复制----------------------------------
> python app.py db init
> python app.py db migrate
> python app.py db upgrade
> ```

#### 加密

> md5 sha1 sha256 sha512

```python
import hashlib

msg = '你好世界'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5.hexdigest())# 32

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest()) # 40

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest()) # 64

sha512 = hashlib.sha512(msg.encode('utf-8'))
print(sha512.hexdigest()) # 128
```

#### 查询

- 查询全部

  ````python
  模型类.query.all() ==> select * from user;
  ````

- 条件查询

  ```python
  模型类.query.filter_by(字段名 = 值) ==> select * from user where 字段名 = 值;
  模型类.query.filter_by(字段名 = 值).first() ==> select * from user where 字段名 = 值 limit 1;
  模型类.query.filter() 里面是布尔的条件 >>> 模型类.query.filter(模型名.字段名 == 值)
  模型类.query.filter_by() 里面是一个等值 >>> 模型类.query.filter_by(字段名 = 值)
  ```

- 模糊查询

  ```python
  User.query.filter().all()    ---> 列表
  User.query.filter().first()  ---> 对象
  # like查询--------------
  User.query.filter(User.username.endswith('z')).all() ===》select * from user where username like '%z';
  User.query.filter(User.username.startswith('z')).all() ===》select * from user where username like 'z%';
  User.query.filter(User.username.contains('z')).all() ===》select * from user where username like '%z%';
  User.query.filter(User.username.like('z%')).all() ===》select * from user where username like 'z%';
  ```

- 多条件查询&&特殊

  > `and_`(并且)，`or_`(或者)，`not_`(不等于)，`in_`(存在)
  
  ```python
  # or查询--------------
  User.query.filter(or_(User.username.like('z%'),user.username.contains('i'))).all() ===》select * from user where username like 'z%' or username like '%i%';
  # and查询--------------
  User.query.filter(and_(User.rdatetime < '2020-05-25 10:30:00', user.username.contains('i'))).all() ===》select * from user where rdatetime < '2020-05-25 10:30:00' and username like '%i%';
User.query.filter(and_(User.rdatetime.__lt__('2020-05-25 10:30:00'), user.username.contains('i'))).all() ===》select * from user where rdatetime < '2020-05-25 10:30:00' and username like '%i%';
  # not查询--------------
  User.query.filter(not_(User.rdatetime < '2020-05-25 10:30:00')).all() ===》select * from user where rdatetime >= '2020-05-25 10:30:00';
  # in查询
  User.query.filter(User.phone.in_(['123','456'])).all() ===》select * from user where phone in ['123','456'];
  ```
  
  > 补充：`__gt__`(大于),`__lt__`(小于),`__ge__`(gt equal 大于等于),`__le__`(le equal 小于等于)  ===>   范围：通常用于整型、时间日期
  >
  > 也可以用  >  <  >=  <=  !=
  
- 排序

  ```python
  # 升序
  User.query.filter(User,username.contains('z')).order_by('rdatetime').all() >>> select * from user where username like '%z%' order by rdatetime;
  User.query.filter(User,username.contains('z')).order_by(User.rdatetime).all() >>> select * from user where username like '%z%' order by rdatetime;
  # 降序
  User.query.filter(User,username.contains('z')).order_by(-User.rdatetime).all() >>> select * from user where username like '%z%' order by rdatetime desc;
  ```

  > order_by(参数)
  >
  > 直接是字符串：’字段名‘  但是不能倒序 >>>> order_by('username')
  >
  > 字段名：模型.字符 >>>> order_by(User.username)---升序 以及order_by(-User.username) ---降序

- 限制

  ```python
  User.query.limit(2).all() >>> select * from User limit(2)
  User.query.offset(2).limit(2).all() >>> select * from User limit(2,2)
  ```

- 总结

  ```python
  User.query.all() 全部
  User.query.get() 一个
  User.query.filter() 多个或单个
  	如果检索的字段是字符串(varchar,db.String)
  	User.username.startswith('') >>> z%
  	User.username.endswith('') >>> %z
  	User.username.contains('') >>> %z%
  	User.username.like('') >>> %z%
  	User.username.in_(['']) >>> ['123','456']
  	User.username == '' >>> 等值
  	如果检索的字段是整型或者日期类型
  	User.age.__lt__(18) >>> 小于
  	User.age.__gt__(18) >>> 大于
  	User.age.__le__(18) >>> 小于等于
  	User.age.__ge__(18) >>> 大于等于
  	User.age.between(18,20) >>> 范围
  	多条件：and_,or_
  	非：not_
  User.query.filter_by()
  ```

#### 删除

##### 逻辑删除

  > 定义数据库中的表的时候，添加一个字段isdelete，通过此字段控制是否删除

  ```python
id = request.args.get('id')
user = User.query.get(id)
user.isdelete = True
db.session.commit()
  ```

##### 物理删除

  > 彻底从数据库中删除

  ```python
id = request.args.get('id')
user = User.query.get(id)
db.session.delete(user)
db.session.commit()
  ```

#### 更新

  ```python
username = request.form.get('username')
phone = request.form.get('phone')
id = request.form.get('id')
user = User.query.get(id)
user.username = username
user.phone = phone
db.session.commit()
  ```

###   Flask博客

#### 外键的设置方法

```python
# 分别在不同的models.py中填写---------
# article/models.py
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# user/models.py
articles = db.relationship('Article', backref='user')
# 分别在相同的models.py中填写---------
# article/models.py
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
users = db.relationship('User', backref='article')
```

> 缺一不可，但是并未要求必须写在同一个文件中

#### 通过外键调用另一个表的方法

```python
{# 根据文章找作者 #}
{% for article in articles %}
	<div>作者：{{ article.user.username }}</div>
{% endfor %}

{# 根据用户找文章 #}
{% for article in user.articles %}
    <div>创建时间：{{ article.pdatetime }}</div>
{% endfor %}
```

> 注意：调用另一个表的话必须在这个表中设置`relationship`来连接另一个表

#### 创建模板base.html

##### 安装Flask_Bootstrap

> Flask_Bootstrap和Bootstrap_Flask不能同时存在

```python
pipenv install flask-bootstrap
```

##### 配置Flask_Bootstrap

```python
exts/__init__.py
#----------------------
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
```

##### 初始化Flask_Bootstrap

```python
apps/__init__.py
#--------------------
bootstrap.init_app(app=app)
```

##### 常用基本快

```
{% block html_attribs %}{% endblock %}
{% block title %}{% endblock %}
{% block styles %}{% endblock %}
{% block body %}{% endbody %}
{% block header %}{% endblock %}
{% block navbar %}{% endblock %}
{% block content %}{% endblock %}
{% block footer %}{% endblock %}
{% block scripts %}{% endblock %}
```

###### 样式模块

```python
{% block styles %}
	{{ super() }}
{% endblock %}
{% block scripts %}
    {{ super() }}
{% endblock %}
```

> {{ super() }}引入父模板的样式

#### 加密

> 更强的加密方式

```
加密方法：
pwdhash = generate_password_hash(pwd)
检查加密：
check_password_hash(pwdhash,pwd) ===> 布尔类型
```

#### 会话机制￥登录&退出￥

> cookie是存储在本地浏览器上，session存储在服务上

##### cookie方式

```python
保存：
	通过response对象保存
	response = redirect(xxx)
	response = render_template(xxx)
	response = Response()
	response = make_response()
	response = jsonify()
	# 通过对象调用方法
	response.set_cookie(key,value,max_age)
	
获取：
	通过request对象获取
	request.form.get()
	request.args.get()
	cookie也在request对象中
	request,cookies.get(key) --> value
	
删除：
	通过response对象删除,把浏览器中的key=value删除了
	response = redirect(xxx)
	response = render_template(xxx)
	response = Response()
	response = make_response()
	response = jsonify()
	# 通过对象调用方法
	response.delete_cookie(key)
```

##### session机制

> 注意：记得要导入
>
> ```python
> form flask import session
> ```
>
> 以及加密匙
>
> ```python
> # settings.py
> SECRET_KEY = '密匙内容'
> ```

```python
保存：
	session['uid'] = user.id
	
获取：
	uid = session['uid']# 个人不建议
	uid = session.get('uid')
	
删除：
	del session['uid']# 不推荐 只会删除session中的这个键值对，不会删除session空间和cookie
    session.clear() # 删除session的内存空间和cookie
```

##### 手机号登录[短信验证码]

> 具体情况具体分析，没什么好写的
>
> 原理为：点击`发送验证码`按钮，发送手机号码到后端，后端再转发给短信服务供应商，供应商再将`验证码`发给用户和后端，用户就收到验证码后，输入验证码，点击提交，再次发给后端，经过后端的对比判断，成功则发生`session`给用户，用户凭借`session`访问网页

#### 钩子函数

```python
在app上的钩子函数：
    before_first_request ---> 处理第一次请求之前执行
    before_request ---> 在请求(request)之前做出响应
    after_request ---> 在响应(response)之前做出响应
    teardown_appcontext ---> 不管是否有异常，注册的函数都会在每次请求之后执行
    template_filter ---> 在使用Jinja2模板的时候自定义过滤器
    context_processor ---> 上下文处理器
    errorhandler(404) ---> errorhandler接收状态码，可以自定义返回这种状态码的响应的处理方法
# ------------------------------------------
在蓝图上的钩子函数：
    before_app_first_request ---> 处理第一次请求之前执行
    before_app_request ---> 在每次请求之前执行
    after_app_request ---> 在响应(response)之前做出响应
    teardown_appcontext ---> 不管是否有异常，注册的函数都会在每次请求之后执行
    template_filter ---> 在使用Jinja2模板的时候自定义过滤器
    context_processor ---> 上下文处理器
    errorhandler(404) ---> errorhandler接收状态码，可以自定义返回这种状态码的响应的处理方法
```

#### 实现个人信息修改、密码修改、发表文章的菜单切换

[BNFJHJ.gif](https://s1.ax1x.com/2020/10/30/BNFJHJ.gif)

```javascript
$(window).bind('hashchange', function () {
    switch (location.hash) {
        case "#tag=1":
            $("form").addClass("hidden").removeClass("show");
            $("#1").removeClass("hidden").addClass("show");
            $('li[class="active"]').removeClass("active");
            $('#menu1').addClass("active");
            break;
        case "#tag=2":
            $("form").addClass("hidden").removeClass("show");
            $("#2").removeClass("hidden").addClass("show");
            $('li[class="active"]').removeClass("active");
            $('#menu2').addClass("active");
            break;
        case "#tag=3":
            $("form").addClass("hidden").removeClass("show");
            $("#3").removeClass("hidden").addClass("show");
            $('li[class="active"]').removeClass("active");
            $('#menu3').addClass("active");
            break;
        default:
            break;

    }
});

let url = window.location.href;
if (url.indexOf("#tag=2") >= 0) { //判断url地址中是否包含code字符串
    $("form").addClass("hidden").removeClass("show");
    $("#2").removeClass("hidden").addClass("show");
    $('li[class="active"]').removeClass("active");
    $('#menu2').addClass("active");
} else if (url.indexOf("#tag=3") >= 0) {
    $("form").addClass("hidden").removeClass("show");
    $("#3").removeClass("hidden").addClass("show");
    $('li[class="active"]').removeClass("active");
    $('#menu3').addClass("active");
} else {
    $("form").addClass("hidden").removeClass("show");
    $("#1").removeClass("hidden").addClass("show");
    $('li[class="active"]').removeClass("active");
    $('#menu1').addClass("active");
}
```

#### 发表文章注意事项

> 为了实现存储emoji表情，需要将数据中代表文章内容的字段类型text修改成blob
>
> 对应Flask-SQLAlchemy的方法为

```python
content = db.Column(db.Text, nullable=False)
```

修改成

```python
content = db.Column(db.LargeBinary(16777216), nullable=False)
```

##### 注意

> blob是二进制类型
>
> 将文章内容展示需要记得转换格式，需要完成两个自定义过滤器：转码&字数限制

```python
@user_bp.app_template_filter('cdecode')
def content_decode(content):
    content = content.decode('utf-8')
    return content

@user_bp.app_template_filter('cfew')
def content_cfew(content):
    return content[:100]
```

#### 文章展示功能的实现

##### `paginate`函数

```python
pageination = Article.query.order_by(-Article.pdatetime).paginate(page=1,per_page=3) # 返回的是对象，即pageination是对象
#------------------
pageination.items # [<Article 4>,<Article 3>,<Article 2>]
pageination.page # 当前页码数
pageination.prev_num # 当前页的前一个页码数
pageination.next_num # 当前页的后一个页码数
pageination.has_next # True 有上一页吗
pageination.has_prev # True 有下一页吗
pageination.pages # 总共有多少页
pageination.total # 总的记录有几条
# --------具体实现------------
# 通过request获取页数信息，通过paginate返回轨规定数量的内容
page = int(request.args.get("page", 1))
pagination = Article.query.order_by(-Article.pdatetime).paginate(page=page, per_page=4)
```

##### 实现方法

```html
<div class="col-sm-12 col-sm-offset-1 col-md-10 col-lg-offset-1 col-lg-10">
        <div class="row">
            {% for article in pagination.items %}
                <div class="col-sm-5 col-md-4 col-lg-3">
                    <div class="thumbnail">
                        <img src="{{ url_for('static',filename=user.icon) }}" alt="...">
                        <div class="caption">
                            <h3><a href="{{ url_for('article.detail') }}?aid={{ article.id }}">{{ article.title }}</a></h3>
                            <p><span>作者：{{ article.user.username }}</span></p>
                            <p><span>{{ article.content | cdecode | cfew | striptags }}</span></p>
                            <p><span>发布时间：{{ article.pdatetime }}</span></p>
                            <p>
                                <span>收藏量：{{ article.save_num }}</span>  <span>点击量：{{ article.click_num }}</span>  <span>点赞量：{{ article.love_num }}</span>
                            </p>
                            <p>
                                <a href="#" class="btn btn-primary" role="button">点击阅读</a>
                                <a href="#" class="btn btn-default" role="button">Button</a>
                            </p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
        <nav aria-label="Page navigation">
            <ul class="pagination">

                <li {% if not pagination.has_prev %} class="disabled" {% endif %}>
                    <a {% if pagination.has_prev %}href="{{ url_for('user.index') }}?page={{ pagination.prev_num }}"{% endif %} aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>

                {% for page_num in range(pagination.pages) %}
                    <li {% if pagination.page == page_num + 1 %}class="active"{% endif %}><a
                            href="{{ url_for('user.index') }}?page={{ page_num + 1 }}">{{ page_num + 1 }}</a></li>
                {% endfor %}

                <li {% if not pagination.has_next %} class="disabled" {% endif %}>
                    <a {% if pagination.has_next %} href="{{ url_for('user.index') }}?page={{ pagination.next_num }}" {% endif %} aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>

            </ul>
        </nav>
    </div>
```

#### 文章详情功能的实现

```html
<div class="col-md-9 col-lg-offset-2 col-lg-6">
        <div class="row">
            <div class="col-sm-12">
                <div class="thumbnail">
                    <div class="caption">
                        <h3>{{ article.title }}</h3>
                        <p><span>{{ article.content | cdecode | safe }}</span></p>
                    </div>
                </div>
            </div>
        </div>
        <nav aria-label="...">
            <ul class="pager">
                <li class="previous"><a href="#"><span aria-hidden="true">&larr;</span> Older</a></li>
                <li class="next"><a href="#">Newer <span aria-hidden="true">&rarr;</span></a></li>
            </ul>
        </nav>
    </div>
    <div class="col-md-3">
        <div class="row">
            <div class="col-sm-12">
                <div class="thumbnail">
                    <img src="{{ url_for('static',filename=article.user.icon) }}" alt="...">
                    <div class="caption">
                        <h3><a href="{{ url_for('article.detail') }}?aid={{ article.id }}">{{ article.title }}</a></h3>
                        <p><span>作者：{{ article.user.username }}</span></p>
                        <p><span>发布时间：{{ article.pdatetime }}</span></p>
                        <p>
                            <button class="btn btn-primary" type="button" id="save_num">
                                收藏量： <span class="badge">{{ article.save_num }}</span>
                            </button>
                            <button class="btn btn-primary" type="button" id="click_num">
                                点击量： <span class="badge">{{ article.save_num }}</span>
                            </button>
                            <button class="btn btn-primary" type="button" id="love_num">
                                点赞量： <span class="badge">{{ article.save_num }}</span>
                            </button>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <div class="thumbnail">
                    <div class="caption">
                        <h3>一言</h3>
                        <p>往者不可谏，来者犹可追。</p>
                        <p><span>作者：{{ article.user.username }}</span></p>
                        <p><span>发布时间：{{ article.pdatetime }}</span></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
```

##### 点赞、收藏、点击功能的实现

> `javascript`具体脚本，其他几个也一样

````javascript
$(function () {
    $('#click_num').click(function () {
        let $this = $(this);
        if ($this.hasClass('btn-danger')) {
            $.get('{{ url_for('article.click') }}', {aid:{{article.id}}, pk: 'del'}, function (data) {
                $this.children('span').text(data.num);
                $this.removeClass('btn-danger');
            })
        } else {
            $.get('{{ url_for('article.click') }}', {aid:{{article.id}}, pk: 'add'}, function (data) {
                $this.children('span').text(data.num);
                $this.addClass('btn-danger');
            })
        }
    });
})
````

> 后端具体，其他几个也一样

```python
@article_bp.route("/love", endpoint='love')
def article_love():
    pk = request.args.get('pk')
    id = request.args.get('aid')
    article = Article.query.get(id)
    if pk == 'add':
        article.love_num += 1
    else:
        article.love_num -= 1
    db.session.commit()
    return jsonify(num=article.love_num)
```

#### 文件管理

##### 本地上传

> 表单中必须有`enctype="multipart/form-data"`

```python
# html
<form action="{{ url_for('user.user_change') }}" method="post" id="1" enctype="multipart/form-data">
</form>
# view.py
icon = request.files.get('icon') # FileStorage
# 属性和方法：FileStorage >>> icon
icon_name = icon.filename # 文件名称
icon.save(path) # 保存文件 path上传的路径：os.path.join(Config.UPLOAD_ICON_DIR, icon_name)
icon.read() # 读取文件 转换成二进制
```

##### 云端上传(对象存储)

> 本地的资源是有限或者空间是有限的
>
> 七牛云 ----> [七牛云 For Python SDK](https://developer.qiniu.com/kodo/sdk/1242/python)
>
> 但是七牛云需要实名认证，所以我使用的是WebDav
>
> WebDav的坏处也有，就是预览WebDav服务器上的图片需要登录

#### 文章详情后续-评论

> 评论的上一页和下一页带的连接必须带有`aid`(即文章id)
>
> 实现评论上下页的方法和文章展示、相册管理都一样(通过`paginate`函数实现)

#### 实现缓存(redis的使用)

> 缓存键值对

```python
# 设置
cahe.set(key,value,timeout=sencond)
cache.set_many([(key,value),(key,value),(key,value),(key,value)……])
# 获取
cache.get(key)
cache.get_many(key1,key2,key3……)
# 删除
cacha.delete(key)
cacha_delete_many(key1,key2,key3……)
cacha.clear()
```

> 视图函数的缓存

```python
@user_bp.route('/')
@cache.cached(timeout=50)
def index():
	pass
	……
```

#### Flask-WTF[WTFORM]表

> 这样不但可以增加对表单的判断，还可以防止CSRF攻击

##### 安装语法

```python
pip install flask-WTF
```

##### 定义form.py

```python
class UserForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(),length(min=6,max=12,message='用户名长度必须在6~12位')])
    password = PasswordField('password',validators=[DataRequired(),length(min=6,max=12,message='密码长度必须在6~12位')])
```

> 各种Field类型：
>
> StringField
>
> PasswordField
>
> TextAreaField
>
> ……
>
> 各种验证：
>
> DataRequired
>
> EqualTo
>
> Length
>
> ……

##### 使用方法

> 它将是具有csrf保护的会话安全形式
>
> 为了生成csrf令牌，您必须具有一个密钥，该密钥通常与Flask应用程序的密钥相同。如果要使用另一个密钥，请对其进行配置

```python
# 定义SECRET_KEY
app.config['SECRET_KEY'] = 'as5,dawd123asd'
# 定义form
form = UserForm()
return render_template('user.html',form=form)
```

```html
# ----文件user.html---
<form action="{{ url_for('index') }}" method="POST" enctype="multipart/form-data">
        <p>{{ form.csrf_token }}</p>
        <p>{{ form.name.label }}:{{ form.name }}{% if form.name.errors %}{{ form.name.errors.0 }}{% endif %}</p>
        <p>{{ form.password.label }}:{{ form.password }}{% if form.password.errors %}
            {{ form.password.errors.0 }}{% endif %}</p>
</form>
```

##### 提交表单验证

> 在视图函数里面使用，可以判断接受到的表单数据是否有问题

```python
if form.validate_on_submit(): ---> 主要通过validate_on_submit进行校验
    return '提交成功'
```

##### 增加form验证

> 例如：用户名不能以数字开头

```python
def validate_name(self,data):
    if self.name.data[0].isdigit():
        raise ValidationError('用户名不能以数字开头')
```

##### 文件上传

```python
# 定义form.py
class UserForm(FlaskForm):
	……
	# 上传使用的就是FileField，如果需要指定上传文件的类型需要使用FileAllowed
	icon = FileField(label='用户头像', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'], message='该文件不被允许上传')])
# 模板中的使用同其他类型的字段，但是必须在form上面：enctype="multipart/form-data"
# 视图函数如果验证成功，通过：
	icon = uform.ico.data ---> icon是FileStorage类型
	filename = secure_filename(icon.filename)
	icon.save(os.path.join(UPLOAD_DIR, filename))
```

##### 添加验证码---获取密钥需要FQ

> 它带有许多配置，您必须实现它们。

| RECAPTCHA_PUBLIC_KEY  | **必需**公共密钥。                                           |
| --------------------- | ------------------------------------------------------------ |
| RECAPTCHA_PRIVATE_KEY | **必需**私钥。                                               |
| RECAPTCHA_API_SERVER  | **可选**指定您的Recaptcha API服务器。                        |
| RECAPTCHA_PARAMETERS  | **可选**的JavaScript（api.js）参数字典。                     |
| RECAPTCHA_DATA_ATTRS  | **可选**数据属性选项字典。 https://developers.google.com/recaptcha/docs/display |

```python
# 定义form.py
recaptcha = RecaptchaField(label='验证码')
# 定义app.py,设置验证码密钥
# 公共密钥
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# 私钥
app.config['RECAPTCHA_PTOVATE_KEY'] = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
```

##### 添加图形验证码

```python
# 定义验证码生成器--uitl.py
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def generate_image(length):
    s = 'qwertyuiopasdfghjklzxcvbnm123456789'
    # 设置画布大小
    size = (130, 50)
    # 设置画布背景颜色
    im = Image.new('RGB', size, color=get_random_color())
    # 创建字体
    font = ImageFont.truetype(r'C:\Windows\Fonts\ariali.ttf', size=35)
    # 这里的‘C:\Windows\Fonts\ariali.ttf’需要自行更改
    # 创建ImageDraw对象--创建画笔
    draw = ImageDraw.Draw(im)
    code = ''
    for i in range(length):
        c = random.choice(s)
        code += c
        draw.text((9 + random.randint(5, 20) + 30 * i, random.randint(1, 20)),
                  text=c,
                  fill=get_random_color(),
                  font=font)
    # 绘制干扰线
    for i in range(6):
        x1 = random.randint(0, 130)
        y1 = random.randint(0, 50 / 2)
        x2 = random.randint(0, 130)
        y2 = random.randint(50 / 2, 50)
        draw.line(((x1, y1), (x2, y2)), fill=get_random_color())

    # 添加滤镜
    im = im.filter(ImageFilter.EDGE_ENHANCE)
    im.show()
    return im, code


if __name__ == '__main__':
    generate_image(4)


# 调用验证码
@app.route('/image')
def get_image():
    im, code = generate_image(4)
    # 将image对象换成二进制
    buffer = BytesIO()
    im.save(buffer, 'JPEG')
    buf_bytes = buffer.getvalue()
    # 验证码保存到session中
    session['valid'] = code
    response = make_response(buf_bytes)
    response.headers['Content-Type'] = 'image/jpg'
    return response
 
# 获取验证码--html中
<p>{{ form.recaptcha.label }}:{{ form.recaptcha }}<img src="{{ url_for('get_image') }}" alt=""></p>

# 实现点击刷新验证码
$('img').click(function () {
    $(this).attr('src', '{{ url_for('get_image') }}?ran=' + Math.random());
})


# 验证验证码-定义form.py
def validate_recaptcha(self,data):
    input_code = data.data
    code = session.get('valid')
    if input_code.lower() != code.lower():
        raise ValidationError('验证码错误')
```

##### 使用``bootstrap`构建网站时使用Flask-WTF

> 在引入bootsrap的base后

```
{% extends 'bootstrap/base.html' %}
{% import 'bootstrap/wtf.html' as wtf %}
```

> 在表单的位置

```
{% block centent %}
	<form action="{{ url_for('index') }}" method="POST" enctype="multipart/form-data">
		{{ wtf.quick_form(form,button_map={'submit_button':'primary'},form_type= 'horizontal',horizontal_columns=('lg',5,2)) }}
	</form>
{% endblock%}
```

> 加载指定项，例如加载定义的name

```
{% block centent %}
	<form action="{{ url_for('index') }}" method="POST" enctype="multipart/form-data">
		{{ wtf.quick_form(form,button_map={'submit_button':'primary'},form_type= 'horizontal',horizontal_columns=('lg',5,2)) }}
		{{ wtf.form_field(form.name)}}
	</form>
{% endblock%}
```

#### 闪现

> 在一个请求结束的时候添加flash闪现

```
#-----app.py
flash('恭喜！验证成功','info')
flash('哈哈','error')
flash(username,'warning')
class Dorm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    sex = db.Column(db.String(1))
    isDelete = db.Column(db.Integer, default=0)  # 是否删除-->方便找回

    def __str__(self):
        return self.id
#------index.html
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
{% block body %}{% endblock %}
```

> 在当前请求中渲染获取或者仅仅下一个请求中可以获取

```python
# 添加闪现：（后面类型是可选择的）
flash('恭喜！验证成功','info')
flash('哈哈','error')
flash(username,'warning')
# 获取闪现内容：
get_flash_messages(with_categories=[True/False])
get_flashed_messages(category_filter=["error"]) 可选的
有针对性的的获取对应类型的闪现消息
```

> 如果想要闪现多一个选项，那么就要设置**with_categories=True**(默认为False)

#### 日志log

> uwsgi --> uwsgi.log

##### 创建日志

> 使用app自带的

```
app.logger.info()
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

> 通过logging进行创建

```
import logging
# 创建日志logging对象，默认flask的名字为app
logger=logging.getLogger(__name__)
```

##### 保存日志到文件

> **保存日志的方法1**

```
logging.basicConfig(filename='log.txt',filemode='a'，level=logging.WARNING,format='[%(asctime)s] %(name)s in %(module)s: %(message)s')
```

> **保存日志的方式2**

```
# 设置logger日志等级WARNING
logger.setLevel(level=logging.WARNING)
# 在设置等级以及之上的日志信息将被保存在'log.txt'当中
# 创建handler对象
handler = logging.FileHandler('log.txt')
# 设置handler日志等级INFO
handler.setLevel(level=logging.INFO)
# 设置输出格式
formatter = logging.Formatter('[%(asctime)s] %(name)s in %(module)s: %(message)s')
# 在设置等级以及之上的日志信息将被设定的格式输出
handler.setFormatter(formatter)
# 添加handler对象给记录器
logger.addHandler(handler)
```

> **保存日志的方式3**
>
> 使用`logger.info('message')`

#### API(restfull)

> 即Representational State Transfer的缩写。我对这个词组的翻译是"表现层状态转化"。

> 什么是RESTful框架:
>
> ①每一个URI代表一种资源
>
> > ## URI、URL和URN
> >
> > [统一资源定位符](https://baike.baidu.com/item/统一资源定位符/4438100)（Uniform Resource Locator，URL）,[统一资源名称](https://baike.baidu.com/item/统一资源名称/4437154)（Uniform Resource Name，URN）是URI的子集。
>
> ②客户端和服务器之间，传递这种资源的某种表现层
>
> > ## 表现层（Representation）
> >
> > "资源"是一种信息实体，它可以有多种外在表现形式。我们把"资源"具体呈现出来的形式，叫做它的"表现层"（Representation）。
>
> ③客户端通过四个HTTP动词(GET、POST、PUT、DELETE、[PATCH])，对服务器端资源进行操作，实现"表现层状态转化"。
>
> > ## GET、POST、PUT、DELETE
> >
> > GET用来获取资源，POST用来新建资源（也可以用于更新资源），PUT用来更新资源，DELETE用来删除资源。
>
> > ## 状态转化（State Transfer）
> >
> > 访问一个网站，就代表了客户端和服务器的一个互动过程。在这个过程中，势必涉及到数据和状态的变化。
> >
> > 互联网通信协议HTTP协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生"状态转化"（State Transfer）。而这种转化是建立在表现层之上的，所以就是"表现层状态转化"。

##### 前后端分离：

> 前端：app、小程序、pc页面
> 后端：没有页面，mtv(模型+模板+视图)  
> 				mv(模型+视图)
> 				模板的使用：跟原来的用法相同
> 				视图：api构建视图
>
> > ## 视图
> >
> > ```python
> > #①安装库
> > pip install flask-restful
> > 
> > #②创建api对象
> > api = Api(app=app) 
> > api = Api(app=蓝图对象)
> > 	
> > #③定义类视图：
> > from flask_restful import Resource
> > class xxxApi(Resource):
> > 	def get(self):
> > 		pass
> > 	……………………
> > #④绑定
> > api.add_resource(xxxApi.'/user')
> > ```
>
> > ## 路由
> >
> > ```python
> > @app.route('/user')
> > def user():			----> 视图函数
> > 	……
> > 	return response对象
> > 
> > ```
>
> ```python
> restful: ---> api ---> 接口 ---> 资源 ---> url
> 
> class xxx(Resource): ----> 类视图
> 	def get(self):
> 		pass
> 	………………
> 路径产生：
> api,add_resource(Resource的子类.'/user')
> api,add_resource(Resource的子类.'/user')
> api,add_resource(Resource的子类.'/user')
> ```

##### API返回

> 返回可解析对象(字符串、字典、元组……)

> 返回不可解析对象(自定义对象)
>
> > 定义API格式
> >
> > ```python
> > user_fields = {
> >        'id': fields.Integer,
> >        '用户名': fields.String(attribute='username',default='匿名')
> >    }
> >    ```
> 
> > 使用方法--装饰器
> >
>> ```python
> > @marshal_with(user_fields)
> > ```

> ## 定制fields(key)
>
> 客户端能可能到的时：id，用户名，密码，phone，datetime这五个key
> 默认key的名字是跟model中模型属性名一致，如果不想让前端看到命名，则可以修改
> 但必须结合attribute='模型的字段名'
>
> ## 定制fields(value)
>
> > 继承Raw
>
> ```python
> class IsDelete(fields.Raw):
> ```
>
> > 重写方法
>
> ```python
>     def format(self, value):
>         print(value)
>         return '删除' if value else '未删除'
> ```
>
> > 使用
>
> ```python
> user_fields = {
>     'isDelete': fields.Boolean(attribute='isdelete'), # 未自定义
>     'cn_isDelete': IsDelete(attribute='isdelete') # 自定义
> }
> ```

> ## URI
>
> > xxxlist  --->  点击具体的一个获取详情 ---->详情
>
> ```python
> user_fields_1 = {
>     'uri':fields.Url('single_user',absolute=True)
> }
> class UserSimpleResource(Resource):
>     @marshal_with(user_fields_1)
>     def get(self, id):
>         user = User.query.get(id)
>         return user
> api.add_resource(UserSimpleResource, "/user/<int:id>",endpoint="single_user")
> ```
>
> > 定义两个user_fields
> >
> > ①列表
> >
> > ②详情

> ## return data
>
> > 注意：data必须符合json格式
> >
> > ```python
> > {
> > 	'aa':10,
> > 	'bb':[
> > 		{
> > 			'id':1,
> > 			'xxs':[
> > 				{}
> > 			]
> > 		}
> > 	]
> > }
> > ```
> >
> > 如果直接返回不能有自定义对象User、Friend…………
> >
> > 如果有这种对象，需要：``marchal()``、`marchal_with()`帮助进行转换
> >
> > ```python
> > ①marchal(对象，对象的fields格式) # 对象的fields格式是指字典的输出格式
> >   marchal([对象，对象]，对象的fields格式)
> > ② marchak_with()作为装饰器修饰请求方法
> >    @marshal_with(user_fields_1)
> >     def get(self, id):
> >         user = User.query.get(id)
> >         return user
> >    参数 user_fields_1 ，类型：dict类型
> >    fields.Nested(fields.String) --> ['aa','bb']
> >    fields.Nested(user_fields_1) --> 按照user_fields_1的格式转换成user_fields_1对象
> > ```

##### API接收

> 单个参数
>
> > 通过添加API时，定义输入的参数`uid`
> >
> > ```python
> > class UserSimpleResource(Resource):
> >     @marshal_with(user_fields)
> >     def get(self, uid):
> >         users = User.query.get(uid)
> >         return users
> > api.add_resource(UserSimpleResource, "/user/<int:uid>")
> > ```
>
> > 多个参数
> >
> > ```python
> > # 参数解析
> > parser = reqparse.RequestParser(bundle_errors=True)  # 产生一个解析对象
> > parser.add_argument('username', type=str, required=True, help='必须输入用户名', location=["form"])
> > 
> > class UserResource(Resource):
> >     def post(self):
> >         args = parser.parse_args()
> >         username = args.get('username')
> >         print(username)
> > ```

##### 跨域·解决方案

> 跨域问题来源于JavaScript的“同源策略”，即只有 协议——主机名+端口号 (如存在)相同，则允许互相访问。也就是说JavaScript只能访问和操作自己域名下的资源，不能访问和操作其他域名下额资源。跨域问题只针对JS和ajax的，html本身没有跨域问题

> ## ①使用第三方扩展 flask-cors
>
> ```python
> form flask_cors import CORS
> cors = CORS()
> #与app绑定
> cors.init_app(app=app,suports_credentials=True)
> ```
>
> ## ②添加Header允许访问
>
> ```python
> response = make_response()
> # 允许所有来者访问
> response.headers['Acccess-Control-Allow-Origin'] = * 
> # 允许访问方式
> response.headers['Acccess-Control-Allow-Method'] = 'GET,POST'
> # 允许访问头
> response.headers['Acccess-Control-Allow-Header'] = 'x-requerst-with，Content-type'
> ```

##### 蓝图与API的使用

```
user_bp = Blueprint('user',__name__)
api = Api(user_bp)
class xxxApi(Resource):
	pass
api.add_resource(xxxApi,'/xxxx')
```

##### API与注册、登录

> ## 获取数据的方式
>
> ```python
> # 之前在视图里面使用 request.form or request.args 获取信息
> # 而在API中则是通过 创建参数解析-->再从参数中获取数据
> parser = reqparse.RequestParser(bundle_errors=True)
> parser.add_argument('name',type='类型 or 正则', help='不符合type则返回学校')
> 
> class xxApi(Resource):
> 	def post(self):
> 		args = parser.parse_args()
> 		name = args.get('name')
> ```
>
> ## 登录证明
>
> ```
> # session cookie cache（redis）
> # cache用法，具体用法搜索redis
> cache.set('name') # 写入
> cache.get() # 获取
> ```
>
> 

### 搭建到服务器上

> 虚拟环境`virtualenv`使用命令行`workon`进入虚拟环境
>
> 虚拟环境`Pipenv`使用命令行`pipenv shell `进入虚拟环境

#### Nginx服务器

> Flask内置的服务器，不建议使用，线程处理、并发量有限，所以部署网站就是用Nginx
>
> Nginx服务器的优点：轻量级、并发能力强、高度模块化、负载均衡、反向代理

#### 安装Nginx

> 使用管理工具安装
>
> 安装前的准备步骤，使用`yum repolist`，查看是否有`nginx`开头的源，没有就需要去配置[配置项看官方文档](http://nginx.org/en/linux_packages.html)
>
> 最好不要设置开机自启，因为后面使用时，需要按照其他配置文件运行

```shell
yum install epel-release
yum install nginx
systemctl enable nginx
systemctl start nginx
systemctl restart nginx
```

##### nginx控制

```
nginx
nginx -s stop
nginx -s quit
nginx -s reload
```

##### nginx配置文件

###### 配置文件结构

```shell
main						#全局设置
events {					#工作模式
	……
}
http{						#http的配置
	……
	upstream xxx{			#负载均衡配置
		……
	}
	server{					#主机设置
		……
		location xxx{		#URL匹配
			……
		}
	}
}
```

###### nginx配置文件-全局设置(main)

下面时一个main区域，他是一个全局的设置：

```
user nobody nobody;
worker_processes 2;
error_log  /usr/local/var/log/nginx/error.log  notice;
pid        /usr/local/var/run/nginx/nginx.pid;
worker_rlimit_nofile 1024;
```

> `user` 来指定Nginx Worker进程运行用户以及用户组，默认由nobody账号运行。
>
> `worker_processes`来指定了Nginx要开启的子进程数。每个Nginx进程平均耗费10M~12M内存。根据经验，一般指定1个进程就足够了，如果是多核CPU，建议指定和CPU的数量一样的进程数即可。我这里写2，那么就会开启2个子进程，总共3个进程。
>
> `error_log`用来定义全局错误日志文件。日志输出级别有debug、info、notice、warn、error、crit可供选择，其中，debug输出日志最为最详细，而crit输出日志最少。
>
> `pid`用来指定进程id的存储文件位置。
>
> `worker_rlimit_nofile`用于指定一个nginx进程可以打开的最多文件描述符数目，这里是65535，需要使用命令“ulimit -n 65535”来设置。

###### nginx配置文件-工作模式(events)

events模块来用指定nginx的工作模式和工作模式及连接数上限，一般是这样：

```
events {
    use kqueue; #mac平台
    worker_connections  1024;
}
```

> `use`用来指定Nginx的工作模式。Nginx支持的工作模式有select、poll、kqueue、epoll、rtsig和/dev/poll。其中select和poll都是标准的工作模式，kqueue和epoll是高效的工作模式，不同的是epoll用在Linux平台上，而kqueue用在BSD系统中，因为Mac基于BSD,所以Mac也得用这个模式，对于Linux系统，epoll工作模式是首选。
>
> `worker_connections`用于定义Nginx每个进程的最大连接数，即接收前端的最大请求数，默认是1024。最大客户端连接数由`worker_processes`和`worker_connections`决定，即`Max_clients=worker_processes*worker_connections`，在作为反向代理时，Max_clients变为：`Max_clients = worker_processes * worker_connections/4`。 
> 进程的最大连接数受Linux系统进程的最大打开文件数限制，在执行操作系统命令“ulimit -n 65536”后worker_connections的设置才能生效。

###### nginx配置文件-http的设置

http模块可以说是最核心的模块了，它负责HTTP服务器相关属性的配置，它里面的server和upstream子模块，至关重要，等到反向代理和负载均衡以及虚拟目录等会仔细说。

```
http{
    include       mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /usr/local/var/log/nginx/access.log  main;
    sendfile        on;
    tcp_nopush      on;
    tcp_nodelay     on;
    keepalive_timeout  10;
    #gzip  on;
    upstream myproject {
        .....
    }
    server {
        ....
    }
}
```

> 下面详细介绍下这段代码中每个配置选项的含义。 
> `include` 来用设定文件的mime类型,类型在配置文件目录下的mime.type文件定义，来告诉nginx来识别文件类型。
>
> `default_type`设定了默认的类型为二进制流，也就是当文件类型未定义时使用这种方式，例如在没有配置asp 的locate 环境时，Nginx是不予解析的，此时，用浏览器访问asp文件就会出现下载了。
>
> `log_format`用于设置日志的格式，和记录哪些参数，这里设置为``main`，刚好用于`access_log`来纪录这种类型。
>
> main的类型日志如下：也可以增删部分参数。
>
> ```
> 127.0.0.1 - - [21/Apr/2015:18:09:54 +0800] "GET /index.php HTTP/1.1" 200 87151 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36"
> ```
>
> `access_log` 用来纪录每次的访问日志的文件地址，后面的`main`是日志的格式样式，对应于`log_format`的`main`。
>
> `sendfile`参数用于开启高效文件传输模式。将tcp_nopush和tcp_nodelay两个指令设置为on用于防止网络阻塞。
>
> `keepalive_timeout`设置客户端连接保持活动的超时时间。在超过这个时间之后，服务器会关闭该连接。
>
> 还有很多各种配置，以后等用到来再说。

###### nginx配置文件-主机设置(server)

sever 模块是http的子模块，它用来定一个虚拟主机，我们先讲最基本的配置，这些在后面再讲。

我们看一下一个简单的server 是如何做的？

```
server {
        listen       8080;
        server_name  localhost 192.168.12.10 www.yangyi.com;
        # 全局定义，如果都是这一个目录，这样定义最简单。
        root   /Users/yangyi/www;
        index  index.php index.html index.htm; 
        charset utf-8;
        access_log  usr/local/var/log/host.access.log  main;
        aerror_log  usr/local/var/log/host.error.log  error;
        ....
}
```

> `server`标志定义虚拟主机开始。 
> `listen`用于指定虚拟主机的服务端口。 
> `server_name`用来指定IP地址或者域名，多个域名之间用空格分开。 
> `root` 表示在这整个`server`虚拟主机内，全部的root web根目录。注意要和`locate {}`下面定义的区分开来。 
> `index `全局定义访问的默认首页地址。注意要和``locate {}``下面定义的区分开来。 
> `charset`用于设置网页的默认编码格式。 
> `access_log`用来指定此虚拟主机的访问日志存放路径，最后的main用于指定访问日志的输出格式。

###### nginx配置文件-URL匹配(location)

location模块是nginx中用的最多的，也是最重要的模块了，什么负载均衡啊、反向代理啊、虚拟域名啊都与它相关。慢慢来讲：

location 根据它字面意思就知道是来定位的，定位URL，解析URL，所以，它也提供了强大的正则匹配功能，也支持条件判断匹配，用户可以通过location指令实现Nginx对动、静态网页进行过滤处理。像我们的php环境搭建就是用到了它。

我们先来看这个，设定默认首页和虚拟机目录。

```
location / {
            root   /Users/yangyi/www;
            index  index.php index.html index.htm;
        }
```

`location /`表示匹配访问根目录。

`root`指令用于指定访问根目录时，虚拟主机的web目录，这个目录可以是相对路径（相对路径是相对于nginx的安装目录）。也可以是绝对路径。

`index`用于设定我们只输入域名后访问的默认首页地址，有个先后顺序：`index.php index.html index.htm`，如果没有开启目录浏览权限，又找不到这些默认首页，就会报403错误。

location 还有一种方式就是正则匹配，开启正则匹配这样：`location ~`。后面加个`~`。

下面这个例子是运用`正则匹配`来链接php。我们之前搭建环境也是这样做：

```
location ~ \.php$ {
            root           /Users/yangyi/www;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            include        fastcgi.conf;
        }
```

`\.php$` 熟悉正则的我们直到，这是匹配`.php`结尾的URL，用来解析`php`文件。里面的root也是一样，用来表示虚拟主机的根目录。 
`fast_pass`链接的是`php-fpm` 的地址，之前我们也搭建过。其他几个参数我们以后再说

location 还有其他用法，等讲到实例的时候，再看吧。

###### nginx配置-负载均衡设置(upstrean)

upstream 模块负债负载均衡模块，通过一个简单的调度算法来实现客户端IP到后端服务器的负载均衡。我先学习怎么用，具体的使用实例以后再说。

```
upstream iyangyi.com{
    ip_hash;
    server 192.168.12.1:80;
    server 192.168.12.2:80 down;
    server 192.168.12.3:8080  max_fails=3  fail_timeout=20s;
    server 192.168.12.4:8080;
}
```

在上面的例子中，通过``upstream`指令指定了一个负载均衡器的名称`iyangyi.com`。这个名称可以任意指定，在后面需要的地方直接调用即可。

里面是``ip_hash`这是其中的一种负载均衡调度算法，下面会着重介绍。紧接着就是各种服务器了。用`server`关键字表识，后面接ip。

Nginx的``负载均衡``模块目前支持``4种调度算法``:

> `weight` 轮询（默认）。每个请求按时间顺序逐一分配到不同的后端服务器，如果后端某台服务器宕机，故障系统被自动剔除，使用户访问不受影响。weight。指定轮询权值，weight值越大，分配到的访问机率越高，主要用于后端每个服务器性能不均的情况下。
> `ip_hash`。每个请求按访问IP的hash结果分配，这样来自同一个IP的访客固定访问一个后端服务器，有效解决了动态网页存在的session共享问题。
> `fair`。比上面两个更加智能的负载均衡算法。此种算法可以依据页面大小和加载时间长短智能地进行负载均衡，也就是根据后端服务器的响应时间来分配请求，响应时间短的优先分配。Nginx本身是不支持fair的，如果需要使用这种调度算法，必须下载Nginx的upstream_fair模块。
> `url_hash`。按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，可以进一步提高后端缓存服务器的效率。Nginx本身是不支持url_hash的，如果需要使用这种调度算法，必须安装Nginx 的hash软件包。

在HTTP Upstream模块中，可以通过server指令指定后端服务器的IP地址和端口，同时还可以设定每个后端服务器在负载均衡调度中的状态。常用的状态有：

> `down`，表示当前的server暂时不参与负载均衡。
> `backup`，预留的备份机器。当其他所有的非backup机器出现故障或者忙的时候，才会请求backup机器，因此这台机器的压力最轻。
> `max_fails`，允许请求失败的次数，默认为1。当超过最大次数时，返回proxy_next_upstream 模块定义的错误。
> `fail_timeout`，在经历了max_fails次失败后，暂停服务的时间。max_fails可以和fail_timeout一起使用。
> 注意 当负载调度算法为ip_hash时，后端服务器在负载均衡调度中的状态不能是weight和backup。

##### 完整的nginx配置文件

```
#user administrator administrators;  #配置用户或者组，默认为nobody nobody。
#worker_processes 2;  #允许生成的进程数，默认为1

pid /var/log/nginx/nginx.pid;   #指定nginx进程运行文件存放地址
error_log /var/log/error.log warn;  #制定日志路径，级别。这个设置可以放入全局块，http块，server块，级别以此为：debug|info|notice|warn|error|crit|alert|emerg

events {
    #accept_mutex on;   #设置网路连接序列化，防止惊群现象发生，默认为on
    #multi_accept on;  #设置一个进程是否同时接受多个网络连接，默认为off
    #use epoll;      #事件驱动模型，select|poll|kqueue|epoll|resig|/dev/poll|eventport
    worker_connections  1024;    #最大连接数，默认为512
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    #access_log off; #取消服务日志    
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';
                  
    access_log /var/log/access.log main;  #combined为日志格式的默认值
    sendfile on;   #允许sendfile方式传输文件，默认为off，可以在http块，server块，location块。
    #sendfile_max_chunk 100k;  #每个进程每次调用传输数量不能大于设定的值，默认为0，即不设上限。
    keepalive_timeout 65;  #连接超时时间，默认为75s，可以在http，server，location块。
    #upstream mysvr {   
    #  server 127.0.0.1:7878;
    #  server 192.168.10.121:3333 backup;  #热备
     #}
    #error_page 404 https://www.baidu.com; #错误页
    
    server {
    	listen	80;
    	server_name	localhost;
    	
    	root /root/myproject/flaskblog;
    	
    	location /static {
    		alias /root/myproject/flaskblog/static;
    	}
    	
    	location / {
    		root /etc/nginx/uwsqi_params;
    		uwsgi_pass localhost:8080;
    	}
    	error_page 500 502 503 504 /50x.html;
    	location = /50x.html {
    		root /usr/share/nginx/html;
    	}
    } 
}
```

#### 安装python

##### 1.安装相应的编译工具

在root用户下(不要用普通用户,麻烦),全部复制粘贴过去,一次性安装即可.

```shell
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum install -y libffi-devel zlib1g-dev
yum install zlib* -y
```

##### 2.下载安装包

```shell
wget wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
```

##### 3.解压

```shell
tar -xvJf  Python-3.7.2.tar.xz
```

##### 4.创建编译安装目录

```shell
mkdir /usr/local/python3 
```

##### 5.安装

```shell
cd Python-3.7.2
./configure --prefix=/usr/local/python3 --enable-optimizations --with-ssl 
#第一个指定安装的路径,不指定的话,安装过程中可能软件所需要的文件复制到其他不同目录,删除软件很不方便,复制软件也不方便.
#第二个可以提高python10%-20%代码运行速度.
#第三个是为了安装pip需要用到ssl,后面报错会有提到.
make && make install
```

[what-does-enable-optimizations-do-while-compiling-python](https://stackoverflow.com/questions/41405728/what-does-enable-optimizations-do-while-compiling-python)

##### 6.创建软链接

```shell
ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3
```

##### 7.验证是否成功

```shell
python3 -V
pip3 -V | pip3 --version
# 失败就重新配置软连接
python -V
pip -V | pip --version
# 失败就重新下载
yum install -y epel-release
yum install -y python-pip
# 安装完后继续验证
```

##### 8.报错处理

错误1.

```bash
zipimport.ZipImportError: can't decompress data; zlib not available Makefile:1099: recipe for target 'install' failed make: *** [install] Error 1
```

需要安装依赖

```bash
yum -y install zlib1g-dev
```

错误2.

```bash
ModuleNotFoundError: No module named '_ctypes'
```

需要安装依赖

```bash
yum -y install libffi-devel 
```

这两个错误需要的依赖已经添加到一开始的依赖安装上去了
[参考文章](https://blog.csdn.net/elija940818/article/details/79238813)

##### 9.安装pipenv

在centos中使用python3.7或以上版本,进行pip install 命令容易报错

```bash
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https:*******: There was a problem confirming the ssl certificate: 
Can't connect to HTTPS URL because the SSL module is not available. - skipping
```

**在./configure过程中，如果没有加上–with-ssl参数时，默认安装的软件涉及到ssl的功能不可用，刚好pip3过程需要ssl模块，而由于没有指定，所以该功能不可用。解决办法是重新对python3.6进行编译安装，用一下过程来实现编译安装:**

```bash
cd Python-3.7.2
./configure --with-ssl
make && make install
```

即可正常使用pip安装.
这个也在安装python的时候指定了.

> 假如安装完`pipenv`后使用时，出现`pipenv: 未找到命令`

```bash
# 找到pipenv的位置
find / -name "pipenv"
# 创建软连接
ln -s /usr/local/python3/bin/pipenv /usr/bin/pipenv
```

> `/usr/local/python3/bin/pipenv`是我`pipenv`的目录位置
>
> 另外在使用`find`命令时出现，`find: ‘/run/user/1000/gvfs’: 权限不够`这个只是一个BUG

```bash
umount /run/user/1000/gvfs    // 卸载该文件
rm -rf /run/user/1000/gvfs    // 删除该文件
```

##### 10.修改pip安装源

修改系统pip安装源
在家目录下新建`.pip`文件夹,进入文件夹新建文件`pip.conf`之后写入相应镜像网站地址

```shell
cd ~
mkdir .pip
cd .pip
vim pip.conf

#进入后添加以下内容,保存退出.
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
```

修改pipenv安装源
在自己的虚拟环境中找到`Pipfile`文件,将其中的`url = "https://pypi.org/simple"`修改为你需要的国内镜像,如`https://mirrors.aliyun.com/pypi/simple/`

```shell
[root@localhost myproject]# vim Pipfile 


[[source]]
name = "pypi"
url = "https://pypi.org/simple" # 改为url = "https://mirrors.aliyun.com/pypi/simple/"
verify_ssl = true

[dev-packages] #这里是开发环境专属包,使用pipenv install --dev package来安装专属开发环境的包

[packages] # 全部环境的通用包,安装在这里.

[requires]
python_version = "3.7"
```

#### 安装MySQL

> 在CentOS中默认安装有MariaDB，这个是MySQL的分支，但为了需要，还是要在系统中安装MySQL，而且安装完成之后可以直接覆盖掉MariaDB。

##### 下载并安装MySQL官方的 Yum Repository

```
wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql-community-server
```

##### MySQL数据库配置

```
# 启动MySQL数据库
systemctl start mysqld.service
# 查看运行状态
systemctl status mysqld.service
# 获取MySQL默认密码
grep "password" /var/log/mysqld.log
# 会打印出 [Note] A temporary password is generated for root@localhost:&&&
# &&&的位置就是临时密码
```

**进入数据库后，修改密码**

```
mysql>  ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
```

> 其中`new password`替换成你要设置的密码，注意:密码设置必须要大小写字母数字和特殊符号（,/';:等）,不然不能配置成功

###### 将数据库密码修改成弱密码的方法

> 首先你完成上一步，不然无法修改密码策略【好像是这样的】

```sql
# 设置密码策略为弱密码，但是现在还不能设置成123456，应为当前最小位数为8位
mysql> set global validate_password_policy=0;
Query OK, 0 rows affected (0.00 sec)
# 设置密码最小位数为4，无论你设置成1、2、3，最低长度都是 4
mysql> set global validate_password_length=4;
Query OK, 0 rows affected (0.00 sec)
# 设置MySQL密码
mysql> ALTER USER USER() IDENTIFIED BY '123456';
Query OK, 0 rows affected (0.05 sec)
```

##### 开启mysql的远程访问

> 执行以下命令开启远程访问限制（注意：下面命令开启的IP是 192.168.0.1，如要开启所有的，用%代替IP）：
>
> 如果这里也想用弱密码开启的话，方法和上面一样

```shell
mysql> grant all privileges on *.* to 'root'@'192.168.0.1' identified by '123456' with grant option;
mysql> flush privileges; 
mysql> exit
```

##### 为firewalld（防火墙）添加开放端口

> 添加mysql端口3306和Tomcat端口8080

```shell
firewall-cmd --zone=public --add-port=3306/tcp --permanent
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
```

##### 更改mysql的语言，设置成utf8mb4

> 进入数据库

```sql
mysql> status
```

> 查看`Server characterset`和`Db     characterset`是不是`utf-8`
>
> 如果不是的话

```shell
vi /etc/my.cnf
```

> `[client]`和`[mysql]`手动添加

```shell
[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
init_connect='SET NAMES utf8mb4'
```

> 记得要查看一下，配置是否生效

```sql
mysql> SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
+--------------------------+--------------------+
| Variable_name            | Value              |
+--------------------------+--------------------+
| character_set_client     | utf8mb4            |
| character_set_connection | utf8mb4            |
| character_set_database   | utf8mb4            |
| character_set_filesystem | binary             |
| character_set_results    | utf8mb4            |
| character_set_server     | utf8mb4            |
| character_set_system     | utf8               |
| collation_connection     | utf8mb4_unicode_ci |
| collation_database       | utf8mb4_unicode_ci |
| collation_server         | utf8mb4_unicode_ci |
+--------------------------+--------------------+
```

> 最后记得重启数据库`systemctl restart mysqld`

#### 安装redis

##### 1.安装gcc依赖

```shell
yum install -y gcc 
```

##### 2.下载并解压安装包以及编译

> 请看清文件下载并解压的位置，后面有要用到
>
> 自身位置获取的方法：
>
> ①从命令行的前面就可以看出所处的位置`[root@localhost local]`，这里就是在名为`local`的位置
>
> ②使用`pwd`

```shell
wget http://download.redis.io/releases/redis-5.0.3.tar.gz
tar -zxvf redis-5.0.3.tar.gz
cd redis-5.0.3
make
```

##### 3.安装指定安装目录

```shell
make install PREFIX=/usr/local/redis
```

##### 4.启动服务并设置为后台启动

###### 4.1前台启动

```shell
cd /usr/local/redis/bin/
./redis-server
```

###### 4.2后台启动

> 注意：这里就要用到之前所说的**位置** ====> **源码目录**
>
> 从 redis 的源码目录中复制 redis.conf 到 redis 的安装目录

```shell
cp /usr/local/redis-5.0.3/redis.conf /usr/local/redis/bin/
```

> 修改 redis.conf 文件，把 **daemonize no** 改为 **daemonize yes**

```shell
vi redis.conf
```

> 记住在esc状态下，输入`/daemonize no`可以快速的找到位置

> 后台启动测试

```shell
./redis-server redis.conf
ps -ef |grep redis
```

##### 5.设置开启自启

> 添加开机启动服务配置

```
vi /etc/systemd/system/redis.service
```

> 在文件中添加一下内容
>
> 如果你的安装路径和我之前写的路径不一致，那么`[Service]`下的`ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/bin/redis.conf`需要修改成你自己的软件安装路径

```
[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/bin/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

> 配置完成后，设置开机自启

```
systemctl daemon-reload
systemctl start redis.service
systemctl enable redis.service
```

##### 6.设置软连接

```shell
ln -s /usr/local/redis/bin/redis-cli /usr/bin/redis
```

> 设置完成后，输入`redis`进行测试

#### 开始使用`pycharm`进行连接

##### 1.配置远程服务器Deployment

> tools->Deployment->configuration
>
> 选择SFTP模式

##### 2.配置Python解释器

> 方法一：在创建项目时进行配置【File->New Project->Existing interpreter】
>
> 方法二：在创建项目之前进行配置【File->Settings->Pycharm->Preferences】
>
> 如果是配置Python虚拟环境，需要找到创建的虚拟Python环境下的Python文件【文件位置类似于：/root/.virtualenvs/flask_blog/bin/python】

##### 3.设置代码自动在服务器上进行同步

> tools->Deployment->Options
>
> 2020.2版本：
>
> 【Upload changed fles atomatially to the defut server】选择Always即可
>
> 2020.2版本之前的版本：
>
> 还要记得打钩【Upload external changes】

##### 4.快速完成依赖库的配置

```shell
# 导出依赖库的信息到 requirements.txt 文件中
pip freeze > requirements.txt
# 读取 requirements.txt 中依赖库的信息并安装
pip install -r requirements.txt

# 删除依赖库
# 1.删除全部python依赖库
pip freeze | xargs pip uninstall -y
# 2.如果您通过VCS安装了软件包，则需要排除这些行并手动删除软件包（从下面的注释中升高）：
pip freeze | grep -v "^-e" | xargs pip uninstall -y
# 3.当然导出到文件后，在读取文件来删除依赖库也可以
pip freeze > requirements.txt
pip uninstall -r requirements.txt
```

##### 5.多半需要修改的文件

> `settings.py`(Flask的配置文件)

```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskblog'
# 注意数据库名称、数据库引擎、用户名、密码、数据库地址、端口、库的名称
```

#### Flask项目部署

##### 1.安装uwsgi

```shell
pip3 install uwsgi
```

##### 2.配置uwsgi

```
-------------file path：uwsgi.ini--------
[uwsgi] # 这里必须要两个，不然会报错，当然可以先试试一个，会不会报错，报错再添
[uwsgi]
# 这个是和Nginx服务器连接时使用的，也许其他的服务器也可以
# 这里的值要和Nginx配置文件中的值要一致
#socket=localhost:8080

# 端口（使用nginx连接时，使用socket，直接做web服务器，使用http）
http=0.0.0.0:8080

# 项目目录
chdir=/root/myproject/flaskblog

# 指定Python解释器包(库)位置
env=/root/.virtualenvs/flask_blog/lib/python3.7/site-packages

# 指定项目的application的位置
# 如果用%(chdir)/app.py来写位置的话，会报错
#module =app.py
wsgi-file=/root/myproject/flaskblog/app.py

# flask应用实例的名称，是flask独有的配置项（django不需要）。由于flask存在特殊的机制，可以实例化多个application，需要明确指出，收到请求时，uwsgi应该调用哪个应用实例。
callable=app

# 启用主进程
master=true

# 修改解析数据包大小的限制
buffer-size = 65536

# 自动移除unixSocket和pid文件当服务停止的时候
vacuum=true

# 序列化接受的内容，如果可能的话
thunder-lock=true

# 设置启动用户
# uid=root

# 进程数
processes=4

#线程
threads=10

#pidfile文件
pidfile=%(chdir)/uwsgi.pid

#记录日志
daemonize=%(chdir)/uwsgi.log
```

> 如果查看`uwsgi.log`文件，里面会显示一下错误：
>
> ```
> # 这一条的话，解决不了，也没啥大问题，最后成不成，还是要看网页是否可以打开
> WSGI app 0 (mountpoint='') ready in 3 seconds on interpreter 0xf20e70 pid: 3140 (default app)
> # 这一条可以解决，就是让你在uwsgi.ini文件中设置uid的值
> uWSGI running as root, you can use --uid/--gid/--chroot options
> ```
>
> **启动uwsgi**
>
> ```
> uwsgi --ini /root/myproject/flaskblog/uwsgi.ini
> ```
>
> 启动时最好使用绝对定位，相对定位不靠谱

##### 3.配置Nginx

> 这时记得修改`uwsgi.ini`文件，将配置项http注释掉，配置socket的值

```
user  root;
#nginx进程，一般数值为cpu核数
worker_processes 1;
#错误日志存放目录
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;
error_log /var/log/nginx/error.log warn;
#进程pid存放位置
pid /var/log/nginx.pid;

#工作模式及连接数上限
events {
  #单个后台worker process进程的最大并发链接数
  worker_connections 1024;
}


http {
  #文件扩展名与类型映射表
  include /etc/nginx/mime.types;
  #默认文件类型
  default_type application/octet-stream;
  #设置日志模式
  log_format main '$remote_addr - $remote_user [$time_local] "$request" '
  '$status $body_bytes_sent "$http_referer" '
  '"$http_user_agent" "$http_x_forwarded_for"';
  #nginx访问日志
  access_log /var/log/nginx/access.log main;
  #开启高效传输模式
  sendfile on;
  #激活tcp_nopush参数可以允许把httpresponse header和文件的开始放在一个文件里发布， 积极的作用是减少网络报文段的数量
  #tcp_nopush     on;
  #连接超时时间，单位是秒
  #keepalive_timeout  0;
  keepalive_timeout 65;
  #开启gzip压缩功能
  #gzip on;

  #基于域名(本地)的虚拟主机
  server {
    #监听端口,记得开端口
    listen 80;
    server_name localhost;

    root /root/myproject/flaskblog;

    location /static {
      #配置静态文件
      alias /root/myproject/flaskblog/static;
    }

    location / {
      #引入uwsgi_params文件;
      include /etc/nginx/uwsgi_params;
      #主机
      uwsgi_pass localhost:8080;
      uwsgi_param UWSGI_PYHOME /root/.virtualenvs/flask_blog/lib/python3.7/site-packages;
      uwsgi_param UWSGI_CHDIR /root/myproject/flaskblog; #项目根目录
      uwsgi_param UWSGI_SCRIPT flaskblog.app;
    }
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
      root /usr/share/nginx/html;
    }
  }
}
```

> 检查配置文件是否正确
>
> ```shell
> # 检查指定配置文件
> nginx -t -c /root/myproject/flaskblog/nginx.conf
> # 检查默认配置文件
> nginx -t
> ```

##### 启动nginx

```
nginx -c /root/myproject/flaskblog/nginx.conf
# 可能还需要重启uwsgi
uwsgi --reload /root/myproject/flaskblog/uwsgi.pid
```

#### 虚拟机的疑难杂症

##### 安装wget失败，提示`Could not resolve host mirrorlist.centos.org`（无法解析host）

方法一：虚拟网络编辑器还原默认值

方法二：修改`/etc/sysconfig/network-scripts/ifcfg-ens33`

```
TYPE=Ethernet
PROXY_ME_THOD=none
BROWSER_ONLY=no
BOOTPROTO-dhcp
DEF_ROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens 33
UID=5b315f91-4a6c-498C-abc9-9e8525bc2fbd # 这一条不用管
ONBOOT=yes
IPADDR=192.168.1.11
PREFIX=24
GATEWAY=192.168.1.1
DNS1=198.168.1.1
IPV6_PRIVACY=no
```

> 记得还要重启网络服务
>
> systemctl start network.service
>
> 或者
>
> service network restart

方法三：重新安装

#### 启动nginx、uwsgi的二三事

##### 关于uwsgi的二三事

> uwsgi.ini文件中不可以有(包含空格的)空行，会报错。报错，端口依旧会占用，使用以下命令：
>
> ```
> # 获取占用端口的进程信息
> netstat -pan | grep 端口
> # 杀掉进程
> kill -9 pid(进程id)
> ```
>
> 这样才能继续使用启动命令。

> 有问题就看uwsgi.log

### 本地Flask服务器上的请求缓慢

#### 原因

> 在支持ipv6的操作系统上进行配置，如现代Linux系统，OS X 10.4或更高版本以及Windows Vista，如果访问本地服务器，某些浏览器可能会非常慢。原因是有时候localhost被配置为在ipv4和ipv6 socktes上可用，一些浏览器将尝试首先访问ipv6，然后尝试访问ivp4。

#### 解决方法

> windows下的方法：
>
> 打开hosts文件将下面这些
>
> ```hosts
> # localhost name resolution is handled within DNS itself.
> #	127.0.0.1       localhost
> #	::1             localhost
> ```
>
> 改成
>
> ```hosts
> # localhost name resolution is handled within DNS itself.
> #	127.0.0.1       localhost
> 	::1             localhost
> ```
>
> 就可以解决本地服务请求缓慢的问题