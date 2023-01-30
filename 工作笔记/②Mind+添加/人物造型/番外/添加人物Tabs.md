## 添加翻译信息

在 `translations/messages/src/components/scratch/tag-button/tag-button.js`里面添加人物标签的翻译信息

```js
mind: {
    id: 'gui.libraryTags.mind',
    defaultMessage: 'Mind',
    description: 'libraryTags for Mind'
},
```

## 添加启用标签

在`src/lib/libraries/sprite-tags.js`里面添加要添加的标签的信息

```js
{tag: 'Mind+'},
```

## 