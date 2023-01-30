#ThreeJs #互动 #OrbitControls 
# 创建相机控件OrbitControls
>[参考网址](https://threejs.org/docs/index.html?q=OrbitControls#examples/zh/controls/OrbitControls)

```
const controls = new OrbitControls(camera, renderer.domElement);
// 绑定事件
controls.addEventListener("change", render); // use only if there is no animation loop
// 最小距离
controls.minDistance = 1;
// 最大距离
controls.maxDistance = 10;
// 启用或禁用摄像机平移
controls.enablePan = false;
 ```
 >事件：render = () => {renderer.render(scene, camera)}

```
// 启动旋转
controls.autoRotate = true;
// 旋转速度
controls.autoRotateSpeed = 20;
// 关闭阻尼
controls.enableDamping = false
// 更新控制
setInterval(()=>{
 controls.update()
},20)
 ```