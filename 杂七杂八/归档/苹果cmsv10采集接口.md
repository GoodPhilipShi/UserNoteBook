## 苹果cmsAPI接口说明

> http://www.360doc.com/content/20/0211/22/30583588_891365559.shtml
>
> https://zy.yilans.net/help/

### 基本的接口解析

#### 视频列表详情-vod/?ac=list

`http://域名/api.php/provide/vod/?ac=list`

```json
例子链接:http://zy.yilans.net/api.php/provide/vod/?ac=list
{"code":1,"msg":"\u6570\u636e\u5217\u8868","page":1,"pagecount":10236,"limit":"10","total":102357,"list":[{"vod_id":159147,"vod_name":"\u65b0\u95fb30\u5206","type_id":3,"type_name":"\u7efc\u827a","vod_en":"xinwen30fen","vod_time":"2020-10-22 12:30:48","vod_remarks":"\u66f4\u65b0\u81f32020-10-16\u671f","vod_play_from":"cntv,qiyi"},{"vod_id":242547,"vod_name":"\u65b0\u95fb\u76f4\u64ad\u95f4","type_id":3,"type_name":"\u7efc\u827a","vod_en":"xinwenzhibojian","vod_time":"2020-10-22 12:30:47","vod_remarks":"\u66f4\u65b0\u81f32020-10-16\u671f","vod_play_from":"qiyi"},{"vod_id":158749,"vod_name":"\u5927\u63ed\u79d8","type_id":3,"type_name":"\u7efc\u827a","vod_en":"dajiemi","vod_time":"2020-10-22 12:30:44","vod_remarks":"\u66f4\u65b0\u81f32020-10-16\u671f","vod_play_from":"qiyi,sohu"},{"vod_id":158596,"vod_name":"\u517b\u751f\u5802","type_id":3,"type_name":"\u7efc\u827a","vod_en":"yangshengtang","vod_time":"2020-10-22 12:30:44","vod_remarks":"\u66f4\u65b0\u81f32020-10-16\u671f","vod_play_from":"qiyi,sohu,mgtv,wasu,qq,youku"},{"vod_id":242492,"vod_name":"\u5996\u624b\u6467\u82b1","type_id":21,"type_name":"\u9b54\u5e7b\u7247","vod_en":"yaoshoucuihua","vod_time":"2020-10-22 12:30:43","vod_remarks":"\u9ad8\u6e05\u6b63\u7247","vod_play_from":"qq"},{"vod_id":242484,"vod_name":"\u5e73\u884c\u8ff7\u9014","type_id":13,"type_name":"\u56fd\u4ea7\u5267","vod_en":"pingxingmitu","vod_time":"2020-10-22 12:30:42","vod_remarks":"\u66f4\u65b0\u81f36\/\u517118\u96c6","vod_play_from":"youku"},{"vod_id":261109,"vod_name":"\u6211\u51ed\u672c\u4e8b\u5355\u8eab","type_id":13,"type_name":"\u56fd\u4ea7\u5267","vod_en":"wopingbenshidanshen","vod_time":"2020-10-22 12:30:42","vod_remarks":"\u66f4\u65b0\u81f36\u96c6","vod_play_from":"youku"},{"vod_id":242279,"vod_name":"\u6821\u56ed\u5973\u5927\u5175","type_id":13,"type_name":"\u56fd\u4ea7\u5267","vod_en":"xiaoyuannvdabing","vod_time":"2020-10-22 12:30:40","vod_remarks":"\u66f4\u65b0\u81f321\/\u517126\u96c6","vod_play_from":"youku"},{"vod_id":158562,"vod_name":"\u7efc\u827a\u5927\u7206\u70b8","type_id":3,"type_name":"\u7efc\u827a","vod_en":"zongyidabaozha","vod_time":"2020-10-22 12:30:36","vod_remarks":"\u66f4\u65b0\u81f32020-10-16\u671f","vod_play_from":"qq"},{"vod_id":158568,"vod_name":"\u7ecf\u5178\u4f20\u5947","type_id":3,"type_name":"\u7efc\u827a","vod_en":"jingdianchuanqi","vod_time":"2020-10-22 12:30:34","vod_remarks":"\u66f4\u65b0\u81f32020-10-16\u671f","vod_play_from":"qq,qiyi,sohu,pptv,youku"}],"class":[{"type_id":1,"type_name":"\u7535\u5f71"},{"type_id":2,"type_name":"\u8fde\u7eed\u5267"},{"type_id":3,"type_name":"\u7efc\u827a"},{"type_id":4,"type_name":"\u52a8\u6f2b"},{"type_id":5,"type_name":"8090\u5f71\u89c6\u5a31\u4e50\u8d44\u8baf"},{"type_id":6,"type_name":"\u52a8\u4f5c\u7247"},{"type_id":7,"type_name":"\u559c\u5267\u7247"},{"type_id":8,"type_name":"\u7231\u60c5\u7247"},{"type_id":9,"type_name":"\u79d1\u5e7b\u7247"},{"type_id":10,"type_name":"\u6050\u6016\u7247"},{"type_id":11,"type_name":"\u5267\u60c5\u7247"},{"type_id":12,"type_name":"\u6218\u4e89\u7247"},{"type_id":13,"type_name":"\u56fd\u4ea7\u5267"},{"type_id":14,"type_name":"\u6e2f\u53f0\u5267"},{"type_id":15,"type_name":"\u65e5\u97e9\u5267"},{"type_id":16,"type_name":"\u6b27\u7f8e\u5267"},{"type_id":20,"type_name":"\u60ca\u609a\u7247"},{"type_id":21,"type_name":"\u9b54\u5e7b\u7247"},{"type_id":22,"type_name":"\u5192\u9669\u7247"},{"type_id":23,"type_name":"\u60ac\u7591\u7247"},{"type_id":25,"type_name":"\u7eaa\u5f55\u7247"},{"type_id":26,"type_name":"\u72af\u7f6a\u7247"},{"type_id":27,"type_name":"\u5fae\u7535\u5f71"},{"type_id":28,"type_name":"\u5176\u4ed6\u7247"},{"type_id":29,"type_name":"\u52a8\u753b\u7247"},{"type_id":30,"type_name":"\u5f71\u89c6\u8d44\u8baf"},{"type_id":31,"type_name":"\u5f71\u89c6\u5267\u7167"},{"type_id":32,"type_name":"\u5f71\u89c6\u9884\u544a"},{"type_id":33,"type_name":"\u5a31\u4e50\u516b\u5366"}]}
# ---------------一般来说返回的数据是Unicode编码的---------------
# ---------------------------解码过后---------------------------
{"code":1,"msg":"数据列表","page":1,"pagecount":10236,"limit":"10","total":102357,"list":[{"vod_id":159147,"vod_name":"新闻30分","type_id":3,"type_name":"综艺","vod_en":"xinwen30fen","vod_time":"2020-10-22 12:30:48","vod_remarks":"更新至2020-10-16期","vod_play_from":"cntv,qiyi"},{"vod_id":242547,"vod_name":"新闻直播间","type_id":3,"type_name":"综艺","vod_en":"xinwenzhibojian","vod_time":"2020-10-22 12:30:47","vod_remarks":"更新至2020-10-16期","vod_play_from":"qiyi"},{"vod_id":158749,"vod_name":"大揭秘","type_id":3,"type_name":"综艺","vod_en":"dajiemi","vod_time":"2020-10-22 12:30:44","vod_remarks":"更新至2020-10-16期","vod_play_from":"qiyi,sohu"},{"vod_id":158596,"vod_name":"养生堂","type_id":3,"type_name":"综艺","vod_en":"yangshengtang","vod_time":"2020-10-22 12:30:44","vod_remarks":"更新至2020-10-16期","vod_play_from":"qiyi,sohu,mgtv,wasu,qq,youku"},{"vod_id":242492,"vod_name":"妖手摧花","type_id":21,"type_name":"魔幻片","vod_en":"yaoshoucuihua","vod_time":"2020-10-22 12:30:43","vod_remarks":"高清正片","vod_play_from":"qq"},{"vod_id":242484,"vod_name":"平行迷途","type_id":13,"type_name":"国产剧","vod_en":"pingxingmitu","vod_time":"2020-10-22 12:30:42","vod_remarks":"更新至6\/共18集","vod_play_from":"youku"},{"vod_id":261109,"vod_name":"我凭本事单身","type_id":13,"type_name":"国产剧","vod_en":"wopingbenshidanshen","vod_time":"2020-10-22 12:30:42","vod_remarks":"更新至6集","vod_play_from":"youku"},{"vod_id":242279,"vod_name":"校园女大兵","type_id":13,"type_name":"国产剧","vod_en":"xiaoyuannvdabing","vod_time":"2020-10-22 12:30:40","vod_remarks":"更新至21\/共26集","vod_play_from":"youku"},{"vod_id":158562,"vod_name":"综艺大爆炸","type_id":3,"type_name":"综艺","vod_en":"zongyidabaozha","vod_time":"2020-10-22 12:30:36","vod_remarks":"更新至2020-10-16期","vod_play_from":"qq"},{"vod_id":158568,"vod_name":"经典传奇","type_id":3,"type_name":"综艺","vod_en":"jingdianchuanqi","vod_time":"2020-10-22 12:30:34","vod_remarks":"更新至2020-10-16期","vod_play_from":"qq,qiyi,sohu,pptv,youku"}],"class":[{"type_id":1,"type_name":"电影"},{"type_id":2,"type_name":"连续剧"},{"type_id":3,"type_name":"综艺"},{"type_id":4,"type_name":"动漫"},{"type_id":5,"type_name":"8090影视娱乐资讯"},{"type_id":6,"type_name":"动作片"},{"type_id":7,"type_name":"喜剧片"},{"type_id":8,"type_name":"爱情片"},{"type_id":9,"type_name":"科幻片"},{"type_id":10,"type_name":"恐怖片"},{"type_id":11,"type_name":"剧情片"},{"type_id":12,"type_name":"战争片"},{"type_id":13,"type_name":"国产剧"},{"type_id":14,"type_name":"港台剧"},{"type_id":15,"type_name":"日韩剧"},{"type_id":16,"type_name":"欧美剧"},{"type_id":20,"type_name":"惊悚片"},{"type_id":21,"type_name":"魔幻片"},{"type_id":22,"type_name":"冒险片"},{"type_id":23,"type_name":"悬疑片"},{"type_id":25,"type_name":"纪录片"},{"type_id":26,"type_name":"犯罪片"},{"type_id":27,"type_name":"微电影"},{"type_id":28,"type_name":"其他片"},{"type_id":29,"type_name":"动画片"},{"type_id":30,"type_name":"影视资讯"},{"type_id":31,"type_name":"影视剧照"},{"type_id":32,"type_name":"影视预告"},{"type_id":33,"type_name":"娱乐八卦"}]}
```

##### 解析

#### 视频详情地址-vod/?ac=detail

`http://域名/api.php/provide/vod/?ac=detail`

#### 文章列表地址-art/?ac=list

`http://域名/api.php/provide/art/?ac=list`

#### 文章详情地址-art/?ac=detail

`http://域名/api.php/provide/art/?ac=detail`

### 进阶的接口解析

#### 列表接收

> ac=分类 ==> list 视频列表 detail 视频详情
>
> t=类别ID ==> 9 科幻片 ==> type_id 从3开始
>
> pg=页码
>
> wd=搜索关键字
>
> h=几小时内的数据



#### 内容接收

> ac=分类
>
> ids=数据ID，多个ID逗号分割。
>
>  t=类型ID
>
>  pg=页码
>
>  h=几小时内的数据

