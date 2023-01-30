
## 修改src\lib\python\ssh-manage\pip-updateversion-list.js

```diff
 const updateInnerPipList = {
     common: null,
     unihiker: [
         { name: 'pinpong', version: '0.5.0', filename: 'pinpong-0.5.0-py3-none-any.whl' },
+        { name: "siot", version: "0.1.3", filename: "siot-0.1.3-py3-none-any.whl"}
     ]
 };
```

## 添加`siot.whl`文件到`E:\1workspace\mindPlus\resources\static\pip\remote-ssh\unihiker`

![[Pasted image 20230110112816.png]]

## 服务器文件修改

>[!TIP] 路径 ==/var/www/html/MindPlus/Python/resource/ssh/unihiker/==

1. 删除`pinpong-0.4.9-py3-none-any.whl`
2. 添加`siot-0.1.3-py3-none-any.whl`

## 修改拉取资源脚本

>[!TIP] 路径 ==compat\update-resources.py==

## 修改发送Qos1消息积木描述



![[Pasted image 20230110112631.png]]