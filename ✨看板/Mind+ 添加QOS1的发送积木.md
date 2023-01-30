
# 上传模式调研结果

## 调研上传模式下的MQTT是否存在Qos选项

>[!NOTE] 查找方法
>通过`MQTT`积木的`block-generator`代码查询所调用的`addInclude`的参数
>![[Pasted image 20230103093440.png]]
>然后再在`mindPlus\Arduino\libraries`文件夹中搜索相应的`.h`文件

### ❌ESP8266 AC 网络 MQTT

![[Pasted image 20230103094513.png]]

>E:\1workspace\mindPlus\Arduino\libraries\DFRobot_Esp8266MQTT\DFRobot_Esp8266MQTT.h

![[Pasted image 20221228145455.png]]

> [!TIP]- ESP8266 无MPY模式
> ![[Pasted image 20230103094623.png]]


### ❌掌控(ESP32) AC 网络 MQTT

![[Pasted image 20230103094930.png]]

> E:\1workspace\mindPlus\Arduino\libraries\DFRobot_Iot\DFRobot_Iot.h

![[Pasted image 20230103095107.png]]


### ✔掌控(ESP32) MPY 网络 MQTT

![[Pasted image 20230103095735.png]]

>[!TIP]- 仓库路径
>[mpython/simple.py at master · labplus-cn/mpython · GitHub](https://github.com/labplus-cn/mpython/blob/master/port/modules/umqtt/simple.py)

![[Pasted image 20230103100813.png]]

> [!INFO] 生成代码位置
> src\lib\block-generator\MicroPython\internetService\mqtt.js:147
> 生成代码涉及到其他主板

### ❌RMTT(ESP32) AC 网络 MQTT

![[Pasted image 20230103121830.png]]

库等同于 [[#❌掌控(ESP32) AC 网络 MQTT]]

### ❌RMTT(ESP32) MPY 网络 MQTT

![[Pasted image 20230103121903.png]]

> 没有网络模块

### ✔Maixduino MPY 网络 MQTT

![[Pasted image 20230103102305.png]]

>[!TIP]- 仓库路径
> [dfrobotcd/MaixduinoFirmware of Gitee](https://gitee.com/dfrobotcd/MaixduinoFirmware)
> 
> 不过我没有权限

![[02Y95ENA@LYT@H$W2}@PMY1.png]]

### ❌FireBeetle ESP32-E AC 网络 MQTT

![[Pasted image 20230103102550.png]]

库等同于 [[#❌掌控(ESP32) AC 网络 MQTT]]

> [!TIP]- FireBeetle ESP32-E 无MPY模式
> ![[Pasted image 20230103102918.png]]

### ❌FireBeetle ESP32 AC 网络 MQTT

![[Pasted image 20230103102950.png]]

库等同于 [[#❌掌控(ESP32) AC 网络 MQTT]]

> [!TIP]- FireBeetle ESP32 无MPY模式
> ![[Pasted image 20230103103007.png]]


## 调研上传模式下的Obloq是否存在Qos选项

### ❌Pico AC 通信 Obloq

![[Pasted image 20230103103244.png]]
> E:\1workspace\mindPlus\Arduino\libraries\Pico_Obloq\Pico_Obloq.h

![[Pasted image 20230103103457.png]]

### ❌Pico MPY 通信 Obloq

![[Pasted image 20230103104735.png]]

> 没有通信模块

### ❌ESP8266 AC 通信 Obloq

![[Pasted image 20230103121339.png]]

> 没有Obloq

### ❌Maixduino MPY 通信 Obloq

![[Pasted image 20230103121358.png]]

> 没有通信模块

### ❌RMTT(ESP32) AC 通信 Obloq

![[Pasted image 20230103121652.png]]

> 没有Obloq

### ❌RMTT(ESP32) MPY 通信 Obloq

![[Pasted image 20230103122039.png]]

> 没有通信模块

###  ❌FireBeetle ESP32-E AC 通信 Obloq

![[Pasted image 20230103122316.png]]

> 没有Obloq

###  ❌FireBeetle ESP32 AC 通信 Obloq

![[Pasted image 20230103122316.png]]

> 没有Obloq

### ❌Mega2560 AC 通信 Obloq

![[Pasted image 20230103131200.png]]

>E:\1workspace\mindPlus\Arduino\libraries\DFRobot_Obloq\DFRobot_Obloq.h

![[Pasted image 20221228145534.png]]


### ❌掌控(ESP32) AC 通信 Obloq

![[Pasted image 20230103122316.png]]

> 没有Obloq

### ❌掌控(ESP32) MPY 通信 Obloq

![[Pasted image 20230103131515.png]]

> 没有Obloq

### ❌Arduino Nano AC 通信 Obloq

![[Pasted image 20230103131618.png]]

>E:\1workspace\mindPlus\Arduino\libraries\DFRobot_Obloq_I2C\DFRobot_Obloq_I2C.h

![[Pasted image 20230103093246.png]]


![[Pasted image 20230103131633.png]]

> E:\1workspace\mindPlus\Arduino\libraries\UNO_Obloq\UNO_Obloq.h

![[Pasted image 20230103131742.png]]

### ❌Arduino UNO AC 通信 Obloq

![[Pasted image 20230103131839.png]]

库等同于[[#❌Arduino Nano AC 通信 Obloq]]

### ❌Leonardo AC 通信 Obloq

![[Pasted image 20230103131927.png]]

库等同于[[#❌Mega2560 AC 通信 Obloq]]

![[Pasted image 20230103132024.png]]

库等同于[[#❌Arduino Nano AC 通信 Obloq]]

### ❌micro:bit AC 通信 Obloq

![[Pasted image 20230103132209.png]]

库等同于[[#❌Leonardo AC 通信 Obloq]]

## 添加方案

已知上传模式下MPY的掌控、Maixduino可以配置Qos，并且函数雷同，参数一致
```python
def publish(self, topic, msg, retain=False, qos=0)
```

所以添加方案为: 

### VM

otherModules\scratch-vm\src\blocks\internetService\scratch3_mpyMqtt.js

>[!INFO]- 复制
>
>~~~javascript
>{
>    opcode: 'mpy_MQTTpublish',
>    text: formatMessage({
>        id: "gui.blocklyText.mpy.MQTTpublish",
>        description: 'MQTT publish to topic',
>        default: 'publish [DATA] to topic [TOPIC]'
>    }),
>    blockType: BlockType.COMMAND,
>    specials: { language: [LanguageMicropython], type: 'add' },
>    arguments: {
>        DATA: {
>            type: ArgumentType.STRING,
>            defaultValue: 'hello',
>            inputParams: { isQuote: { [LanguageMicropython]: true } },
>        },
>        TOPIC: {
>            type: ArgumentType.STRING,
>            defaultValue: 'topic1',
>            inputParams: { isQuote: { [LanguageMicropython]: true } },
>        }
>    }
>},

> [!TIP] 修改`opcode`的==命名==即可

> [!INFO] 粘贴
>
> ~~~javascript
> {
>     opcode: 'mpy_MQTTpublish_qos1',
>     text: formatMessage({
>         id: "gui.blocklyText.mpy.MQTTpublishQos1",
>         description: 'MQTT publish to topic',
>         default: 'publish [DATA] to topic [TOPIC]'
>     }),
>     blockType: BlockType.COMMAND,
>     specials: { language: [LanguageMicropython], type: 'add' },
>     arguments: {
>         DATA: {
>             type: ArgumentType.STRING,
>             defaultValue: 'hello',
>             inputParams: { isQuote: { [LanguageMicropython]: true } },
>         },
>         TOPIC: {
>             type: ArgumentType.STRING,
>             defaultValue: 'topic1',
>             inputParams: { isQuote: { [LanguageMicropython]: true } },
>         }
>     }
> },
> ~~~

> [!TIP]- 并且添加上`mpy_MQTTpublish_qos1`函数
>
> ~~~diff
>   mpy_MQTTpublish(args, util) {}
> + mpy_MQTTpublish_qos1(args, util) {}
> ~~~

### 代码生成 - 添加`mpy_MQTTpublish_qos1`的生成代码

src\lib\block-generator\MicroPython\internetService\mqtt.js

> [!TIP] 照着`mpy_MQTTpublish(block, parameter)`写

```diff
mpy_MQTTpublish_qos1(block, parameter) {
    let data = parameter.DATA.code;
    let topic = parameter.TOPIC.code;
    this.addImport(this.board === 'maixduino' ? 'from umqtt import MQTTClient' : 'from umqtt.simple import MQTTClient');
    this.addCode(`mqtt.publish(str(${topic}), str(${data}).encode('utf-8'), qos=1)`);
}
```

### 添加翻译

> otherModules\scratch-l10n\editor\extensions

> [!TIP] 紧跟`gui.blocklyText.mpy.MQTTpublish`进行添加翻译

```
"gui.blocklyText.mpy.MQTTpublishQos1": "publish Qos1 message [DATA] to topic [TOPIC]",
"gui.blocklyText.mpy.MQTTpublishQos1": "发布Qos1消息 [DATA] 至 主题 [TOPIC]",
```

## 测试

### Maixduino

![[Pasted image 20230103143410.png]]

### 掌控板
![[3WO@)_CR[HM]6KP(BYJA}WF.png]]

![[Pasted image 20230103154209.png]]

# 实时模式调研结果

## ✔调研是否存在QOS选项

![[Pasted image 20230103154805.png]]

>otherModules\scratch-vm\src\blocks\internetService\scratch3_mqtt.js

```javascript
mqtt_mqttSend (args, util) { //发送消息
    if (this.product.pageIndex !== 0) return;
    return this.mqtt.mqttSend(args.TOPIC, args.MSG);
}
```

>[!TIP]- 通过`mqttSend`跳转到封装模块文件`mqtt.js`
>otherModules\scratch-vm\src\modules\mqtt.js

```javascript
mqttSend(topicKey, message) {
    return new Promise((resolve) => {
        if (this.client && this.connectedFlag) {
            this.client.publish(this.topicObj[topicKey], message.toString(), { qos: 0, retain: false }, () => {
                resolve();
            });
        } else {
            resolve();
        }
    })
}
```

## 添加方案

>[!INFO] 方案
>1. 在封装的`mqttSend`添加Qos参数
>2. 重新封装一个`mqttSend` --> `mqttSendQos1`
>>[!success] 选择方案1

### 修改`mqttSend`


```diff
-   mqttSend(topicKey, message) {
+   mqttSend(topicKey, message, qos=1) {
        return new Promise((resolve) => {
            if (this.client && this.connectedFlag) {
-               this.client.publish(this.topicObj[topicKey], message.toString(), { qos: 0, retain: false }, () => {
+               this.client.publish(this.topicObj[topicKey], message.toString(), { qos: qos, retain: false }, () => {
                    resolve();
                });
            } else {
                resolve();
            }
        })
    }
```

### 添加积木

> [!TIP] 基于`mqtt_mqttSend`的积木代码修改

```javascript
{
    opcode: 'mqtt_mqttSend_Qos1',
    isEdgeActivated: false,
    shouldRestartExistingThreads: false,
    blockType: BlockType.COMMAND,
    text: formatMessage({
        id: 'gui.blocklyText.mqtt.mqttSendQos1',
        description: 'block msg for mqttSend',
        default: 'mqtt send message [MSG] to cloud platform [TOPIC]'
    }),
    arguments: {
        MSG: {
            type: ArgumentType.STRING,
            defaultValue: 'hello',
            dfCheck: {[LanguageCpp]: DataType.NUMBER.concat([DataType.STRING])}
        },
        TOPIC: {
            type: ArgumentType.STRING,
            menu: 'topicMenu',
            onlyField: true,
            options: buildFieldMenu(TOPIC, "A"),
            defaultValue: TOPIC.A
        }
    },
    prompts: getPrompts(board, 'mqtt.mqtt_mqttSend_Qos1')
},
```

> [!TIP] 注意
>
> 记得在
>
> ~~~javascript
> mqtt_mqttSend (args, util) { //发送消息
>     if (this.product.pageIndex !== 0) return;
>     return this.mqtt.mqttSend(args.TOPIC, args.MSG);
> }
> ~~~
>
> 后面添加
>
> ~~~javascript
> mqtt_mqttSend_Qos1 (args, util) { //发送消息
>     if (this.product.pageIndex !== 0) return;
>     return this.mqtt.mqttSend(args.TOPIC, args.MSG, 1);
> }
> ~~~

### 添加翻译

```
"gui.blocklyText.mqtt.mqttSendQos1": "MQTT send Qos1 message [MSG] to cloud platform [TOPIC]",
"gui.blocklyText.mqtt.mqttSendQos1": "MQTT 发送Qos1消息[MSG]至[TOPIC]",
"gui.blocklyText.mqtt.mqttSendQos1": "MQTT 發送Qos1消息[MSG]至[TOPIC]",
```

## 测试

![[Pasted image 20230103162134.png]]

# Python 模式添加

>[!TIP]- 在siot 1.0.3版本之前
>![[Pasted image 20230103164427.png]]
>
>![[Pasted image 20230103163906.png]]
>
>由于`siot`库在封装的时候，没有预留出Qos的选项，所以无法添加发送Qos1的积木

目前已知最新版本的siot库(v1.0.3), 已经添加上了一个`publish_save`的函数

![[4VDD``BR_G[DY)VXR~HBNBQ.png]]

按照[[#添加方案]]类似的方法添加即可