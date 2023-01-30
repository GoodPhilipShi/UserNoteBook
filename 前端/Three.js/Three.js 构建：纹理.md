#ThreeJs 
# 纹理
## 纹理加载器 TextureLoader
>[参考网址](https://threejs.org/docs/index.html#api/zh/loaders/TextureLoader)

```
TextureLoader( manager : LoadingManager )
LoadingManager( onLoad : Function, onProgress : Function, onError : Function )
```

| 参数       | 描述                                        | 具体含义 |
| ---------- | ------------------------------------------- | -------- |
| onLoad     | 所有加载器加载完成后，将调用此函数.(可选)   | ✔        |
| onProgress | 当每个项目完成后，将调用此函数.(可选)       | ✔        |
| onError    | 当一个加载器遇到错误时，将调用此函数.(可选) | ✔        | 

```js
const texture = new THREE.TextureLoader().load( 'textures/land_ocean_ice_cloud_2048.jpg' );
```
>如果是在脚手架里面用, 例如react里面用, 就需要这样用
```js
import Image from './C.png';
const texture = new THREE.TextureLoader().load(Image);
// 修改格式
// https://threejs.org/docs/index.html?q=Loader#api/en/textures/Texture.format
texture.format = RGBAFormat;
```
>如果纹理具有透明要素的话, 就要开启透明功能
```js
new THREE.MeshBasicMaterial({map: texture,transparent: true})
```

>ps:  在使用完后，记得销毁  `sphere.dispose()`
>一般是在 ` new Mesh(模型, 材质)` 之后

## Canaves转纹理 CanvasTexture

```js
let canva = document.createElement("canvas");
canva.width = width;
canva.height =height;
canva.style.width = width / 2;
let ctx = canva.getContext("2d");
// 创建
ctx.fillStyle = "#00000000";
ctx.fillRect(0, 0, width, height);
let texture = new CanvasTexture(canva);
```
> 同上
```js
new THREE.MeshBasicMaterial({map: texture,transparent: true})
```