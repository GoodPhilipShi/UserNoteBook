# React学习

## 前提准备【环境准备】

- ### 方式一：在浏览器中编写代码

- ### 方式二：搭建本地开发环境

  > 虽然在本地搭建环境要费一些时间，但是你可以选择自己喜欢的编辑器来完成开发。以下是具体步骤：
  >
  > 1. 确保你安装了较新版本的 [Node.js](https://nodejs.org/en/)。
  >
  > 2. 按照 [Create React App 安装指南](https://react.docschina.org/docs/create-a-new-react-app.html#create-react-app)创建一个新的项目
  >
  >    ```react
  >    npx create-react-app my-app
  >    ```
  >
  > 3. 删除掉新项目中 `src/` 文件夹下的所有文件。
  >
  >    > 注意：
  >    >
  >    > **不要删除整个 `src` 文件夹，删除里面的源文件**。我们会在接下来的步骤中使用示例代码替换默认源文件。
  >
  >    ```react
  >    cd my-app
  >    cd src
  >    
  >    # 如果你使用 Mac 或 Linux:
  >    rm -f *
  >    
  >    # 如果你使用 Windows:
  >    del *
  >    
  >    # 然后回到项目文件夹
  >    cd ..
  >    ```
  >
  > 4. 在 `src/` 文件夹中创建一个名为 `index.css` 的文件，并拷贝[这些 CSS 代码](https://codepen.io/gaearon/pen/oWWQNa?editors=0100)。
  >
  > 5. 在 `src/` 文件夹下创建一个名为 `index.js` 的文件，并拷贝[这些 JS 代码](https://codepen.io/gaearon/pen/oWWQNa?editors=0010)。
  >
  > 6. 拷贝以下三行代码到 `src/` 文件夹下的 `index.js` 文件的顶部：
  >
  >    ```react
  >    import React from 'react';
  >    import ReactDOM from 'react-dom';
  >    import './index.css';
  >    ```
  >
  > 现在，在项目文件夹下执行 `npm start` 命令，然后在浏览器访问 `http://localhost:3000`。这样你就可以在浏览器中看见一个空的井字棋的棋盘了。
  >

## 概览

### React 是什么？

React 是一个声明式，高效且灵活的用于构建用户界面的 JavaScript 库。使用 React 可以将一些简短、独立的代码片段组合成复杂的 UI 界面，这些代码片段被称作“组件”。

React 中拥有多种不同类型的组件，我们先从 `React.Component` 的子类开始介绍：

```react
class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// 用法示例: <ShoppingList name="Mark" />
```

我们马上会讨论这些又奇怪、又像 XML 的标签。我们通过使用组件来告诉 React 我们希望在屏幕上看到什么。当数据发生改变时，React 会高效地更新并重新渲染我们的组件。

其中，ShoppingList 是一个 **React 组件类**，或者说是一个 **React 组件类型**。一个组件接收一些参数，我们把这些参数叫做 `props`（“props” 是 “properties” 简写），然后通过 `render` 方法返回需要展示在屏幕上的视图的层次结构。

`render` 方法的返回值*描述*了你希望在屏幕上看到的内容。React 根据描述，然后把结果展示出来。更具体地来说，`render` 返回了一个 **React 元素**，这是一种对渲染内容的轻量级描述。大多数的 React 开发者使用了一种名为 “JSX” 的特殊语法，JSX 可以让你更轻松地书写这些结构。语法 `<div />` 会被编译成 `React.createElement('div')`。上述的代码等同于：

```react
return React.createElement('div', {className: 'shopping-list'},
  React.createElement('h1', /* ... h1 children ... */),
  React.createElement('ul', /* ... ul children ... */)
);
```

如果你对这个比较感兴趣，可以查阅 [API 文档](https://react.docschina.org/docs/react-api.html#createelement)了解有关 `createElement()` 更详细的用法。但在接下来的教程中，我们并不会直接使用这个方法，而是继续使用 JSX。

在 JSX 中你可以任意使用 JavaScript 表达式，只需要用一个大括号把表达式括起来。每一个 React 元素事实上都是一个 JavaScript 对象，你可以在你的程序中把它当保存在变量中或者作为参数传递。

前文中的 `ShoppingList` 组件只会渲染一些内置的 DOM 组件，如`<div />`、`<li />`等。但是你也可以组合和渲染自定义的 React 组件。例如，你可以通过 `<ShoppingList />` 来表示整个购物清单组件。每个组件都是封装好的，并且可以单独运行，这样你就可以通过组合简单的组件来构建复杂的 UI 界面。

## 编程之始：Hello World!

> 最简易的 React 示例如下：

```react
<script type="text/babel">
    ReactDOM.render(
      <h1>Hello, world!</h1>,
      document.getElementById('root')
    );
</script>
```

## JSX 简介

> ❗❗假设JSX代码就在HTML页面中时需要注意**`<script type="text/babel">`**一个都不可少，不然无法生效❗❗

> 使用前先声明变量：

```react
const element = <h1>Hello, world!</h1>;
```

> 它被称为 JSX，是一个 JavaScript 的语法扩展。我们建议在 React 中配合使用 JSX，JSX 可以很好地描述 UI 应该呈现出它应有交互的本质形式。JSX 可能会使人联想到模版语言，但它具有 JavaScript 的全部功能。
>
> JSX 可以生成 React “元素”。

### 在 JSX 中嵌入表达式

在下面的例子中，我们声明了一个名为 `name` 的变量，然后在 JSX 中使用它，并将它包裹在大括号中：

```react
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

在 JSX 语法中，你可以在大括号内放置任何有效的 [JavaScript 表达式](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#Expressions)。例如，`2 + 2`，`user.firstName` 或 `formatName(user)` 都是有效的 JavaScript 表达式。

在下面的示例中，我们将调用 JavaScript 函数 `formatName(user)` 的结果，并将结果嵌入到 `<h1>` 元素中。

```react
function formatName(user) {
	return '我姓' + user.lastName + '叫' + user.firstName;
}

const user = {
	firstName: '六记',
	lastName: '许'
};

const element = (
	<h1>Hello, {formatName(user)}!  </h1>
);

ReactDOM.render(
	element,
	document.getElementById('root')
);
```

> 为了便于阅读，我们会将 JSX 拆分为多行。同时，我们建议将内容包裹在括号中，虽然这样做不是强制要求的，但是这可以避免遇到`自动插入分号`陷阱。

### JSX 也是一个表达式

```react
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;  }
  return <h1>Hello, Stranger.</h1>;}
```

### JSX 特定属性

你可以通过使用引号，来将属性值指定为字符串字面量：

```react
const element = <div tabIndex="0"></div>;
```

也可以使用大括号，来在属性值中插入一个 JavaScript 表达式：

```react
const element = <img src={user.avatarUrl}></img>;
```

在属性中嵌入 JavaScript 表达式时，不要在大括号外面加上引号。你应该仅使用引号（对于字符串值）或大括号（对于表达式）中的一个，对于同一属性不能同时使用这两种符号。

> **警告：**
>
> 因为 JSX 语法上更接近 JavaScript 而不是 HTML，所以 React DOM 使用 `camelCase`（小驼峰命名）来定义属性的名称，而不使用 HTML 属性名称的命名约定。
>
> 例如，JSX 里的 `class` 变成了 [`className`](https://developer.mozilla.org/en-US/docs/Web/API/Element/className)，而 `tabindex` 则变为 [`tabIndex`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/tabIndex)。

### 使用 JSX 指定子元素

假如一个标签里面没有内容，你可以使用 `/>` 来闭合标签，就像 XML 语法一样：

```react
const element = <img src={user.avatarUrl} />;
```

JSX 标签里能够包含很多子元素:

```react
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

### JSX 防止注入攻击

你可以安全地在 JSX 当中插入用户输入内容：

```react
const title = response.potentiallyMaliciousInput;
// 直接使用是安全的：
const element = <h1>{title}</h1>;
```

React DOM 在渲染所有输入内容之前，默认会进行[转义](https://stackoverflow.com/questions/7381974/which-characters-need-to-be-escaped-on-html)。它可以确保在你的应用中，永远不会注入那些并非自己明确编写的内容。所有的内容在渲染之前都被转换成了字符串。这样可以有效地防止 [XSS（cross-site-scripting, 跨站脚本）](https://en.wikipedia.org/wiki/Cross-site_scripting)攻击。

### JSX 表示对象

Babel 会把 JSX 转译成一个名为 `React.createElement()` 函数调用。

以下两种示例代码完全等效：

```react
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

`React.createElement()` 会预先执行一些检查，以帮助你编写无错代码，但实际上它创建了一个这样的对象：

```react
// 注意：这是简化过的结构
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world!'
  }
};
```

这些对象被称为 “React 元素”。它们描述了你希望在屏幕上看到的内容。React 通过读取这些对象，然后使用它们来构建 DOM 以及保持随时更新。

> **提示：**
>
> 我们推荐在你使用的编辑器中，使用 [“Babel” 提供的语言定义](https://babeljs.io/docs/editors)，来正确地高亮显示 ES6 和 JSX 代码。本网站使用与其兼容的 [Oceanic Next](https://github.com/voronianski/oceanic-next-color-scheme/) 配色方案。

## 元素渲染

> 元素是构成 React 应用的最小砖块。

元素描述了你在屏幕上想看到的内容。

```react
const element = <h1>Hello, world</h1>;
```

与浏览器的 DOM 元素不同，React 元素是创建开销极小的普通对象。React DOM 会负责更新 DOM 来与 React 元素保持一致。

### 将一个元素渲染为 DOM

假设你的 HTML 文件某处有一个 `<div>`：

```react
<div id="root"></div>
```

我们将其称为“根” DOM 节点，因为该节点内的所有内容都将由 React DOM 管理。

想要将一个 React 元素渲染到根 DOM 节点中，只需把它们一起传入 [`ReactDOM.render()`](https://react.docschina.org/docs/react-dom.html#render)：

```react
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

页面上会展示出 “Hello, world”。

### 更新已渲染的元素

React 元素是 不可变对象。一旦被创建，你就无法更改它的子元素或者属性。一个元素就像电影的单帧：它代表了某个特定时刻的 UI。

根据我们已有的知识，更新 UI 唯一的方式是创建一个全新的元素，并将其传入 `ReactDOM.render()`。

例如：一个计时器：

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}
setInterval(tick, 1000);
```

这个例子会在 `setInterval()` 回调函数，每秒都调用  `ReactDOM.render()`。

## 组件 & Props

组件允许你将 UI 拆分为独立可复用的代码片段，并对每个片段进行独立构思。本指南旨在介绍组件的相关理念。你可以[参考详细组件 API](https://react.docschina.org/docs/react-component.html)。

组件，从概念上类似于 JavaScript 函数。它接受任意的入参（即 “props”），并返回用于描述页面展示内容的 React 元素。

### 函数组件与 class 组件

定义组件最简单的方式就是编写 JavaScript 函数：

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

该函数是一个有效的 React 组件，因为它接收唯一带有数据的 “props”（代表属性）对象与并返回一个 React 元素。这类组件被称为“函数组件”，因为它本质上就是 JavaScript 函数。

你同时还可以使用 [ES6 的 class](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes) 来定义组件：

```react
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

上述两个组件在 React 里是等效的。

### 渲染组件

之前，我们遇到的 React 元素都只是 DOM 标签：

```react
const element = <div />;
```

不过，React 元素也可以是用户自定义的组件：

```react
const element = <Welcome name="Sara" />;
```

当 React 元素为用户自定义组件时，它会将 JSX 所接收的属性（attributes）以及子组件（children）转换为单个对象传递给组件，这个对象被称之为 “props”。

例如，这段代码会在页面上渲染 “Hello, Sara”：

```react
function Welcome(props) {  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;ReactDOM.render(
  element,
  document.getElementById('root')
);
```

让我们来回顾一下这个例子中发生了什么：

1. 我们调用 `ReactDOM.render()` 函数，并传入 `<Welcome name="Sara" />` 作为参数。
2. React 调用 `Welcome` 组件，并将 `{name: 'Sara'}` 作为 props 传入。
3. `Welcome` 组件将 `<h1>Hello, Sara</h1>` 元素作为返回值。
4. React DOM 将 DOM 高效地更新为 `<h1>Hello, Sara</h1>`。

> **注意：** 组件名称必须以大写字母开头。
>
> React 会将以小写字母开头的组件视为原生 DOM 标签。例如，`<div />` 代表 HTML 的 div 标签，而 `<Welcome />` 则代表一个组件，并且需在作用域内使用 `Welcome`。
>
> 你可以在[深入 JSX](https://react.docschina.org/docs/jsx-in-depth.html#user-defined-components-must-be-capitalized)中了解更多关于此规范的原因。

### 组合组件

组件可以在其输出中引用其他组件。这就可以让我们用同一组件来抽象出任意层次的细节。按钮，表单，对话框，甚至整个屏幕的内容：在 React 应用程序中，这些通常都会以组件的形式表示。

例如，我们可以创建一个可以多次渲染 `Welcome` 组件的 `App` 组件：

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
          <Welcome name="Sara" />
          <Welcome name="Cahal" />
          <Welcome name="Edite" />
      </div>
  );
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
);
```

通常来说，每个新的 React 应用程序的顶层组件都是 `App` 组件。但是，如果你将 React 集成到现有的应用程序中，你可能需要使用像 `Button` 这样的小组件，并自下而上地将这类组件逐步应用到视图层的每一处。

### 提取组件

将组件拆分为更小的组件。

例如，参考如下 `Comment` 组件：

```react
function Comment(props) {
    return (
        <div className="Comment">
            <div className="UserInfo">
                <img className="Avatar"
                    src={props.author.avatarUrl}
                    alt={props.author.name}/>
                <div className="UserInfo-name">
                    {props.author.name}
                </div>
            </div>
            <div className="Comment-text">
                {props.text}
            </div>
            <div className="Comment-date">
                {formatDate(props.date)}
            </div>
        </div>
  );
}
```

该组件用于描述一个社交媒体网站上的评论功能，它接收 `author`（对象），`text` （字符串）以及 `date`（日期）作为 props。

该组件由于嵌套的关系，变得难以维护，且很难复用它的各个部分。因此，让我们从中提取一些组件出来。

首先，我们将提取 `Avatar` 组件：

```react
function Avatar(props) {
  return (
    <img className="Avatar" src={props.user.avatarUrl} alt={props.user.name} />  );
}
```

`Avatar` 不需知道它在 `Comment` 组件内部是如何渲染的。因此，我们给它的 props 起了一个更通用的名字：`user`，而不是 `author`。

我们建议从组件自身的角度命名 props，而不是依赖于调用组件的上下文命名。

我们现在针对 `Comment` 做些微小调整：

```react
function Comment(props) {
    return (
      <div className="Comment">
          <div className="UserInfo">
              <Avatar user={props.author} />
              <div className="UserInfo-name">
                  {props.author.name}
              </div>
            </div>
            <div className="Comment-text">
                {props.text}
            </div>
            <div className="Comment-date">
                {formatDate(props.date)}
            </div>
        </div>
    );
}
```

接下来，我们将提取 `UserInfo` 组件，该组件在用户名旁渲染 `Avatar` 组件：

```react
function UserInfo(props) {
  return (
    <div className="UserInfo">
          <Avatar user={props.user} />
          <div className="UserInfo-name">
              {props.user.name}
          </div>
      </div>
  );
}
```

进一步简化 `Comment` 组件：

```react
function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

