# 摇杆

>[!tip]- 代码隐藏
>~~~tsx
>import { css } from "@emotion/css";
> import styled from "@emotion/styled";
> import { InputNumber, Space } from "antd";
> import React, { FC, useEffect, useRef, useState } from "react";
> import { mqttManager } from "util/mqtt";
> import { useProjectContentJson } from "util/project-detials";
> import {
>     useCustomComponent,
>     useSelectedComponent
> } from "util/project-detials/component";
> import { CustomComponent, ProjectContent } from "util/project-detials/type";
> 
> interface CustomRockerProps {
>     data: CustomComponent & Partial<CustomRockerData>;
> }
> 
> interface CustomRockerData {
>     frequency?: number /** 频率 ms 默认500ms */;
> }
> 
> export const RockerDefaultConfig: OmitRequired<CustomRockerProps["data"]> = {
>     title: "摇杆",
>     size: {
>         width: 200,
>         height: 200,
>     },
>     frequency: 500,
> };
> 
> const sendWithFrequency = (topic?: string, frequency: number = 500) => {
>     let startTime = new Date().getTime();
>     return (pos?: { x: number; y: number }, immediately: boolean = false) => {
>         // 只传immediately重置定时器
>         if (!pos && immediately) startTime = new Date().getTime();
>         if (topic && pos) {
>             let currentTime = new Date().getTime();
>             // console.log(currentTime, startTime, frequency)
>             if (currentTime - startTime > frequency || immediately) {
>                 if (mqttManager.isConnected()) {
>                     let { x, y } = pos;
>                     mqttManager.send(
>                         topic,
>                         `${Math.floor(x * 100)},${Math.floor(y * 100)}`,
>                         0
>                     );
>                 }
>                 // 重置定时器
>                 startTime = currentTime;
>             }
>         }
>     };
> };
> 
> export const CustomRocker: FC<CustomRockerProps> = ({ data }) => {
>     const projectContent = useProjectContentJson();
>     const rockerRef = useRef<HTMLDivElement>(null);
>     const [bigRockerSize, setBigRockerSize] = useState<number>(200);
>     const [smallRockerSize, setSmallRockerSize] = useState<number>(80);
> 
>     const startPosition = useRef<{ x: number; y: number }>({ x: 0, y: 0 });
>     const currentPosition = useRef<{ x: number; y: number }>({ x: 0, y: 0 });
> 
>     const theme = projectContent.theme;
>     const { size, topic, frequency } = data;
> 
>     const send = sendWithFrequency(topic, frequency);
> 
>     const onMouseDown: React.MouseEventHandler<HTMLDivElement> = (event) => {
>         // INFO: 鼠标MouseDown时
>         const { pageX, pageY } = event;
>         startPosition.current = {
>             x: pageX,
>             y: pageY,
>         };
> 
>         // 注册事件
>         document.addEventListener("mouseup", onMouseUp, { once: true });
>         document.addEventListener("mousemove", onMouseMove);
> 
>         const ev = event || window.event;
> 
>         ev.stopPropagation();
>         // ev.cancelable = true;
>         ev.preventDefault();
> 
>         ev.nativeEvent.stopPropagation();
>         ev.nativeEvent.stopImmediatePropagation();
>     };
> 
>     const onMouseUp = (_: MouseEvent) => {
>         // INFO: 之前鼠标是按下的并且鼠标松开时，直接发送
>         send(currentPosition.current, true);
>         // 卸载事件
>         document. removeEventListener ("mousemove", onMouseMove);
>         document. removeEventListener ("mouseup", onMouseUp);
>         // 样式恢复
>         rockerRef.current && (rockerRef.current.style.left = "");
>         rockerRef.current && (rockerRef.current.style.top = "");
>         currentPosition.current = {x:0,y:0}
>     };
> 
>     const onMouseMove = (event: MouseEvent) => {
>         const ev = event || window.event;
> 
>         ev.stopPropagation();
>         ev.preventDefault();
>         ev.stopImmediatePropagation();
>         ev.cancelBubble = true;
> 
>         const { pageX, pageY } = event;
> 
>         let x = pageX - startPosition.current.x,
>             y = pageY - startPosition.current.y,
>             z = Math.sqrt(Math.pow(Math.abs(x), 2) + Math.pow(Math.abs(y), 2));
> 
>         if (z > bigRockerSize / 2) {
>             let proportion = bigRockerSize / 2 / z;
>             x = Math.floor(x * proportion);
>             y = Math.floor(y * proportion);
>         }
>         
>         // 发送信息事件
>         send({ x: x / (bigRockerSize / 2), y: -y / (bigRockerSize / 2) });
> 
>         // 存储坐标值
>         currentPosition.current = {
>             x: x / (bigRockerSize / 2),
>             y: -y / (bigRockerSize / 2),
>         };
> 
>         rockerRef.current &&
>             (rockerRef.current.style.left = `calc(50% + ${x}px)`);
>         rockerRef.current &&
>             (rockerRef.current.style.top = `calc(50% + ${y}px)`);
>     };
> 
>     useEffect(() => {
>         if (
>             size?.width !== undefined &&
>             size?.width !== null &&
>             size?.height !== undefined &&
>             size?.height !== null
>         ) {
>             let bg = size.width >= size.height ? size.height : size.width;
>             setBigRockerSize(bg);
>             setSmallRockerSize((bg / 5) * 2);
>         } else {
>             setBigRockerSize(200);
>             setSmallRockerSize(80);
>         }
>     }, [size]);
> 
>     // INFO: 自适应大小
> 
>     return (
>         <Container theme={theme} size={size}>
>             <RockerComponent
>                 size={bigRockerSize}
>                 // image={{ url: "../component-lib/rocker/摇杆_大.png" }}
>                 className={css`
>                     position: relative;
>                     left: 50%;
>                     top: 50%;
>                     transform: translate(-50%, -50%);
>                     background: rgb(209 209 209 / 20%);
>                     border: 1px solid rgba(105, 112, 117, 0.5);
>                 `}
>                 <RockerComponent
>                     size={smallRockerSize}
>                     className={css`
>                         position: absolute;
>                         left: 50%;
>                         top: 50%;
>                         transform: translate(-50%, -50%);
>                         background: #c1c1c1;
>                     `}
>                </RockerComponent>
>                 <RockerComponent
>                     size={smallRockerSize}
>                     // image={{ url: "../component-lib/rocker/摇杆_小.png" }}
>                     className={css`
>                         position: absolute;
>                         left: 50%;
>                         top: 50%;
>                         transform: translate(-50%, -50%);
>                         background: #c1c1c1;
>                         &:active {
>                             background: rgb(60, 179, 145);
>                             box-shadow: inset 0 0 12px 4px
>                                 rgba(45, 132, 107, 0.9);
>                         }
>                     `}
>                     ref={rockerRef}
>                     draggable
>                     onMouseDown={onMouseDown}
>                </RockerComponent>
>             </RockerComponent>
>         </Container>
>     );
> };
>
> const Container = styled.div<{
>     size: CustomComponent["size"];
>     theme: ProjectContent["theme"];
> }>`
>     position: relative;
>     width: ${(props) => `${props.size?.width}px`};
>     height: ${(props) => `${props.size?.height}px`};
>     border-radius: 4px;
>     /* background: ${(props) =>
>         props.theme === "light" ? "#ffffff" : "#100c2a"}; */
>     /* padding: 10px 10px; */
> `;
> 
> const RockerComponent = styled.div<{
>     size: number;
>     color?: string;
>     image?: boolean | { url: string } | string;
> }>`
>     width: ${(props) => `${props.size}px`};
>     height: ${(props) => `${props.size}px`};
>     /* position: relative; */
>     border-radius: ${(props) => `${props.size / 2}px`};
>     background-color: ${(props) => props.color};
>     background-image: ${(props) =>
>         props.image !== undefined &&
>         props.image !== false &&
>         props.image.constructor !== String
>             ? `url("${(props.image as { url: string }).url}")`
>             : props.image};
>     background-repeat: no-repeat;
>     background-size: cover;
> `;
> 
> const SettingWrapper = styled(Space)`
>     margin: 0 12px;
>     display: flex;
>     flex-direction: column;
> `;
> 
> const SettingItem = styled.div<{ height?: string; width?: string }>`
>     height: ${(props) => props.height || "30px"};
>     width: ${(props) => props.width || "auto"};
>     display: flex;
>     flex-direction: row;
>     align-items: center;
> `;
> 
> const SettingLabel = styled.span`
>     width: 60px;
> `;
> 
> const InputWrapper = styled.div<{
>     width?: string;
>     height?: string;
>     marginLeft: string;
> }>`
>     width: ${(props) => props.width || "80px"};
>     height: ${(props) => props.height || "30px"};
>     display: flex;
>     justify-content: center;
>     align-items: center;
>     padding: 8px 8px;
>     border-radius: 4px;
>     background: #f0f0f0;
>     margin-left: ${(props) => props.marginLeft};
> `;
>~~~

