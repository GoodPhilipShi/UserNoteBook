#半球光 #ThreeJs
# 灯光
>举一个例子: HemisphereLight
>[参考网址](https://threejs.org/docs/index.html?q=HemisphereLight#api/zh/lights/HemisphereLight)

```
HemisphereLight( skyColor : Integer, groundColor : Integer, intensity : Float )
```

| 参数        | 描述                       | 具体含义 |
| ----------- | -------------------------- | -------- |
| skyColor    | 天空中发出光线的颜色(可选) | ✔        |
| groundColor | 地面发出光线的颜色(可选)   | ✔ 阴影   |
| intensity   | 光照强度(可选)             | ✗        | 

```js
// const light = new THREE.HemisphereLight(0xffffff, 0x080808, 1.5);
const light = new THREE.HemisphereLight('rgb(255,255,255)', 'rgb(8,8,8)', 1.5);
light.position.set(-1.25, 1, 1.25);
scene.add(light);
```