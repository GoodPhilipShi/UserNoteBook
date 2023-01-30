#ThreeJs
# 材质

## Lambert网格材质(MeshLambertMaterial)

```js
// 创建 x,y,z 横切面
const clipPlanes = [
    new THREE.Plane(new THREE.Vector3(1, 0, 0), 0),
    new THREE.Plane(new THREE.Vector3(0, -1, 0), 0),
    new THREE.Plane(new THREE.Vector3(0, 0, -1), 0),
];
const material = new THREE.MeshLambertMaterial({
    // 启动透明功能
    transparent: true,
    opacity: 0.5,
    // 颜色
    color: new THREE.Color().setHSL(Math.random(), 0.5, 0.5),
    // 面
    side: THREE.DoubleSide,
    // 用户定义的剪裁平面，在世界空间中指定为THREE.Plane对象。
	// 这些平面适用于所有使用此材质的对象。空间中与平面的有符号距离为负的点被剪裁（未渲染）
    clippingPlanes: clipPlanes,
    // 更改剪裁平面的行为，以便仅剪切其交叉点，而不是它们的并集。
    clipIntersection: true
});
```

>PS: 在使用完后，记得销毁 `material.dispose()`
>一般是在 ` new Mesh(模型, 材质)` 之后