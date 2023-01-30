#ThreeJs #旋转
# 方法1
>通过互动功能，进行旋转
```js
// 启动旋转
controls.autoRotate = true;
// 旋转速度
controls.autoRotateSpeed = 20;
// 关闭阻尼
controls.enableDamping = false


// ①第一种 更新控制
setInterval(()=>{
 controls.update()
},20)
// ②第二种 推荐✔
window.requestAnimationFrame(()=>{controls.update()});
```
# 方法2
>通过属性`rotation`旋转
```js
group.rotation.y += 0.005
```