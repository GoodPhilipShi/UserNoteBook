# 创建ZeroTier for Docker

## 步骤1: 确认TUN是否存在
```bash
ls /dev/net/tun
```
>如果没有回应(`/dev/net/tun`)
>则要么没有TUN需要手动创建, 要么创建了但是忘记路径了(这个就自己想办法)

## 步骤1.5: 创建TUN

### 0. 打开SSH端口(默认22)

### 1. 通过SSH连接NAS

```COMMAND
ssh NAS账号@NAS的IP:SSH端口
```

### 2. 进入ROOT权限

```bash
sudo -i
```

### 3. 将脚本写入 */usr/local/etc/rc.d/tun.sh* 将在启动时设置 */dev/net/tun*

```bash
echo -e '#!/bin/sh -e \ninsmod /lib/modules/tun.ko' > /usr/local/etc/rc.d/tun.sh
```

### 4. 赋予权限

```bash
chmod a+x /usr/local/etc/rc.d/tun.sh
```

### 5.  运行脚本

```bash
/usr/local/etc/rc.d/tun.sh
```

### 6. 然后重复 [[#步骤1 确认TUN是否存在|步骤1]]

## 步骤2: 创建容器(运行映像)

>!!这里是使用`/volume1/docker/ZeroTier/`作为ZeroTier的数据文件存储路径，所以这个文件夹必须存在

```bash
docker run -d           \
  --name ZeroTier             \
  --restart=always      \
  --device=/dev/net/tun \
  --net=host            \
  --cap-add=NET_ADMIN   \
  --cap-add=SYS_ADMIN   \
  -v /volume1/docker/ZeroTier/:/volume1/docker/ZeroTier/ zerotier/zerotier-synology:latest
```

# 使用方法

## 查看状态

### 命令行

```bash
docker exec -it ZeroTier zerotier-cli status
```

### 图形化

![[Pasted image 20220122233651.png]]

## 加入网络

### 命令行

```bash
docker exec -it ZeroTier zerotier-cli join 创建好的虚拟网络ID
```

### 图形化

![[Pasted image 20220122233731.png]]

## 列出已加入的网络

### 命令行

```bash
docker exec -it ZeroTier zerotier-cli listnetworks
```

### 图形化

![[Pasted image 20220122233750.png]]