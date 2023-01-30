### 设置name值为字符串

```typescript
interface A {
  name: string
}
```

### 设置name值为可选项(可写、可不写)

```typescript
interface A {
  name?: string;
};
```

### 接口B继承接口A

> 接口B会覆盖接口A

```typescript
interface A {
  name?: string;
}
interface B extends A {
  name: string;
}
```


### 创建Object接口A

```typescript
interface A {
  [key:string]: string
}

const objA:A = {"1":"2"}
```

### 创建

### 删除接口A的name

> 去除类型中某些项

```typescript
interface A {
  name: string;
  age: number;
}
type ExcludeA = Omit<A, "name">
// 结果预览
// ExcludeA 等于 
interface ExcludeA {
  age: number;
}
// ---end---
```

> 多个的话用`|`进行分隔
> 例如: `Omit<A, "name"|"age">`

### 提取接口A中的name

```typescript
interface A {
  name: string;
  age: number;
}
type ExcludeA = Pick<A, "name">
// 结果预览
// ExcludeA 等于 
interface ExcludeA {
  name: string;
}
// ---end---
```


### 全部改成可选项(可写、可不写)

> 类型中所有选项变为可选，即加上?

```typescript
interface A {
  name: string;
  age: number;
}
type ExcludeA = Partial<A, "name">
// 结果预览
// ExcludeA 等于 
interface ExcludeA {
  name?: string;
  age?: number;
}
// ---end---
```

### 全部改成必填

> 类型中所有选项变为必填，即去除?

```typescript
interface A {
  name?: string;
  age?: number;
}
type ExcludeA = Required<A, "name">
// 结果预览
// ExcludeA 等于 
interface ExcludeA {
  name: string;
  age: number;
}
// ---end---
```