最初看上去，提取组件可能是一件繁重的工作，但是，在大型应用中，构建可复用组件库是完全值得的。根据经验来看，如果 UI 中有一部分被多次使用（`Button`，`Panel`，`Avatar`），或者组件本身就足够复杂（`App`，`FeedStory`，`Comment`），那么它就是一个可复用组件的候选项。

### Props 的只读性

组件无论是使用[函数声明还是通过 class 声明](https://react.docschina.org/docs/components-and-props.html#function-and-class-components)，都决不能修改自身的 props。来看下这个 `sum` 函数：

```react
function sum(a, b) {
  return a + b;
}
```

这样的函数被称为[“纯函数”](https://en.wikipedia.org/wiki/Pure_function)，因为该函数不会尝试更改入参，且多次调用下相同的入参始终返回相同的结果。

相反，下面这个函数则不是纯函数，因为它更改了自己的入参：

```react
function withdraw(account, amount) {
  account.total -= amount;
}
```

React 非常灵活，但它也有一个严格的规则：

**所有 React 组件都必须像纯函数一样保护它们的 props 不被更改。**

当然，应用程序的 UI 是动态的，并会伴随着时间的推移而变化。

## State & 生命周期

本页面介绍了 React 组件中 state 和生命周期的概念。你可以查阅[详细的组件 API 参考文档](https://react.docschina.org/docs/react-component.html)。

在[元素渲染](https://react.docschina.org/docs/rendering-elements.html#rendering-an-element-into-the-dom)章节中，我们只了解了一种更新 UI 界面的方法。通过调用 `ReactDOM.render()` 来修改我们想要渲染的元素：

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
      element,
      document.getElementById('root')
  );
}
setInterval(tick, 1000);
```

在本章节中，我们将学习如何封装真正可复用的 `Clock` 组件。它将设置自己的计时器并每秒更新一次。

我们可以从封装时钟的外观开始：

```react
function Clock(props) {
  return (
    <div>
          <h1>Hello, world!</h1>
          <h2>It is {props.date.toLocaleTimeString()}.</h2>
      </div>
  );
}

function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,
      document.getElementById('root')
  );
}

