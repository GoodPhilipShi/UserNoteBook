---
title: Mind+在线服务相关
date created: 星期一, 一月 30日 2023, 8:53:56 早上
date modified: 星期一, 一月 30日 2023, 9:03:48 上午
---

# Mind+ 在线服务相关

> 须知:

> ​	SSH 账号: root
>
> ​	SSH 密码: Hid***\*\*\*t5353
>
> ​	包括: 语音识别、AI 图像识别、TinyWebDB、部分天气服务 (Nginx 反代)、当前服务器的 SSL 证书、跨域

> ​	SSH 账号: mindplus
>
> ​	SSH 密码: hid***\*\*\*t
>
> ​	包括: 主要天气服务程序、用户统计 (谷歌、百度)、mindplus 的 IDE、蓝牙、备案、当前服务器的 SSL 证书、跨域

## 天气服务

> 请求连接: <https://statistic.dfrobot.top/online/api/weather?appid=&appsecret=&user=df&city=%E6%88%90%E9%83%BD&version=v6&vue=1> 

### Nginx 反代

/etc/nginx/nginx.config

```
include ./conf/statistic.conf;
```

/etc/nginx/conf/statistic.conf

```
location /online/api/weather {
      proxy_pass  http://server.mindplus.top/api/weather;
}
```

> 追更溯源
>
> server.mindplus.top  --->  49.234.196.11

/etc/nginx/nginx.config

```
server {
    listen      80;
    server_name  server.mindplus.top;
    #charset koi8-r;
    #access_log  logs/host.access.log  main;
      set $cors_origin "";
    if ($http_origin ~* "^https://ide.mindplus.top$") {
            set $cors_origin $http_origin;
    }
    if ($http_origin ~* "^http://localhost:8601") {
            set $cors_origin $http_origin;
    }
    add_header Access-Control-Allow-Origin $cors_origin;
    location / {
	    proxy_redirect off;
        proxy_pass  http://127.0.0.1:5665;
      	add_header Access-Control-Allow-Origin  $cors_origin;
    }
}
```

### 旧版源代码 1(ip: 47.75.240.161)

/home/dfrobot/go/src/mindplus_statistic/controllers/webconfig:56

```go
server_config["weather"] = "https://www.tianqiapi.com/api/"
```

/home/dfrobot/go/src/mindplus_statistic/controllers/online.go:149

```go
func (c *OnlineController) Weather() {

	// c.Ctx.ResponseWriter.Header().Set("Access-Control-Allow-Origin", c.Ctx.Request.Header.Get("Origin"))

	city := c.Input().Get("cityid")
	url := GetConfig("weather")

	fmt.Println(url)
	// var token_arr map[string]string
	// 读取参数

	req_twice := httplib.Get(url)
	// 账号和秘钥在http://www.tianqiapi.com/?action=v1 申请获取
	req_twice.Param("appid", "29549952")
	req_twice.Param("appsecret", "2WngPSdn")
	req_twice.Param("cityid", city)
	req_twice.Param("version", "v6")
	req_twice.Param("vue", "1")
	str, err := req_twice.String()

	if err != nil {
	    // t.Fatal(err)
		fmt.Println("weather error== ",err)
		// req_twice.Debug("baiduTokenServer error== ",err)
	}

	c.Ctx.WriteString(str)
	// 获取前端传递的参数
}
```

### 旧版源代码 2(ip: 49.234.196.11)

> 增加了自定义功能

/home/mindplus/program/mindplus_weather/controllers/weather.go:52

