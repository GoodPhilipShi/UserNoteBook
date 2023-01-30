#ThreeJs
# 基础要素
> 前提信息
```js
width = window.innerWidth;
height = window.innerHeight;
```
## 摄像 Camera
>举一个例子: PerspectiveCamera
>[参考网址](https://threejs.org/docs/index.html?q=PerspectiveCamera#api/zh/cameras/PerspectiveCamera)

```ts
PerspectiveCamera( fov : Number, aspect : Number, near : Number, far : Number )
```

| 参数   | 描述                     | 具体含义 |
| ------ | ------------------------ | -------- |
| fov    | 摄像机视锥体垂直视野角度 | ✗        |
| aspect | 摄像机视锥体长宽比       | ✗        |
| near   | 摄像机视锥体近端面       | ✗        |
| far    | 摄像机视锥体远端面       | ✗        | 

```js
camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 10000);
// 将摄像头放到 x,y,z
camera.position.set(2, 2, 2);
// 相机朝向Y
camera.up.set(0, 1, 0);
// 相机看向 0，0，0
camera.lookAt(0, 0, 0);
```

## 场景 Scene
>[参考网址](https://threejs.org/docs/index.html?q=Scene#api/zh/scenes/Scene)

```ts
Scene()
```

```js
scene = new THREE.Scene();
```

### 添加模型(对象)
```js
scene.add()
```
### 删除模型(对象)
```
scene.remove()
```

## 渲染器 Renderer
>举一个例子: WebGLRenderer
>[参考网址](https://threejs.org/docs/index.html?q=WebGLRenderer#api/zh/renderers/WebGLRenderer)

```ts
WebGLRenderer( parameters : Object )
```

>参数过多

```js
renderer = new THREE.WebGLRenderer({
	antialias:true,
	alpha:true
});
// 调整渲染器大小
renderer.setSize(width, height);
// 设置设备像素比
renderer.setPixelRatio(window.devicePixelRatio);
// 定义渲染器是否考虑对象级剪切平面默认
renderer.localClippingEnabled = true;
// 设置清空渲染器的颜色
// 将1修改为0，背景为透明 --> 获得 #canvas-frame 的背景
renderer.setClearColor(0xffffff, 1);
renderer.clearColor()
// 将渲染后的DOM对象放到 #canvas-frame 里面
document.getElementById("canvas-frame").appendChild(renderer.domElement);
```