setInterval(tick, 1000);
```

然而，它忽略了一个关键的技术细节：`Clock` 组件需要设置一个计时器，并且需要每秒更新 UI。

理想情况下，我们希望只编写一次代码，便可以让 `Clock` 组件自我更新：

```react
ReactDOM.render(
  <Clock />,  document.getElementById('root')
);
```

我们需要在 `Clock` 组件中添加 “state” 来实现这个功能。

State 与 props 类似，但是 state 是私有的，并且完全受控于当前组件。

### 将函数组件转换成 class 组件

通过以下五步将 `Clock` 的函数组件转成 class 组件：

1. 创建一个同名的 [ES6 class](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes)，并且继承于 `React.Component`。
2. 添加一个空的 `render()` 方法。
3. 将函数体移动到 `render()` 方法之中。
4. 在 `render()` 方法中使用 `this.props` 替换 `props`。
5. 删除剩余的空函数声明。

```react
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

现在 `Clock` 组件被定义为 class，而不是函数。

每次组件更新时 `render` 方法都会被调用，但只要在相同的 DOM 节点中渲染 `<Clock />` ，就仅有一个 `Clock` 组件的 class 实例被创建使用。这就使得我们可以使用如 state 或生命周期方法等很多其他特性。

### 向 class 组件中添加局部的 state

我们通过以下三步将 `date` 从 props 移动到 state 中：

1. 把 `render()` 方法中的 `this.props.date` 替换成 `this.state.date` ：

```react
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
        </div>
    );
  }
}
```