```go
func (c *WeatherController) Weather() {
  // c.Ctx.ResponseWriter.Header().Set("Access-Control-Allow-Origin", c.Ctx.Request.Header.Get("Origin"))

  city := c.Input().Get("cityid")
  cityname := c.Input().Get("cityname")
  url := GetConfig("weather")

  appid  := c.Input().Get("appid")
  //? c.Input().Get("appid") : "29549952"
  appsecret := c.Input().Get("appsecret")
  user := c.Input().Get("user")
  //? c.Input().Get("appsecret") : "2WngPSdn"

  if(appid == "" || user == "df"){
    appid = "29549952"
  }

  if(appsecret == "" || user == "df"){
    appid = "2WngPSdn"
  }

  // var token_arr map[string]string
  // 读取参数

  cached_id := GetCachedData(city)
  cached_name := GetCachedData(cityname)
  fmt.Println("cached_id===", cached_id, cached_name)

  if cached_id != "" {
    c.Ctx.WriteString(cached_id)
    fmt.Println("using cache")
    return
  }

  if cached_name != "" {
    c.Ctx.WriteString(cached_name)
    fmt.Println("using cache")
    return
  }

  // cached_name
  fmt.Println("url===", url)
  req_twice := httplib.Get(url)
  // 账号和秘钥在http://www.tianqiapi.com/?action=v1 申请获取
  req_twice.Param("appid", appid)
  req_twice.Param("appsecret", appsecret)
  req_twice.Param("cityid", city)
  req_twice.Param("city", cityname)
  req_twice.Param("version", "v6")
  req_twice.Param("vue", "1")
  str, err := req_twice.String()

  // SetCachedData(city || cityname, str)
  if err != nil {
    fmt.Println("weather error== ",err)
    c.Ctx.WriteString("500")
    return
  }


  var coll map[string]interface{}
  if err := json.Unmarshal([]byte(str), &coll); err == nil {
      fmt.Println("==============json str 转map=======================")
      // fmt.Println(coll)
      if city != ""{
        SetCachedData(city, str)
      }else{
        // 当请求为城市名，根据返回的城市ID再保存一次数据，避免下一次相同的请求
        SetCachedData(cityname, str)
        // fmt.Println("cached id=====",coll["cityid"][0:6])
        id_inner := coll["cityid"]
        // SetCachedData(id_inner, str)
        fmt.Println("city_id======", id_inner)
      }
  }
  c.Ctx.WriteString(str)
}
```

### 新版源代码 (ip: 49.234.196.11)

/home/ubuntu/go/src/mindplus_weather/controllers/webconfig:57

```go
server_config["weather"] = "http://www.yiketianqi.com/api/"
```

/home/ubuntu/go/src/mindplus_weather/controllers/weather.go:76

```go
func (c *WeatherController) Weather() {
  // c.Ctx.ResponseWriter.Header().Set("Access-Control-Allow-Origin", c.Ctx.Request.Header.Get("Origin"))
  var completeWeather WeatherInfo
  var simpleWeather WeatherInfoSimple

  city := c.Input().Get("cityid")
  cityname := c.Input().Get("city")
  simple := c.Input().Get("simple")
  url := GetConfig("weather")
  if cityname == "" {
    cityname = c.Input().Get("cityname")
  }


  appid := c.Input().Get("appid")
  appsecret := c.Input().Get("appsecret")
  user := c.Input().Get("user")

  if((appid == "" || appsecret == "") && user != "df"){
    c.Ctx.WriteString("{\"errcode\":501,\"errmsg\":\"账号信息不完整，请检查后再输入\"}")
    return
  }
  if(appid == "" && user == "df"){
    appid = defaultAccount
  }
  if(appsecret == "" && user == "df"){
    appsecret = defaultPasswd
  }
  if(city == "" && cityname == ""){
    c.Ctx.WriteString("{\"errcode\":404,\"errmsg\":\"城市不能为空\"}")
    return
  }

  // 读取参数
  cached_id := GetCachedData(city)
  cached_name := GetCachedData(cityname)
  // fmt.Println("cached_id===", cached_id, cached_name)


  if cached_id != "" {
    if simple != "" {
      json.Unmarshal([]byte(cached_id), &simpleWeather)
      weather_simple, _ := json.Marshal(simpleWeather)
      c.Ctx.WriteString(string(weather_simple))
    }else{
      c.Ctx.WriteString(cached_id)
    }
    fmt.Println("using cache")
    return
  }
  if cached_name != "" {
    if simple != "" {
      json.Unmarshal([]byte(cached_name), &simpleWeather)
      weather_simple, _ := json.Marshal(simpleWeather)
      c.Ctx.WriteString(string(weather_simple))
    }else{
      c.Ctx.WriteString(cached_name)
    }
    fmt.Println("using cache")
    return
  }

  // cached_name
  fmt.Println("url===", url, appid, city, cityname)
  req_twice := httplib.Get(url)
  // 账号和秘钥在http://www.tianqiapi.com/?action=v1 申请获取
  req_twice.Param("appid", appid)
  req_twice.Param("appsecret", appsecret)
  req_twice.Param("cityid", city)
  req_twice.Param("city", cityname)
  req_twice.Param("version", "v6")
  req_twice.Param("vue", "1")
  str, err := req_twice.String() //发送请求
  fmt.Println("cached name=====",appid, appsecret)

  // SetCachedData(city || cityname, str)
  if err != nil {
    fmt.Println("weather error== ",err)
    c.Ctx.ResponseWriter.WriteHeader(500)
    return
  }

  if err := json.Unmarshal([]byte(str), &completeWeather); err == nil {
      fmt.Println("==============json str 转map=======================")
      name_inner := completeWeather.City
      id_inner := completeWeather.Cityid
      // 当请求为城市名，根据返回的城市ID再保存一次数据，避免下一次相同的请求
      // 判断返回信息中是否存在错误提示，有错误提示时不缓存
      // fmt.Println("cached id=====",completeWeather["cityid"][0:6])
      // 请求城市与返回城市不一致时，返回错误
      fmt.Println("cached id=====",name_inner, id_inner, cityname, city)

      if name_inner != "" {
        if((name_inner != cityname && cityname != "") || (id_inner != city && city != "")) {
           fmt.Println("city is wrong ")
           // c.Ctx.ResponseWriter.WriteHeader(500)
           c.Ctx.WriteString("{\"errcode\":404,\"errmsg\":\"城市"+cityname+"不存在\"}")
           return
        }
      }

      if id_inner != "" {
        weatherStr, _ := json.Marshal(completeWeather)
        SetCachedData(name_inner, string(weatherStr))
        SetCachedData(id_inner, string(weatherStr))  //断言，转换interface为string
        if(simple != "") {
          json.Unmarshal([]byte(str), &simpleWeather)
          simpleWeatherStr, _ := json.Marshal(simpleWeather)
          c.Ctx.WriteString(string(simpleWeatherStr))
        }else{
          c.Ctx.WriteString(string(weatherStr))
        }
      }else{
        c.Ctx.WriteString(str)
      }
      fmt.Println("city_id======", id_inner)
  }
}
```

