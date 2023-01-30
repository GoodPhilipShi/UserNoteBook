# PlaneHelper 平面助手
>[PlaneHelper – three.js docs](https://threejs.org/docs/index.html?q=PlaneHelper#api/zh/helpers/PlaneHelper)

```js
// 创建助手(显示X，Y，Z平面轴)
const helpers = new Group();
helpers.add(new PlaneHelper(clipPlanes[0], 2, "rgb(255,0,0)"));
helpers.add(new PlaneHelper(clipPlanes[1], 2, "rgb(0,255,0)"));
helpers.add(new PlaneHelper(clipPlanes[2], 2, "rgb(0,0,255)"));
// 默认隐藏
helpers.visible = true;
scene.add(helpers);
```

# AxesHelper 轴助手
>[AxesHelper – three.js docs](https://threejs.org/docs/index.html?q=AxesHelper#api/zh/helpers/AxesHelper)

```js
const axesHelper = new AxesHelper(500);
scene.add(axesHelper);
```

# GridHelper 网格助手
> [GridHelper – three.js docs](https://threejs.org/docs/index.html?q=GridHelper#api/zh/helpers/GridHelper)

```js
const gridHelper = new GridHelper(500, 200);
scene.add(gridHelper);
```

# PointLightHelper 点光源辅助对象
> [PointLightHelper – three.js docs](https://threejs.org/docs/index.html?q=PointLightHelper#api/zh/helpers/PointLightHelper)

```js
const light = new HemisphereLight(
    "rgb(255,255,255)",
    "rgb(255,255,255)",
    1.58
);
light.position.set(-50.25, 52, -50.25);
// light.position.set(0, 0, 0);
scene.add(light);
```

```js
const pointLightHelper = new PointLightHelper(light, 0.1);
pointLightHelper.position.set(-50.25, 52, -50.25);
scene.add(pointLightHelper);
```