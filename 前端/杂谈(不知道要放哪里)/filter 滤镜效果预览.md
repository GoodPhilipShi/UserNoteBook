# filter 滤镜效果预览

![](https://image-static.segmentfault.com/394/780/3947806493-622f3c2819520_fix732)

# shadow 阴影

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document</title>
  <style>
    #w1 {
      width: 50px;
      height: 50px;
      font-size: 36px;
      font-weight: 900;
      box-shadow: 0 0 2px red;
    }

    #w2 {
      width: 50px;
      height: 50px;
      font-size: 36px;
      font-weight: 900;
      filter: drop-shadow(0px 0px 2px red);
    }
  </style>
</head>

<body>
  <p id="w1">九</p>
  <p id="w2">九</p>
</body>

</html>
```

![](https://image-static.segmentfault.com/210/033/2100335540-622f565f25f7e_fix732)