## 逻辑梳理

>[!done] 使用 `useRef` 进行保存坐标

1. 鼠标按下 (MouseDown) 时
	1. 注册全局事件

	```js
	document. addEventListener ("mouseup", onMouseUp, { once: true });
    document.addEventListener("mousemove", onMouseMove);
	```

	2. 阻止鼠标事件冒泡

	```js
	const ev = event || window. event;
	ev. stopPropagation ();
	// ev. cancelable = true;
	ev. preventDefault ();
	ev. nativeEvent. stopPropagation ();
	ev.nativeEvent.stopImmediatePropagation();
	```

	3. 记录初始坐标 (**记住是使用什么来获取的 xy 坐标，例如，pageX, pageY **)
2. 鼠标移动 (MouseMove) 时
	1. 使用与鼠标按下时获取主标同样的方式获取现在 xy 坐标，并进行比对
	2. 边缘检测

		> bigRockerSize 是摇杆的直径

		```js
		let x = pageX - startPosition. current. x,
            y = pageY - startPosition.current.y,
            z = Math.sqrt(Math.pow(Math.abs(x), 2) + Math.pow(Math.abs(y), 2));

        if (z > bigRockerSize / 2) {
            let proportion = bigRockerSize / 2 / z;
            x = Math.floor(x * proportion);
            y = Math.floor(y * proportion);
        }
	    ```

	3. 通过 `useRef` 进行 DOM 操作，减少刷新
3. 鼠标松开时
	1. 坐标 ref 归零
	2. 卸载鼠标移动事件、鼠标松开事件 (?)

