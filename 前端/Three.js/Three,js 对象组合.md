#ThreeJs 
# 组合 Group
>好处是统一管理所有对象，进行一致性操作(一起旋转，一起移动...)
>[参考网址](https://threejs.org/docs/index.html?q=Group#api/zh/objects/Group)

```ts
const group = new THREE.Group();
```

## 添加对象
```ts
group.add(object : Object3D)
```


## 注意事项
### 删除组合的子对象
```ts
group.remove(object : Object3D)
```

>效果没有，不清楚是使用失误，还是API异常
>所以尽量少使用
### 更新组合中的子对象
```js
group.children[i].material = materialTexture
```
```js
let texture = new CanvasTexture(SphereModMeshs[i].ModMeshObjectCanvas);
let UpSphereMod = new SphereGeometry(SphereModMeshs[i].ModMeshObjectRadius, 50, 100);
let materialTexture = new MeshLambertMaterial({
	map: texture,
	transparent: true,
	side: DoubleSide,
	...options.Material,
});
UpSphereModMesh = new Mesh(UpSphereMod, materialTexture);
/* 主要内容如下:  */
// 更新组合中子对象的第i个的物体(渲染好的3D模型(?大概是这个意思))
group.children[i].material = materialTexture
// 销毁纹理
texture.dispose()
// 销毁3D模型：球
UpSphereMod.dispose();
// 销毁材质
materialTexture.dispose();
```