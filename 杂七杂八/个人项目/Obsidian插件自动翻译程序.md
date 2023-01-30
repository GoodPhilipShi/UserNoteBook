[[./A/translatePlugins.py|项目文件所在(右键打开文件所在位置)]]
# 项目描述
Obsidian插件自动翻译程序 是基于Google翻译API实现的针对Obsidian插件菜单\信息的一个翻译软件

# 项目要求
- [x] 减少个人干预
- [x] 懒人一键模式
- [x] 多任务

# 实现方式

> 技术: *Python*、*[GitHub - foyoux/pygtrans: 谷歌翻译, 支持 APIKEY](https://github.com/foyoux/pygtrans)*

1. 通过正则表达式提取出待翻译的信息
2. 将待翻译的信息通过谷歌翻译
3. 最后将翻译好的信息通过 <u>正则表达式</u> 进行替换

# 改进空间

1. 实现免FQ翻译
    > 不知道为什么使用[Google 翻译](https://translate.google.cn/)来进行翻译会
    > `requests.exceptions.ConnectionError: HTTPSConnectionPool(host='translate.google.cn', port=443): Max retries exceeded with url: /translate_a/t?tl=zh-CN&sl=auto&ie=UTF-8&oe=UTF-8&client=at&dj=1&format=html&v=1.0 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x037C28B0>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。'))`
2. 实现GUI化

# 未来预想

1. GUI版本
2. 拖拽插件文件夹，进行翻译
3. 向MT管理器的翻译功能看齐