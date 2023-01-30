# Tilt.js

一个微小的 requestAnimationFrame 为 jQuery 提供了 60+fps 的轻量级视差倾斜效果。

重量只是⚖**1.71kb 压缩包**

[Github: A tiny 60+fps parallax tilt hover effect for jQuery.](https://github.com/gijsroge/tilt.js)

## Tilt.js Options

| 每一项      | 描述                               | 默认                            |
| ----------- | ---------------------------------- | ------------------------------- |
| maxTilt     | 最大倾斜                           | 20                              |
| perspective | 变换透视，越低倾斜越极端           | 1000                            |
| easing      | 进入/退出时缓动                    | "cubic-bezier(.03,.98,.52,.99)" |
| scale       | 比例, 2 = 200%, 1.5 = 150%以此类推 | 1                               |
| speed       | 进入/退出转换的速度                | 300                             |
| transition  | 在进入/退出时设置过渡              | true                            |
| disableAxis | 应该禁用哪个轴。可以是 X 或 Y      | null                            |
| reset       | 如果倾斜效果必须在退出时重置       | true                            |
| glare       | 是否启用眩光效果                   | false                           |
| maxGlare    | 最大眩光,0 - 1                     | 1                               |

## Tilt.js Events

```js
const tilt = $('.js-tilt').tilt();
tilt.on('change', callback);  // parameters: event, transforms
tilt.on('tilt.mouseLeave', callback); // parameters: event
tilt.on('tilt.mouseEnter', callback); // parameters: event
```

## Tilt.js Methods

```js
const tilt = $('.js-tilt').tilt();

// 销毁实例
tilt.tilt.destroy.call(tilt);

// 获取实例
tilt.tilt.getValues.call(tilt); // returns [{},{},etc..]

// 重置实例
tilt.tilt.reset.call(tilt);
```

## Tilt.js Usage

### HTML下使用

```html
<!DOCTYPE html>
<body>
    <div data-tilt></div> <!-- Tilt element -->
    <script src="jquery.js" ></script> <!-- Load jQuery first -->
    <script src="tilt.js"></script> <!-- Load Tilt.js library -->
</body>
```

### NodeJs下使用

```shell
yarn add tilt.js
npm install --save tilt.js
```

## Tilt.js CDN

-   [https://cdnjs.cloudflare.com/ajax/libs/tilt.js/1.2.1/tilt.jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/tilt.js/1.2.1/tilt.jquery.min.js)
-   [https://unpkg.com/tilt.js@1.2.1/dest/tilt.jquery.min.js](https://unpkg.com/tilt.js@1.2.1/dest/tilt.jquery.min.js)

## 类似的还有...

-   **Vanilla JS:** [https://github.com/micku7zu/vanilla-tilt.js](https://github.com/micku7zu/vanilla-tilt.js)
-   **React:** [https://github.com/jonathandion/react-tilt](https://github.com/jonathandion/react-tilt)
-   **React** [https://github.com/jonahallibone/react-tilty](https://github.com/jonahallibone/react-tilty)
-   **Polymer:** [https://github.com/YingshanDeng/polymer-tilt](https://github.com/YingshanDeng/polymer-tilt)
-   **Preact** [https://github.com/RomanistHere/preact-tilt](https://github.com/RomanistHere/preact-tilt)