### API

> API 地址: <http://www.yiketianqi.com/api/>

| 参数名    | 必选 | 类型   | 说明          |                                                          |
| :-------- | :--- | :----- | :------------ | -------------------------------------------------------- |
| appid     | 是   | string | 用户 appid     | 注册开发账号                                             |
| appsecret | 是   | string | 用户 appsecret | 注册开发密钥                                             |
| version   | 是   | string | 接口版本标识  | 固定值: `v6` 每个接口的 version 值都不一样                 |
| cityid    | 否   | string | 城市 ID        | 请参考 [城市ID列表](https://yikeapi.com/help/tianqicity) |
| city      | 否   | string | 城市名称      | 不要带市和区; 如: 青岛、铁西                             |
| vue       | 否   | string | 跨域参数      | 如果您使用的是 react、vue、angular 请填写值: `1`           |

### 在线版调用

otherModules\scratch-vm\src\blocks\internetService\scratch3_weather.js

## 语音识别 (47.75.240.161)

### Nginx 反代

/etc/nginx/conf/statistic.conf:94

```
location /online/speechToText {
      add_header Access-Control-Allow-Headers *;
      add_header Access-Control-Allow-Origin $cors_origin;
      # proxy_set_header Content-Type "audio/pcm;rate=16000";
      # add_header Access-Control-Allow-Credentials true;
      # add_header Access-Control-Allow-Methods 'GET,POST,OPTIONS';
      proxy_pass  https://vop.baidu.com/pro_api;
}
```

### 源代码 (直接反代，已经不走下面的代码了)

> /home/dfrobot/go/src/mindplus_statistic/controllers/online.go:52

```go
func (c *OnlineController) SpeechToText() {

	// c.Ctx.ResponseWriter.Header().Set("Access-Control-Allow-Origin", c.Ctx.Request.Header.Get("Origin"))

	url := GetConfig("speechToText")

	token_id := c.Input().Get("access_token")
	// token_id := GetServerTokenid(key1, key2)["access_token"]
	// fmt.Println("input=====",c.Ctx.Input.RequestBody)
	fmt.Println("input=====",c.Ctx.Input.RequestBody)
	// fmt.Println("input=====",string(c.Ctx.Input.RequestBody))

	var ob speechData
  	var err error

	json.Unmarshal(c.Ctx.Input.RequestBody, &ob)

	// var token_arr map[string]string

	// var msg =[]byte(ob.Speech)
	// ob.Speech = base64.StdEncoding.EncodeToString(ob.Speech)
	// ob.Speech = base64.StdEncoding.EncodeToString(msg)
	// fmt.Println(base64.StdEncoding.DecodeString(ob.Speech))
	ob.Token = token_id
	//fmt.Println("speechtotext token=====", token_id)
	configdata,_ := json.Marshal(ob)

	// 读取参数，根据前端参数向服务器发送请求

	req_twice := httplib.Post(url)
	req_twice.Header("Content-Type","application/json")


	// fmt.Println("sssssss=", string(configdata))
	req_twice.Body(configdata)
	// req_twice.Body(params)

	// access_token
	str, err := req_twice.String()
	// str, err := req_twice.Response()
	// req_twice.ToJSON(&token_arr)
	fmt.Println("str====", str)
	if err != nil {
	    // t.Fatal(err)
		fmt.Println("baiduTokenServer error==",err)
	}

	c.Ctx.WriteString(str)
}
```

### API

> API 地址: <https://vop.baidu.com/pro_api>

### 在线版调用

src\lib\speechAI.js

## AI 图像识别 (47.75.240.161)

### Nginx 反代

/etc/nginx/conf/statistic.conf:82

```
location /online/face/v3/faceset/group/add {
      proxy_pass  https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/add;
}
location /online/face/v3/faceset/user/add {
      proxy_pass  https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add;
}
location /online/face/v3/search {
      proxy_pass  https://aip.baidubce.com/rest/2.0/face/v3/search;
}
```

### 在线版调用

> 还包括了各种识别

otherModules\scratch-vm\src\blocks\internetService\scratch3_AI.js

## 用户统计 (离线版) -- 目前已停用 (47.75.240.161)

### Nginx 反代

/etc/nginx/conf/statistic.conf:79

```
location /collect/ {
    proxy_pass   http://127.0.0.1:6667;
}
```

## 用户统计 (在线版)(49.234.196.11)

> 下面使用的目录为 MindPlusWeb 源代码目录

src\lib\analytics.js

````
import GoogleAnalytics from 'react-ga';

GoogleAnalytics.initialize(process.env.GA_ID || window.GA_ID || 'UA-147518009-1', {
    debug: process.env.DEV,
    titleCase: true,
    sampleRate: process.env.DEV ? 100 : 0,
    forceSSL: true
});

module.exports = GoogleAnalytics;
````

> 调用的话
>
> 在很多文件中进行调用, 如下
>
> ```
> import analytics from '../lib/analytics';
> analytics.event({
>     category: 'error',
>     action: 'load project',
>     label: String(error)
> });
> ```
>

## TinyWebDB

### Nginx 反代

/etc/nginx/conf/statistic.conf:73

```
location / {
      proxy_pass   http://127.0.0.1:6666;
      add_header Access-Control-Allow-Origin $cors_origin;
      client_max_body_size 100m;
}
```

> 补充:
>
> /home/dfrobot/go/src/mindplus_statistic/conf/app.conf
>
> ```
> appname = mindplus_statistic
> httpport = 6666
> runmode = dev
> 
> copyrequestbody = true
> ```
>

### 源代码

/home/dfrobot/go/src/mindplus_statistic/controllers/online.go:106

```
func (c *OnlineController) Tinywebdb() {
	// http://localhost:7077/online/tinywebdb
	// c.Ctx.ResponseWriter.Header().Set("Access-Control-Allow-Origin", c.Ctx.Request.Header.Get("Origin"))

	url := c.Input().Get("db")
	user := c.Input().Get("user")
	secret := c.Input().Get("secret")
	action := c.Input().Get("action")

	tag := c.Input().Get("tag")
	no := c.Input().Get("no")
	count := c.Input().Get("count")
	value := c.Input().Get("value")
	type_c := c.Input().Get("type")

	fmt.Println(url)

	req_twice := httplib.Get(url)
	req_twice.Param("user", user)
	req_twice.Param("secret", secret)
	req_twice.Param("action", action)
	req_twice.Param("tag", tag)
	req_twice.Param("no", no)
	req_twice.Param("count", count)
	req_twice.Param("value", value)
	req_twice.Param("type", type_c)

	str, err := req_twice.String()
	if err != nil {
	    // t.Fatal(err)
	  // 设置响应状态码
	  c.Ctx.ResponseWriter.WriteHeader(500)
		fmt.Println("tinywebdb error== ",err)
		c.Ctx.WriteString("{error: true}")
		return
	}

	c.Ctx.WriteString(str)
	// 获取前端传递的参数
}
```

### 在线版调用

otherModules\scratch-vm\src\blocks\internetService\scratch3_tinywebdb.js

## 跨域 (47.75.240.161)

/etc/nginx/conf/statistic.conf:61

```conf
set $cors_origin "";
if ($http_origin ~* "^https://ide.mindplus.top$") {
        set $cors_origin $http_origin;
}
if ($http_origin ~* "^http://localhost:8601") {
        set $cors_origin $http_origin;
}
# 运行跨域的网址
add_header Access-Control-Allow-Origin $cors_origin;
```

## 添加证书 (mindplus 在线服务的证书)

> ip: 47.75.240.161
>
> statistic.dfrobot.top 的 SSL 证书
>
> 该证书是从阿里云申请的免费证书，有效期 1 年

/etc/nginx/conf/statistic.conf:44

```conf
#SSL 访问端口号为 443
listen 443;
#填写绑定证书的域名
server_name statistic.dfrobot.top;
#启用 SSL 功能
ssl on;
#证书文件名称
ssl_certificate 4812228_statistic.dfrobot.top.pem;
#私钥文件名称
ssl_certificate_key 4812228_statistic.dfrobot.top.key;
ssl_session_timeout 5m;
#请按照以下协议配置
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
#请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
ssl_prefer_server_ciphers on;
```

## 添加证书 (mindplus 在线 IDE 的证书)

> ip: 49.234.196.11
>
> ide.dfrobot.top 的 SSL 证书
>
> 该证书是从阿里云申请的免费证书，有效期 1 年

/etc/nginx/conf/statistic.conf:173

```
listen 443;
server_name ide.mindplus.top;
ssl on;
ssl_certificate cert/4812219_ide.mindplus.top.pem;
ssl_certificate_key cert/4812219_ide.mindplus.top.key;
ssl_session_timeout 5m;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
ssl_prefer_server_ciphers on;
```

## 在线版 BLE(低功耗蓝牙)、BT(蓝牙)

> 下面使用的目录为 MindPlusWeb 源代码目录

### 1. 乐高扩展库

otherModules\scratch-vm\src\extensions\scratch3_boost\index.js:6

otherModules\scratch-vm\src\extensions\scratch3_microbit\index.js:6

otherModules\scratch-vm\src\extensions\scratch3_wedo2\index.js:6

```
const BLE = require('../../io/ble');
```

### 2. BLE\BT 库

#### 2.1 BLE

otherModules\scratch-vm\src\io\ble.js

```
this._socket = runtime.getScratchLinkSocket('BLE');
```

#### 2.2 BT(并没有使用)

otherModules\scratch-vm\src\io\bt.js

```
this._socket = runtime.getScratchLinkSocket('BT');
```

#### 2.3 Runtime

otherModules\scratch-vm\src\engine\runtime.js

```
// 1762
// 1. 这个基本都没有被调用
configureScratchLinkSocketFactory (factory) {
    this._linkSocketFactory = factory;
}

// 1772
_defaultScratchLinkSocketFactory (type) {
    return new ScratchLinkWebSocket(type);
}

// 1750
getScratchLinkSocket (type) {
    // 2. 所以只会使用this._defaultScratchLinkSocketFactory
    // 即 new ScratchLinkWebSocket(type)
    const factory = this._linkSocketFactory || this._defaultScratchLinkSocketFactory;
    return factory(type);
}
```

### 3. 配置 (改版 Mind+)ScratchLink 的 WebSocket 地址

otherModules\scratch-vm\src\util\scratch-link-websocket.js

```
constructor (type) {
    this._type = type;
    // ....
}

open () {
    let base = "wss://dflink.mindplus.top:20110";
    switch (this._type) {
    case 'BLE':
        this._ws = new WebSocket(base+'/scratch/ble');
        break;
    case 'BT':
        this._ws = new WebSocket(base+'/scratch/bt');
        break;
    default:
        throw new Error(`Unknown ScratchLink socket Type: ${this._type}`);
    }
    // ....
}
```

## 在线备案 (ip: 49.234.196.11)

> <http://www.mindplus.top/>

/var/www/html/webpage/index.html

```
<a href="http://beian.miit.gov.cn" target="_blank">沪ICP备09038501号-7</a>
```

> 具体备案流程由李亮进行
>
> 后面由李亮提供备案号，然后替换即可