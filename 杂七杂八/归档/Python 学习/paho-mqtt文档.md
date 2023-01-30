# paho-mqtt 机翻文档

## Project description 项目描述

本文档描述了[Eclipse Paho](https://translate.google.com/translate?hl=zh-CN&prev=_t&sl=auto&tl=zh-CN&u=http://eclipse.org/paho/) MQTT Python客户端库的源代码，其中实现MQTT协议的版本5.0、3.1.1和3.1。

该代码提供了一个客户端类，该客户端类使应用程序可以连接到[MQTT](https://translate.google.com/translate?hl=zh-CN&prev=_t&sl=auto&tl=zh-CN&u=http://mqtt.org/)代理以进行发布
消息，并订阅主题并接收已发布的消息。它还提供了一些帮助
这些函数使将一次性消息发布到MQTT服务器非常简单。

它支持Python 2.7.9+或3.5+。

MQTT协议是机器对机器（M2M）/“物联网”连接协议。
作为一种非常轻量级的发布/订阅消息传递传输设计，它对于
与需要较小代码占用量和/或网络带宽的远程位置的连接
非常珍贵。

Paho is an [Eclipse Foundation](https://www.eclipse.org/org/foundation/) project.

## Installation 安装

The latest stable version is available in the Python Package Index (PyPi) and can be installed using

最新的稳定版本在Python软件包索引（PyPi）中可用，可以使用以下命令安装

```bash
pip install paho-mqtt
```

Or with `virtualenv`:

或与virtualenv：

```bash
virtualenv paho-mqtt
source paho-mqtt/bin/activate
pip install paho-mqtt
```

To obtain the full code, including examples and tests, you can clone the git repository:

要获取完整的代码（包括示例和测试），可以克隆git存储库:

```bash
git clone https://github.com/eclipse/paho.mqtt.python
```

Once you have the code, it can be installed from your repository as well:

获得代码后，也可以从存储库中安装它

```bash
cd paho.mqtt.python
python setup.py install
```

To perform all test (including MQTT v5 test), you also need to clone paho.mqtt.testing in paho.mqtt.python folder:

要执行所有测试（包括MQTT v5测试），您还需要在paho.mqtt.python文件夹中克隆paho.mqtt.testing：

```bash
git clone https://github.com/eclipse/paho.mqtt.testing.git
```

## Known limitations 已知限制

The following are the known unimplemented MQTT feature.

When clean_session is False, the session is only stored in memory not persisted. This means that when client is restarted (not just reconnected, the object is recreated usually because the program was restarted) the session is lost. This result in possible message lost.

The following part of client session is lost:

- QoS 2 messages which have been received from the Server, but have not been completely acknowledged.

  Since the client will blindly acknowledge any PUBCOMP (last message of a QoS 2 transaction), it won’t hang but will lost this QoS 2 message.

- QoS 1 and QoS 2 messages which have been sent to the Server, but have not been completely acknowledged.

  This means that message passed to publish() may be lost. This could be mitigated by taking care that all message passed to publish() has a corresponding on_publish() call.

  It also means that the broker may have the Qos2 message in the session. Since the client start with an empty session it don’t know it and will re-use the mid. This is not yet fixed.

Also when clean_session is True, this library will republish QoS > 0 message accross network reconnection. This means that QoS > 0 message won’t be lost. But the standard say that if we should discard any message for which the publish packet was sent. Our choice means that we are not compliant with the standard and it’s possible for QoS 2 to be received twice. You should you clean_session = False if you need the QoS 2 guarantee of only one delivery.

## Usage and API 用法和API 

Detailed API documentation is available through **pydoc**. Samples are available in the **examples** directory.

The package provides two modules, a full client and a helper for simple publishing.

可通过**pydoc**获得详细的API文档。示例中提供了**examples**目录

该软件包提供了两个模块，一个完整的客户端和一个用于简单发布的助手

### Getting Started 入门

Here is a very simple example that subscribes to the broker $SYS topic tree and prints out the resulting messages:

这是一个非常简单的示例，该示例订阅了代理$ SYS主题树并打印出结果消息：

```python
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```

### Client 客户

You can use the client class as an instance, within a class or by subclassing. The general usage flow is as follows:

您可以将客户机类用作实例，在类中或通过子类化来使用。一般使用流程如下

- Create a client instance  创建一个客户端实例
- Connect to a broker using one of the `connect*()` functions  使用`connect*()` 函数之一连接到代理
- Call one of the `loop*()` functions to maintain network traffic flow with the broker  调用`loop*()`函数之一来与代理保持网络流量
- Use `subscribe()` to subscribe to a topic and receive messages 使用`subscribe()`订阅主题并接收消息
- Use `publish()` to publish messages to the broker 使用`publish()` 将消息发布到代理
- Use `disconnect()` to disconnect from the broker  使用`disconnect()`与代理断开连接

Callbacks will be called to allow the application to process events as necessary. These callbacks are described below.

将调用回调以允许应用程序根据需要处理事件。这些回调描述如下。

#### Constructor  构造器/ reinitialise 重新初始化

##### CLIENT()

```python
Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
```

The `Client()` constructor takes the following arguments:

该 `Client()` 构造函数采用下列参数：

- client_id

  the unique client id string used when connecting to the broker. If `client_id` is zero length or `None`, then one will be randomly generated. In this case the `clean_session` parameter must be `True`.

  连接到代理时使用的唯一客户端ID字符串。如果`client_id` 为零长度或`None` ，那么将随机生成一个。在这种情况下，`clean_session`参数必须是`True`。

- clean_session

  a boolean that determines the client type. If `True`, the broker will remove all information about this client when it disconnects. If `False`, the client is a durable client and subscription information and queued messages will be retained when the client disconnects.Note that a client will never discard its own outgoing messages on disconnect. Calling connect() or reconnect() will cause the messages to be resent. Use reinitialise() to reset a client to its original state.

  确定客户机类型的布尔值

  如果为`True`，则代理将在断开连接时删除有关此客户端的所有信息。

  如果为 `False`，则客户端是持久客户端和订阅

  当客户端断开连接时，信息和排队的消息将保留。注意客户端在断开连接时永远不会丢弃自己的传出消息

  调用`connect()`或`reconnect()`

  将导致重新发送消息。使用`reinitialise()`将客户端重置为其原始状态。

- userdata

  user defined data of any type that is passed as the `userdata` parameter to callbacks. It may be updated at a later point with the `user_data_set()` function.

  用户定义的任何类型的数据，都将作为`userdata`参数传递给回调。可能是

  稍后使用`user_data_set()`函数进行更新。

- protocol

  the version of the MQTT protocol to use for this client. Can be either `MQTTv31` or `MQTTv311`

  用于此客户端的MQTT协议的版本。可以是`MQTTv31` 或`MQTTv311`

- transport

  set to “websockets” to send MQTT over WebSockets. Leave at the default of “tcp” to use raw TCP.
  
  设置为“ websockets”以通过WebSocket发送MQTT。保留默认值“ tcp”以使用原始TCP。

###### Constructor Example 构造函数示例

```python
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
```

##### REINITIALISE()

```python
reinitialise(client_id="", clean_session=True, userdata=None)
```

The `reinitialise()` function resets the client to its starting state as if it had just been created. It takes the same arguments as the `Client()` constructor.

`reinitialise()`函数可以将客户端重置为其初始状态。

它采用与`Client()`构造函数相同的参数

###### Reinitialise Example  重新初始化示例

```python
mqttc.reinitialise()
```

#### Option functions  选项功能

These functions represent options that can be set on the client to modify its behaviour. In the majority of cases this must be done *before* connecting to a broker.

这些函数表示可以在客户端上设置以修改其行为的选项。在大多数情况下，这必须在*连接到代理之前*完成。

##### MAX_INFLIGHT_MESSAGES_SET()

```python
max_inflight_messages_set(self, inflight)
```

Set the maximum number of messages with QoS>0 that can be part way through their network flow at once.

Defaults to 20. Increasing this value will consume more memory but can increase throughput.

设置QoS>0的消息的最大数量，这些消息可以同时部分通过其网络流。

默认为20。增加此值将消耗更多内存，但可以提高吞吐量。

##### MAX_QUEUED_MESSAGES_SET()

```python
max_queued_messages_set(self, queue_size)
```

Set the maximum number of outgoing messages with QoS>0 that can be pending in the outgoing message queue.

Defaults to 0. 0 means unlimited. When the queue is full, any further outgoing messages would be dropped.

设置可以在传出中挂起的，QoS> 0的最大传出消息数的消息队列。

默认为0。0表示无限制。当队列已满时，将丢弃任何进一步的传出消息。

##### MESSAGE_RETRY_SET()

```python
message_retry_set(retry)
```

Set the time in seconds before a message with QoS>0 is retried, if the broker does not respond.

This is set to 5 seconds by default and should not normally need changing.

如果代理未响应，请设置重试QoS> 0的消息之前的时间（以秒为单位）

默认情况下，此设置为5秒，通常不需要更改。

##### WS_SET_OPTIONS()

```python
ws_set_options(self, path="/mqtt", headers=None)
```

Set websocket connection options. These options will only be used if `transport="websockets"` was passed into the `Client()` constructor.

设置websocket连接选项。仅当transport =“ websockets”时才使用这些选项

被传递到`Client()`构造函数中。

- path

  在代理上使用的mqtt路径

- headers

  Either a dictionary specifying a list of extra headers which should be appended to the standard websocket headers, or a callable that takes the normal websocket headers and returns a new dictionary with a set of headers to connect to the broker.
  
  要么指定应附加到标准websocket标头的额外标头列表的字典，要么是采用正常websocket标头并返回带有一组标头的新词典以连接到代理的callable。

Must be called before `connect*()`. An example of how this can be used with the AWS IoT platform is in the **examples** folder.

必须在`connect*()`之前调用。  **examples**文件夹中是如何与AWS IoT平台一起使用的示例。

##### TLS_SET()

```python
tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS, ciphers=None)
```

Configure network encryption and authentication options. Enables SSL/TLS support.

配置网络加密和身份验证选项。启用SSL / TLS支持。

- ca_certs

  a string path to the Certificate Authority certificate files that are to be treated as trusted by this client. If this is the only option given then the client will operate in a similar manner to a web browser. That is to say it will require the broker to have a certificate signed by the Certificate Authorities in `ca_certs` and will communicate using TLS v1, but will not attempt any form of authentication. This provides basic network encryption but may not be sufficient depending on how the broker is configured. By default, on Python 2.7.9+ or 3.4+, the default certification authority of the system is used. On older Python version this parameter is mandatory.

  将被此客户端视为受信任的证书颁发机构证书文件的字符串路径。如果这是唯一的选择，那么客户端将以类似于web浏览器的方式运行。也就是说，它将要求代理拥有由证书颁发机构在“ca_certs”中签名的证书，并将使用TLS v1进行通信，但不会尝试任何形式的身份验证。这提供了基本的网络加密，但可能还不够，这取决于代理的配置方式。默认情况下，在Python 2.7.9+或3.4+上，使用系统的默认证书颁发机构。在较旧的Python版本中，此参数是必需的。

- certfile, keyfile

  strings pointing to the PEM encoded client certificate and private keys respectively. If these arguments are not `None` then they will be used as client information for TLS based authentication. Support for this feature is broker dependent. Note that if either of these files in encrypted and needs a password to decrypt it, Python will ask for the password at the command line. It is not currently possible to define a callback to provide the password.

  分别指向PEM编码的客户端证书和私钥的字符串。如果这些参数不是`None` ，则它们将用作基于TLS的身份验证的客户端信息。此功能的支持依赖于代理。请注意，如果这两个文件中的任何一个处于加密状态并且需要密码来解密，Python将在命令行中请求密码。当前无法定义回调来提供密码。

- cert_reqs

  定义客户强加给代理的证书要求。 默认情况下，这是`ssl.CERT_REQUIRED`，这意味着代理必须提供证书。 有关此参数的更多信息，见ssl pydoc有关此参数的更多信息。

- tls_version

  specifies the version of the SSL/TLS protocol to be used. By default (if the python version supports it) the highest TLS version is detected. If unavailable, TLS v1 is used. Previous versions (all versions beginning with SSL) are possible but not recommended due to possible security problems.

  指定要使用的SSL/TLS协议的版本。默认情况下（如果python版本支持它），将检测到最高的TLS版本。如果不可用，则使用TLS v1。以前的版本（所有以SSL开头的版本）是可能的，但由于可能存在安全问题，不建议使用。

- ciphers

  a string specifying which encryption ciphers are allowable for this connection, or `None` to use the defaults. See the ssl pydoc for more information.
  
  一个字符串，指定此连接允许使用哪些加密密码，或使用“None”使用默认值。有关更多信息，请参阅sslpydoc。

Must be called before `connect*()`.

必须在 `connect*()`之前调用

##### TLS_SET_CONTEXT()

```python
tls_set_context(context=None)
```

Configure network encryption and authentication context. Enables SSL/TLS support.

配置网络加密和身份验证上下文。启用SSL / TLS支持。

- context

  an ssl.SSLContext object. By default, this is given by `ssl.create_default_context()`, if available (added in Python 3.4).
  
  ssl.SSLContext对象。默认情况下，它由 `ssl.create_default_context()`给出，如果
  
  可用（在Python 3.4中添加）。

If you’re unsure about using this method, then either use the default context, or use the `tls_set` method. See the ssl module documentation section about [security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for more information.

如果不确定使用此方法，请使用默认上下文，或使用`tls_set`方法。请参阅有关ssl模块文档的部分[安全方面的考虑](https://translate.google.com/translate?hl=zh-CN&prev=_t&sl=auto&tl=zh-CN&u=https://docs.python.org/3/library/ssl.html%23ssl-security#ssl-security)更多信息。

Must be called before `connect*()`.

必须在 `connect*()`之前调用

##### TLS_INSECURE_SET()

```python
tls_insecure_set(value)
```

Configure verification of the server hostname in the server certificate.

在服务器证书中配置对服务器主机名的验证。

If `value` is set to `True`, it is impossible to guarantee that the host you are connecting to is not impersonating your server. This can be useful in initial server testing, but makes it possible for a malicious third party to impersonate your server through DNS spoofing, for example.

如果`value` 设置为`True`，则无法保证所连接的主机没有模拟服务器。这在最初的服务器测试中很有用，但它使恶意第三方有可能通过DNS欺骗来模拟您的服务器。

Do not use this function in a real system. Setting value to True means there is no point using encryption.

不要在实际系统中使用此功能。将值设置为True意味着使用加密没有意义。

Must be called before `connect*()` and after `tls_set()` or `tls_set_context()`.

必须在`connect*()`之前和`tls_set()`或`tls_set_context()`之后调用。

##### ENABLE_LOGGER()

```python
enable_logger(logger=None)
```

Enable logging using the standard python logging package (See PEP 282). This may be used at the same time as the `on_log` callback method.

使用标准python日志包启用日志记录（请参阅PEP 282）。这可以与`on_log`回调方法同时使用。

If `logger` is specified, then that `logging.Logger` object will be used, otherwise one will be created automatically.

如果指定了`logger` ，则`logging.Logger`对象将被使用，否则将自动创建一个。

Paho logging levels are converted to standard ones according to the following mapping:

Paho日志记录级别根据以下映射转换为标准级别：

| Paho               | logging                                 | 翻译                 |
| :----------------- | :-------------------------------------- | -------------------- |
| `MQTT_LOG_ERR`     | `logging.ERROR`                         | 错误                 |
| `MQTT_LOG_WARNING` | `logging.WARNING`                       | 警告                 |
| `MQTT_LOG_NOTICE`  | `logging.INFO` *(no direct equivalent)* | 消息(*无直接等效项*) |
| `MQTT_LOG_INFO`    | `logging.INFO`                          | 消息                 |
| `MQTT_LOG_DEBUG`   | `logging.DEBUG`                         | 故障                 |

##### DISABLE_LOGGER()

```python
disable_logger()
```

Disable logging using standard python logging package. This has no effect on the `on_log` callback.

使用标准python日志记录包禁用日志记录。这对`on_log` 回调没有影响。

##### USERNAME_PW_SET()

```python
username_pw_set(username, password=None)
```

Set a username and optionally a password for broker authentication. Must be called before `connect*()`.

为代理身份验证设置用户名和密码（可选）。必须在 `connect*()`之前调用。

##### USER_DATA_SET()

```python
user_data_set(userdata)
```

Set the private user data that will be passed to callbacks when events are generated. Use this for your own purpose to support your application.

设置生成事件时将传递给回调的专用用户数据。为您自己的目的使用它来支持您的应用程序。

##### WILL_SET()

```python
will_set(topic, payload=None, qos=0, retain=False)
```

Set a Will to be sent to the broker. If the client disconnects without calling `disconnect()`, the broker will publish the message on its behalf.

设置将要发送给代理的will消息。 如果客户端在不调用`disconnect（）`的情况下断开连接，则代理将代表它发布消息。

- topic

  the topic that the will message should be published on.

  will消息应发布的主题。

- payload

  the message to send as a will. If not given, or set to `None` a zero length message will be used as the will. Passing an int or float will result in the payload being converted to a string representing that number. If you wish to send a true int/float, use `struct.pack()` to create the payload you require.

  随便发送的消息。 如果未给出，或设置为 `None` ，则零长度消息将用作will消息。 传递int或float会导致有效负载被转换为表示该数字的字符串。 如果你想发送一个真正的int / float，使用`struct.pack（）`创建你需要的有效载荷。

- qos

  the quality of service level to use for the will.

  用于will消息的服务质量级别

- retain

  if set to `True`, the will message will be set as the “last known good”/retained message for the topic.
  
  如果设置为`True`, ，则will消息将被设置为该主题的“最后一次知悉” /保留消息。

Raises a `ValueError` if `qos` is not 0, 1 or 2, or if `topic` is `None` or has zero string length.

如果`qos`不是0、1或2，或者如果`topic`是`None`或具有零字符串长度，则引发`ValueError`。

##### RECONNECT_DELAY_SET

```python
reconnect_delay_set(min_delay=1, max_delay=120)
```

The client will automatically retry connection. Between each attempt it will wait a number of seconds between `min_delay` and `max_delay`.

客户端将自动重试连接。 在每次尝试之间，它将在`min_delay`和`max_delay`之间等待几秒钟。

When the connection is lost, initially the reconnection attempt is delayed of `min_delay` seconds. It’s doubled between subsequent attempt up to `max_delay`.

当连接断开时，最初的重新连接尝试会延迟 `min_delay` 秒。 在后续尝试中达到`max_delay`（最大延迟时间）的时间增加了一倍

The delay is reset to `min_delay` when the connection complete (e.g. the CONNACK is received, not just the TCP connection is established).

当连接完成（例如，接收到连接，而不仅仅是建立TCP连接）时，延迟将重置为`min_delay`。

#### Connect 连接/ reconnect 重新连接/ disconnect 断开

##### CONNECT()

```python
connect(host, port=1883, keepalive=60, bind_address="")
```

The `connect()` function connects the client to a broker. This is a blocking function. It takes the following arguments:

函数将`connect()` 连接到代理。这是一个阻塞函数。它采用以下参数：

- host

  the hostname or IP address of the remote broker

  远程代理的主机名或IP地址

- port

  the network port of the server host to connect to. Defaults to 1883. Note that the default port for MQTT over SSL/TLS is 8883 so if you are using `tls_set()` or `tls_set_context()`, the port may need providing manually

  要连接到的服务器主机的网络端口。默认为1883。请注意，SSL/TLS上MQTT的默认端口是8883，因此如果使用的是`tls_set()`或`tls_set_context()`，则可能需要手动提供该端口

- keepalive

  maximum period in seconds allowed between communications with the broker. If no other messages are being exchanged, this controls the rate at which the client will send ping messages to the broker

  与代理通信之间允许的最长时间（秒）。如果没有其他消息被交换，这将控制客户端向代理发送ping消息的速率

- bind_address

  the IP address of a local network interface to bind this client to, assuming multiple interfaces exist
  
  要将此客户端绑定到的本地网络接口的IP地址（假定存在多个接口）

###### Callback 回调

When the client receives a CONNACK message from the broker in response to the connect it generates an `on_connect()` callback.

当客户端收到来自代理的CONNACK消息以响应连接时，它将生成一个`on_connect()`回调。

###### Connect Example 连接示例

```python
mqttc.connect("mqtt.eclipse.org")
```

##### CONNECT_ASYNC()

```python
connect_async(host, port=1883, keepalive=60, bind_address="")
```

Use in conjunction with `loop_start()` to connect in a non-blocking manner. The connection will not complete until `loop_start()` is called.

与`loop_start（）`结合使用以非阻塞方式连接。 直到调用 `loop_start()` ，连接才会完成。

###### Callback (connect)

When the client receives a CONNACK message from the broker in response to the connect it generates an `on_connect()` callback.

当客户端收到来自代理的CONNACK消息以响应连接时，它将生成一个`on_connect()` 回调。

##### CONNECT_SRV()

```python
connect_srv(domain, keepalive=60, bind_address="")
```

Connect to a broker using an SRV DNS lookup to obtain the broker address. Takes the following arguments:

使用SRV DNS查找连接到代理以获得代理地址。 采用以下参数：

- domain

  the DNS domain to search for SRV records. If `None`, try to determine the local domain name.
  
  DNS域以搜索SRV记录。 如果为`None`,，请尝试确定本地域名。

See `connect()` for a description of the `keepalive` and `bind_address` arguments.

有关`keepalive`和`bind_address`参数的描述，请参见`connect（）`。

###### Callback (connect_srv)

When the client receives a CONNACK message from the broker in response to the connect it generates an `on_connect()` callback.

当客户端收到来自代理的CONNACK消息以响应连接时，它将生成一个`on_connect()`回调。

###### SRV Connect Example SRV 连接示例

```python
mqttc.connect_srv("eclipse.org")
```

##### RECONNECT()

```python
reconnect()
```

Reconnect to a broker using the previously provided details. You must have called `connect*()` before calling this function.

使用先前提供的详细信息重新连接到代理。 在调用此函数之前，您必须已调用 `connect*()`。

###### Callback (reconnect)

When the client receives a CONNACK message from the broker in response to the connect it generates an `on_connect()` callback.

当客户端收到来自代理的CONNACK消息以响应连接时，它将生成一个`on_connect()`回调。

##### DISCONNECT()

```python
disconnect()
```

Disconnect from the broker cleanly. Using `disconnect()` will not result in a will message being sent by the broker.

完全断开与代理的连接。使用`disconnect()`不会导致代理发送will消息。

Disconnect will not wait for all queued message to be sent, to ensure all messages are delivered, `wait_for_publish()` from `MQTTMessageInfo` should be used. See `publish()` for details.

断开连接不会等待所有排队的消息发送，以确保所有消息都已传递，应使用`MQTTMessageInfo` 中的`wait_for_publish()` 。 有关详细信息，请参见`publish()`。

###### Callback (disconnect)

When the client has sent the disconnect message it generates an `on_disconnect()` callback.

客户端发送断开连接消息后，它将生成`on_disconnect()`回调。

#### Network loop 网络循环

These functions are the driving force behind the client. If they are not called, incoming network data will not be processed and outgoing network data may not be sent in a timely fashion. There are four options for managing the network loop. Three are described here, the fourth in “External event loop support” below. Do not mix the different loop functions.

这些功能是客户的驱动力。 如果未调用它们，则不会处理传入的网络数据，也可能无法及时发送传出的网络数据。 有四个用于管理网络环路的选项。 这里描述了三个，下面是“外部事件循环支持”中的第四个。 不要混用不同的循环功能。

##### LOOP()

```python
loop(timeout=1.0, max_packets=1)
```

Call regularly to process network events. This call waits in `select()` until the network socket is available for reading or writing, if appropriate, then handles the incoming/outgoing data. This function blocks for up to `timeout` seconds. `timeout` must not exceed the `keepalive` value for the client or your client will be regularly disconnected by the broker.

定期打电话处理网络事件。此调用在`select()`中等待，直到网络socket可以读或写（如果合适），然后处理传入/传出数据。此函数最多阻塞`timeout` 秒。`timeout`不能超过客户端的`keepalive`值，否则代理会定期断开客户端的连接。

The `max_packets` argument is obsolete and should be left unset.

`max_packets` 参数已过时，应保持未设置。

###### Loop Example  循环示例

```python
run = True
while run:
    mqttc.loop()
```

##### LOOP_START() / LOOP_STOP()

```python
loop_start()
loop_stop(force=False)
```

These functions implement a threaded interface to the network loop. Calling `loop_start()` once, before or after `connect*()`, runs a thread in the background to call `loop()` automatically. This frees up the main thread for other work that may be blocking. This call also handles reconnecting to the broker. Call `loop_stop()` to stop the background thread. The `force` argument is currently ignored.

这些功能实现了到网络循环的线程接口。 在`loop_start()`之前或之后调用一次`connect*()`会在后台运行线程以自动调用`loop()`。 这样可以将主线程释放给其他可能阻塞的工作。 此调用还处理重新连接到代理。 调用`loop_stop（）`停止后台线程。`force`参数目前被忽略。

###### Loop Start/Stop Example  循环启动/停止示例

```python
mqttc.connect("mqtt.eclipse.org")
mqttc.loop_start()

while True:
    temperature = sensor.blocking_read()
    mqttc.publish("paho/temperature", temperature)
```

##### LOOP_FOREVER()

```python
loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)
```

This is a blocking form of the network loop and will not return until the client calls `disconnect()`. It automatically handles reconnecting.

这是网络循环的一种阻塞形式，直到客户端调用`disconnect（）`时才会返回。 它会自动处理重新连接。

Except for the first connection attempt when using connect_async, use `retry_first_connection=True` to make it retry the first connection. Warning: This might lead to situations where the client keeps connecting to an non existing host without failing.

除了在使用connect_async时尝试进行第一次连接之外，请使用`retry_first_connection = True`使其重试第一个连接。 警告：这可能会导致客户端不断连接到不存在的主机而不会失败的情况。

The `timeout` and `max_packets` arguments are obsolete and should be left unset.

`timeout` 和 `max_packets`参数已过时，应保留为未设置状态。

#### Publishing  出版

Send a message from the client to the broker.

从客户端向代理发送消息。

##### PUBLISH()

```python
publish(topic, payload=None, qos=0, retain=False)
```

This causes a message to be sent to the broker and subsequently from the broker to any clients subscribing to matching topics. It takes the following arguments:

这将导致消息发送到代理，然后从代理发送到订阅匹配主题的任何客户端。 它采用以下参数：

- topic

  the topic that the message should be published on

  消息应发布的主题

- payload

  the actual message to send. If not given, or set to `None` a zero length message will be used. Passing an int or float will result in the payload being converted to a string representing that number. If you wish to send a true int/float, use `struct.pack()` to create the payload you require

  实际发送的消息。 如果未给出或设置为“无”，则将使用零长度的消息。 传递int或float会导致有效负载被转换为表示该数字的字符串。 如果你想发送一个真正的int / float，使用`struct.pack（）`创建你需要的有效载荷

- qos

  the quality of service level to use

  使用的服务质量水平

- retain

  if set to `True`, the message will be set as the “last known good”/retained message for the topic.
  
  如果设置为`True`，则该消息将被设置为该主题的“最后一次知悉” /保留消息。

Returns a MQTTMessageInfo which expose the following attributes and methods:

返回一个MQTTMessageInfo，它公开以下属性和方法：

- `rc`, the result of the publishing. It could be `MQTT_ERR_SUCCESS` to indicate success, `MQTT_ERR_NO_CONN` if the client is not currently connected, or `MQTT_ERR_QUEUE_SIZE` when `max_queued_messages_set` is used to indicate that message is neither queued nor sent.

  `rc`，发布的结果。 

  结果可以是`MQTT_ERR_SUCCESS`以指示成功，`MQTT_ERR_NO_CONN`（如果客户端当前未连接）或`MQTT_ERR_QUEUE_SIZE`（当`max_queued_messages_set`用于指示消息既未排队也未发送时

- `mid` is the message ID for the publish request. The mid value can be used to track the publish request by checking against the mid argument in the `on_publish()` callback if it is defined. `wait_for_publish` may be easier depending on your use-case.

  `mid` 是发布请求的消息ID。

  中间值可用于通过检查`on_publish()`回调中的mid参数来跟踪发布请求 （如果已定义）。`wait_for_publish`可能会更容易，具体取决于您的用例。

- `wait_for_publish()` will block until the message is published. It will raise ValueError if the message is not queued (rc == `MQTT_ERR_QUEUE_SIZE`).

  `wait_for_publish()` 将阻塞，直到消息发布。如果消息未排队，则会引发ValueError（rc == `MQTT_ERR_QUEUE_SIZE`）

- `is_published` returns True if the message has been published. It will raise ValueError if the message is not queued (rc == `MQTT_ERR_QUEUE_SIZE`).

  如果消息已发布，则`is_published`返回True。如果消息未排队，则会引发ValueError（rc == `MQTT_ERR_QUEUE_SIZE`）

A `ValueError` will be raised if topic is `None`, has zero length or is invalid (contains a wildcard), if `qos` is not one of 0, 1 or 2, or if the length of the payload is greater than 268435455 bytes.

如果topic为`None`、长度为零或无效（包含通配符）、如果`qos`不是0、1或2这三个数中的一个，如果有效负载的长度大于268435455字节，则将引发`ValueError`。

###### Callback (publish)

When the message has been sent to the broker an `on_publish()` callback will be generated.

当消息被发送到代理后，将生成一个`on_publish()`回调。

#### Subscribe 订阅/ Unsubscribe  取消订阅

##### SUBSCRIBE()

```python
subscribe(topic, qos=0)
```

Subscribe the client to one or more topics.

为客户端订阅一个或多个主题。

This function may be called in three different ways:

此函数可以用三种不同的方式调用：

###### Simple string and integer

简单字符串和整数

e.g. `subscribe("my/topic", 2)`

例如 `subscribe("my/topic", 2)`

- topic

  a string specifying the subscription topic to subscribe to.

  一个字符串，指定要订阅的订阅主题。

- qos

  the desired quality of service level for the subscription. Defaults to 0.
  
  订阅所需的服务质量级别。 预设为0。

###### String and integer tuple

字符串和整数元组

e.g. `subscribe(("my/topic", 1))`

- topic

  a tuple of `(topic, qos)`. Both topic and qos must be present in the tuple.

  类似于`(topic, qos)`这样的元组。 元组中必须同时存在topic和qos。

- qos

  not used.

###### List of string and integer tuples

字符串和整数元组列表

e.g. `subscribe([("my/topic", 0), ("another/topic", 2)])`

This allows multiple topic subscriptions in a single SUBSCRIPTION command, which is more efficient than using multiple calls to `subscribe()`.

这允许在单个SUBSCRIPTION命令中进行多个主题订阅，这比使用多次调用`subscribe()`的效率更高。

- topic

  a list of tuple of format `(topic, qos)`. Both topic and qos must be present in all of the tuples.

  格式为 `(topic, qos)`的元组列表。 所有元组中都必须存在topic和qos。

- qos

  not used.

The function returns a tuple `(result, mid)`, where `result` is `MQTT_ERR_SUCCESS` to indicate success or `(MQTT_ERR_NO_CONN, None)` if the client is not currently connected. `mid` is the message ID for the subscribe request. The mid value can be used to track the subscribe request by checking against the mid argument in the `on_subscribe()` callback if it is defined.

该函数返回一个元组`(result, mid)`，其中`result`为`MQTT_ERR_SUCCESS`表示成功，或者为`(MQTT_ERR_NO_CONN, None)`如果客户端当前未连接。`mid`是订阅请求的消息ID。 通过检查`on_subscribe()`回调中的mid参数（如果已定义），可以使用mid值来跟踪订阅请求。

Raises a `ValueError` if `qos` is not 0, 1 or 2, or if topic is `None` or has zero string length, or if `topic` is not a string, tuple or list.

如果`qos`不为0、1或2，或者topic为`None`或字符串长度为零，或者topic为非字符串，元组或列表，则引发‘ValueError’。

###### Callback (subscribe)

When the broker has acknowledged the subscription, an `on_subscribe()` callback will be generated.

当代理确认订阅后，将生成一个`on_subscribe()`的回调。

##### UNSUBSCRIBE()

```python
unsubscribe(topic)
```

Unsubscribe the client from one or more topics.

取消订阅客户一个或多个主题。

- topic

  a single string, or list of strings that are the subscription topics to unsubscribe from.
  
  要取消订阅的订阅主题的单个字符串或字符串列表。

Returns a tuple `(result, mid)`, where `result` is `MQTT_ERR_SUCCESS` to indicate success, or `(MQTT_ERR_NO_CONN, None)` if the client is not currently connected. `mid` is the message ID for the unsubscribe request. The mid value can be used to track the unsubscribe request by checking against the mid argument in the `on_unsubscribe()` callback if it is defined.

返回一个元组`(result, mid)`，其中`result`是`MQTT_ERR_SUCCESS`表示成功，或者返回`(MQTT_ERR_NO_CONN, None)`如果客户端当前未连接。 `mid`是退订请求的消息ID。 中间值可以通过检查`on_unsubscribe()`回调中的mid参数（如果已定义）来用于跟踪取消订阅请求。

Raises a `ValueError` if `topic` is `None` or has zero string length, or is not a string or list.

如果`topic`为`None`或字符串长度为零，或者不是字符串或列表，则引发“ ValueError”。

###### Callback (unsubscribe)

When the broker has acknowledged the unsubscribe, an `on_unsubscribe()` callback will be generated.

当代理确认退订后，将生成一个`on_unsubscribe()`回调。

#### Callbacks  回调

##### ON_CONNECT()

```python
on_connect(client, userdata, flags, rc)
```

Called when the broker responds to our connection request.

当代理响应我们的连接请求时调用。

- client

  the client instance for this callback

  此回调的客户端实例(对象)

- userdata

  the private user data as set in `Client()` or `user_data_set()`

  在`Client()`或`user_data_set()`中设置的私人用户数据

- flags

  response flags sent by the broker

  代理发送的响应标志

- rc

  the connection result

  连接结果

- flags is a dict that contains response flags from the broker:

  flags是包含来自代理的响应标志的dict：
  
  flags[‘session present’] - this flag is useful for clients that areusing clean session set to 0 only. If a client with clean session=0, that reconnects to a broker that it has previously connected to, this flag indicates whether the broker still has the session information for the client. If 1, the session still exists.
  
  flags[‘session present’]-此标志对于仅使用设置为0的干净会话的客户端非常有用。如果clean session=0的客户机重新连接到它以前连接到的代理，则此标志指示代理是否仍具有该客户机的会话信息。如果为1，则会话仍然存在。

The value of rc indicates success or not:

rc值表示成功与否：

> 0: Connection successful 1: Connection refused - incorrect protocol version 2: Connection refused - invalid client identifier 3: Connection refused - server unavailable 4: Connection refused - bad username or password 5: Connection refused - not authorised 6-255: Currently unused.
>
> 0:连接成功1:连接被拒绝-协议不正确版本2:连接被拒绝-客户端标识符无效3:连接被拒绝-服务器不可用4:连接被拒绝-用户名或密码错误5:连接被拒绝-未授权6-255:当前未使用。

###### On Connect Example 连接回调示例

```python
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+connack_string(rc))

mqttc.on_connect = on_connect
...
```

##### ON_DISCONNECT()

```python
on_disconnect(client, userdata, rc)
```

Called when the client disconnects from the broker.

当客户端与代理断开连接时调用。

- client

  the client instance for this callback

  此回调的客户端实例

- userdata

  the private user data as set in `Client()` or `user_data_set()`

  在`Client()` 或`user_data_set()`中设置的专用用户数据`

- rc

  the disconnection result
  
  断开连接的结果

The rc parameter indicates the disconnection state. If `MQTT_ERR_SUCCESS` (0), the callback was called in response to a `disconnect()` call. If any other value the disconnection was unexpected, such as might be caused by a network error.

rc参数表示断开状态。如果 `MQTT_ERR_SUCCESS` （0），则调用回调以响应`disconnect()`调用。如果任何其他值是意外的断开连接，例如可能是由网络错误引起的。

###### On Disconnect Example  断开连接回调示例

```python
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

mqttc.on_disconnect = on_disconnect
...
```

##### ON_MESSAGE()

```
on_message(client, userdata, message)
```

Called when a message has been received on a topic that the client subscribes to and the message does not match an existing topic filter callback. Use `message_callback_add()` to define a callback that will be called for specific topic filters. `on_message` will serve as fallback when none matched.

当已收到有关客户端订阅的主题的消息且该消息与现有主题过滤器回调不匹配时，调用此方法。 使用`message_callback_add（）`定义将为特定主题过滤器调用的回调。 如果没有匹配，`on_message`将作为后备。

- client

  the client instance for this callback

  此回调的客户端实例

- userdata

  the private user data as set in `Client()` or `user_data_set()`

  在 `Client()` 或`user_data_set()`中设置的私人用户数据

- message

  an instance of MQTTMessage. This is a class with members `topic`, `payload`, `qos`, `retain`.
  
  MQTTMessage的实例。 这是一个具有成员`topic`,`payload`,`qos`,`retain`.成员的课程。

###### On Message Example  消息回调示例

```python
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

mqttc.on_message = on_message
...
```

##### MESSAGE_CALLBACK_ADD()

This function allows you to define callbacks that handle incoming messages for specific subscription filters, including with wildcards. This lets you, for example, subscribe to `sensors/#` and have one callback to handle `sensors/temperature` and another to handle `sensors/humidity`.

此功能使您可以定义用于处理特定订阅过滤器（包括通配符）的传入消息的回调。 例如，这使您可以订阅`sensors/#`，并有一个回调来处理`sensors/temperature`，而有另一个回调来处理`sensors/humidity`。

```
message_callback_add(sub, callback)
```

- sub

  the subscription filter to match against for this callback. Only one callback may be defined per literal sub string

  与该回调匹配的订阅过滤器。 每个文字子字符串只能定义一个回调

- callback

  the callback to be used. Takes the same form as the `on_message` callback.
  
  要使用的回调。 采用与`on_message`回调相同的形式。

If using `message_callback_add()` and `on_message`, only messages that do not match a subscription specific filter will be passed to the `on_message` callback.

如果使用`message_callback_add（）`和`on_message`，则只有与订阅专用过滤器不匹配的消息才会被传递到`on_message`回调中。

If multiple sub match a topic, each callback will be called (e.g. sub `sensors/#` and sub `+/humidity` both match a message with a topic `sensors/humidity`, so both callbacks will handle this message).

如果多个子匹配一个主题，则将调用每个回调（例如，子`sensors /＃`和子`+ /湿度'都将一条消息与主题“传感器/湿度”匹配，因此这两个回调都将处理此消息）。

##### MESSAGE_CALLBACK_REMOVE()

Remove a topic/subscription specific callback previously registered using `message_callback_add()`.

删除先前使用`message_callback_add（）`注册的特定于主题/订阅的回调。

```python
message_callback_remove(sub)
```

- sub

  the subscription filter to remove
  
  要删除的订阅过滤器

##### ON_PUBLISH()

```python
on_publish(client, userdata, mid)
```

Called when a message that was to be sent using the `publish()` call has completed transmission to the broker. For messages with QoS levels 1 and 2, this means that the appropriate handshakes have completed. For QoS 0, this simply means that the message has left the client. The `mid` variable matches the mid variable returned from the corresponding `publish()` call, to allow outgoing messages to be tracked.

当要使用`publish()`调用发送的消息已完成向代理的传输时，调用此方法。 对于QoS级别为1和2的消息，这意味着适当的握手已完成。 对于QoS 0，这仅表示消息已离开客户端。 `mid`变量与从相应的`publish()`调用返回的“ mid”变量匹配，以允许跟踪传出的消息。

This callback is important because even if the publish() call returns success, it does not always mean that the message has been sent.

此回调很重要，因为即使`publish()`调用返回成功，也并不总是意味着消息已发送。

##### ON_SUBSCRIBE()

```python
on_subscribe(client, userdata, mid, granted_qos)
```

Called when the broker responds to a subscribe request. The `mid` variable matches the mid variable returned from the corresponding `subscribe()` call. The `granted_qos` variable is a list of integers that give the QoS level the broker has granted for each of the different subscription requests.

当代理响应订阅请求时调用。 `mid`变量与从相应的`subscribe()`调用返回的`mid`变量匹配。`granted_qos`变量是整数列表，这些整数给出代理已为每个不同的订阅请求授予的QoS级别。

##### ON_UNSUBSCRIBE()

```python
on_unsubscribe(client, userdata, mid)
```

Called when the broker responds to an unsubscribe request. The `mid` variable matches the mid variable returned from the corresponding `unsubscribe()` call.

当代理响应退订请求时调用。`mid`变量与从相应的`unsubscribe()`调用返回的mid变量匹配。

##### ON_LOG()

```python
on_log(client, userdata, level, buf)
```

Called when the client has log information. Define to allow debugging. The `level` variable gives the severity of the message and will be one of `MQTT_LOG_INFO`, `MQTT_LOG_NOTICE`, `MQTT_LOG_WARNING`, `MQTT_LOG_ERR`, and `MQTT_LOG_DEBUG`. The message itself is in `buf`.

当客户端具有日志信息时调用。 定义以允许调试。`level`变量给出消息的严重性，将是`MQTT_LOG_INFO`， `MQTT_LOG_NOTICE`，`MQTT_LOG_WARNING`，`MQTT_LOG_ERR`和`MQTT_LOG_DEBUG`之一。 消息本身在`buf`中。

This may be used at the same time as the standard Python logging, which can be enabled via the `enable_logger` method.

这可以与标准的Python日志记录同时使用，可以通过`enable_logger`方法启用。

##### ON_SOCKET_OPEN()

```python
on_socket_open(client, userdata, sock)
```

Called when the socket has been opened. Use this to register the socket with an external event loop for reading.

socket打开时调用。 使用此寄存器将socket注册到外部事件循环以进行读取。

##### ON_SOCKET_CLOSE()

```python
on_socket_close(client, userdata, sock)
```

Called when the socket is about to be closed. Use this to unregister a socket from an external event loop for reading.

在socket即将关闭时调用。 使用它从外部事件循环中注销socket以进行读取。

##### ON_SOCKET_REGISTER_WRITE()

```python
on_socket_register_write(client, userdata, sock)
```

Called when a write operation to the socket failed because it would have blocked, e.g. output buffer full. Use this to register the socket with an external event loop for writing.

当对socket的写操作由于阻塞而失败时调用，例如 输出缓冲区已满。 使用此寄存器将socket注册到外部事件循环以进行写入。

##### ON_SOCKET_UNREGISTER_WRITE()

```python
on_socket_unregister_write(client, userdata, sock)
```

Called when a write operation to the socket succeeded after it had previously failed. Use this to unregister the socket from an external event loop for writing.

在socket先前失败之后成功对其进行写操作时调用。 使用此命令从外部事件循环注销socket以进行写入。

#### External event loop support 外部事件循环支持

##### LOOP_READ()

```python
loop_read(max_packets=1)
```

Call when the socket is ready for reading. `max_packets` is obsolete and should be left unset.

当socket准备读取时调用。`max_packets`已过时，应保留为未设置状态。

##### LOOP_WRITE()

```python
loop_write(max_packets=1)
```

Call when the socket is ready for writing. `max_packets` is obsolete and should be left unset.

当socket准备好写入时调用。 `max_packets`已过时，应保留为未设置状态。

##### LOOP_MISC()

```python
loop_misc()
```

Call every few seconds to handle message retrying and pings.

每隔几秒钟打电话一次，以处理消息重试和ping操作。

##### SOCKET()

```
socket()
```

Returns the socket object in use in the client to allow interfacing with other event loops. This call is particularly useful for [select](https://docs.python.org/3/library/select.html#select.select) based loops. See `examples/loop_select.py`.

返回客户端中使用的socket对象，以允许与其他事件循环进行交互。 对于基于 [select](https://docs.python.org/3/library/select.html#select.select) 的循环，此调用特别有用。 参见`examples / loop_select.py`。

##### WANT_WRITE()

```
want_write()
```

Returns true if there is data waiting to be written, to allow interfacing the client with other event loops. This call is particularly useful for [select](https://docs.python.org/3/library/select.html#select.select) based loops. See `examples/loop_select.py`.

如果有等待写入的数据，则返回true，以允许客户端与其他事件循环连接。 对于基于 [select](https://docs.python.org/3/library/select.html#select.select) 的循环，此调用特别有用。 参见`examples / loop_select.py`。

##### STATE CALLBACKS  状态回调

```
on_socket_open
on_socket_close
on_socket_register_write
on_socket_unregister_write
```

Use these callbacks to get notified about state changes in the socket. This is particularly useful for event loops where you register or unregister a socket for reading+writing. See `examples/loop_asyncio.py` for an example.

使用这些回调可获取有关socket状态更改的通知。 这对于事件循环特别有用，在事件循环中，您注册或注销socket以进行读写。 有关示例，请参见`examples / loop_asyncio.py`。

When the socket is opened, `on_socket_open` is called. Register the socket with your event loop for reading.

打开socket后，将调用`on_socket_open`。 在事件循环中注册socket以进行读取。

When the socket is about to be closed, `on_socket_close` is called. Unregister the socket from your event loop for reading.

当socket即将关闭时，调用`on_socket_close`。 从事件循环中注销socket以进行读取。

When a write to the socket failed because it would have blocked, e.g. output buffer full, `on_socket_register_write` is called. Register the socket with your event loop for writing.

如果对socket的写操作由于被阻止而失败，例如 如果输出缓冲区已满，则调用`on_socket_register_write`。 在事件循环中注册socket以进行写入。

When the next write to the socket succeeded, `on_socket_unregister_write` is called. Unregister the socket from your event loop for writing.

当下一次成功写入socket时，将调用`on_socket_unregister_write`。 从事件循环中注销socket以进行写入。

The callbacks are always called in this order:

回调始终按以下顺序调用：

- `on_socket_open`
- Zero or more times:  零次或多次：
  - `on_socket_register_write`
  - `on_socket_unregister_write`
- `on_socket_close`

#### Global helper functions  全局助手功能

The client module also offers some global helper functions.

客户端模块还提供了一些全局帮助器功能。

`topic_matches_sub(sub, topic)` can be used to check whether a `topic` matches a `subscription`.

可用于检查`topic`是否与`subscription`相匹配。

For example:

例如：

> the topic `foo/bar` would match the subscription `foo/#` or `+/bar`
>
> 主题`foo/bar`将与订阅`foo/#`或`+/bar`匹配
>
> the topic `non/matching` would not match the subscription `non/+/+`
>
> 主题`non/matching` 与订阅`non/+/+`不匹配

`connack_string(connack_code)` returns the error string associated with a CONNACK result.

返回与CONNACK结果相关的错误字符串。

`error_string(mqtt_errno)` returns the error string associated with a Paho MQTT error number.

返回与Paho MQTT错误编号关联的错误字符串。

### Publish  发布

This module provides some helper functions to allow straightforward publishing of messages in a one-shot manner. In other words, they are useful for the situation where you have a single/multiple messages you want to publish to a broker, then disconnect with nothing else required.

该模块提供了一些帮助程序功能，以一种一次性的方式直接发布消息。 换句话说，它们适用于以下情况：您有一条/多条消息要发布到代理，然后断开连接而无需其他任何操作。

The two functions provided are `single()` and `multiple()`.

提供的两个函数是`single()`和`multiple()`。

#### Single 单次

Publish a single message to a broker, then disconnect cleanly.

将单个消息发布给代理，然后彻底断开连接。

```
single(topic, payload=None, qos=0, retain=False, hostname="localhost",
    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,
    protocol=mqtt.MQTTv311, transport="tcp")
```

##### PUBLISH SINGLE FUNCTION ARGUMENTS  发布单次方法的参数

- topic

  the only required argument must be the topic string to which the payload will be published.

  唯一必需的参数必须是有效负载将发布到的主题字符串。

- payload

  the payload to be published. If “” or None, a zero length payload will be published.

  要发布的有效负载。 如果为空或None，则将发布零长度的有效负载。

- qos

  the qos to use when publishing, default to 0.

  发布时要使用的qos，默认为0。

- retain

  set the message to be retained (True) or not (False).

  将邮件设置为保留（True）或不保留（False）。

- hostname

  a string containing the address of the broker to connect to. Defaults to localhost.

  包含要连接的代理地址的字符串。 默认为localhost。

- port

  the port to connect to the broker on. Defaults to 1883.

  连接到代理的端口。 默认为1883。

- client_id

  the MQTT client id to use. If “” or None, the Paho library will generate a client id automatically.

  使用的MQTT客户端ID。 如果为空或None，则Paho库将自动生成一个客户端ID。

- keepalive

  the keepalive timeout value for the client. Defaults to 60 seconds.

  客户端的keepalive超时值。 默认为60秒。

- will

  a dict containing will parameters for the client:will = {‘topic’: “<topic>”, ‘payload’:”<payload”>, ‘qos’:<qos>, ‘retain’:<retain>}.Topic is required, all other parameters are optional and will default to None, 0 and False respectively.Defaults to None, which indicates no will should be used.

  包含客户端的will参数的字典：will = {‘topic’: “<topic>”, ‘payload’:”<payload”>, ‘qos’:<qos>, ‘retain’:<retain>}。主题 是必需的，所有其他参数都是可选的，分别默认为None，0和False。默认为None，表示不应该使用will。

- auth

  a dict containing authentication parameters for the client:auth = {‘username’:”<username>”, ‘password’:”<password>”}Username is required, password is optional and will default to None if not provided.Defaults to None, which indicates no authentication is to be used.

  包含客户端身份验证参数的字典：auth = {‘username’:”<username>”, ‘password’:”<password>”}用户名是必需的，密码是可选的，如果未提供，则默认为None。 无，表示不使用身份验证。

- tls

  a dict containing TLS configuration parameters for the client:dict = {‘ca_certs’:”<ca_certs>”, ‘certfile’:”<certfile>”, ‘keyfile’:”<keyfile>”, ‘tls_version’:”<tls_version>”, ‘ciphers’:”<ciphers”>}ca_certs is required, all other parameters are optional and will default to None if not provided, which results in the client using the default behaviour - see the paho.mqtt.client documentation.Defaults to None, which indicates that TLS should not be used.

  包含客户端的TLS配置参数的字典：ddict = {‘ca_certs’:”<ca_certs>”, ‘certfile’:”<certfile>”, ‘keyfile’:”<keyfile>”, ‘tls_version’:”<tls_version>”, ‘ciphers’:”<ciphers”>} ca_certs是必需的，所有其他参数都是可选的，如果未提供，则默认为无，这将导致客户端使用默认行为-请参阅paho.mqtt.client文档。 默认为无，表示不应该使用TLS。

- protocol

  choose the version of the MQTT protocol to use. Use either `MQTTv31` or `MQTTv311`.

  选择要使用的MQTT协议的版本。 使用`MQTTv31`或`MQTTv311`。

- transport

  set to “websockets” to send MQTT over WebSockets. Leave at the default of “tcp” to use raw TCP.
  
  设置为“ websockets”以通过WebSocket发送MQTT。 保留默认值“ tcp”以使用原始TCP。

##### PUBLISH SINGLE EXAMPLE 一次发布单个的示例

```python
import paho.mqtt.publish as publish

publish.single("paho/test/single", "payload", hostname="mqtt.eclipse.org")
```

#### Multiple 多次

Publish multiple messages to a broker, then disconnect cleanly.

将多个消息发布到代理，然后彻底断开连接。

```python
multiple(msgs, hostname="localhost", port=1883, client_id="", keepalive=60,
    will=None, auth=None, tls=None, protocol=mqtt.MQTTv311, transport="tcp")
```

##### PUBLISH MULTIPLE FUNCTION ARGUMENTS  发布多次方法的参数

- msgs

  a list of messages to publish. Each message is either a dict or a tuple.If a dict, only the topic must be present. Default values will be used for any missing arguments. The dict must be of the form:msg = {‘topic’:”<topic>”, ‘payload’:”<payload>”, ‘qos’:<qos>, ‘retain’:<retain>}topic must be present and may not be empty. If payload is “”, None or not present then a zero length payload will be published. If qos is not present, the default of 0 is used. If retain is not present, the default of False is used.If a tuple, then it must be of the form:(“<topic>”, “<payload>”, qos, retain)
  
  要发布的消息列表。 每条消息要么是一个字典，要么是一个元组。 默认值将用于所有缺少的参数。 dict的格式必须为：msg = {‘topic’:”<topic>”, ‘payload’:”<payload>”, ‘qos’:<qos>, ‘retain’:<retain>} topic必须是 存在且不能为空。 如果有效载荷为“”，无或不存在，则将发布零长度的有效载荷。 如果不存在qos，则使用默认值0。 如果不存在保留，则使用默认值False。如果是元组，则其格式必须为：(“<topic>”, “<payload>”, qos, retain)

See `single()` for the description of `hostname`, `port`, `client_id`, `keepalive`, `will`, `auth`, `tls`, `protocol`, `transport`.

请参阅`single（）`中有关`hostname`, `port`, `client_id`, `keepalive`, `will`, `auth`, `tls`, `protocol`, `transport`.的描述。

##### PUBLISH MULTIPLE EXAMPLE 一次发布多个的示例

```python
import paho.mqtt.publish as publish

msgs = [{'topic':"paho/test/multiple", 'payload':"multiple 1"},
    ("paho/test/multiple", "multiple 2", 0, False)]
publish.multiple(msgs, hostname="mqtt.eclipse.org")
```

### Subscribe  订阅

This module provides some helper functions to allow straightforward subscribing and processing of messages.

此模块提供了一些帮助程序功能，以允许直接订阅和处理消息。

The two functions provided are `simple()` and `callback()`.

提供的两个函数是`simple（）`和`callback（）`。

#### Simple  简单

Subscribe to a set of topics and return the messages received. This is a blocking function.

订阅一组主题并返回收到的消息。 这是一个阻塞功能。

```python
simple(topics, qos=0, msg_count=1, retained=False, hostname="localhost",
    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,
    protocol=mqtt.MQTTv311)
```

##### SIMPLE SUBSCRIBE FUNCTION ARGUMENTS  简单的订阅功能参数

- topics

  the only required argument is the topic string to which the client will subscribe. This can either be a string or a list of strings if multiple topics should be subscribed to.

  唯一需要的参数是客户端将订阅的主题字符串。 如果应该订阅多个主题，则可以是字符串，也可以是字符串列表。

- qos

  the qos to use when subscribing, defaults to 0.

  订阅时使用的qos，默认为0。

- msg_count

  the number of messages to retrieve from the broker. Defaults to 1. If 1, a single MQTTMessage object will be returned. If >1, a list of MQTTMessages will be returned.

  从代理检索的消息数。 默认值为1。如果为1，将返回单个MQTTMessage对象。 如果> 1，将返回MQTTMessages列表。

- retained

  set to True to consider retained messages, set to False to ignore messages with the retained flag set.

  设置为True以考虑保留的消息，设置为False忽略设置了保留标志的消息。

- hostname

  a string containing the address of the broker to connect to. Defaults to localhost.

  包含要连接的代理地址的字符串。 默认为localhost。

- port

  the port to connect to the broker on. Defaults to 1883.

  连接到代理的端口。 默认为1883。

- client_id

  the MQTT client id to use. If “” or None, the Paho library will generate a client id automatically.

  使用的MQTT客户端ID。 如果为空或None，则Paho库将自动生成一个客户端ID。

- keepalive

  the keepalive timeout value for the client. Defaults to 60 seconds.

  客户端的keepalive超时值。 默认为60秒。

- will

  a dict containing will parameters for the client:will = {‘topic’: “<topic>”, ‘payload’:”<payload”>, ‘qos’:<qos>, ‘retain’:<retain>}.Topic is required, all other parameters are optional and will default to None, 0 and False respectively.Defaults to None, which indicates no will should be used.

  包含客户端的意志参数的字典：will = {‘topic’: “<topic>”, ‘payload’:”<payload”>, ‘qos’:<qos>, ‘retain’:<retain>}。主题 是必需的，所有其他参数都是可选的，分别默认为None，0和False。默认为None，表示不应该使用will。

- auth

  a dict containing authentication parameters for the client:auth = {‘username’:”<username>”, ‘password’:”<password>”}Username is required, password is optional and will default to None if not provided.Defaults to None, which indicates no authentication is to be used.

  包含客户端身份验证参数的字典：auth = {‘username’:”<username>”, ‘password’:”<password>”}用户名是必需的，密码是可选的，如果未提供，则默认为None。 无，表示不使用身份验证。

- tls

  a dict containing TLS configuration parameters for the client:dict = {‘ca_certs’:”<ca_certs>”, ‘certfile’:”<certfile>”, ‘keyfile’:”<keyfile>”, ‘tls_version’:”<tls_version>”, ‘ciphers’:”<ciphers”>}ca_certs is required, all other parameters are optional and will default to None if not provided, which results in the client using the default behaviour - see the paho.mqtt.client documentation.Defaults to None, which indicates that TLS should not be used.

  包含客户端的TLS配置参数的字典：dict = {‘ca_certs’:”<ca_certs>”, ‘certfile’:”<certfile>”, ‘keyfile’:”<keyfile>”, ‘tls_version’:”<tls_version>”, ‘ciphers’:”<ciphers”>} ca_certs是必需的，所有其他参数都是可选的，如果未提供，则默认为无，这将导致客户端使用默认行为-请参阅paho.mqtt.client文档。 默认为无，表示不应该使用TLS。

- protocol

  choose the version of the MQTT protocol to use. Use either `MQTTv31` or `MQTTv311`.
  
  选择要使用的MQTT协议的版本。 使用`MQTTv31`或`MQTTv311`。

##### SIMPLE EXAMPLE  简单的例子

```python
import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("paho/test/simple", hostname="mqtt.eclipse.org")
print("%s %s" % (msg.topic, msg.payload))
```

#### Using Callback 使用回调

Subscribe to a set of topics and process the messages received using a user provided callback.

订阅一组主题并使用用户提供的回调处理收到的消息。

```python
callback(callback, topics, qos=0, userdata=None, hostname="localhost",
    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,
    protocol=mqtt.MQTTv311)
```

##### CALLBACK SUBSCRIBE FUNCTION ARGUMENTS  回调订阅功能参数

- callback

  an “on_message” callback that will be used for each message received, and of the form`def on_message(client, userdata, message) `

  一个“ on_message”回调，将用于接收到的每条消息，格式为`def on_message(client, userdata, message) `

- topics

  the topic string to which the client will subscribe. This can either be a string or a list of strings if multiple topics should be subscribed to.

  客户端将订阅的主题字符串。 如果应该订阅多个主题，则可以是字符串，也可以是字符串列表。

- qos

  the qos to use when subscribing, defaults to 0.

  订阅时使用的qos，默认为0。

- userdata

  a user provided object that will be passed to the on_message callback when a message is received.
  
  用户提供的对象，将在收到消息时传递给on_message回调。

See `simple()` for the description of `hostname`, `port`, `client_id`, `keepalive`, `will`, `auth`, `tls`, `protocol`.

请参阅`simple（）`中有关`hostname`，`port`，`client_id`，`keepalive`，`will`，`auth`，`tls`，`protocol`的描述。

##### CALLBACK EXAMPLE  回调示例

```python
import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

subscribe.callback(on_message_print, "paho/test/callback", hostname="mqtt.eclipse.org")
```

## Reporting bugs  报告错误

Please report bugs in the issues tracker at https://github.com/eclipse/paho.mqtt.python/issues.

请通过https://github.com/eclipse/paho.mqtt.python/issues报告问题跟踪器中的错误。

## More information  更多信息

Discussion of the Paho clients takes place on the [Eclipse paho-dev mailing list](https://dev.eclipse.org/mailman/listinfo/paho-dev).

关于Paho客户的讨论在[Eclipse paho-dev邮件列表](https://dev.eclipse.org/mailman/listinfo/paho-dev)上进行。

General questions about the MQTT protocol itself (not this library) are discussed in the [MQTT Google Group](https://groups.google.com/forum/?fromgroups#!forum/mqtt).

[MQTT Google网上论坛](https://groups.google.com/forum/?fromgroups#!forum/mqtt)中讨论了有关MQTT协议本身（不是此库）的一般问题。

There is much more information available via the [MQTT community site](http://mqtt.org/).

可通过[MQTT社区网站](http://mqtt.org/)获得更多信息。