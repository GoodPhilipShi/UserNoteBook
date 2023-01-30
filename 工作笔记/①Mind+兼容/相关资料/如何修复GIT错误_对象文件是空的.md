## 错误代码如下

```shell
error: object file .git/objects/31/65329bb680e30595f242b7c4d8406ca63eeab0 is empty
fatal: loose object 3165329bb680e30595f242b7c4d8406ca63eeab0 (stored in .git/objects/31/65329bb680e30595f242b7c4d8406ca63eeab0) is corrupt
```

or

```shell
error: 对象文件 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277 为空
error: 对象文件 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277 为空
fatal: 松散对象 9492551fd46bc51f2ddbfd346662eea346238277（保存在 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277）已损坏
```

## 方法如下

```shell
git fsck --full
```

```
error: 对象文件 .git/objects/18/78641aad7ff5409f1891527c4bc4707b2d132e 为空
error: 不能 mmap .git/objects/18/78641aad7ff5409f1891527c4bc4707b2d132e: 没有那个文件或目录
error: 1878641aad7ff5409f1891527c4bc4707b2d132e: object corrupt or missing: .git/objects/18/78641aad7ff5409f1891527c4bc4707b2d132e
error: 对象文件 .git/objects/2b/6055f7aa1e94425f52a0a2e73a84ca24b9ecfc 为空
error: 不能 mmap .git/objects/2b/6055f7aa1e94425f52a0a2e73a84ca24b9ecfc: 没有那个文件或目录
error: 2b6055f7aa1e94425f52a0a2e73a84ca24b9ecfc: object corrupt or missing: .git/objects/2b/6055f7aa1e94425f52a0a2e73a84ca24b9ecfc
error: 对象文件 .git/objects/3e/cf62271a9a6fd8eff96252b2b0425279615214 为空
error: 不能 mmap .git/objects/3e/cf62271a9a6fd8eff96252b2b0425279615214: 没有那个文件或目录
error: 3ecf62271a9a6fd8eff96252b2b0425279615214: object corrupt or missing: .git/objects/3e/cf62271a9a6fd8eff96252b2b0425279615214
error: 对象文件 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277 为空
error: 不能 mmap .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277: 没有那个文件或目录
error: 9492551fd46bc51f2ddbfd346662eea346238277: object corrupt or missing: .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277
error: 对象文件 .git/objects/e7/207fb4f7ced8e97dfad101301b1bcc9da91009 为空
error: 不能 mmap .git/objects/e7/207fb4f7ced8e97dfad101301b1bcc9da91009: 没有那个文件或目录
error: e7207fb4f7ced8e97dfad101301b1bcc9da91009: object corrupt or missing: .git/objects/e7/207fb4f7ced8e97dfad101301b1bcc9da91009
error: 对象文件 .git/objects/f1/a0e78cc8706fed9c1cf10a0d1b16f2136e91b6 为空
error: 不能 mmap .git/objects/f1/a0e78cc8706fed9c1cf10a0d1b16f2136e91b6: 没有那个文件或目录
error: f1a0e78cc8706fed9c1cf10a0d1b16f2136e91b6: object corrupt or missing: .git/objects/f1/a0e78cc8706fed9c1cf10a0d1b16f2136e91b6
检查对象目录中: 100% (256/256), 完成.
检查对象中: 100% (88038/88038), 完成.
error: 对象文件 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277 为空
error: 对象文件 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277 为空
fatal: 松散对象 9492551fd46bc51f2ddbfd346662eea346238277（保存在 .git/objects/94/92551fd46bc51f2ddbfd346662eea346238277）已损坏
```

### 删除所为空的对象文件

```shell
rm .git/objects/18/78641aad7ff5409f1891527c4bc4707b2d132e ...
```

### 手动获得最后两条reflog

```shell
# tail -n 2 .git/logs/refs/heads/分支名称
tail -n 2 .git/logs/refs/heads/V1.7.2-RC2.0
```

```
1425c27b6600e1cf639fb868fc8c4e35c2824955 6c041b05b85eb0b4ec103c5c6568a1e543d2acde 六 <1183417329@qq.com> 1650528435 +0800       pull: Merge made by the 'recursive' strategy.
```

> 结果

```
1425c27b6600e1cf639fb868fc8c4e35c2824955
6c041b05b85eb0b4ec103c5c6568a1e543d2acde
```

> 筛选
> 通过`git show`来查看这两条分支修改了什么
> 选时间最近的一条

```shell
git show 1425c27b6600e1cf639fb868fc8c4e35c2824955
```

### 将HEAD指向

```shell
git update-ref HEAD 1425c27b6600e1cf639fb868fc8c4e35c2824955
```

### 修复上游分支

```shell
git branch --unset-upstream
git branch --set-upstream-to=origin/V1.7.2-RC2.0
```

### 重新拉取

```shell
git pull
```