1. 添加一个 [class 构造函数](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes#Constructor)，然后在该函数中为 `this.state` 赋初值：

```react
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

通过以下方式将 `props` 传递到父类的构造函数中：

```react
  constructor(props) {
    super(props);    this.state = {date: new Date()};
  }
```

Class 组件应该始终使用 `props` 参数来调用父类的构造函数。

1. 移除 `<Clock />` 元素中的 `date` 属性：

```react
ReactDOM.render(
  <Clock />,  document.getElementById('root')
);
```

我们之后会将计时器相关的代码添加到组件中。

代码如下：

```react
class Clock extends React.Component {
  constructor(props) {    super(props);    this.state = {date: new Date()};  }
  render() {
    return (
        <div>
            <h1>Hello, world!</h1>
            <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
        </div>
    );
  }
}

ReactDOM.render(
  <Clock />,  document.getElementById('root')
);
```

接下来，我们会设置 `Clock` 的计时器并每秒更新它。

### 将生命周期方法添加到 Class 中

在具有许多组件的应用程序中，当组件被销毁时释放所占用的资源是非常重要的。

当 `Clock` 组件第一次被渲染到 DOM 中的时候，就为其[设置一个计时器](https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setInterval)。这在 React 中被称为“挂载（mount）”。

同时，当 DOM 中 `Clock` 组件被删除的时候，应该[清除计时器](https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/clearInterval)。这在 React 中被称为“卸载（unmount）”。

我们可以为 class 组件声明一些特殊的方法，当组件挂载或卸载时就会去执行这些方法：

```react
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {  }
  componentWillUnmount() {  }
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

这些方法叫做“生命周期方法”。

`componentDidMount()` 方法会在组件已经被渲染到 DOM 中后运行，所以，最好在这里设置计时器：

```react
  componentDidMount() {
    this.timerID = setInterval(() => this.tick(),1000);
  }
```

接下来把计时器的 ID 保存在 `this` 之中（`this.timerID`）。

尽管 `this.props` 和 `this.state` 是 React 本身设置的，且都拥有特殊的含义，但是其实你可以向 class 中随意添加不参与数据流（比如计时器 ID）的额外字段。

我们会在 `componentWillUnmount()` 生命周期方法中清除计时器：

```react
  componentWillUnmount() {
    clearInterval(this.timerID);
  }
```

最后，我们会实现一个叫 `tick()` 的方法，`Clock` 组件每秒都会调用它。

使用 `this.setState()` 来时刻更新组件 state：

```react
class Clock extends React.Component {
   constructor(props) {
      super(props);
      this.state = {date: new Date()};
   }

   componentDidMount() {
      this.timerID = setInterval(
         () => this.tick(),
         1000
      );
   }

   componentWillUnmount() {
      clearInterval(this.timerID);
   }

   tick() {
      this.setState({date: new Date()});}
   render() {
      return (
         <div>
            <h1>Hello, world!</h1>
            <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
         </div>
      );
   }
}

ReactDOM.render(
   <Clock />,
   document.getElementById('root')
);
```

现在时钟每秒都会刷新。

让我们来快速概括一下发生了什么和这些方法的调用顺序：

1. 当 `<Clock />` 被传给 `ReactDOM.render()`的时候，React 会调用 `Clock` 组件的构造函数。因为 `Clock` 需要显示当前的时间，所以它会用一个包含当前时间的对象来初始化 `this.state`。我们会在之后更新 state。
2. 之后 React 会调用组件的 `render()` 方法。这就是 React 确定该在页面上展示什么的方式。然后 React 更新 DOM 来匹配 `Clock` 渲染的输出。
3. 当 `Clock` 的输出被插入到 DOM 中后，React 就会调用 `ComponentDidMount()` 生命周期方法。在这个方法中，`Clock` 组件向浏览器请求设置一个计时器来每秒调用一次组件的 `tick()` 方法。
4. 浏览器每秒都会调用一次 `tick()` 方法。 在这方法之中，`Clock` 组件会通过调用 `setState()` 来计划进行一次 UI 更新。得益于 `setState()` 的调用，React 能够知道 state 已经改变了，然后会重新调用 `render()` 方法来确定页面上该显示什么。这一次，`render()` 方法中的 `this.state.date` 就不一样了，如此以来就会渲染输出更新过的时间。React 也会相应的更新 DOM。
5. 一旦 `Clock` 组件从 DOM 中被移除，React 就会调用 `componentWillUnmount()` 生命周期方法，这样计时器就停止了。

### 正确地使用 State

关于 `setState()` 你应该了解三件事：

#### 不要直接修改 State

例如，此代码不会重新渲染组件：

```react
// Wrong
this.state.comment = 'Hello';
```

而是应该使用 `setState()`:

```react
// Correct
this.setState({comment: 'Hello'});
```

构造函数是唯一可以给 `this.state` 赋值的地方：

#### State 的更新可能是异步的

出于性能考虑，React 可能会把多个 `setState()` 调用合并成一个调用。

因为 `this.props` 和 `this.state` 可能会异步更新，所以你不要依赖他们的值来更新下一个状态。

例如，此代码可能会无法更新计数器：

```react
// Wrong
this.setState({
  counter: this.state.counter + this.props.increment,
});
```

要解决这个问题，可以让 `setState()` 接收一个函数而不是一个对象。这个函数用上一个 state 作为第一个参数，将此次更新被应用时的 props 做为第二个参数：

```react
// Correct
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

上面使用了[箭头函数](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)，不过使用普通的函数也同样可以：

```react
// Correct
this.setState(function(state, props) {
  return {
    counter: state.counter + props.increment
  };
});
```

#### State 的更新会被合并

当你调用 `setState()` 的时候，React 会把你提供的对象合并到当前的 state。

例如，你的 state 包含几个独立的变量：

```react
  constructor(props) {
    super(props);
    this.state = {
        posts: [],
        comments: []
    };
  }
```

然后你可以分别调用 `setState()` 来单独地更新它们：

```react
  componentDidMount() {
    fetchPosts().then(response => {
      this.setState({
        posts: response.posts      });
    });

    fetchComments().then(response => {
      this.setState({
        comments: response.comments      });
    });
  }
```

这里的合并是浅合并，所以 `this.setState({comments})` 完整保留了 `this.state.posts`， 但是完全替换了 `this.state.comments`。

> **重点**
>
> - 所有的setState都需要添加大括号
> - 大括号内需要添加counter

### 数据是向下流动的

不管是父组件或是子组件都无法知道某个组件是有状态的还是无状态的，并且它们也并不关心它是函数组件还是 class 组件。

这就是为什么称 state 为局部的或是封装的的原因。除了拥有并设置了它的组件，其他组件都无法访问。

组件可以选择把它的 state 作为 props 向下传递到它的子组件中：

```react
<h2>It is {this.state.date.toLocaleTimeString()}.</h2>
```

这对于自定义组件同样适用：

```react
<FormattedDate date={this.state.date} />
```

`FormattedDate` 组件会在其 props 中接收参数 `date`，但是组件本身无法知道它是来自于 `Clock` 的 state，或是 `Clock` 的 props，还是手动输入的：

```react
function FormattedDate(props) {
  return <h2>It is {props.date.toLocaleTimeString()}.</h2>;
}
```

这通常会被叫做“自上而下”或是“单向”的数据流。任何的 state 总是所属于特定的组件，而且从该 state 派生的任何数据或 UI 只能影响树中“低于”它们的组件。

如果你把一个以组件构成的树想象成一个 props 的数据瀑布的话，那么每一个组件的 state 就像是在任意一点上给瀑布增加额外的水源，但是它只能向下流动。

为了证明每个组件都是真正独立的，我们可以创建一个渲染三个 `Clock` 的 `App` 组件：

```react
function App() {
  return (
      <div>
          <Clock />
          <Clock />
          <Clock />
      </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

每个 `Clock` 组件都会单独设置它自己的计时器并且更新它。

在 React 应用中，组件是有状态组件还是无状态组件属于组件实现的细节，它可能会随着时间的推移而改变。你可以在有状态的组件中使用无状态的组件，反之亦然。

### 📌Class 组件 & 生命周期 补充

> React 的组件可以定义为 class 或函数的形式。class 组件目前提供了更多的功能，这些功能将在此章节中详细介绍。如需定义 class 组件，需要继承 `React.Component`：

```react
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

#### 挂载

当组件实例被创建并插入 DOM 中时，其生命周期调用顺序如下：

- [**`constructor()`**](https://react.docschina.org/docs/react-component.html#constructor) -- 初始化函数

  > **避免将 props 的值复制给 state！这是一个常见的错误：**
  >
  > ```react
  > constructor(props) {
  >  super(props);
  >  // 不要这样做
  >  this.state = { color: props.color };
  > }
  > ```
  >
  > 如此做毫无必要（你可以直接使用 `this.props.color`），同时还产生了 bug（更新 prop 中的 `color` 时，并不会影响 state）。
  >
  > **只有在你刻意忽略 prop 更新的情况下使用。**此时，应将 prop 重命名为 `initialColor` 或 `defaultColor`。必要时，你可以修改它的 `key`，以强制“重置”其内部 state。
  >
  > 如下：
  >
  > ```react
  > class EmailInput extends Component {
  >   state = { email: this.props.defaultEmail };
  > 
  >   handleChange = event => {
  >     this.setState({ email: event.target.value });
  >   };
  > 
  >   render() {
  >     return <input onChange={this.handleChange} value={this.state.email} />;
  >   }
  > }
  > // 使用方法
  > <EmailInput
  >   defaultEmail={this.props.user.email}
  >   key={this.props.user.id}
  > />
  > ```

- [`static getDerivedStateFromProps()`](https://react.docschina.org/docs/react-component.html#static-getderivedstatefromprops)

- [**`render()`**](https://react.docschina.org/docs/react-component.html#render) -- 实现方法

- [**`componentDidMount()`**](https://react.docschina.org/docs/react-component.html#componentdidmount)

### 📌setStare方法-中括号-补充

> 用中括号更新传入数据对应的状态

```react
class Reservation extends React.Component {
   constructor(props) {
      super(props);
      this.state = {isGoing: true};
      this.handleInputChange = this.handleInputChange.bind(this);
   }
   handleInputChange(event) {
      const value = '5';
      const name = 'isGoing';
      this.setState({
         [name]: value // 属性名不是name, 而是name变量的值
      }); 				//==> this.setState({isGoing:value})
   }
   render() {
      return (
      		//无视ing
      );
   }
}

ReactDOM.render(
   <Reservation/>,
   document.getElementById('root')
)
```

## 事件处理

React 元素的事件处理和 DOM 元素的很相似，但是有一点语法上的不同：

- React 事件的命名采用小驼峰式（camelCase），而不是纯小写。
- 使用 JSX 语法时你需要传入一个函数作为事件处理函数，而不是一个字符串。

例如，传统的 HTML：

```react
<button onclick="activateLasers()">
  Activate Lasers
</button>
```

在 React 中略微不同：

```react
<button onClick={activateLasers}>  Activate Lasers
</button>
```

在 React 中另一个不同点是你不能通过返回 `false` 的方式阻止默认行为。你必须显式的使用 `preventDefault` 。例如，传统的 HTML 中阻止链接默认打开一个新页面，你可以这样写：

```react
<a href="#" onclick="console.log('The link was clicked.'); return false">
  Click me
</a>
```

在 React 中，可能是这样的：

```react
function ActionLink() {
  function handleClick(e) {
      e.preventDefault();
      console.log('The link was clicked.');
  }
  return (
    <a href="#" onClick={handleClick}>
          Click me
    </a>
  );
}
```

在这里，`e` 是一个合成事件。React 根据 [W3C 规范](https://www.w3.org/TR/DOM-Level-3-Events/)来定义这些合成事件，所以你不需要担心跨浏览器的兼容性问题。如果想了解更多，请查看 [`SyntheticEvent`](https://react.docschina.org/docs/events.html) 参考指南。

使用 React 时，你一般不需要使用 `addEventListener` 为已创建的 DOM 元素添加监听器。事实上，你只需要在该元素初始渲染的时候添加监听器即可。

当你使用 [ES6 class](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes) 语法定义一个组件的时候，通常的做法是将事件处理函数声明为 class 中的方法。例如，下面的 `Toggle` 组件会渲染一个让用户切换开关状态的按钮：

```react
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // 为了在回调中使用 `this`，这个绑定是必不可少的
    this.handleClick = this.handleClick.bind(this);  }

  handleClick() {
      this.setState(state => ({
          isToggleOn: !state.isToggleOn
      }));
  }
  render() {
    return (
      <button onClick={this.handleClick}>
            {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

你必须谨慎对待 JSX 回调函数中的 `this`，在 JavaScript 中，class 的方法默认不会[绑定](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_objects/Function/bind) `this`。如果你忘记绑定 `this.handleClick` 并把它传入了 `onClick`，当你调用这个函数的时候 `this` 的值为 `undefined`。

这并不是 React 特有的行为；这其实与 [JavaScript 函数工作原理](https://www.smashingmagazine.com/2014/01/understanding-javascript-function-prototype-bind/)有关。通常情况下，如果你没有在方法后面添加 `()`，例如 `onClick={this.handleClick}`，你应该为这个方法绑定 `this`。

如果觉得使用 `bind` 很麻烦，这里有两种方式可以解决。如果你正在使用实验性的public class fields 语法，你可以使用 class fields 正确的绑定回调函数：

```react
class LoggingButton extends React.Component {
    // 此语法确保 `handleClick` 内的 `this` 已被绑定。  
    // 注意: 这是 *实验性* 语法。  
    handleClick = () => {
        console.log('this is:', this);
    }
    render() {
        return (
            <button onClick={this.handleClick}>
                Click me
            </button>
        );
    }
}
```

[Create React App](https://github.com/facebookincubator/create-react-app) 默认启用此语法。

如果你没有使用 class fields 语法，你可以在回调中使用[箭头函数](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/Arrow_functions)：

```react
class LoggingButton extends React.Component {
    handleClick() {
        console.log('this is:', this);
    }
    render() {
        // 此语法确保 `handleClick` 内的 `this` 已被绑定。
        return (
            <button onClick={() => this.handleClick()}>
                Click me
            </button>
        );
    }
}
```

此语法问题在于每次渲染 `LoggingButton` 时都会创建不同的回调函数。在大多数情况下，这没什么问题，但如果该回调函数作为 prop 传入子组件时，这些组件可能会进行额外的重新渲染。我们通常建议在构造器中绑定或使用 class fields 语法来避免这类性能问题。

### 向事件处理程序传递参数

在循环中，通常我们会为事件处理函数传递额外的参数。例如，若 `id` 是你要删除那一行的 ID，以下两种方式都可以向事件处理函数传递参数：

```react
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

上述两种方式是等价的，分别通过[箭头函数](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)和 [`Function.prototype.bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) 来实现。

在这两种情况下，React 的事件对象 `e` 会被作为第二个参数传递。如果通过箭头函数的方式，事件对象必须显式的进行传递，而通过 `bind` 的方式，事件对象以及更多的参数将会被隐式的进行传递。

#### 事件传参详解

```react
// 传参后，重写元素渲染
function App() {
   function get_name(){
      name = document.querySelector('#lastname').value
      props.author.name = name
      ReactDOM.render(<App />,document.querySelector('body'))
   }
   return (
      <div id="root">
         <input type="text" value={props.author.name} />
         <input id='lastname' />
         <input type="button" value="修改名称" onClick={get_name} />
      </div>
   );
}

// 传参后，重写元素渲染
class App extends React.Component {
   get_name(){
      name = document.querySelector('#lastname').value
      props.author.name = name
      ReactDOM.render(<App />,document.querySelector('body'))
   }

   render() {
      return (
         <div id="root">
            <input type="text" value={props.author.name} />
            <input id='lastname' />
            <input type="button" value="修改名称" onClick={this.get_name} />
         </div>
      );
   }
}

ReactDOM.render(<App />,document.querySelector('body'))

```

## 条件渲染

在 React 中，你可以创建不同的组件来封装各种你需要的行为。然后，依据应用的不同状态，你可以只渲染对应状态下的部分内容。

React 中的条件渲染和 JavaScript 中的一样，使用 JavaScript 运算符 `if`或者 条件运算符 去创建元素来表现当前的状态，然后让 React 根据它们来更新 UI。

观察这两个组件:

```react
function UserGreeting(props) {
    return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
    return <h1>Please sign up.</h1>;
}
```

再创建一个 `Greeting` 组件，它会根据用户是否登录来决定显示上面的哪一个组件。

```react
function Greeting(props) {
	const isLoggedIn = props.isLoggedIn;
	if (isLoggedIn) {
		return <UserGreeting />;
	}
	return <GuestGreeting />;}
ReactDOM.render(
	// Try changing to isLoggedIn={true}:
	<Greeting isLoggedIn={false} />,  document.getElementById('root'));
```

这个示例根据 `isLoggedIn` 的值来渲染不同的问候语。

### 元素变量

你可以使用变量来储存元素。 它可以帮助你有条件地渲染组件的一部分，而其他的渲染部分并不会因此而改变。

在下面的示例中，我们将创建一个名叫 `LoginControl` 的[有状态的组件](https://react.docschina.org/docs/state-and-lifecycle.html#adding-local-state-to-a-class)。

它将根据当前的状态来渲染 `<LoginButton />` 或者 `<LogoutButton />`。同时它还会渲染上一个示例中的 `<Greeting />`。

```react
function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}

class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }

  handleLogoutClick() {
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    if (isLoggedIn) {
        button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
        button = <LoginButton onClick={this.handleLoginClick} />;
    }
    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
            {button}
        </div>
    );
  }
}

ReactDOM.render(
  <LoginControl />,
  document.getElementById('root')
);
```

声明一个变量并使用 `if` 语句进行条件渲染是不错的方式，但有时你可能会想使用更为简洁的语法。

### 与运算符 &&

```react
function Mailbox(props) {
  const unreadMessages = props.unreadMessages;
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 &&        <h2>          You have {unreadMessages.length} unread messages.        </h2>      }    </div>
  );
}

const messages = ['React', 'Re: React', 'Re:Re: React'];
ReactDOM.render(
  <Mailbox unreadMessages={messages} />,
  document.getElementById('root')
);
```

> 之所以能这样做，是因为在 JavaScript 中，`true && expression` 总是会返回 `expression`, 而 `false && expression` 总是会返回 `false`。
>
> 因此，如果条件是 `true`，`&&` 右侧的元素就会被渲染，如果是 `false`，React 会忽略并跳过它。
>
> 请注意，返回 false 的表达式会使 `&&` 后面的元素被跳过，但会返回 false 表达式。在下面示例中，render 方法的返回值是 `<div>0</div>`。

```react
render() {
  const count = 0;  return (
    <div>
      { count && <h1>Messages: {count}</h1>}    </div>
  );
}
```

### 三目运算符

另一种内联条件渲染的方法是使用 JavaScript 中的三目运算符 [`condition ? true : false`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)。

在下面这个示例中，我们用它来条件渲染一小段文本

```react
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
      <div>
          The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in. 
      </div>
  );
}
```

同样的，它也可以用于较为复杂的表达式中，虽然看起来不是很直观：

```react
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
    <div>
          {
              isLoggedIn? 
              <LogoutButton onClick={this.handleLogoutClick} />:
              <LoginButton onClick={this.handleLoginClick} />
          }
    </div>
  );
}
```

就像在 JavaScript 中一样，你可以根据团队的习惯来选择可读性更高的代码风格。需要注意的是，如果条件变得过于复杂，那你应该考虑如何[提取组件](https://react.docschina.org/docs/components-and-props.html#extracting-components)。

### 阻止组件渲染

在极少数情况下，你可能希望能隐藏组件，即使它已经被其他组件渲染。若要完成此操作，你可以让 `render` 方法直接返回 `null`，而不进行任何渲染。

下面的示例中，`<WarningBanner />` 会根据 prop 中 `warn` 的值来进行条件渲染。如果 `warn` 的值是 `false`，那么组件则不会渲染:

```react
function WarningBanner(props) {
  if (!props.warn) {    return null;  }
  return (
    <div className="warning">
      Warning!
    </div>
  );
}

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {showWarning: true};
    this.handleToggleClick = this.handleToggleClick.bind(this);
  }

  handleToggleClick() {
    this.setState(state => ({
      showWarning: !state.showWarning
    }));
  }

  render() {
    return (
      <div>
        <WarningBanner warn={this.state.showWarning} />        <button onClick={this.handleToggleClick}>
          {this.state.showWarning ? 'Hide' : 'Show'}
        </button>
      </div>
    );
  }
}

ReactDOM.render(
  <Page />,
  document.getElementById('root')
);
```

在组件的 `render` 方法中返回 `null` 并不会影响组件的生命周期。例如，上面这个示例中，`componentDidUpdate` 依然会被调用。

## 列表 & Key

### 渲染多个组件

你可以通过使用 `{}` 在 JSX 内构建一个[元素集合](https://react.docschina.org/docs/introducing-jsx.html#embedding-expressions-in-jsx)。

下面，我们使用 Javascript 中的 [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) 方法来遍历 `numbers` 数组。将数组中的每个元素变成 `<li>` 标签，最后我们将得到的数组赋值给 `listItems`：

```react
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>  <li>{number}</li>);
ReactDOM.render(
  <ul>{listItems}</ul>,  document.getElementById('root')
);
```

### 基础列表组件

通常你需要在一个`组件`中渲染列表。

我们可以把前面的例子重构成一个组件，这个组件接收 `numbers` 数组作为参数并输出一个元素列表。

```react
function NumberList(props) {
    const numbers = props.numbers;
    const listItems = numbers.map((number) =><li>{number}</li>);
    return (<ul>{listItems}</ul>);
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
    <NumberList numbers={numbers} />,  document.getElementById('root')
);
```

当我们运行这段代码，将会看到一个警告 `a key should be provided for list items`，意思是当你创建一个元素时，必须包括一个特殊的 `key` 属性。

让我们来给每个列表元素分配一个 `key` 属性来解决上面的那个警告：

```react
function NumberList(props) {
    const numbers = props.numbers;
    const listItems = numbers.map((number) =>
          <li key={number.toString()}>
              {number}
          </li>);
    return (<ul>{listItems}</ul>);
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```

### map() 方法

```react
 const listItems = numbers.map((number) =>
          <li key={number.toString()}>
              {number}
          </li>);
```

>### 定义和用法
>
>map() 方法返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值。<br>map() 方法按照原始数组元素顺序依次处理元素。<br>**注意：** map() 不会对空数组进行检测。<br>**注意：** map() 不会改变原始数组。

### 📌列表 & Key[绑定点击事件]补充

```react
function Listitem(props) {
   const number = props.number;
   return (
      <li>
         <button onClick={() => console.log(number)}>
            {number}
         </button>
      </li>
   )
}

class Login extends React.Component {
   constructor(props) {
      super(props);
   }
   render() {
      const listItems = this.props.numbers.map((number) =>
         <Listitem number={number}/>
      );
      return (
         listItems
      );
   }
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
   <Login numbers={numbers}/>,
   document.querySelector('#root')
)
```

## 表单

### 受控组件

在 HTML 中，表单元素（如`<input>`、 `<textarea>` 和 `<select>`）之类的表单元素通常自己维护 state，并根据用户输入进行更新。而在 React 中，可变状态（mutable state）通常保存在组件的 state 属性中，并且只能通过使用 [`setState()`](https://react.docschina.org/docs/react-component.html#setstate)来更新。

我们可以把两者结合起来，使 React 的 state 成为“唯一数据源”。渲染表单的 React 组件还控制着用户输入过程中表单发生的操作。被 React 以这种方式控制取值的表单输入元素就叫做“受控组件”。

例如，如果我们想让前一个示例在提交时打印出名称，我们可以将表单写为受控组件：

```react
class NameForm extends React.Component {
	constructor(props) {
		super(props);
		this.state = {value: ''};

		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleChange(event) {
		this.setState({value: event.target.value});
	}

	handleSubmit(event) {
		alert('提交的名字: ' + this.state.value);
		event.preventDefault();
	}

	render() {
		return (
			<form onSubmit={this.handleSubmit}>
				<label>
					名字:
					<input type="text" value={this.state.value} onChange={this.handleChange} />
				</label>
				<input type="submit" value="提交" />
			</form>
		);
	}
}
ReactDOM.render(
	<NameForm/>,
	document.querySelector('#root')
)
```

> 由于在表单元素上设置了 `value` 属性，因此显示的值将始终为 `this.state.value`，这使得 React 的 state 成为唯一数据源。由于 `handlechange` 在每次按键时都会执行并更新 React 的 state，因此显示的值将随着用户输入而更新。
>
> 对于受控组件来说，输入的值始终由 React 的 state 驱动。你也可以将 value 传递给其他 UI 元素，或者通过其他事件处理函数重置，但这意味着你需要编写更多的代码。

### 📌preventDefault 方法

> 取消事件的默认动作。

```javascript
event.preventDefault()
```

### textarea 标签

在 HTML 中, `<textarea>` 元素通过其子元素定义其文本:

```html
<textarea>
  你好， 这是在 text area 里的文本
</textarea>
```

而在 React 中，`<textarea>` 使用 `value` 属性代替。这样，可以使得使用 `<textarea>` 的表单和使用单行 input 的表单非常类似：

```react
class Textarea extends React.Component {
   constructor(props) {
      super(props);
      this.state = {
         value:'开始新的旅程'
      };
      this.changetext = this.changetext.bind(this);
   }
   changetext(event){
      this.setState({value: event.target.value});
      console.log(this.state.value);
   }
   render() {
      return (
         <textarea value={this.state.value} onChange={this.changetext}></textarea>
      )
   }
}
ReactDOM.render(
   <Textarea />,
   document.getElementById('root')
)
```

### 📌target 事件属性

target 事件属性可返回事件的目标节点（触发该事件的节点），如生成事件的元素、文档或窗口。

```javascript
event.target
```

### select 标签

在 HTML 中，`<select>` 创建下拉列表标签。例如，如下 HTML 创建了水果相关的下拉列表：

```html
<select>
  <option value="grapefruit">葡萄柚</option>
  <option value="lime">酸橙</option>
  <option selected value="coconut">椰子</option>
  <option value="mango">芒果</option>
</select>
```

请注意，由于 `selected` 属性的缘故，椰子选项默认被选中。React 并不会使用 `selected` 属性，而是在根 `select` 标签上使用 `value` 属性。这在受控组件中更便捷，因为您只需要在根标签中更新它。

```react
class SelectF extends React.Component {
   constructor(props) {
      super(props);
      let moren = props.numbers[0];
      let morenvalue = moren.number + ' - ' + moren.title;
      this.state = {value: morenvalue};

      this.handleChange = this.handleChange.bind(this);
   }

   handleChange(event) {
      this.setState({value: event.target.value});
      console.log(event.target.value);
   }

   render() {
      const numbers = this.props.numbers;
      const options = numbers.map((number) => <option key={number.id}>{number.number} - {number.title}</option>);
      return (
         <select value={this.state.value} onChange={this.handleChange}>
            {options}
         </select>
      )
   }
}

const numbers = [
   {id: 0, number: 1, title: '西瓜'},
   {id: 1, number: 2, title: '冬瓜'},
   {id: 2, number: 3, title: '哈密瓜'}
];
ReactDOM.render(
   <SelectF numbers={numbers}/>,
   document.getElementById('root')
)
```

```react
class FlavorForm extends React.Component {
   constructor(props) {
      super(props);
      this.state = {value: 'coconut'};

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
   }

   handleChange(event) {
      this.setState({value: event.target.value});
   }

   handleSubmit(event) {
      alert('你喜欢的风味是: ' + this.state.value);
      event.preventDefault();
   }

   render() {
      return (
         <form onSubmit={this.handleSubmit}>
            <label>
               选择你喜欢的风味:
               <select value={this.state.value} onChange={this.handleChange}>
                  <option value="grapefruit">葡萄柚</option>
                  <option value="lime">酸橙</option>
                  <option value="coconut">椰子</option>
                  <option value="mango">芒果</option>
               </select>
            </label>
            <input type="submit" value="提交" />
         </form>
      );
   }
}
ReactDOM.render(
   <FlavorForm/>,
   document.getElementById('root')
)
```

总的来说，这使得 `<input type="text">`, `<textarea>` 和 `<select>` 之类的标签都非常相似—它们都接受一个 `value` 属性，你可以使用它来实现受控组件。

### 处理多个输入

当需要处理多个 `input` 元素时，我们可以给每个元素添加 `name` 属性，并让处理函数根据 `event.target.name` 的值选择要执行的操作。

```react
class Reservation extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			isGoing: true,
			numberOfGuests: 2
		};

		this.handleInputChange = this.handleInputChange.bind(this);
	}

	handleInputChange(event) {
		const target = event.target;
		const value = target.name === 'isGoing' ? target.checked : target.value;
		const name = target.name;

		this.setState({
			[name]: value
		});
	}

	render() {
		return (
			<form>
				<label>
					参与:
					<input
						name="isGoing"
						type="checkbox"
						checked={this.state.isGoing}
						onChange={this.handleInputChange}/>
				</label>
				<br/>
				<label>
					来宾人数:
					<input
						name="numberOfGuests"
						type="number"
						value={this.state.numberOfGuests}
						onChange={this.handleInputChange}/>
				</label>
			</form>
		);
	}
}
```

### 受控输入空值

在[受控组件](https://react.docschina.org/docs/forms.html#controlled-components)上指定 value 的 prop 会阻止用户更改输入。如果你指定了 `value`，但输入仍可编辑，则可能是你意外地将`value` 设置为 `undefined` 或 `null`。

下面的代码演示了这一点。（输入最初被锁定，但在短时间延迟后变为可编辑。）

```react
ReactDOM.render(<input value="hi" />, mountNode);

setTimeout(function() {
  ReactDOM.render(<input value={null} />, mountNode);
}, 1000);
```

> 在指定了value后，必须实现重新渲染，这样才能实现编辑。

## 状态提升

例子，创建一个用于计算水在给定温度下是否会沸腾的温度计算器

```react
function BoilingVerdict(props) {
   if (props.celsius >= 100) {
      return <p>沸腾.</p>;
   }
   return <p>未沸腾.</p>;
}
```

```react
class Acg extends React.Component {
   constructor(props) {
      super(props);
      this.state = {value:''};
      this.handchange = this.handchange.bind(this);
   }
   handchange(event) {
      this.setState({value:event.target.value});
   }
   render() {
      return (
         <fieldset>
            <legend>检测是否沸腾</legend>
            <input type="text" value={this.state.value} onChange={this.handchange}/>
            <BoilingVerdict celsius={parseFloat(this.state.value)}/>
         </fieldset>
      )
   }

}
ReactDOM.render(
   <Acg />
   ,document.getElementById('root')
)
```

### 状态提升·进阶

例子，创建一个华氏度、温氏度转换

> 主要函数

```react
function toCelsius(fahrenheit) {
   return (fahrenheit - 32) * 5 / 9;
}

function toFahrenheit(celsius) {
   return (celsius * 9 / 5) + 32;
}
```

```react
const selectitem = {
   c: '摄氏度',
   f: '华氏度'
}

class Acg extends React.Component {
   constructor(props) {
      super(props);
      this.handchange = this.handchange.bind(this);
   }

   handchange(event) {
      this.props.onChange(event.target.value);
   }

   render() {
      const se = this.props.selected;
      const value = this.props.value;
      return (
         <fieldset>
            <legend>请输入{selectitem[se]}</legend>
            <input type="text" value={value} onChange={this.handchange}/>
         </fieldset>
      )
   }

}

class Abc extends React.Component {
   constructor(props) {
      super(props);
      this.state = {
         value: '',
         scale: 'c'
      };
      this.handchangec = this.handchangec.bind(this);
      this.handchangef = this.handchangef.bind(this);
   }

   handchangec(value) {
      this.setState({scale: 'c', value: value});
   }

   handchangef(value) {
      this.setState({scale: 'f', value: value});
   }

   tryconvert(value, convert) {
      const input = parseFloat(value);
      const output = Number.isNaN(input) ? '' : convert(input);
      return output;
   }

   render() {
      const value = this.state.value;
      const scale = this.state.scale;
      const celsius = scale === 'f' ? this.tryconvert(value, toCelsius) : value;
      const fahrenheit = scale === 'c' ? this.tryconvert(value, toFahrenheit) : value;
      return (
         <div>
            <Acg selected='c' value={celsius} onChange={this.handchangec}/>
            <Acg selected='f' value={fahrenheit} onChange={this.handchangef}/>
         </div>
      )
   }

}

ReactDOM.render(
   <Abc/>
   , document.getElementById('root')
)
```

### 📌parseFloat 方法

> parseFloat() 函数可解析一个字符串，并返回一个浮点数。

```javascript
parseFloat(string)
```

该函数指定字符串中的首个字符是否是数字。如果是，则对字符串进行解析，直到到达数字的末端为止，然后以数字返回该数字，而不是作为字符串。

> **注意：** 字符串中只返回第一个数字。<br>**注意：** 开头和结尾的空格是允许的。<br>**注意：** 如果字符串的第一个字符不能被转换为数字，那么 parseFloat() 会返回 NaN。

## 组合 vs 继承

React 有十分强大的组合模式。我们推荐使用组合而非继承来实现组件间的代码重用

### 包含关系

有些组件无法提前知晓它们子组件的具体内容。

我们建议这些组件使用一个特殊的 `children` prop 来将他们的子组件传递到渲染结果中：

```react
class Aoe extends React.Component {
   constructor(props) {
      super(props);
   }
   render() {
      return (
         <div name={'name is '+this.props.name} style={styles[this.props.styleName]}>
            {this.props.children}
         </div>
      )
   }
}
```

这使得别的组件可以通过 JSX 嵌套，将任意组件作为子组件传递给它们。

```react
function Ccc(props){
   return (
      <li>{props.number}</li>
   )
}
class Abc extends React.Component {
   constructor(props) {
      super(props);
   }
   render() {
      return (
         <Aoe name="liebiao" styleName="container">
            <Ccc number='9'/>
            <Ccc number='9'/>
            <Ccc number='6'/>
         </Aoe>
      )
   }
}
var styles = ({
   container: {
      color:'red'
   }
});
ReactDOM.render(
   <Abc/>
   , document.getElementById('root')
)
```

### 特例关系

有些时候，我们会把一些组件看作是其他组件的特殊实例，比如 `WelcomeDialog` 可以说是 `Dialog` 的特殊实例。

在 React 中，我们也可以通过组合来实现这一点。“特殊”组件可以通过 props 定制并渲染“一般”组件：

```react
function Dialog(props) {
   return (
      <div>
         <h1 className="Dialog-title">
            {props.title}      </h1>
         <p className="Dialog-message">
            {props.message}      </p>
      </div>
   );
}
function WelcomeDialog() {
   return (
      <Dialog title="Welcome" message="Thank you for visiting our spacecraft!"/>
   );
}
ReactDOM.render(
   <WelcomeDialog/>
   , document.getElementById('root')
)
```

## React 哲学

> - 从设计稿开始
>
> - 第一步：将设计好的 UI 划分为组件层级
>
> - 第二步：用 React 创建一个静态版本
>
> - 第三步：确定 UI state 的最小（且完整）表示
>
> - 第四步：确定 state 放置的位置
>
> - 第五步：添加反向数据流

![Component diagram](https://react.docschina.org/static/eb8bda25806a89ebdc838813bdfa3601/6b2ea/thinking-in-react-components.png)

```react
var styles = ({
   'red': {
      color: 'red'
   }
});

function Eee(props) {
   let style;
   if(!props.stocked){
      style = styles.red
   }
   return (
      <thead>
         <tr style={style}>
            <td>{props.name}</td>
            <td>{props.price}</td>
         </tr>
      </thead>
   )
}

function Ddd(props) {
   return (
      <thead>
      <tr>
         <th>{props.title}</th>
      </tr>
      </thead>
   )
}

function Ccc(props) {
   return (
      <div>
         <table>
            <thead>
            <tr>
               <th>{props.one}</th>
               <th>{props.two}</th>
            </tr>
            </thead>
         </table>
         <table>
            {props.children}
         </table>
      </div>
   )
}

class Bbb extends React.Component{
   constructor(props) {
      super(props);
      this.state = {value:''};
      this.handChange = this.handChange.bind(this);
      this.handCheckboxChange = this.handCheckboxChange.bind(this);
   }
   handChange(e){
      this.setState({value:e.target.value});
      this.props.onChangeV(e.target.value);
   }
   handCheckboxChange(e){
      let state = e.target.checked;
      this.props.onChangeC(state);
   }
   render() {
      return (
         <div>
            <input type="text" placeholder="Search..." onChange={this.handChange} value={this.state.value}/>
            <label><input type="checkbox" onChange={this.handCheckboxChange}/>Only show products in stock</label>
         </div>
      )
   }
}

function Aaa(props) {
   return (
      <div>
         <div name='top'>
            {props.top}
         </div>
         <div name='down'>
            {props.down}
         </div>
      </div>
   )
}

function dedupe(array) {//去重
   return Array.from(new Set(array));
}

class ProcessingItems extends React.Component{
   constructor(props) {
      super(props);
   }
   render() {
      let items = this.props.items;
      let categorys = dedupe(items.map((item) => item.category));
      let processingItems = new Array();
      for (var i = 0; i < categorys.length; i++) {
         processingItems.push(<Ddd title={categorys[i]}/>);
         for (var j = 0; j < items.length; j++) {
            if (items[j].category == categorys[i]) {
               processingItems.push(<Eee name={items[j].name} price={items[j].price} stocked={items[j].stocked}/>)
            }
         }
      }
      return processingItems
   }
}
const Items = [
   {category: "Sporting Goods", price: "$49.99", stocked: true, name: "Football"},
   {category: "Sporting Goods", price: "$9.99", stocked: true, name: "Baseball"},
   {category: "Sporting Goods", price: "$29.99", stocked: false, name: "Basketball"},
   {category: "Electronics", price: "$99.99", stocked: true, name: "iPod Touch"},
   {category: "Electronics", price: "$399.99", stocked: false, name: "iPhone 5"},
   {category: "Electronics", price: "$199.99", stocked: true, name: "Nexus 7"}
]
class Show extends React.Component{
   constructor(props) {
      super(props);
      this.state = {items:Items}
      this.handChangeV = this.handChangeV.bind(this);
      this.handChangeC = this.handChangeC.bind(this);
   }
   handChangeV(value){
      console.log(value);
      let it = new Array();
      if(value != ''){
         for(let i=0;i<Items.length;i++){
            if(Items[i].name === value){
               it.push(Items[i]);
            }
            this.setState({items:it});
         }
      }else {
         this.setState({items:Items});
      }
   }
   handChangeC(value){
      let v = value;
      let it = new Array();
      if(value){
         for(let i=0;i<Items.length;i++){
            if(Items[i].stocked){
               it.push(Items[i]);
            }
            this.setState({items:it});
         }
      }else {
         this.setState({items:Items});
      }

   }

   render() {
      return (
         <Aaa
            top={
               <Bbb onChangeV={this.handChangeV} onChangeC={this.handChangeC}/>
            }
            down={
               <Ccc one='Name' two='Price'>
                  <ProcessingItems items={this.state.items}/>
               </Ccc>
            }
         />
      )
   }
}

ReactDOM.render(
   <Show/>, document.getElementById('root')
)
```

## Refs & DOM

### 创建 Refs①

> **使用`React.createRef()`API创建`ref`**

```react
class Inputs_Refs_Focus extends React.Component {
   constructor() {
      super();
      this.inputUserName = React.createRef();
      this.inputPassWord = React.createRef();
      this.state = {
         username: '',
         password: ''
      };
      this.changeUserName = this.changeUserName.bind(this);
      this.changePassWord = this.changePassWord.bind(this);
      this.setUserNameFocus = this.setUserNameFocus.bind(this);
      this.setPassWordFocus = this.setPassWordFocus.bind(this);
   }

   componentDidMount() {
      this.setUserNameFocus();
   }

   changeUserName(e) {
      this.setState({username: e.target.value});
   }

   changePassWord(e) {
      this.setState({password: e.target.value});
   }
```

### 访问 Refs

````react
   setUserNameFocus() {
      this.inputUserName.current.focus();
   }

   setPassWordFocus() {
      this.inputPassWord.current.focus();
   }
````

### 为 DOM 元素添加 ref

```react
   render() {
      return (
         <div>
            <input type="text" value={this.state.username}
                   placeholder="用户名" onChange={this.changeUserName}
                   ref={this.inputUserName}/>
            <input type="button" value="用户名焦点"
                   onClick={this.setUserNameFocus}/>
            <br/>
            <input type="password" value={this.state.password}
                   placeholder="密码" onChange={this.changePassWord}
                   ref={this.inputPassWord}/>
            <input type="button" value="密码焦点"
                   onClick={this.setPassWordFocus}/>
            <br/>
            <input type="button" value="登录"/>
         </div>
      )
   }
}

ReactDOM.render(
   <Inputs_Refs_Focus />,
   document.getElementById('root')
)
```

> #### Refs 与函数组件
>
> 默认情况下，**你不能在函数组件上使用 `ref` 属性**，因为它们没有实例：
>
> ```react
> function MyFunctionComponent() {
>   return <input />;
> }
> 
> class Parent extends React.Component {
>   constructor(props) {
>     super(props);
>     this.textInput = React.createRef();
>   }
>   render() {
>     return (
>       <MyFunctionComponent ref={this.textInput} />
>     );
>   }
> }
> ```
>
> 如果要在函数组件中使用 `ref`，你可以使用 [`forwardRef`](https://react.docschina.org/docs/forwarding-refs.html)（可与 [`useImperativeHandle`](https://react.docschina.org/docs/hooks-reference.html#useimperativehandle) 结合使用），或者可以将该组件转化为 class 组件。
>
> 不管怎样，你可以**在函数组件内部使用 `ref` 属性**，只要它指向一个 DOM 元素或 class 组件：

### 创建 Refs②

> **使用`回调`的方法创建`refs`**

```react
class Inputs_Refs_Focus extends React.Component {
   constructor() {
      super();
      this.inputUserName = null;
      this.setUserName = element => {
         this.inputUserName = element;
      };
   }
    componentDidMount() {
      this.setUserNameFocus();
   }
```

### 访问Refs

> **使用`回调`创建的Refs，就直接是一个DOM对象了，所以就不需要`current`来获取DOM对象**

```react
   setUserNameFocus() {
      this.inputUserName.focus();
   }
   render() {
      return (
         <div>
            <input type="text" ref={this.setUserName} placeholder="用户名"/>
            <input type="button" value="用户名焦点" onClick={this.setUserNameFocus}/>
         </div>
      )
   }
}
ReactDOM.render(
   <Inputs_Refs_Focus/>,
   document.getElementById('root')
)
```

### 找不同-API&回调

- ### 创建Ref

  **`API`创建Ref**

  ```react
  this.inputUserName = React.createRef();
  ```

  **`回调`创建Ref**

  ```react
  this.inputUserName = null;
  this.setUserName = element => {
      this.inputUserName = element;
  };
  ```

  > API创建的方式更简洁一些，更直观
  >
  > 回调创建的方式有些繁琐

- ### 使用Ref

  **`API`的Ref使用**

  ```react
  <input type="text" ref={this.inputUserName} placeholder="用户名"/>
  ```

  **`回调`的Ref使用**

  ```react
  <input type="text" ref={this.setUserName} placeholder="用户名"/>
  ```

  > API的Ref可以直接使用，更醒目
  >
  > 回调的Ref同样简洁，但是就不够一目了然

  ### 获取焦点

  ```react
  this.inputUserName.current.focus(); //API
  this.inputUserName.focus(); //回调
  ```

  > API的Ref不是DOM对象，是一个接收底层 DOM 元素作为其 `current` 属性的函数，所以需要使用`current`属性来获取DOM对象
  >
  > 回调的Ref就是DOM对象或者null

## 📌JS脚本补充

### 时间戳转换成 `yyyy-MM-dd HH:mm:ss`

```javascript
//时间戳转换方法    date:时间戳数字
function formatDate(date) {
  var date = new Date(date);
  var YY = date.getFullYear() + '-';
  var MM = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
  var DD = (date.getDate() < 10 ? '0' + (date.getDate()) : date.getDate());
  var hh = (date.getHours() < 10 ? '0' + date.getHours() : date.getHours()) + ':';
  var mm = (date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()) + ':';
  var ss = (date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds());
  return YY + MM + DD +" "+hh + mm + ss;
}
```

## 📌React CDN链接补充

```html
<script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script crossorigin src="https://unpkg.com/babel-standalone@6.26.0/babel.min.js"></script>
```

