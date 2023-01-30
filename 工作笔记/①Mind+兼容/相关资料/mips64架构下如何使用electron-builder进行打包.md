麒麟官方实现了

[麒麟生态](https://eco.kylinos.cn/document/science.html)

具体文档《银河麒麟桌面操作系统V10electron应用开发者指南》下载连接如下:

[银河麒麟桌面操作系统V10electron应用开发者指南.pdf](https://eco.kylinos.cn/home/plugs/download/id/37500.html)

> 具体内容，请搜索`4.4.打包（electron-builder 方式`

太过繁琐，但是成功的话打包也许会很轻松

通过 [electron-packager](https://github.com/electron/electron-packager) 和 [electron-installer-debian](https://github.com/electron-userland/electron-installer-debian) 实现打包, 会先复制全部项目内容到`/tmp/`进行处理，然后再复制到指定的位置(`electron-packager . mindPlus --out ./scratch/`)`./scratch`。但是对于Mind+来说就太过麻瓜了，会爆出`ENOSPC: no space left on device, copyfile 'Arduino/hardware/tools/maixduino/kflash/1.0.2/kflash' -> '/tmp/electron-packager/linux-mips64el/mindPlus-linux-mips64el/resources/app/Arduino/hardware/tools/maixduino/kflash/1.0.2/kflash'`类似的问题

ps： 记得修改`node_modules/electron-packager/src/targets.js`文件

```diff
  const buildVersions = {
    darwin: {
      arm64: '>= 11.0.0-beta.1',
      universal: '>= 11.0.0-beta.1'
    },
    linux: {
      arm64: '>= 1.8.0',
-     mips64el: '^1.8.2-beta.5'
+     mips64el: '>= 1.8.2-beta.5'
    },
    mas: {
      arm64: '>= 11.0.0-beta.1',
      universal: '>= 11.0.0-beta.1'
    },
    win32: {
      arm64: '>= 6.0.8'
    }
  }
```