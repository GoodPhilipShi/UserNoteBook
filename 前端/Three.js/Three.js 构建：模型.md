#ThreeJs
# 模型
## 球-球缓冲几何体（SphereGeometry）
>[参考网址](https://threejs.org/docs/index.html#api/zh/geometries/SphereGeometry)

```ts
SphereGeometry(radius : Float, widthSegments : Integer, heightSegments : Integer, phiStart : Float, phiLength : Float, thetaStart : Float, thetaLength : Float)
```

| 参数           | 描述                                                   | 具体含义 |
| -------------- | ------------------------------------------------------ | -------- |
| radius         | 球体半径，默认为1                                      | ✔        |
| widthSegments  | 水平分段数（沿着经线分段），最小值为3，默认值为32。    | ✗        |
| heightSegments | 垂直分段数（沿着纬线分段），最小值为2，默认值为16。    | ✗        |
| phiStart       | 指定水平（经线）起始角度，默认值为0。。                | ✗        |
| phiLength      | 指定水平（经线）扫描角度的大小，默认值为 Math.PI * 2。 | ✗        |
| thetaStart     | 指定垂直（纬线）起始角度，默认值为0。                  | ✗        |
| thetaLength    | 指定垂直（纬线）扫描角度大小，默认值为 Math.PI。       | ✗        |



```js
const sphere = new THREE.SphereGeometry(i / 30, 48, 24);
```

>ps:  在使用完后，记得销毁  `sphere.dispose()`
>一般是在 ` new Mesh(模型, 材质)` 之后