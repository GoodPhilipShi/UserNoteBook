## 关键点: apt-get --fix-broken install/apt-get -f install
`E: 有未能满足的依赖关系。请尝试不指明软件包的名字来运行“apt-get --fix-broken install”`

初步解决方法: 

```shell
sudo apt-get --fix-broken install
```

```
dpkg: 处理归档 /var/cache/apt/archives/nodejs_12.16.3-1_mips64el.deb (--unpack)时出错：
 正试图覆盖 /usr/include/node/common.gypi，它同时被包含于软件包 libnode-dev 14.16.1~dfsg-1.lnd.5
dpkg-deb: 错误: 粘贴 子进程被信号(断开的管道) 终止了
在处理时有错误发生：
 /var/cache/apt/archives/nodejs_12.16.3-1_mips64el.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

当提示重写文件发生冲突时，可以选择强制重写文件

```shell
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nodejs_12.16.3-1_mips64el.deb
```

```shell
sudo dpkg -i --force-overwrite [文件名]
```