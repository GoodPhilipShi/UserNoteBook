## 一、Go语言的知识图谱

![在这里插入图片描述](https://img-blog.csdnimg.cn/9b3292ad981c43fbbeb1ef30453767bf.png)  
上图表示了go的应用领域，包括容器如k8s, 服务发现如consul，kv存储如etcd，中间件如codis, 存储如minio，分布式数据库tidb，此外还有devops、区块链、人工智能、web框架、微服务等等领域的应用。

## 二、Go语言概述

## 2.1、为什么需要Go语言

相比C++和java, Go语言更年轻，他存在的意义何在呢？  
1）在计算领域，是C/C++的天下，因为执行效率高，但缺点是开发和编译效率低。  
2）对于Java，虽然编译速度快、开发效率高，但执行效率不如C/C++。  
3）而动态语言如Python，由于没有强类型约束，很多问题需要在运行时发现：这种低级错误由编译器来发现更好些。  
综上，期待出现一种语言来解决上述语言的缺点，Go语言这时出现，它易于开发、快速编译、高效执行。

Go语言起源于2007年，由google 2009年发布。  
Go编译后的代码，运行速度可媲美C/C++，且编译速度更快，因此风靡全球，被称为21世纪的C语言（Go不仅具备C的性能与安全，且提供了21世纪互联网环境下服务端开发的各种使用特性）  
Go语言的设计哲学是：简单、实用。

Go语言是对类C语言的重大改进，它可以访问底层操作系统，还提供了强大的网络编程和并发编程的支持。Go语言可进行网络编程、系统编程、并发编程、分布式编程。

1）并发场景性能快  
2）静态的语言：没有面向对象中的“类”  
3）支持自动垃圾回收  
4）编译型语言：编译速度快

Go遵循简洁编程原则：  
1）它没有隐式的数值转换  
2）没有构造函数和析构函数  
3）没有运算符重载  
4）没有默认参数  
5）也没有继承  
6）没有泛型  
7）没有异常  
8）没有宏  
9）没有函数修饰  
10）更没有线程局部存储

Go承诺保证向后兼容：  
用之前的Go语言编写程序可以用新版本的Go语言编译器和标准库直接构建而不需要修改代码

Go语言支持交叉编译，即可以在Linux系统上开发基于Windows上运行的程序，因为这是一门完全支持UTF-8的语言，不仅体现在他可以处理使用UTF-8编码的字符串，就连他的源码稳居格式都是使用UTF-8编码。

## 2.2、Go是编译型语言

Go代码在运行前，需要使用编译器来编译代码，编译器将源代码编译成二进制（或字节码）格式；在编译代码时，编译器会做错误检查、性能优化，然后输出可在不同平台上运行的二进制文件。

要运行Go程序，需要的步骤：  
1）使用文本编辑器写Go代码  
2）编译程序  
3）运行编译后得到的可执行文件。

这与Python, Javascript等语言不同，Go自带了编译器。

## 2.3、Go语言的特性

### 1、语法简单

Go语法与C类似，但没有C那些隐秘晦涩的规则，Go语法简单严谨，无歧义。

### 2、并发模型

Go引入了携程Goroutine，从根本上将一切都并发化，运行时用goroutine运行所有的一切，包括main.main入口函数。

Goroutine用类携程的方式来处理并发单元，却又在运行时层面做了更深度的优化处理。但语法上的并发编程变得极为简单，无需处理回调，无需关注现场切换。

goroutine搭配channel，实现CSP模型。将并发单元间的数据耦合拆解开来，各司其职。这样对所有纠结于内存共享、锁粒度的程序员都是一种解脱。

### 3、内存分配

将一起并发化虽然好，但也带来了新问题，即如何实现高并发下内存的分配和管理。Go选择了tcmalloc，他本就是为了并发儿设计的高性能内存分配组件。

去除因配合垃圾回收而修改的内容，内存分配器完整保留了tcmailoc的原始架构。使用cache为当前线程提供无锁分配，多个central在不同线程间平衡内存单元复用。在更高层次里，heap管理大块内存分配，用以切分成不同等级的复用内存块。快速分配和二级平衡机制，让内存分配器能优秀地完成高压力下的内存管理任务。

除了偶尔因性能问题而被迫采用对象池和自主内存管理外，我们基本无需参与内存管理操作。

### 4、垃圾回收

相比Java, Go的垃圾回收面临的困难更多，因为指针的存在。幸好，指针运算被阻止，否则要做到精确回收都难。  
每次版本升级，垃圾回收期都是核心组件里修改最多的部分，从并发清理，到降低STW的时间，直到Go的1.5版本实现并发标记，逐步引入三色标记和写屏障等，都是为了能让垃圾回收在不影响用户逻辑的情况下更好地工作。但当前最新版本的垃圾回收算法也只能说堪用，距离好用还有不少距离。

### 5、静态链接

静态链接，只需编译后的一个可执行文件（将运行时、依赖库直接打包到可执行文件内部），无需附加任何东西，就能部署。这种简单的方式对于编写系统软件有极大好处，无需实现安装运行环境和下载各种第三方库。

### 6、标准库

Go的标准库算比较丰富，其中值得称道的事net/http，仅需要简单的几条语句，就能实现一个高性能的web server，大批基于此的优秀第三方Framework更将Go推到了Web/微服务 开发标准之一的位置。

### 7、工具链

完整的工具链对日常开发极有帮助，Go的工具链做的不错，无论是编译、格式化、错误检查、帮助文档，还是第三方包的下载、更新，都有对应的工具。虽然这些工具算不上多完善，但简单易用。

Go内置的测试框架，其中包括单元测试、性能测试、代码覆盖率、数据竞争，及用来调优的pprof，都是包子代码正确与稳定运行的必备利器。

此外，还可通过环境变量输出运行时的监控信息，尤其是垃圾回收和并发调度跟踪，可进一步帮助我们改善算法，获得最佳的运行期表现。

## 2.4、Go语言为并发而生

Go语言的祖先C语言的指令都是串行执行，即同一时刻仅有一个指令在使用CPU。  
随着多核处理器的发展，一些语言框架（如Java Netty）也在致力于提高多核CPU使用效率，但仍需要开发人员花精力去搞懂这些框架的原理及使用方法。

Go语言是在多核和网络化时代诞生的语言，天生就从底层支持并发，无需第三方库，程序员可以在写程序时很轻松地指定怎样使用CPU资源。

Go的并发，基于goroutine，可以将goroutine理解为一种虚拟线程。Go语言运行时会参与调度goroutine，并将goroutine合理地分配到每个CPU中，最大限度地使用CPU性能。

多个goroutine之间，通过使用channel通信，channel是一种内置的数据结构，可以让用户在不同的goroutine之间同步发送具有类型的消息。这种编程模型更倾向于在goroutine之间发送消息，而不是让多个goroutine争夺同一个数据的使用权。

程序可以把并发goroutine间的通信设计为生产者/消费者模式，将要通信的数据放入channel，然后channel另一端的代码将这些数据并发消费。

【goroutine与channel的例子】：生产者每秒生成一个字符串，并放入channel，生产者使用两个goroutine并发写入channel，消费者在main()函数的goroutine中处理。

```
package main
import (
        "fmt"
        "math/rand"
        "time"
)
// 数据生产者
func producer(header string, channel chan<- string) {
     // 无限循环, 不停地生产数据
     for {
         // 将随机数和字符串格式化为字符串发送给通道
         channel <- fmt.Sprintf("%s: %v", header, rand.Int31())
         // 等待1秒
         time.Sleep(time.Second)
     }
}
// 数据消费者
func customer(channel <-chan string) {
     // 不停地获取数据
     for {
         // 从通道中取出数据, 此处会阻塞直到信道中返回数据
         message := <-channel
         // 打印数据
         fmt.Println(message)
     }
}
func main() {
    // 创建一个字符串类型的通道
    channel := make(chan string)
    // 创建producer()函数的并发goroutine
    go producer("cat", channel)
    go producer("dog", channel)
    // 数据消费函数
    customer(channel)
}
```

运行结果：

```
dog: 2019727887
cat: 1298498081
dog: 939984059
cat: 1427131847
cat: 911902081
dog: 1474941318
dog: 140954425
cat: 336122540
cat: 208240456
dog: 646203300
```

可以看到，在并发的生产者、消费者过程中，程序员无需创建线程，无需线程池，也无需加锁，仅通过goroutine和channel，即可实现并发的目的。

## 2.5、各语言性能测试

表中数据的单位为秒，数值越小表明运行性能越好：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/482428bdeeb64b76a1ac79006202a011.png)  
从上表可以看出，go语言的性能接近于java, 不如C/C++。

## 2.6、Go语言的标准库

学习编程语言，重点不单是学语法，而是熟悉其生态圈，标准库是生态圈中的重要一环。  
Go语言的标准库，提供了构建模块和公共接口，包括I/O操作、文本处理、图像、密码学、网络和分布式应用程序等，并支持许多标准化的文件格式和编解码协议。

Go语言的编译器也是标准库中的一部分，他通过词法器扫描源码，使用语法树获得源码的逻辑分支等。  
Go语言的周边工具，都是建立在标准库上，用标准库可以完成绝大部分需求。

Go语言常见的包及功能如下表：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6ec481a565e74074886c7308c2b26d45.png)

## 三、Go语言环境

## 3.1、Go语言开发环境的安装

1、从官网下载go安装包  
https://golang.google.cn/dl/

2、以mac os为例，双击goxxx.pkg文件，一路next安装完成

3、安装完成后，在终端执行go version，可以看到安装的版本号

```
peng.shi@H7HT0YWMTC ~ % go version
go version go1.18.1 darwin/amd64
```

4、设置GOPATH环境变量  
默认会设置好gopath路径，可在终端执行：go env 命令

```
peng.shi@H7HT0YWMTC ~ % go env
GO111MODULE=""
GOARCH="amd64"
GOBIN=""
GOCACHE="/Users/peng.shi/Library/Caches/go-build"
GOENV="/Users/peng.shi/Library/Application Support/go/env"
GOEXE=""
GOEXPERIMENT=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="darwin"
GOINSECURE=""
GOMODCACHE="/Users/peng.shi/go/pkg/mod"
GONOPROXY=""
GONOSUMDB=""
GOOS="darwin"
GOPATH="/Users/peng.shi/go"
GOPRIVATE=""
GOPROXY="https://proxy.golang.org,direct"
GOROOT="/usr/local/go"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/darwin_amd64"
GOVCS=""
GOVERSION="go1.18.1"
GCCGO="gccgo"
GOAMD64="v1"
AR="ar"
CC="clang"
CXX="clang++"
CGO_ENABLED="1"
GOMOD="/dev/null"
GOWORK=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -arch x86_64 -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/yf/28dxgytd4q3blgvrcq_l7hq00000gp/T/go-build1265247406=/tmp/go-build -gno-record-gcc-switches -fno-common"
```

也可以在终端执行：vi ~/.bash\_profile，然后输入：

```
export GOPATH=$HOME/go
```

退出编辑器后再 source ~/.bash\_profile，其中，$Home可通过echo $HOME查看：

```
peng.shi@H7HT0YWMTC ~ % echo $HOME
/Users/peng.shi
```

另外，GOROOT 也就是 Go 开发包的安装目录，默认在 /usr/local/go，如不没有，可以在~/.base\_profile中设置，然后再source ~/.bash\_profile

在使用Goland等开发IDE时，会提示输入gopath路径，输入相应即可。

## 3.2、Go语言的IDE

### 1、Goland

Goland 是由 JetBrains 公司开发的**收费**的商用IDE，号称符合人体工程学。

### 2、LiteIDE

轻量级开发环境，免费。

### 3、GoClipse

通过在Eclipse安装go插件，可以使用Eclipse开发go

## 3.3、Go语言工程结构

要想构建一个go工程，需要把工程的目录添加到gopath中，多个项目之间用 ; 分隔，项目的构建是靠 gopath 来实现的。

### 3.3.1、Go工程的目录结构

Go语言的一个项目的目录通常分下面三个子目录：

#### 1、src目录：存项目和库的源文件

以package形式组织存放Go的源文件，这里的包与src下的每个子目录对应，例如，如果一个源文件被什么为属于log包，那他就会保存在 src/log 目录中。

src目录下，如果要放go文件，需要在文件中加名为main的package，通常都是把go文件放在某个目录(package)下，然后其他人引用该文件时，先import其package。

go跟java一样，在代码的第一行必须是 package <包名>

另外需要知道的是，Go语言会通过 go get 命令，把获取到的源文件下载到src目录下对应的文件夹中。

#### 2、pkg目录：存编译后生成的包/库的归档文件

pkg目录，用于存放 go install 命令安装某个包后的归档文件。归档文件是指那些以 ”.a" 结尾的文件。  
编译和安装项目代码的过程，一般会以代码包为单位进行，比如 log 包被编译安装后，将生成一个名为 log.a 的归档文件，并存放在当前项目的 pkg 目录下。

#### 3、bin目录：保存由Go命令源文件生成的可执行文件

在通过 go install 命令完成安装后，保存由 Go 命令源文件生成的可执行文件。在类Unix系统下，可执行文件与源文件的文件名相同，在window系统下，可执行文件的名称是命令源文件的文件名加 “.exe" 后缀。

3）bin目录：存编译后生成的可执行文件

#### 补充：命令源文件和库文件的区别？

1）命令源文件：如果一个Go源文件被声明为属于main包，且包含main含税，则他就是命令源文件。命令源文件属于程序的入口，可通过Go语言的go run命令运行，或者通过go build命令生成可执行文件。

2）库源文件：指存在于某个包中的普通源文件，并且库源文件中不包含main函数

## 3.4、Go语言的编译和运行

Go跟C语言一样，是静态语言。所以在执行签，需要先将其编译成二进制的可执行文件。

### go build

可通过 go build 命令把go代码编译成二进制的可执行文件

### go run

此命令会先编译，再运行，编译时会产生一个临时文件，但不会生成可执行文件。

## 四、Go语言语法

## 4.1、变量声明

Go是静态语言，因此其变量必须要有明确的类型，这样编译器才能检查变量的正确性。

声明变量语法：

```
var 变量名 变量类型
```

后面无需加分号

声明变量举例：声明a, b两个变量都为int指针类型

```
var a, b *int
```

Go语言的基本数据类型：

```
bool
string
int、int8、int16、int32、int64
uint、uint8、uint16、uint32、uint64、uintptr
byte // uint8 的别名
rune // int32 的别名 代表一个 Unicode 码
float32、float64
complex64、complex128
```

当一个变量被声明后，系统会自动为他赋初始值：  
int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil

变量的命名遵循驼峰命名法，即首个单词小写，每个新单词首字母大写，如startDate。

变量声明的批量格式：

```
var (
    a int
    b string
    c []float32
    d func() bool
    e struct {
        x int
    }
)
```

使用关键字 var 和括号，可以将一组变量定义放在一起。

除了上述两种方式，还可以把变量定义和初始化放一起：

```
名字 := 表达式
```

但这种方式有以下限制：  
1）不能提供数据类型  
2）只能用在函数内部

例如：

```
func main() {
x := 100
a,s := 1, "abc"
}
```

## 4.2、变量初始化

在对变量进行声明后，系统会自动对变量进行初始化，如：

```
整型和浮点型变量的默认值为 0 和 0.0。
字符串变量的默认值为空字符串。
布尔型变量默认为 false。
切片、函数、指针变量的默认为 nil。
```

变量初始化语法：

```
var 变量名 类型 = 表达式
```

举例：

```
var aa int = 100
```

也可以省略类型，采用编译器推导类型的格式：

```
var aa = 100
```

变量赋值，还有一种更精简的写法：

```
aa := 100
```

注意：由于使用了 := ，而不是 = ，因此这种写法左边的aa必须是没有精益过的变量。若定义过，会发生编译错误。

注意：在多个短变量声明和赋值中，至少有一个新声明的变量出现在左值中，即使其他变量名可能是重复声明的，编译也不会报错，如下面写法，不会编译报错：

```
conn, err := net.Dial("tcp", "127.0.0.1:8080")
conn2, err := net.Dial("tcp", "127.0.0.1:8080")
```

Go语言的多重赋值，用于变量值的互换：

```
var a int = 100
var b int = 200
b, a = a, b
fmt.Println(a, b)
```

## 4.3、匿名变量

Go语言支持没有名称的变量、类型或方法，这些统称为匿名变量。匿名变量是为了增强代码的灵活性。  
匿名变量是一个下划线”\_" (\_被称为空白标识符）, \_可以想其他标识符那样用于变量的声明或赋值（任何类型都可以赋值给他），但任何赋值给这个标识符的值都将被抛弃，因此这些值不会在后续的代码中使用。

举例说明：

```
func GetData() (int, int) {
    return 100, 200
}
func main(){
    a, _ := GetData()
    _, b := GetData()
    fmt.Println(a, b)
}
```

运行结果：

```
100 200
```

匿名变量，不占用内存空间，不会分配内存。

## 4.4、变量作用域

1）局部变量：函数内定义的变量，作用域为函数体内，在函数调用结束后，变量就会被销毁。形参的作用域同局部变量。  
2）全局变量：函数外定义的变量，全局变量的声明必须以var开头，如果全局变量和局部变量同名，以局部变量为准。

## 4.5、数据类型

### 4.5.1、整型

整型分为有符号整型（包括 int8、int16、int32 和 int64 ，分别对应8、16、32、64 bit（二进制位）大小的有符号整数）和无符号整型（uint8、uint16、uint32 和 uint64）。  
此外还有两种整数类型 int 和 uint，它们分别对应特定 CPU 平台的字长（机器字大小），由于编译器和计算机硬件的不同，int 和 uint 所能表示的整数大小会在 32bit 或 64bit 之间变化。

大多数情况下，我们只需要 int 一种整型即可。

用来表示unicode的rune跟 int32 等价，用来表示unicode的码点；  
byte等价于uint8, byte用于强调数值是一个原始的数据，而不是一个小的整数。

rune的用法示例：

```
import (
"fmt"
"unicode/utf8"
)

func main() {

var str = "hello 世界"

//golang中string底层是通过byte数组实现的，直接求len 实际是在按字节长度计算  所以一个汉字占3个字节算了3个长度
fmt.Println("len(str):", len(str))

//以下两种都可以得到str的字符串长度

//golang中的unicode/utf8包提供了用utf-8获取长度的方法
fmt.Println("RuneCountInString:", utf8.RuneCountInString(str))

//通过rune类型处理unicode字符
fmt.Println("rune:", len([]rune(str)))

}
```

输出结果：

```
len(str): 12
RuneCountInString: 8
rune: 8
```

### 4.5.2、浮点类型

Go语言支持float32和float64 这两种。

### 4.5.3、复数

复数是由两个浮点数表示，其中一个是实部，一个是虚部。  
复数类型有两种：complex128（64 位实数和虚数）和 complex64（32 位实数和虚数），其中 complex128 为复数的默认类型。

复数的声明方式：

```
var name complex128 = complex(x, y)
```

例子：

```
var x complex128 = complex(1, 2) // 1+2i
var y complex128 = complex(3, 4) // 3+4i
fmt.Println(x*y)                 // "(-5+10i)"
fmt.Println(real(x*y))           // "-5"
fmt.Println(imag(x*y))           // "10"
```

复数也可以用==和!=进行相等比较，只有两个复数的实部和虚部都相等的时候它们才是相等的。

### 4.5.4、bool 类型

布尔类型的值只有两种：true 或 false，默认是false  
布尔型无法参与数值运算，也无法与其他类型进行转换。

### 4.5.5、字符串

Go语言中字符串的内部实现使用 UTF-8 编码，通过 rune 类型，可以方便地对每个 UTF-8 字符进行访问。当然，Go语言也支持按照传统的 ASCII 码方式逐字符进行访问。

可用反引号\`\`来定义多行字符串：

```
const str = `第一行
第二行
第三行
\r\n
`
fmt.Println(str)
```

### 4.5.6、字符类型 byte和rune

Go语言的字符有以下两种：  
1）一种是 uint8 类型，或者叫 byte 型，代表了 ASCII 码的一个字符。  
2）另一种是 rune 类型，代表一个 UTF-8 字符，当需要处理中文、日文或者其他复合字符时，则需要用到 rune 类型。rune 类型等价于 int32 类型。

byte 类型是 uint8 的别名，对于只占用 1 个字节的传统 ASCII 编码的字符来说，完全没有问题，例如 var ch byte = ‘A’，字符使用单引号括起来。

Go语言同样支持 Unicode（UTF-8），因此字符同样称为 Unicode 代码点或者 runes，并在内存中使用 int 来表示。在文档中，一般使用格式 U+hhhh 来表示，其中 h 表示一个 16 进制数。

在书写 Unicode 字符时，需要在 16 进制数之前加上前缀\\u或者\\U。因为 Unicode 至少占用 2 个字节，所以我们使用 int16 或者 int 类型来表示。如果需要使用到 4 字节，则使用\\u前缀，如果需要使用到 8 个字节，则使用\\U前缀。

```
var ch int = '\u0041'
var ch2 int = '\u03B2'
var ch3 int = '\U00101234'
fmt.Printf("%d - %d - %d\n", ch, ch2, ch3) // integer
fmt.Printf("%c - %c - %c\n", ch, ch2, ch3) // character
fmt.Printf("%X - %X - %X\n", ch, ch2, ch3) // UTF-8 bytes
fmt.Printf("%U - %U - %U", ch, ch2, ch3)   // UTF-8 code point
```

结果：

```
65 - 946 - 1053236
A - β - r
41 - 3B2 - 101234
U+0041 - U+03B2 - U+101234
```

格式化说明符%c用于表示字符，当和字符配合使用时，%v或%d会输出用于表示该字符的整数，%U输出格式为 U+hhhh 的字符串。

Unicode 包中内置了一些用于测试字符的函数，这些函数的返回值都是一个布尔值，如下所示（其中 ch 代表字符）：  
判断是否为字母：unicode.IsLetter(ch)  
判断是否为数字：unicode.IsDigit(ch)  
判断是否为空白符号：unicode.IsSpace(ch)

### 4.5.6、数据类型转换

Go语言不存在隐式类型转换，因此所有的类型转换都必须显式的声明：

```
valueOfTypeB = typeB(valueOfTypeA)
```

举例：

```
import (
"fmt"
"math"
)

func main() {
// 输出各数值范围
fmt.Println("int8 range:", math.MinInt8, math.MaxInt8)
fmt.Println("int16 range:", math.MinInt16, math.MaxInt16)
fmt.Println("int32 range:", math.MinInt32, math.MaxInt32)
fmt.Println("int64 range:", math.MinInt64, math.MaxInt64)
// 初始化一个32位整型值
var a int32 = 1047483647
// 输出变量的十六进制形式和十进制值
fmt.Printf("int32: 0x%x %d\n", a, a)
// 将a变量数值转换为十六进制, 发生数值截断
b := int16(a)
// 输出变量的十六进制形式和十进制值
fmt.Printf("int16: 0x%x %d\n", b, b)
// 将常量保存为float32类型
var c float32 = math.Pi
// 转换为int类型, 浮点发生精度丢失
fmt.Println(int(c))
}
```

结果：

```
int8 range: -128 127
int16 range: -32768 32767
int32 range: -2147483648 2147483647
int64 range: -9223372036854775808 9223372036854775807
int32: 0x3e6f54ff 1047483647
int16: 0x54ff 21759
3
```

### 4.5.7、指针

指针对于性能的影响不言而喻，如果你想要做系统编程、操作系统或者网络应用，指针更是不可或缺的一部分。

指针（pointer）在Go语言中可以被拆分为两个核心概念：  
1）类型指针，允许对这个指针类型的数据进行修改，传递数据可以直接使用指针，而无须拷贝数据，类型指针不能进行偏移和运算。  
2）切片，由指向起始元素的原始指针、元素数量和容量组成。

指针需要知道几个概念：指针地址、指针类型和指针取值

#### 指针地址和指针类型

一个指针变量可以指向任何一个值的内存地址，它所指向的值的内存地址在 32 和 64 位机器上分别占用 4 或 8 个字节，占用字节的大小与所指向的值的大小无关。当一个指针被定义后没有分配到任何变量时，它的默认值为 nil。指针变量通常缩写为 ptr。

每个变量在运行时都拥有一个地址，这个地址代表变量在内存中的位置。Go语言中使用在变量名前面添加&操作符（前缀）来获取变量的内存地址（取地址操作）：

```
ptr := &v    // v 的类型为 T
```

```
import (
    "fmt"
)
func main() {
    var cat int = 1
    var str string = "banana"
    fmt.Printf("%p %p", &cat, &str)
}
```

结果：

```
0xc000018080 0xc000010260
```

#### 从指针获取指向的值

```
func main() {
// 准备一个字符串类型
var house = "Malibu Point 10880, 90265"
// 对字符串取地址, ptr类型为*string
ptr := &house
// 打印ptr的类型
fmt.Printf("ptr type: %T\n", ptr)
// 打印ptr的指针地址
fmt.Printf("address: %p\n", ptr)
// 对指针进行取值操作
value := *ptr
// 取值后的类型
fmt.Printf("value type: %T\n", value)
// 指针取值后就是指向变量的值
fmt.Printf("value: %s\n", value)
}
```

结果：

```
ptr type: *string
address: 0xc000096220
value type: string
value: Malibu Point 10880, 90265
```

取地址操作符&和取值操作符\*是一对互补操作符，&取出地址，\*根据地址取出地址指向的值。

#### 创建指针的另一种方法：new() 函数

```
new(类型)
```

例子：

```
str := new(string)
*str = "Go语言教程"
fmt.Println(*str)
```

结果：

```
Go语言教程
```

### 4.5.8、常量 和 const

用const关键字定义常量，常量是在编译时创建的，值不会改变。  
例子：

```
const pi = 3.14159 // 相当于 math.Pi 的近似值
```

常量也可以批量声明：

```
const (
    e  = 2.7182818
    pi = 3.1415926
)
```

#### 无类型常量

Go语言的常量有个不同寻常之处。虽然一个常量可以有任意一个确定的基础类型，例如 int 或 float64，或者是类似 time.Duration 这样的基础类型，但是许多常量并没有一个明确的基础类型。

编译器为这些没有明确的基础类型的数字常量提供比基础类型更高精度的算术运算，可以认为至少有 256bit 的运算精度。这里有六种未明确类型的常量类型，分别是无类型的布尔型、无类型的整数、无类型的字符、无类型的浮点数、无类型的复数、无类型的字符串。

例子：math.Pi 无类型的浮点数常量，可以直接用于任意需要浮点数或复数的地方：

```
var x float32 = math.Pi
var y float64 = math.Pi
var z complex128 = math.Pi
```

如果 math.Pi 被确定为特定类型，比如 float64，那么结果精度可能会不一样，同时对于需要 float32 或 complex128 类型值的地方则需要一个明确的强制类型转换：

```
const Pi64 float64 = math.Pi
var x float32 = float32(Pi64)
var y float64 = Pi64
var z complex128 = complex128(Pi64)
```

### 4.5.9、类型别名 type关键字

类型别名是 Go 1.9 版本添加的新功能，主要用于解决代码升级、迁移中存在的类型兼容性问题。在 C/C++ 语言中，代码重构升级可以使用宏快速定义一段新的代码，Go语言中没有选择加入宏，而是解决了重构中最麻烦的类型名变更问题。

在 Go 1.9 版本之前定义内建类型的代码是这样写的：

```
type byte uint8
type rune int32
```

而在 Go 1.9 版本之后变为：

```
type byte = uint8
type rune = int32
```

定义类型别名的写法为：

```
type TypeAlias = Type
```

类型别名与类型定义表面上看只有一个等号的差异，那么它们之间实际的区别有哪些呢？下面通过一段代码来理解。

```
import (
    "fmt"
)
// 将NewInt定义为int类型
type NewInt int
// 将int取一个别名叫IntAlias
type IntAlias = int
func main() {
    // 将a声明为NewInt类型
    var a NewInt
    // 查看a的类型名
    fmt.Printf("a type: %T\n", a)
    // 将a2声明为IntAlias类型
    var a2 IntAlias
    // 查看a2的类型名
    fmt.Printf("a2 type: %T\n", a2)
}
```

结果：

```
a type: main.NewInt
a2 type: int
```

结果显示 a 的类型是 main.NewInt，表示 main 包下定义的 NewInt 类型，a2 类型是 int，IntAlias 类型只会在代码中存在，编译完成时，不会有 IntAlias 类型。

### 4.5.10、关键字

go语言的关键字：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4f68a453c019409e8f99afe274dfd9fd.png)

go语言的预定义标识符：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/387bfdca855140588d1839193450702e.png)

### 4.5.11、运算符优先级

![在这里插入图片描述](https://img-blog.csdnimg.cn/2d380a9952a04e42b287523e2c936d43.png)

## 4.6、容器

### 4.6.1、数组

数组声明语法：

```
var 数组变量名 [元素数量]Type
```

例子：

```
var a [3]int             // 定义三个整数的数组
fmt.Println(a[0])        // 打印第一个元素
fmt.Println(a[len(a)-1]) // 打印最后一个元素
// 打印索引和元素
for i, v := range a {
    fmt.Printf("%d %d\n", i, v)
}
// 仅打印元素
for _, v := range a {
    fmt.Printf("%d\n", v)
}
```

结果：

```
0
0
0 0
1 0
2 0
0
0
0
```

在数组的定义中，如果在数组长度的位置出现“…”省略号，则表示数组的长度是根据初始化值的个数来计算，因此，上面数组 q 的定义可以简化为：

```
q := [...]int{1, 2, 3}
fmt.Printf("%T\n", q) // "[3]int"
```

#### 比较两个数组是否相等

```
a := [2]int{1, 2}
b := [...]int{1, 2}
c := [2]int{1, 3}
fmt.Println(a == b, a == c, b == c) // "true false false"
d := [3]int{1, 2}
fmt.Println(a == d) // 编译错误：无法比较 [2]int == [3]int
```

### 4.6.2、多维数组

多维数组语法：

```
var array_name [size1][size2]...[sizen] array_type
```

例子：声明二维数组：

```
// 声明一个二维整型数组，两个维度的长度分别是 4 和 2
var array [4][2]int
// 使用数组字面量来声明并初始化一个二维整型数组
array = [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}
// 声明并初始化数组中索引为 1 和 3 的元素
array = [4][2]int{1: {20, 21}, 3: {40, 41}}
// 声明并初始化数组中指定的元素
array = [4][2]int{1: {0: 20}, 3: {1: 41}}
```

例：为数组元素赋值：

```
// 声明两个二维整型数组
var array1 [2][2]int
var array2 [2][2]int
// 为array2的每个元素赋值
array2[0][0] = 10
array2[0][1] = 20
array2[1][0] = 30
array2[1][1] = 40
// 将 array2 的值复制给 array1
array1 = array2
```

### 4.6.3、切片slice

切片（slice）是对数组的一个连续片段的引用，所以切片是一个引用类型。

从数组或切片生成新的切片：

```
slice [开始位置 : 结束位置]
```

切片例子：

```
var a  = [3]int{1, 2, 3}
fmt.Println(a, a[1:2])
```

结果：

```
[1 2 3]  [2]
```

从数组或切片生成新的切片拥有如下特性：  
1）取出的元素数量为：结束位置 - 开始位置；  
2）取出元素不包含结束位置对应的索引，切片最后一个元素使用 slice\[len(slice)\] 获取；  
3）当缺省开始位置时，表示从连续区域开头到结束位置；  
4）当缺省结束位置时，表示从开始位置到整个连续区域末尾；  
5）两者同时缺省时，与切片本身等效；  
6）两者同时为 0 时，等效于空切片，一般用于切片复位。

切片例子：

```
var highRiseBuilding [30]int
for i := 0; i < 30; i++ {
        highRiseBuilding[i] = i + 1
}
// 区间
fmt.Println(highRiseBuilding[10:15])
// 中间到尾部的所有元素
fmt.Println(highRiseBuilding[20:])
// 开头到中间指定位置的所有元素
fmt.Println(highRiseBuilding[:2])
```

结果：

```
[11 12 13 14 15]
[21 22 23 24 25 26 27 28 29 30]
[1 2]
```

表示原有的切片：

```
a := []int{1, 2, 3}
fmt.Println(a[:])
```

结果：

```
[1 2 3]
```

声明新的切片语法：

```
var name []Type
```

例子：

```
// 声明字符串切片
var strList []string
// 声明整型切片
var numList []int
// 声明一个空切片
var numListEmpty = []int{}
// 输出3个切片
fmt.Println(strList, numList, numListEmpty)
// 输出3个切片大小
fmt.Println(len(strList), len(numList), len(numListEmpty))
// 切片判定空的结果
fmt.Println(strList == nil)
fmt.Println(numList == nil)
fmt.Println(numListEmpty == nil)
```

结果：

```
[] [] []
0 0 0
true
true
false
```

第 19 行，numListEmpty 已经被分配到了内存，但没有元素，因此和 nil 比较时是 false。

#### 使用 make() 函数构造切片：会分配新内存

如果需要动态地创建一个切片，可以使用 make() 内建函数：

```
make( []Type, size, cap )
```

例子：

```
a := make([]int, 2)
b := make([]int, 2, 10)
fmt.Println(a, b)
fmt.Println(len(a), len(b))
```

结果：

```
[0 0] [0 0]
2 2
```

其中 a 和 b 均是预分配 2 个元素的切片，只是 b 的内部存储空间已经分配了 10 个，但实际使用了 2 个元素。

注意：  
使用 make() 函数生成的切片一定发生了内存分配操作，但给定开始与结束位置（包括切片复位）的切片只是将新的切片结构指向已经分配好的内存区域，设定开始与结束位置，不会发生内存分配操作。

#### append()为切片添加元素

例子：

```
var numbers []int
for i := 0; i < 10; i++ {
    numbers = append(numbers, i)
    fmt.Printf("len: %d  cap: %d pointer: %p\n", len(numbers), cap(numbers), numbers)
}
```

结果：

```
len: 1  cap: 1 pointer: 0xc0000b2008
len: 2  cap: 2 pointer: 0xc0000b2030
len: 3  cap: 4 pointer: 0xc0000ba020
len: 4  cap: 4 pointer: 0xc0000ba020
len: 5  cap: 8 pointer: 0xc0000bc040
len: 6  cap: 8 pointer: 0xc0000bc040
len: 7  cap: 8 pointer: 0xc0000bc040
len: 8  cap: 8 pointer: 0xc0000bc040
len: 9  cap: 16 pointer: 0xc0000be000
len: 10  cap: 16 pointer: 0xc0000be000
```

代码说明如下：  
第 1 行，声明一个整型切片。  
第 4 行，循环向 numbers 切片中添加 10 个数。  
第 5 行，打印输出切片的长度、容量和指针变化，使用函数 len() 查看切片拥有的元素个数，使用函数 cap() 查看切片的容量情况。

通过查看代码输出，可以发现一个有意思的规律：切片长度 len 并不等于切片的容量 cap。

#### 切片复制

```
copy( destSlice, srcSlice []T) int
```

例子：

```
slice1 := []int{1, 2, 3, 4, 5}
slice2 := []int{5, 4, 3}
copy(slice2, slice1) // 只会复制slice1的前3个元素到slice2中
copy(slice1, slice2) // 只会复制slice2的3个元素到slice1的前3个位置
```

例子：

```
func main() {
// 设置元素数量为1000
const elementCount = 1000
// 预分配足够多的元素切片
srcData := make([]int, elementCount)
// 将切片赋值
for i := 0; i < elementCount; i++ {
srcData[i] = i
}
// 引用切片数据
refData := srcData
// 预分配足够多的元素切片
copyData := make([]int, elementCount)
// 将数据复制到新的切片空间中
copy(copyData, srcData)
// 修改原始数据的第一个元素
srcData[0] = 999
// 打印引用切片的第一个元素
fmt.Println(refData[0])
// 打印复制切片的第一个和最后一个元素
fmt.Println(copyData[0], copyData[elementCount-1])
// 复制原始数据从4到6(不包含)
copy(copyData, srcData[4:6])
for i := 0; i < 5; i++ {
fmt.Printf("%d ", copyData[i])
}
}
```

结果：

```
999
0 999
4 5 2 3 4 
```

#### range关键字：循环迭代切片

```
// 创建一个整型切片，并赋值
slice := []int{10, 20, 30, 40}
// 迭代每一个元素，并显示其值
for index, value := range slice {
    fmt.Printf("Index: %d Value: %d\n", index, value)
}
```

结果：

```
Index: 0 Value: 10
Index: 1 Value: 20
Index: 2 Value: 30
Index: 3 Value: 40
```

#### 多维切片

```
var sliceName [][]...[]sliceType
```

声明一个二维切片：

```
//声明一个二维切片
var slice [][]int
//为二维切片赋值
slice = [][]int{{10}, {100, 200}}
// 为第一个切片追加值为 20 的元素
slice[0] = append(slice[0], 20)
```

### 4.6.4、map

map为一个 key（索引）和一个 value（值），也称关联数组或字典。

map是引用类型，声明语法：

```
var mapname map[keytype]valuetype
```

例子：

```
func main() {
var mapLit map[string]int
//var mapCreated map[string]float32
var mapAssigned map[string]int
mapLit = map[string]int{"one": 1, "two": 2}
mapCreated := make(map[string]float32)
mapAssigned = mapLit
mapCreated["key1"] = 4.5
mapCreated["key2"] = 3.14159
mapAssigned["two"] = 3
fmt.Printf("Map literal at \"one\" is: %d\n", mapLit["one"])
fmt.Printf("Map created at \"key2\" is: %f\n", mapCreated["key2"])
fmt.Printf("Map assigned at \"two\" is: %d\n", mapLit["two"])
fmt.Printf("Map literal at \"ten\" is: %d\n", mapLit["ten"])
}
```

结果：

```
Map literal at "one" is: 1
Map created at "key2" is: 3.141590
Map assigned at "two" is: 3
Map literal at "ten" is: 0
```

#### map容量

和数组不同，map 可以根据新增的 key-value 动态的伸缩，因此它不存在固定长度或者最大限制，但是也可以选择标明 map 的初始容量 capacity，格式如下：

```
make(map[keytype]valuetype, cap)
```

### map遍历

可使用for range来遍历map:

```
scene := make(map[string]int)
scene["route"] = 66
scene["brazil"] = 4
scene["china"] = 960
for k, v := range scene {
    fmt.Println(k, v)
}
```

只遍历value:

```
for _, v := range scene {
```

只遍历key：

```
for k := range scene {
```

#### map元素的删除

```
delete(map, 键)
```

例子：

```
scene := make(map[string]int)
// 准备map数据
scene["route"] = 66
scene["brazil"] = 4
scene["china"] = 960
delete(scene, "brazil")
for k, v := range scene {
    fmt.Println(k, v)
}
```

例子：

```
func main() {
scene := make(map[string]int)
// 准备map数据
scene["route"] = 66
scene["brazil"] = 4
scene["china"] = 960
delete(scene, "brazil")
for k, v := range scene {
fmt.Println(k, v)
}
}
```

结果：

```
route 66
china 960
```

#### 并发场景下的map：sync.Map

Go语言中的 map 在并发情况下，只读是线程安全的，同时读写是线程不安全的。

例子：

```
func main() {
// 创建一个int到int的映射
m := make(map[int]int)
// 开启一段并发代码
go func() {
// 不停地对map进行写入
for {
m[1] = 1
}
}()
// 开启一段并发代码
go func() {
// 不停地对map进行读取
for {
_ = m[1]
}
}()
// 无限循环, 让并发程序在后台执行
for {
}
}
```

结果，编译报错：

```
fatal error: concurrent map read and map write
```

需要并发读写时，一般的做法是加锁，但这样性能并不高，Go语言在 1.9 版本中提供了一种效率较高的并发安全的 sync.Map，sync.Map 和 map 不同，不是以语言原生形态提供，而是在 sync 包下的特殊结构。

sync.Map 有以下特性：  
1）无须初始化，直接声明即可。  
2）sync.Map 不能使用 map 的方式进行取值和设置等操作，而是使用 sync.Map 的方法进行调用，Store 表示存储，Load 表示获取，Delete 表示删除。  
3）使用 Range 配合一个回调函数进行遍历操作，通过回调函数返回内部遍历出来的值，Range 参数中回调函数的返回值在需要继续迭代遍历时，返回 true，终止迭代遍历时，返回 false。

例子：

```
func main() {
var scene sync.Map
// 将键值对保存到sync.Map
scene.Store("greece", 97)
scene.Store("london", 100)
scene.Store("egypt", 200)
// 从sync.Map中根据键取值
fmt.Println(scene.Load("london"))
// 根据键删除对应的键值对
scene.Delete("london")
// 遍历所有sync.Map中的键值对
scene.Range(func(k, v interface{}) bool {
fmt.Println("iterate:", k, v)
return true
})
}
```

结果：

```
100 true
iterate: greece 97
iterate: egypt 200
```

### 4.6.5、list列表

在Go语言中，列表使用 container/list 包来实现，内部的实现原理是双链表，列表能够高效地进行任意位置的元素插入和删除操作。

#### 初始化列表

方式1：通过 container/list 包的 New() 函数初始化 list

```
变量名 := list.New()
```

方式2：通过 var 关键字声明初始化 list

```
var 变量名 list.List
```

#### 向列表中插入元素

双链表支持从队列前方或后方插入元素，分别对应的方法是 PushFront 和 PushBack。

```
l := list.New()
l.PushBack("fist")
l.PushFront(67)
```

例子：

```
import "container/list"
func main() {
l := list.New()
// 尾部添加
l.PushBack("canon")
// 头部添加
l.PushFront(67)
// 尾部添加后保存元素句柄
element := l.PushBack("fist")
// 在fist之后添加high
l.InsertAfter("high", element)
// 在fist之前添加noon
l.InsertBefore("noon", element)
// 使用
l.Remove(element)

for i := l.Front(); i != nil; i = i.Next() {
fmt.Println(i.Value)
}
}
```

结果：

```
67
canon
noon
high
```

## 4.7、nil：空值/零值

在Go语言中，布尔类型的零值（初始值）为 false，数值类型的零值为 0，字符串类型的零值为空字符串""，而指针、切片、映射、通道、函数和接口的零值则是 nil。

nil 是Go语言中一个预定义好的标识符，跟java中的null不同：  
1）nil是不能比较的：

```
func main() {
    fmt.Println(nil==nil)
}
```

会报编译错误：

```
invalid operation: nil == nil (operator == not defined on untyped nil)
```

2）nil不是关键字或保留字

```
var nil = errors.New("my god")
```

这么做编译是不会报错的

3）nil 没有默认类型

```
func main() {
    fmt.Printf("%T", nil)
    print(nil)
}
```

这样会编译报错：

```
use of untyped nil in argument to print
```

4）不同类型的nil的指针是一样的：

```
func main() {
var arr []int
var num *int
fmt.Printf("%p\n", arr)
fmt.Printf("%p", num)
}
```

结果：

```
0x0
0x0
```

5）无论nil的类型是否相同，都不能比较

6）nil 是 map、slice、pointer、channel、func、interface 的零值

```
func main() {
    var m map[int]string
    var ptr *int
    var c chan int
    var sl []int
    var f func()
    var i interface{}
    fmt.Printf("%#v\n", m)
    fmt.Printf("%#v\n", ptr)
    fmt.Printf("%#v\n", c)
    fmt.Printf("%#v\n", sl)
    fmt.Printf("%#v\n", f)
    fmt.Printf("%#v\n", i)
}
```

结果：

```
map[int]string(nil)
(*int)(nil)
(chan int)(nil)
[]int(nil)
(func())(nil)
<nil>
```

7）不同类型的 nil 值占用的内存大小可能是不一样的

```
func main() {
    var p *struct{}
    fmt.Println( unsafe.Sizeof( p ) ) // 8
    var s []int
    fmt.Println( unsafe.Sizeof( s ) ) // 24
    var m map[int]bool
    fmt.Println( unsafe.Sizeof( m ) ) // 8
    var c chan string
    fmt.Println( unsafe.Sizeof( c ) ) // 8
    var f func()
    fmt.Println( unsafe.Sizeof( f ) ) // 8
    var i interface{}
    fmt.Println( unsafe.Sizeof( i ) ) // 16
}
```

结果：

```
8
24
8
8
8
16
```

## 五、流程控制

## 5.1、if else

```
if condition1 {
    // do something
} else if condition2 {
    // do something else
} else {
    // catch-all or default
}
```

关键字 if 和 else 之后的左大括号{必须和关键字在同一行，如果你使用了 else if 结构，则前段代码块的右大括号}必须和 else if 关键字在同一行，这两条规则都是被编译器强制规定的。

### 特殊写法

```
if err := Connect(); err != nil {
    fmt.Println(err)
    return
}
```

Connect 是一个带有返回值的函数，err:=Connect() 是一个语句，执行 Connect 后，将错误保存到 err 变量中。  
err != nil 才是 if 的判断表达式，当 err 不为空时，打印错误并返回。

跟Java不同的是，条件语句，go没有括号

## 5.2、for 循环

与多数语言不同的是，Go语言中的循环语句只支持 for 关键字，而不支持 while 和 do-while 结构

例子：

```
sum := 0
for i := 0; i < 10; i++ {
    sum += i
}
```

Go语言的 for 循环同样支持 continue 和 break 来控制循环，但是它提供了一个更高级的 break，可以选择中断哪一个循环，如下例：

```
for j := 0; j < 5; j++ {
    for i := 0; i < 10; i++ {
        if i > 5 {
            break JLoop
        }
        fmt.Println(i)
    }
}
JLoop:
// ...
```

for的初始语句也可以被忽略：

```
step := 2
for ; step > 0; step-- {
    fmt.Println(step)
}
```

for的条件表达式也可以被忽略：

```
var i int
for ; ; i++ {
    if i > 10 {
        break
    }
}
```

也可以无限循环：

```
var i int
for {
    if i > 10 {
        break
    }
    i++
}
```

只有一个条件的循环：

```
var i int
for i <= 10 {
    i++
}
```

## 5.3、switch case语句

```
var a = "hello"
switch a {
case "hello":
    fmt.Println(1)
case "world":
    fmt.Println(2)
default:
    fmt.Println(0)
}
```

结果：

```
1
```

一分支也可以对应多个值：

```
var a = "mum"
switch a {
case "mum", "daddy":
    fmt.Println("family")
}
```

分支也可以使用表达式：

```
var r int = 11
switch {
case r > 10 && r < 20:
    fmt.Println(r)
}
```

在Go语言中 case 是一个独立的代码块，执行完毕后不会像C语言那样紧接着执行下一个 case，但是为了兼容一些移植代码，依然加入了 fallthrough 关键字来实现这一功能，代码如下：

```
var s = "hello"
switch {
case s == "hello":
    fmt.Println("hello")
    fallthrough
case s != "world":
    fmt.Println("world")
}
```

结果：

```
hello
world
```

## 5.4、goto语句

```
func main() {
    for x := 0; x < 10; x++ {
        for y := 0; y < 10; y++ {
            if y == 2 {
                // 跳转到标签
                goto breakHere
            }
        }
    }
    // 手动返回, 避免执行进入标签
    return
    // 标签
breakHere:
    fmt.Println("done")
}
```

结果：

```
done
```

## 5.5、break跳出循环

```
func main() {
OuterLoop:
    for i := 0; i < 2; i++ {
        for j := 0; j < 5; j++ {
            switch j {
            case 2:
                fmt.Println(i, j)
                break OuterLoop
            case 3:
                fmt.Println(i, j)
                break OuterLoop
            }
        }
    }
}
```

结果：

```
0 2
```

13 和第 16 行，退出 OuterLoop 对应的循环之外，也就是跳转到第 20 行

## 5.6、continue继续下一次循环

```
func main() {
OuterLoop:
for i := 0; i < 2; i++ {
for j := 0; j < 5; j++ {
switch j {
case 2:
fmt.Println(i, j)
continue OuterLoop
}
}
}
}
```

结果：

```
0 2
1 2
```

## 六、函数

## 6.1、函数定义

```
func 函数名(形式参数列表)(返回值列表){
    函数体
}
```

例子：

```
func main() {
fmt.Println(hypot(3, 4)) // "5"
}

func hypot(x, y float64) float64 {
return math.Sqrt(x*x + y*y)
}
```

结果：

```
5
```

Go语言支持多返回值，多返回值能方便地获得函数执行后的多个返回参数，Go语言经常使用多返回值中的最后一个返回参数返回函数执行中可能发生的错误：

```
conn, err := connectToNetwork()
```

### 返回值的类型：

#### 1、同一种类型返回值

如果返回值是同一种类型，则用括号将多个返回值类型括起来，用逗号分隔每个返回值的类型。

```
func typedTwoValues() (int, int) {
    return 1, 2
}
func main() {
    a, b := typedTwoValues()
    fmt.Println(a, b)
}
```

结果：

```
1 2
```

#### 2、带有变量名的返回值

Go语言支持对返回值进行命名，这样返回值就和参数一样拥有参数变量名和类型。

命名的返回值变量的默认值为类型的默认值，即数值为 0，字符串为空字符串，布尔为 false、指针为 nil 等。

```
func namedRetValues() (a, b int) {
    a = 1
    b = 2
    return
}
```

说明：同一种类型返回值，和带有变量名的返回值，只能2选1，同时用会编译报错

### 调用函数

```
返回值变量列表 = 函数名(参数列表)
```

例如：

```
result := add(1,1)
```

## 6.2、函数变量

在Go语言中，函数也是一种类型，可以和其他类型一样保存在变量中，下面的代码定义了一个函数变量 f，并将一个函数名为 fire() 的函数赋给函数变量 f，这样调用函数变量 f 时，实际调用的就是 fire() 函数

```
func fire() {
    fmt.Println("fire")
}
func main() {
    var f func()
    f = fire
    f()
}
```

结果：

```
fire
```

## 6.3、匿名函数

Go语言支持匿名函数，即在需要使用函数时再定义函数，匿名函数没有函数名只有函数体，函数可以作为一种类型被赋值给函数类型的变量，匿名函数也往往以变量方式传递

匿名函数是指不需要定义函数名的一种函数实现方式，由一个不带函数名的函数声明和函数体组成  
匿名函数语法：

```
func(参数列表)(返回参数列表){
    函数体
}
```

例子：将匿名函数赋值给函数变量

```
// 将匿名函数体保存到f()中
f := func(data int) {
    fmt.Println("hello", data)
}
// 使用f()调用
f(100)
```

### 匿名函数作为参数传入

```
// 遍历切片的每个元素, 通过给定函数进行元素访问
func visit(list []int, f func(int)) {
    for _, v := range list {
        f(v)
    }
}
func main() {
    // 使用匿名函数打印切片内容
    visit([]int{1, 2, 3, 4}, func(v int) {
        fmt.Println(v)
    })
}
```

结果：

```
1
2
3
4
```

## 6.4、函数类型实现接口——把函数作为接口来调用

```
// 调用器接口
type Invoker interface {
// 需要实现一个Call方法
Call(interface{})
}

// 结构体类型
type MyStruct struct {
}

// 实现Invoker的Call
func (s *MyStruct) Call(p interface{}) {
fmt.Println("from struct", p)
}

// 函数定义为类型
type FuncCaller func(interface{})

// 实现Invoker的Call
func (f FuncCaller) Call(p interface{}) {
// 调用f函数本体
f(p)
}
func main() {
// 声明接口变量
var invoker Invoker
// 实例化结构体
s := new(MyStruct)
// 将实例化的结构体赋值到接口
invoker = s
// 使用接口调用实例化结构体的方法Struct.Call
invoker.Call(111)
// 将匿名函数转为FuncCaller类型，再赋值给接口
invoker = FuncCaller(func(v interface{}) {
fmt.Println("from function", v)
})
// 使用接口调用FuncCaller.Call，内部会调用函数本体
invoker.Call(222)
}
```

结果：

```
from struct 111
from function 222
```

## 6.5、闭包Closure – 引用了外部变量的匿名函数

Go语言中闭包是引用了自由变量的函数，被引用的自由变量和函数一同存在，即使已经离开了自由变量的环境也不会被释放或者删除，在闭包中可以继续使用这个自由变量，因此，简单的说：  
函数 + 引用环境 = 闭包

一个函数类型就像结构体一样，可以被实例化，函数本身不存储任何信息，只有与引用环境结合后形成的闭包才具有“记忆性”，函数是编译期静态的概念，而闭包是运行期动态的概念。

闭包（Closure）在某些编程语言中也被称为 Lambda 表达式。

```
func main() {
// 准备一个字符串
str1 := "hello world"
// 创建一个匿名函数
foo := func() {

// 匿名函数中访问str
str1 = "hello dude"
}
// 调用匿名函数
foo()
fmt.Println(str1)
}
```

结果：

```
hello dude
```

可以看到，闭包str1拥有了记忆

## 6.6、可变参数

可变参数是指函数传入的参数个数是可变的，为了做到这点，首先需要将函数定义为可以接受可变参数的类型：

```
func myfunc(args ...int) {
    for _, arg := range args {
        fmt.Println(arg)
    }
}
```

例子：

```
func MyPrintf(args ...interface{}) {
for _, arg := range args {
switch arg.(type) {
case int:
fmt.Println(arg, "is an int value.")
case string:
fmt.Println(arg, "is a string value.")
case int64:
fmt.Println(arg, "is an int64 value.")
default:
fmt.Println(arg, "is an unknown type.")
}
}
}
func main() {
var v1 int = 1
var v2 int64 = 234
var v3 string = "hello"
var v4 float32 = 1.234
MyPrintf(v1, v2, v3, v4)
}
```

结果：

```
1 is an int value.
234 is an int64 value.
hello is a string value.
1.234 is an unknown type.
```

## 6.7、defer – 延迟执行语句

Go语言的 defer 语句会将其后面跟随的语句进行延迟处理，在 defer 归属的函数即将返回时，将延迟处理的语句按 defer 的逆序进行执行，也就是说，先被 defer 的语句最后被执行，最后被 defer 的语句，最先被执行。

例子：

```
func main() {
fmt.Println("defer begin")
// 将defer放入延迟调用栈
defer fmt.Println(1)
defer fmt.Println(2)
// 最后一个放入, 位于栈顶, 最先调用
defer fmt.Println(3)
fmt.Println("defer end")
}
```

结果：

```
3
2
1
```

### 使用延迟执行语句在函数退出时释放资源

对于先加锁，再执行业务，最后解锁的代码：

```
var (
    // 一个演示用的映射
    valueByKey      = make(map[string]int)
    // 保证使用映射时的并发安全的互斥锁
    valueByKeyGuard sync.Mutex
)
// 根据键读取值
func readValue(key string) int {
    // 对共享资源加锁
    valueByKeyGuard.Lock()
    // 取值
    v := valueByKey[key]
    // 对共享资源解锁
    valueByKeyGuard.Unlock()
    // 返回值
    return v
}
```

readValue函数采用defer可优化为：

```
func readValue(key string) int {
    valueByKeyGuard.Lock()
   
    // defer后面的语句不会马上调用, 而是延迟到函数结束时调用
    defer valueByKeyGuard.Unlock()
    return valueByKey[key]
}
```

## 6.8、处理运行时错误

Go语言的错误处理思想及设计包含以下特征：  
1）一个可能造成错误的函数，需要返回值中返回一个错误接口（error），如果调用是成功的，错误接口将返回 nil，否则返回错误。  
2）在函数调用后需要检查错误，如果发生错误，则进行必要的错误处理。

Go语言没有类似 Java 或 .NET 中的异常处理机制，虽然可以使用 defer、panic、recover 模拟，但官方并不主张这样做，Go语言的设计者认为其他语言的异常机制已被过度使用，上层逻辑需要为函数发生的异常付出太多的资源，同时，如果函数使用者觉得错误处理很麻烦而忽略错误，那么程序将在不可预知的时刻崩溃。

Go语言希望开发者将错误处理视为正常开发必须实现的环节，正确地处理每一个可能发生错误的函数，同时，Go语言使用返回值返回错误的机制，也能大幅降低编译器、运行时处理错误的复杂度，让开发者真正地掌握错误的处理。

以net包中的Dial()函数举例说明error的用法：net.Dial()是Go net包中用于创建socket连接的函数，有两个返回值：Conn和error，这个函数是阻塞的，在socket操作后，会返回Conn链接对象和error，如果发生错误，error会告知错误的类型，Conn会返回空：

```
func Dial(network, address string) (Conn, error) {
    var d Dialer
    return d.Dial(network, address)
}
```

### 错误接口的定义格式

error是Go语言系统声明的接口类型，代码如下：

```
type error interface {
    Error() string
}
```

所有符合Error()string 格式的方法，都能实现错误接口，Error()方法返回错误描述。

### 自定义一个错误

语法：

```
var err = errors.New("this is an error")
```

在代码中使用错误定义：

```
import (
    "errors"
    "fmt"
)
// 定义除数为0的错误
var errDivisionByZero = errors.New("division by zero")
func div(dividend, divisor int) (int, error) {
    // 判断除数为0的情况并返回
    if divisor == 0 {
        return 0, errDivisionByZero
    }
    // 正常计算，返回空错误
    return dividend / divisor, nil
}
func main() {
    fmt.Println(div(1, 0))
}
```

结果：

```
0 division by zero
```

### 示例：在解析中使用自定义错误

使用 errors.New 定义的错误字符串的错误类型是无法提供丰富的错误信息的，那么，如果需要携带错误信息返回，就需要借助自定义结构体实现错误接口。

下面代码将实现一个解析错误（ParseError），这种错误包含两个内容，分别是文件名和行号，解析错误的结构还实现了 error 接口的 Error() 方法，返回错误描述时，就需要将文件名和行号返回。

```
// 声明一个解析错误
type ParseError struct {
Filename string // 文件名
Line     int    // 行号
}

// 实现error接口，返回错误描述
func (e *ParseError) Error() string {
return fmt.Sprintf("%s:%d", e.Filename, e.Line)
}

// 创建一些解析错误
func newParseError(filename string, line int) error {
return &ParseError{filename, line}
}
func main() {
var e error
// 创建一个错误实例，包含文件名和行号
e = newParseError("main.go", 1)
// 通过error接口查看错误描述
fmt.Println(e.Error())
// 根据错误接口具体的类型，获取详细错误信息
switch detail := e.(type) {
case *ParseError: // 这是一个解析错误
fmt.Printf("Filename: %s Line: %d\n", detail.Filename, detail.Line)
default: // 其他类型的错误
fmt.Println("other error")
}
}
```

结果：

```
main.go:1
Filename: main.go Line: 1
```

## 6.9、宕机panic – 程序终止运行

Go语言的类型系统会在编译时捕获很多错误，但有些错误只能在运行时检查，如数组访问越界、空指针引用等，这些运行时错误会引起宕机。

当宕机发生时，程序会中断运行，并立即执行在该 goroutine（可以先理解成线程）中被延迟的函数（defer 机制），随后，程序崩溃并输出日志信息，日志信息包括 panic value 和函数调用的堆栈跟踪信息，panic value 通常是某种错误信息。

对于每个 goroutine，日志信息中都会有与之相对的，发生 panic 时的函数调用堆栈跟踪信息，通常，我们不需要再次运行程序去定位问题，日志信息已经提供了足够的诊断依据，因此，在我们填写问题报告时，一般会将宕机和日志信息一并记录。

虽然Go语言的 panic 机制类似于其他语言的异常，但 panic 的适用场景有一些不同，由于 panic 会引起程序的崩溃，因此 panic 一般用于严重错误，如程序内部的逻辑不一致。任何崩溃都表明了我们的代码中可能存在漏洞，所以对于大部分漏洞，我们应该使用Go语言提供的错误机制，而不是 panic。

### 手动触发宕机

Go语言可以在程序中手动触发宕机，让程序崩溃。

```
func main() {
    panic("crash")
}
```

结果：

```
panic: crash

goroutine 1 [running]:
main.main()
    D:/code/main.go:4 +0x40
exit status 2
```

以上代码中只用了一个内建的函数 panic() 就可以造成崩溃，panic() 的声明如下：

```
func panic(v interface{})    //panic() 的参数可以是任意类型的。
```

### 在运行依赖的必备资源缺失时主动触发宕机

```
func MustCompile(str string) *Regexp {
    regexp, error := Compile(str)
    if error != nil {
        panic(`regexp: Compile(` + quote(str) + `): ` + error.Error())
    }
    return regexp
}
```

代码说明如下：  
第 1 行，编译正则表达式函数入口，输入包含正则表达式的字符串，返回正则表达式对象。  
第 2 行，Compile() 是编译正则表达式的入口函数，该函数返回编译好的正则表达式对象和错误。  
第 3 和第 4 行判断如果有错，则使用 panic() 触发宕机。  
第 6 行，没有错误时返回正则表达式对象。

手动宕机进行报错的方式不是一种偷懒的方式，反而能迅速报错，终止程序继续运行，防止更大的错误产生，不过，如果任何错误都使用宕机处理，也不是一种良好的设计习惯，因此应根据需要来决定是否使用宕机进行报错。

### 在宕机时触发延迟执行语句

当 panic() 触发的宕机发生时，panic() 后面的代码将不会被运行，但是在 panic() 函数前面已经运行过的 defer 语句依然会在宕机发生时发生作用，参考下面代码：

```
func main() {
    defer fmt.Println("宕机后要做的事情1")
    defer fmt.Println("宕机后要做的事情2")
    panic("宕机")
}
```

结果：

```
宕机后要做的事情2
宕机后要做的事情1
panic: 宕机

goroutine 1 [running]:
main.main()
    D:/code/main.go:8 +0xf8
exit status 2
```

## 6.10、宕机恢复recover – 防止程序崩溃

Recover 是一个Go语言的内建函数，可以让进入宕机流程中的 goroutine 恢复过来，recover 仅在延迟函数 defer 中有效，在正常的执行过程中，调用 recover 会返回 nil 并且没有其他任何效果，如果当前的 goroutine 陷入恐慌，调用 recover 可以捕获到 panic 的输入值，并且恢复正常的执行。

recover类似于java中的try{}catch{}机制

### 程序崩溃时的异常捕获

```
import (
"fmt"
"runtime"
)

// 崩溃时需要传递的上下文信息
type panicContext struct {
myPanicStr string // 所在函数
}

// 保护方式运行一个函数
func ProtectRun(entry func()) {
// 延迟处理的函数
defer func() {
// 发生宕机时，获取panic传递的上下文并打印
err := recover()
switch err.(type) {
case runtime.Error: // 运行时错误
fmt.Println("runtime error:", err)
default: // 非运行时错误
fmt.Println("error:", err)
}
}()
// defer的所附属的函数
entry()
}
func main() {
fmt.Println("运行前")
// 允许一段手动触发的错误
ProtectRun(func() {
fmt.Println("手动宕机前")
// 使用panic传递上下文
panic(&panicContext{
"手动触发panic",
})
fmt.Println("手动宕机后")
})
// 故意造成空指针访问错误
ProtectRun(func() {
fmt.Println("赋值宕机前")
var a *int
*a = 1
fmt.Println("赋值宕机后")
})
fmt.Println("运行后")
}
```

结果：

```
运行前
手动宕机前
error: &{手动触发panic}
赋值宕机前
runtime error: runtime error: invalid memory address or nil pointer dereference
运行后
```

panic 和 recover 的组合有如下特性：  
有 panic 没 recover，程序宕机。  
有 panic 也有 recover，程序不会宕机，执行完对应的 defer 后，从宕机点退出当前函数后继续执行。

## 6.11、计算函数执行时间

在Go语言中我们可以使用 time 包中的 Since() 函数来获取函数的运行时间：

```
func Since(t Time) Duration
```

例子：

```
import (
    "fmt"
    "time"
)
func test() {
    start := time.Now() // 获取当前时间
    sum := 0
    for i := 0; i < 100000000; i++ {
        sum++
    }
    elapsed := time.Since(start)
    fmt.Println("该函数执行完成耗时：", elapsed)
}
func main() {
    test()
}
```

结果：

```
该函数执行完成耗时： 32.276292ms
```

Since() 函数返回从 t 到现在经过的时间，等价于time.Now().Sub(t)。  
使用 time.Now().Sub() 获取函数的运行时间：

```
import (
"fmt"
"time"
)

func test() {
start := time.Now() // 获取当前时间
sum := 0
for i := 0; i < 100000000; i++ {
sum++
}
elapsed := time.Now().Sub(start)
fmt.Println("该函数执行完成耗时：", elapsed)
}
func main() {
test()
}
```

结果：

```
该函数执行完成耗时： 32.669333ms
```

## 6.12、单元测试

Go语言中提供了 testing 包来实现单元测试功能。

### 测试规则

要开始一个单元测试，需要准备一个 go 源码文件，在命名文件时文件名必须以\_test.go结尾，单元测试源码文件可以由多个测试用例（可以理解为函数）组成，每个测试用例的名称需要以 Test 为前缀，例如：

```
func TestXxx( t *testing.T ){
    //......
}
```

编写测试用例有以下几点需要注意：  
1）测试用例文件不会参与正常源码的编译，不会被包含到可执行文件中；  
2）测试用例的文件名必须以\_test.go结尾；  
3）需要使用 import 导入 testing 包；  
4）测试函数的名称要以Test或Benchmark开头，后面可以跟任意字母组成的字符串，但第一个字母必须大写，例如 TestAbc()，一个测试用例文件中可以包含多个测试函数；  
5）单元测试则以(t \*testing.T)作为参数，性能测试以(t \*testing.B)做为参数；  
6）测试用例文件使用go test命令来执行，源码中不需要 main() 函数作为入口，所有以\_test.go结尾的源码文件内以Test开头的函数都会自动执行。

### 单元（功能）测试

在同一文件夹test下创建两个Go语言文件，分别命名为 demo.go 和 demt\_test.go  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c0e979ec90d4313b42c389c67fe5e3d.png)  
demo.go：

```
package test

// 根据长宽获取面积
func GetArea(weight int, height int) int {
return weight * height
}
```

demo\_test.go:

```
package test

import "testing"

func TestGetArea(t *testing.T) {
area := GetArea(40, 50)
if area != 2000 {
t.Error("测试失败")
}
}
```

然后在test目录下执行：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/8dd0eb9870c8444b86d93d8ea074f671.png)  
或者在test目录上执行：go test -v

结果：

```
=== RUN   TestGetArea
--- PASS: TestGetArea (0.00s)
PASS
ok  awesomeProject/test1.180s
```

### 性能（压力）测试

改造demo\_test.go：

```
import "testing"

func BenchmarkGetArea(t *testing.B) {
for i := 0; i < t.N; i++ {
GetArea(40, 50)
}
}
```

这样运行：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/27f29c71e00d4c659ab4d7092efb9e45.png)  
或在test目录执行命令：go test -bench=“.”  
结果：

```
goos: darwin
goarch: amd64
pkg: awesomeProject/test
cpu: VirtualApple @ 2.50GHz
BenchmarkGetArea
BenchmarkGetArea-10    1000000000         0.3174 ns/op
PASS
ok  awesomeProject/test0.541s
```

### 覆盖率测试

改造demo\_test.go：

```
func TestGetArea(t *testing.T) {
area := GetArea(40, 50)
if area != 2000 {
t.Error("测试失败")
}
}
func BenchmarkGetArea(t *testing.B) {
for i := 0; i < t.N; i++ {
GetArea(40, 50)
}
}
```

执行：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/aa43f454396345338846662f879941f0.png)  
或执行命令：go test -cover  
结果：

```
=== RUN   TestGetArea
--- PASS: TestGetArea (0.00s)
PASS
coverage: 100.0% of statements
ok  awesomeProject/test1.357scoverage: 100.0% of statements
```

## 七、结构体struct

结构体是类型中带有成员的复合类型。Go 语言使用结构体和结构体成员来描述真实世界的实体和实体对应的各种属性。

### 关于 Go 语言的类（class）

Go 语言中没有“类”的概念，也不支持“类”的继承等面向对象的概念。  
Go 语言的结构体与“类”都是复合结构体，但 Go 语言中结构体的内嵌配合接口比面向对象具有更高的扩展性和灵活性。

## 7.1、结构体定义

结构体成员是由一系列的成员变量构成，这些成员变量也被称为“字段”。字段有以下特性：  
1）字段拥有自己的类型和值。  
2）字段名必须唯一。  
3）字段的类型也可以是结构体，甚至是字段所在结构体的类型。

使用关键字 type 可以将各种基本类型定义为自定义类型，基本类型包括整型、字符串、布尔等。

结构体的定义语法如下：

```
type 类型名 struct {
    字段1 字段1类型
    字段2 字段2类型
    …
}
```

结构体定义例子：

```
type Point struct {
    X int
    Y int
}
```

同类型的变量也可以写在一行，颜色的红、绿、蓝 3 个分量可以使用 byte 类型表示，定义的颜色结构体如下：

```
type Color struct {
    R, G, B byte
}
```

## 7.2、实例化结构体——为结构体分配内存并初始化

结构体的定义只是一种内存布局的描述，只有当结构体实例化时，才会真正地分配内存，因此必须在定义结构体并实例化后才能使用结构体的字段。

实例化就是根据结构体定义的格式创建一份与格式一致的内存区域，结构体实例与实例间的内存是完全独立的。

Go语言可以通过多种方式实例化结构体，根据实际需要可以选用不同的写法。

### 实例化基本形式

语法：

```
var ins T
```

例子：

```
type Point struct {
    X int
    Y int
}
var p Point
p.X = 10
p.Y = 20
```

### 创建指针类型的结构体

Go语言中，还可以使用 new 关键字对类型（包括结构体、整型、浮点数、字符串等）进行实例化，结构体在实例化后会形成指针类型的结构体。

语法：

```
ins := new(T)
```

例子：

```
type Player struct{
    Name string
    HealthPoint int
    MagicPoint int
}
tank := new(Player)
tank.Name = "Canon"
tank.HealthPoint = 300
```

### 取结构体地址实例化

在Go语言中，对结构体进行&取地址操作时，视为对该类型进行一次 new 的实例化操作，取地址语法如下：

```
ins := &T{}
```

例子：

```
type Command struct {
    Name    string    // 指令名称
    Var     *int      // 指令绑定的变量
    Comment string    // 指令的注释
}
var version int = 1
cmd := &Command{}
cmd.Name = "version"
cmd.Var = &version
cmd.Comment = "show version"
```

取地址实例化是最广泛的一种结构体实例化方式，可以使用函数封装上面的初始化过程，代码如下：

```
func newCommand(name string, varref *int, comment string) *Command {
    return &Command{
        Name:    name,
        Var:     varref,
        Comment: comment,
    }
}
cmd = newCommand(
    "version",
    &version,
    "show version",
)
```

## 7.3、结构体成员变量初始化

### 使用“键值对”初始化结构体

键值对初始化的格式如下：

```
ins := 结构体类型名{
    字段1: 字段1的值,
    字段2: 字段2的值,
    …
}
```

例子：

```
type People struct {
    name  string
    child *People
}
relation := &People{
    name: "爷爷",
    child: &People{
        name: "爸爸",
        child: &People{
                name: "我",
        },
    }
}
```

### 使用多个值列表初始化结构体

语法：

```
ins := 结构体类型名{
    字段1的值,
    字段2的值,
    …
}
```

例子：

```
type Address struct {
    Province    string
    City        string
    ZipCode     int
    PhoneNumber string
}
addr := Address{
    "四川",
    "成都",
    610000,
    "0",
}
fmt.Println(addr)
```

结果：

```
{四川 成都 610000 0}
```

### 初始化匿名结构体

语法：

```
ins := struct {
    // 匿名结构体字段定义
    字段1 字段类型1
    字段2 字段类型2
    …
}{
    // 字段值初始化
    初始化字段1: 字段1的值,
    初始化字段2: 字段2的值,
    …
}
```

键值对初始化部分是可选的，不初始化成员时，匿名结构体的格式变为：

```
ins := struct {
    字段1 字段类型1
    字段2 字段类型2
    …
}
```

例子：

```
// 打印消息类型, 传入匿名结构体
func printMsgType(msg *struct {
    id   int
    data string
}) {
    // 使用动词%T打印msg的类型
    fmt.Printf("%T\n", msg)
}
func main() {
    // 实例化一个匿名结构体
    msg := &struct {  // 定义部分
        id   int
        data string
    }{  // 值初始化部分
        1024,
        "hello",
    }
    printMsgType(msg)
}
```

结果：

```
*struct { id int; data string }
```

## 7.4、构造函数

Go语言的类型或结构体没有构造函数的功能，但是我们可以使用结构体初始化的过程来模拟实现构造函数。

### 多种方式创建和初始化结构体——模拟构造函数重载

例子：

```
type Cat struct {
    Color string
    Name  string
}
func NewCatByName(name string) *Cat {
    return &Cat{
        Name: name,
    }
}
func NewCatByColor(color string) *Cat {
    return &Cat{
        Color: color,
    }
}
```

### 带有父子关系的结构体的构造和初始化——模拟父级构造调用

```
type Cat struct {
    Color string
    Name  string
}
type BlackCat struct {
    Cat  // 嵌入Cat, 类似于派生
}
// “构造基类”
func NewCat(name string) *Cat {
    return &Cat{
        Name: name,
    }
}
// “构造子类”
func NewBlackCat(color string) *BlackCat {
    cat := &BlackCat{}
    cat.Color = color
    return cat
}
```

代码说明如下：  
1）第 6 行，定义 BlackCat 结构，并嵌入了 Cat 结构体，BlackCat 拥有 Cat 的所有成员，实例化后可以自由访问 Cat 的所有成员。  
2）第 11 行，NewCat() 函数定义了 Cat 的构造过程，使用名字作为参数，填充 Cat 结构体。  
3）第 18 行，NewBlackCat() 使用 color 作为参数，构造返回 BlackCat 指针。  
4）第 19 行，实例化 BlackCat 结构，此时 Cat 也同时被实例化。  
5）第 20 行，填充 BlackCat 中嵌入的 Cat 颜色属性，BlackCat 没有任何成员，所有的成员都来自于 Cat。

## 7.5、类型内嵌和结构体内嵌

结构体可以包含一个或多个匿名（或内嵌）字段，即这些字段没有显式的名字，只有字段的类型是必须的，此时类型也就是字段的名字。匿名字段本身可以是一个结构体类型，即结构体可以包含内嵌结构体。

例子：

```
type innerS struct {
    in1 int
    in2 int
}
type outerS struct {
    b int
    c float32
    int // anonymous field
    innerS //anonymous field
}
func main() {
    outer := new(outerS)
    outer.b = 6
    outer.c = 7.5
    outer.int = 60
    outer.in1 = 5
    outer.in2 = 10
    fmt.Printf("outer.b is: %d\n", outer.b)
    fmt.Printf("outer.c is: %f\n", outer.c)
    fmt.Printf("outer.int is: %d\n", outer.int)
    fmt.Printf("outer.in1 is: %d\n", outer.in1)
    fmt.Printf("outer.in2 is: %d\n", outer.in2)
    // 使用结构体字面量
    outer2 := outerS{6, 7.5, 60, innerS{5, 10}}
    fmt.Printf("outer2 is:", outer2)
}
```

结果：

```
outer.b is: 6
outer.c is: 7.500000
outer.int is: 60
outer.in1 is: 5
outer.in2 is: 10
outer2 is:{6 7.5 60 {5 10}}
```

通过类型 outer.int 的名字来获取存储在匿名字段中的数据，于是可以得出一个结论：在一个结构体中对于每一种数据类型只能有一个匿名字段。

### 内嵌结构体

同样地结构体也是一种数据类型，所以它也可以作为一个匿名字段来使用，如同上面例子中那样。外层结构体通过 outer.in1 直接进入内层结构体的字段，内嵌结构体甚至可以来自其他包。内层结构体被简单的插入或者内嵌进外层结构体。这个简单的“继承”机制提供了一种方式，使得可以从另外一个或一些类型继承部分或全部实现。

```
import "fmt"
type A struct {
    ax, ay int
}
type B struct {
    A
    bx, by float32
}
func main() {
    b := B{A{1, 2}, 3.0, 4.0}
    fmt.Println(b.ax, b.ay, b.bx, b.by)
    fmt.Println(b.A)
}
```

结果：

```
1 2 3 4
{1 2}
```

## 7.6、垃圾回收和SetFinalizer

Go语言自带垃圾回收机制（GC）。  
GC 通过独立的进程执行，它会搜索不再使用的变量，并将其释放。  
需要注意的是，GC 在运行时会占用机器资源。

GC 是自动进行的，如果要手动进行 GC，可以使用 runtime.GC() 函数，显式的执行 GC。显式的进行 GC 只在某些特殊的情况下才有用，比如当内存资源不足时调用 runtime.GC() ，这样会立即释放一大片内存，但是会造成程序短时间的性能下降。

finalizer（终止器）是与对象关联的一个函数，通过 runtime.SetFinalizer 来设置，如果某个对象定义了 finalizer，当它被 GC 时候，这个 finalizer 就会被调用，以完成一些特定的任务，例如发信号或者写日志等。

在Go语言中 SetFinalizer 函数是这样定义的：

```
func SetFinalizer(x, f interface{})
```

参数说明如下：  
1）参数 x 必须是一个指向通过 new 申请的对象的指针，或者通过对复合字面值取址得到的指针。  
2）参数 f 必须是一个函数，它接受单个可以直接用 x 类型值赋值的参数，也可以有任意个被忽略的返回值。

SetFinalizer 函数可以将 x 的终止器设置为 f，当垃圾收集器发现 x 不能再直接或间接访问时，它会清理 x 并调用 f(x)。

另外，x 的终止器会在 x 不能直接或间接访问后的任意时间被调用执行，不保证终止器会在程序退出前执行，因此一般终止器只用于在长期运行的程序中释放关联到某对象的非内存资源。例如，当一个程序丢弃一个 os.File 对象时没有调用其 Close 方法，该 os.File 对象可以使用终止器去关闭对应的操作系统文件描述符。-- 这类似于java中的钩子

终止器会按依赖顺序执行：如果 A 指向 B，两者都有终止器，且 A 和 B 没有其它关联，那么只有 A 的终止器执行完成，并且 A 被释放后，B 的终止器才可以执行。

此外，我们也可以使用SetFinalizer(x, nil)来清理绑定到 x 上的终止器。

例子：在函数 entry() 中定义局部变量并设置 finalizer，当函数 entry() 执行完成后，在 main 函数中手动触发 GC，查看 finalizer 的执行情况。

```
import (
    "log"
    "runtime"
    "time"
)
type Road int
func findRoad(r *Road) {
    log.Println("road:", *r)
}
func entry() {
    var rd Road = Road(999)
    r := &rd
    runtime.SetFinalizer(r, findRoad)
}
func main() {
    entry()
    for i := 0; i < 10; i++ {
        time.Sleep(time.Second)
        runtime.GC()
    }
}
```

结果：

```
2022/05/17 14:44:59 road: 999
```

## 7.7、链表操作

### 使用 Struct 定义单链表

例子：为链表赋值，并遍历链表中的每个结点。

```
type Node struct {
    data int
    next *Node
}
func Shownode(p *Node) { //遍历
    for p != nil {
        fmt.Println(*p)
        p = p.next //移动指针
    }
}
func main() {
    var head = new(Node)
    head.data = 1
    var node1 = new(Node)
    node1.data = 2
    head.next = node1
    var node2 = new(Node)
    node2.data = 3
    node1.next = node2
    Shownode(head)
}
```

结果：

```
{1 0xc000096220}
{2 0xc000096230}
{3 <nil>}
```

## 7.8、IO对象及操作

在Go语言中，几乎所有的数据结构都围绕接口展开，接口是Go语言中所有数据结构的核心。  
Go语言标准库的 bufio 包中，实现了对数据 I/O 接口的缓冲功能。  
这些功能封装于接口 io.ReadWriter、io.Reader 和 io.Writer 中，并对应创建了 ReadWriter、Reader 或 Writer 对象，在提供缓冲的同时实现了一些文本基本 I/O 操作功能。

### ReadWriter 对象

ReadWriter 对象可以对数据 I/O 接口 io.ReadWriter 进行输入输出缓冲操作  
ReadWriter 结构定义如下：

```
type ReadWriter struct {
    *Reader
    *Writer
}
```

默认情况下，ReadWriter 对象中存放了一对 Reader 和 Writer 指针，它同时提供了对数据 I/O 对象的读写缓冲功能。

可以使用 NewReadWriter() 函数创建 ReadWriter 对象，该函数的功能是根据指定的 Reader 和 Writer 创建一个 ReadWriter 对象，ReadWriter 对象将会向底层 io.ReadWriter 接口写入数据，或者从 io.ReadWriter 接口读取数据。该函数原型声明如下：

```
func NewReadWriter(r *Reader, w *Writer) *ReadWriter
```

在函数 NewReadWriter() 中，参数 r 是要读取的来源 Reader 对象，参数 w 是要写入的目的 Writer 对象。

### Reader 对象

Reader 对象可以对数据 I/O 接口 io.Reader 进行输入缓冲操作，Reader 结构定义如下：

```
type Reader struct {
    //contains filtered or unexported fields
)
```

默认情况下 Reader 对象没有定义初始值，输入缓冲区最小值为 16。当超出限制时，另创建一个二倍的存储空间。

#### 创建 Reader 对象

可以创建 Reader 对象的函数一共有两个，分别是 NewReader() 和 NewReaderSize()：  
**1、NewReader() 函数**  
NewReader() 函数的功能是按照缓冲区默认长度创建 Reader 对象，Reader 对象会从底层 io.Reader 接口读取尽量多的数据进行缓存。该函数原型如下：

```
func NewReader(rd io.Reader) *Reader
```

**2、NewReaderSize() 函数**  
NewReaderSize() 函数的功能是按照指定的缓冲区长度创建 Reader 对象，Reader 对象会从底层 io.Reader 接口读取尽量多的数据进行缓存。该函数原型如下：

```
func NewReaderSize(rd io.Reader, size int) *Reader
```

其中，参数 rd 是 io.Reader 接口，参数 size 是指定的缓冲区字节长度。

#### 操作 Reader 对象

操作 Reader 对象的方法共有 11 个，分别是 Read()、ReadByte()、ReadBytes()、ReadLine()、ReadRune ()、ReadSlice()、ReadString()、UnreadByte()、UnreadRune()、Buffered()、Peek()

##### 1）Read() 方法

Read() 方法的功能是读取数据，并存放到字节切片 p 中。  
Read() 执行结束会返回已读取的字节数，因为最多只调用底层的 io.Reader 一次，所以返回的 n 可能小于 len§，当字节流结束时，n 为 0，err 为 io. EOF。

该方法如下：

```
func (b *Reader) Read(p []byte) (n int, err error)
```

例子：

```
import (
"bufio"
"bytes"
"fmt"
)

func main() {
data := []byte("你好Go语言")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
var buf [128]byte
n, err := r.Read(buf[:])
fmt.Println(string(buf[:n]), n, err)
}
```

结果：

```
你好Go语言 14 <nil>
```

##### 2) ReadByte() 方法

ReadByte() 方法的功能是读取并返回一个字节，如果没有字节可读，则返回错误信息。该方法原型如下：

```
func (b *Reader) ReadByte() (c byte,err error)
```

例子：

```
import (
"bufio"
"bytes"
"fmt"
)

func main() {
data := []byte("你好Go语言")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
c, err := r.ReadByte()
fmt.Println(string(c), err)
}
```

结果:

```
ä <nil>
```

##### 3) ReadBytes() 方法

ReadBytes() 方法的功能是读取数据直到遇到第一个分隔符“delim”，并返回读取的字节序列（包括“delim”）。如果 ReadBytes 在读到第一个“delim”之前出错，它返回已读取的数据和那个错误（通常是 io.EOF）。只有当返回的数据不以“delim”结尾时，返回的 err 才不为空值。该方法原型如下：

```
func (b *Reader) ReadBytes(delim byte) (line []byte, err error)
```

例子：

```
import (
"bufio"
"bytes"
"fmt"
)

func main() {
data := []byte("你好Go语言, 我要入门")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
var delim byte = ','
line, err := r.ReadBytes(delim)
fmt.Println(string(line), err)
}
```

结果：

```
你好Go语言, <nil>
```

##### 4) ReadLine() 方法

ReadLine() 是一个低级的用于读取一行数据的方法，大多数调用者应该使用 ReadBytes(‘\\n’) 或者 ReadString(‘\\n’)。  
ReadLine 返回一行，不包括结尾的回车字符，如果一行太长（超过缓冲区长度），参数 isPrefix 会设置为 true 并且只返回前面的数据，剩余的数据会在以后的调用中返回。

当返回最后一行数据时，参数 isPrefix 会置为 false。返回的字节切片只在下一次调用 ReadLine 前有效。ReadLine 会返回一个非空的字节切片或一个错误，方法原型如下：

```
func (b *Reader) ReadLine() (line []byte, isPrefix bool, err error)
```

例子：

```
func main() {
data := []byte("Today is a good day, \r\nis it?")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
line, prefix, err := r.ReadLine()
fmt.Println(string(line), prefix, err)
}
```

结果：

```
Today is a good day,  false <nil>
```

##### 5) ReadRune() 方法

ReadRune() 方法的功能是读取一个 UTF-8 编码的字符，并返回其 Unicode 编码和字节数。  
如果编码错误，ReadRune 只读取一个字节并返回 unicode.ReplacementChar(U+FFFD) 和长度 1。该方法原型如下：

```
func (b *Reader) ReadRune() (r rune, size int, err error)
```

例子：

```
func main() {
data := []byte("Today is a good day, \r\nis it?")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
ch, size, err := r.ReadRune()
fmt.Println(string(ch), size, err)
}
```

结果：

```
T 1 <nil>
```

##### 6) ReadSlice() 方法

ReadSlice() 方法的功能是读取数据直到分隔符“delim”处，并返回读取数据的字节切片，下次读取数据时返回的切片会失效  
如果 ReadSlice 在查找到“delim”之前遇到错误，它返回读取的所有数据和那个错误（通常是 io.EOF）。

如果缓冲区满时也没有查找到“delim”，则返回 ErrBufferFull 错误。ReadSlice 返回的数据会在下次 I/O 操作时被覆盖，大多数调用者应该使用 ReadBytes 或者 ReadString。只有当 line 不以“delim”结尾时，ReadSlice 才会返回非空 err。

该方法原型如下：

```
func (b *Reader) ReadSlice(delim byte) (line []byte, err error)
```

例子：

```
func main() {
data := []byte("Today is a good day, is it?")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
var delim byte = ','
line, err := r.ReadSlice(delim)
fmt.Println(string(line), err)
line, err = r.ReadSlice(delim)
fmt.Println(string(line), err)
line, err = r.ReadSlice(delim)
fmt.Println(string(line), err)
}
```

结果：

```
Today is a good day, <nil>
 is it? EOF
 EOF
```

##### 7) ReadString() 方法

ReadString() 方法的功能是读取数据直到分隔符“delim”第一次出现，并返回一个包含“delim”的字符串。  
如果 ReadString 在读取到“delim”前遇到错误，它返回已读字符串和那个错误（通常是 io.EOF）。只有当返回的字符串不以“delim”结尾时，ReadString 才返回非空 err。

该方法原型如下：

```
func (b *Reader) ReadString(delim byte) (line string, err error)
```

例子：

```
func main() {
data := []byte("Today is a good day, is it?")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
var delim byte = ','
line, err := r.ReadString(delim)
fmt.Println(line, err
}
```

结果：

```
Today is a good day, <nil>
```

##### 8) UnreadByte() 方法

UnreadByte() 方法的功能是取消已读取的最后一个字节（即把字节重新放回读取缓冲区的前部）。只有最近一次读取的单个字节才能取消读取。该方法原型如下：

```
func (b *Reader) UnreadByte() error
```

##### 9) UnreadRune() 方法

UnreadRune() 方法的功能是取消读取最后一次读取的 Unicode 字符。如果最后一次读取操作不是 ReadRune，UnreadRune 会返回一个错误（在这方面它比 UnreadByte 更严格，因为 UnreadByte 会取消上次任意读操作的最后一个字节）。该方法原型如下：

```
func (b *Reader) UnreadRune() error
```

##### 10) Buffered() 方法

Buffered() 方法的功能是返回可从缓冲区读出数据的字节数, 示例代码如下：

```
func main() {
data := []byte("Today is a good day, is it?")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
var buf [14]byte
n, err := r.Read(buf[:])
fmt.Println(string(buf[:n]), n, err)
rn := r.Buffered()
fmt.Println(rn)
n, err = r.Read(buf[:])
fmt.Println(string(buf[:n]), n, err)
rn = r.Buffered()
fmt.Println(rn)
}
```

结果：

```
Today is a goo 14 <nil>
13
d day, is it? 13 <nil>
0
```

##### 11) Peek() 方法

Peek() 方法的功能是读取指定字节数的数据，这些被读取的数据不会从缓冲区中清除。  
在下次读取之后，本次返回的字节切片会失效。如果 Peek 返回的字节数不足 n 字节，则会同时返回一个错误说明原因，如果 n 比缓冲区要大，则错误为 ErrBufferFull。  
该方法原型如下：

```
func (b *Reader) Peek(n int) ([]byte, error)
```

例子：

```
func main() {
data := []byte("Today is a good day, is it?")
rd := bytes.NewReader(data)
r := bufio.NewReader(rd)
bl, err := r.Peek(8)
fmt.Println(string(bl), err)
bl, err = r.Peek(14)
fmt.Println(string(bl), err)
bl, err = r.Peek(20)
fmt.Println(string(bl), err)
}
```

结果：

```
Today is <nil>
Today is a goo <nil>
Today is a good day, <nil>
```

### Writer 对象

Writer 对象可以对数据 I/O 接口 io.Writer 进行输出缓冲操作，Writer 结构定义如下：

```
type Writer struct {
    //contains filtered or unexported fields
}
```

默认情况下 Writer 对象没有定义初始值，如果输出缓冲过程中发生错误，则数据写入操作立刻被终止，后续的写操作都会返回写入异常错误。

#### 创建 Writer 对象

创建 Writer 对象的函数共有两个分别是 NewWriter() 和 NewWriterSize()

##### 1) NewWriter() 函数

NewWriter() 函数的功能是按照默认缓冲区长度创建 Writer 对象，Writer 对象会将缓存的数据批量写入底层 io.Writer 接口。该函数原型如下

```
func NewWriter(wr io.Writer) *Writer
```

##### 2) NewWriterSize() 函数

NewWriterSize() 函数的功能是按照指定的缓冲区长度创建 Writer 对象，Writer 对象会将缓存的数据批量写入底层 io.Writer 接口。该函数原型如下：

```
func NewWriterSize(wr io.Writer, size int) *Writer
```

其中，参数 wr 是 io.Writer 接口，参数 size 是指定的缓冲区字节长度。

#### 操作 Writer 对象

操作 Writer 对象的方法共有 7 个，分别是 Available()、Buffered()、Flush()、Write()、WriteByte()、WriteRune() 和 WriteString() 方法

##### 1) Available() 方法

Available() 方法的功能是返回缓冲区中未使用的字节数，该方法原型如下：

```
func (b *Writer) Available() int
```

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
p := []byte("你好Go语言")
fmt.Println("写入前未使用的缓冲区为：", w.Available())
w.Write(p)
fmt.Printf("写入%q后，未使用的缓冲区为：%d\n", string(p), w.Available())
}
```

结果：

```
写入前未使用的缓冲区为： 4096
写入"你好Go语言"后，未使用的缓冲区为：4082
```

##### 2) Buffered() 方法

Buffered() 方法的功能是返回已写入当前缓冲区中的字节数，该方法原型如下：

```
func (b *Writer) Buffered() int
```

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
p := []byte("你好Go语言")
fmt.Println("写入前未使用的缓冲区为：", w.Buffered())
w.Write(p)
fmt.Printf("写入%q后，未使用的缓冲区为：%d\n", string(p), w.Buffered())
w.Flush()
fmt.Println("执行 Flush 方法后，写入的字节数为：", w.Buffered())
}
```

结果：

```
写入前未使用的缓冲区为： 0
写入"你好Go语言"后，未使用的缓冲区为：14
执行 Flush 方法后，写入的字节数为： 0
```

##### 3) Flush() 方法

Flush() 方法的功能是把缓冲区中的数据写入底层的 io.Writer，并返回错误信息。如果成功写入，error 返回 nil，否则 error 返回错误原因。

该方法原型如下：

```
func (b *Writer) Flush() error
```

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
p := []byte("你好Go语言")
w.Write(p)
fmt.Printf("未执行 Flush 缓冲区输出 %q\n", string(wr.Bytes()))
w.Flush()
fmt.Printf("执行 Flush 后缓冲区输出 %q\n", string(wr.Bytes()))
}
```

结果：

```
未执行 Flush 缓冲区输出 ""
执行 Flush 后缓冲区输出 "你好Go语言"
```

##### 4) Write() 方法

Write() 方法的功能是把字节切片 p 写入缓冲区，返回已写入的字节数 nn。如果 nn 小于 len§，则同时返回一个错误原因。该方法原型如下：

```
func (b *Writer) Write(p []byte) (nn int, err error)
```

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
p := []byte("你好Go语言")
n, err := w.Write(p)
w.Flush()
fmt.Println(string(wr.Bytes()), n, err)
}
```

结果：

```
你好Go语言 14 <nil>
```

##### 5) WriteByte() 方法

WriteByte() 方法的功能是写入一个字节，如果成功写入，error 返回 nil，否则 error 返回错误原因。该方法原型如下：

```
func (b *Writer) WriteByte(c byte) error
```

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
var c byte = 'G'
err := w.WriteByte(c)
w.Flush()
fmt.Println(string(wr.Bytes()), err)
}
```

结果：

```
G <nil>
```

##### 6) WriteRune() 方法

WriteRune() 方法的功能是以 UTF-8 编码写入一个 Unicode 字符，返回写入的字节数和错误信息。该方法原型如下：

```
func (b *Writer) WriteRune(r rune) (size int,err error)
```

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
var r rune = 'G'
size, err := w.WriteRune(r)
w.Flush()
fmt.Println(string(wr.Bytes()), size, err)
}
```

结果：

```
G 1 <nil>
```

##### 7) WriteString() 方法

WriteString() 方法的功能是写入一个字符串，并返回写入的字节数和错误信息。如果返回的字节数小于 len(s)，则同时返回一个错误说明原因。该方法原型如下：

```
func (b *Writer) WriteString(s string) (int, error)
```

其中，参数 s 是要写入的字符串。示例代码如下：

例子：

```
func main() {
wr := bytes.NewBuffer(nil)
w := bufio.NewWriter(wr)
s := "你好Go语言"
n, err := w.WriteString(s)
w.Flush()
fmt.Println(string(wr.Bytes()), n, err)
}
```

结果：

```
你好Go语言 14 <nil>
```

## 八、接口interface

接口本身是调用方和实现方均需要遵守的一种协议，大家按照统一的方法命名参数类型和数量来协调逻辑处理的过程。

Go 语言的接口设计是非侵入式的，接口编写者无须知道接口被哪些类型实现。而接口实现者只需知道实现的是什么样子的接口，但无须指明实现哪一个接口。编译器知道最终编译时使用哪个类型实现哪个接口，或者接口应该由谁来实现。

非侵入式设计是 Go 语言设计师经过多年的大项目经验总结出来的设计之道。只有让接口和实现者真正解耦，编译速度才能真正提高，项目之间的耦合度也会降低不少。

## 8.1、接口声明

接口声明的语法：

```
type 接口类型名 interface{
    方法名1( 参数列表1 ) 返回值列表1
    方法名2( 参数列表2 ) 返回值列表2
    …
}
```

对各个部分的说明：  
1）接口类型名：使用 type 将接口定义为自定义的类型名。Go语言的接口在命名时，一般会在单词后面添加 er，如有写操作的接口叫 Writer，有字符串功能的接口叫 Stringer，有关闭功能的接口叫 Closer 等。  
2）方法名：当方法名首字母是大写时，且这个接口类型名首字母也是大写时，这个方法可以被接口所在的包（package）之外的代码访问。  
参数列表、返回值列表：参数列表和返回值列表中的参数变量名可以被忽略，例如：

```
type writer interface{
    Write([]byte) error
}
```

### 开发中常见的接口及写法

Go语言提供的很多包中都有接口，例如 io 包中提供的 Writer 接口：

```
type Writer interface {
    Write(p []byte) (n int, err error)
}
```

这个接口可以调用 Write() 方法写入一个字节数组（\[\]byte），返回值告知写入字节数（n int）和可能发生的错误（err error）。

类似的，还有将一个对象以字符串形式展现的接口，只要实现了这个接口的类型，在调用 String() 方法时，都可以获得对象对应的字符串。在 fmt 包中定义如下：

```
type Stringer interface {
    String() string
}
```

Stringer 接口在Go语言中的使用频率非常高，功能类似于 Java 或者 C# 语言里的 ToString 的操作。

## 8.2、实现接口的条件

### 条件一：接口的方法与实现接口的类型方法格式一致

在类型中添加与接口签名一致的方法就可以实现该方法。签名包括方法中的名称、参数列表、返回参数列表。

例子：

```
// 定义一个数据写入器接口
type DataWriter interface {
WriteData(data interface{}) error
}

// 定义文件结构，用于实现DataWriter接口
type file struct {
}

// 实现DataWriter接口的WriteData方法
func (d *file) WriteData(data interface{}) error {
// 模拟写入数据
fmt.Println("WriteData:", data)
return nil
}
func main() {
// 实例化file
f := new(file)
// 声明一个DataWriter的接口
var writer DataWriter
// 将接口赋值f，也就是*file类型
writer = f
// 使用DataWriter接口进行数据写入
writer.WriteData("data")
}
```

结果：

```
WriteData: data
```

### 条件二：接口中所有方法均被实现

当一个接口中有多个方法时，只有这些方法都被实现了，接口才能被正确编译并使用。

如上述例子中，对接口添加个方法：

```
type DataWriter interface {
WriteData(data interface{}) error

CanWrite() bool
}
```

则编译报错：

```
cannot use f (variable of type *file) as type DataWriter in assignment:
*file does not implement DataWriter (missing CanWrite method)
```

### 类型与接口的关系

在Go语言中类型和接口之间有一对多和多对一的关系

1.  一个类型可以实现多个接口
2.  多个类型可以实现相同的接口

## 8.3、类型断言

类型断言（Type Assertion）是一个使用在接口值上的操作，用于检查接口类型变量所持有的值是否实现了期望的接口或者具体的类型。

类型断言语法：

```
value, ok := x.(T)
```

其中，x 表示一个接口的类型，T 表示一个具体的类型（也可为接口类型）。

该断言表达式会返回 x 的值（也就是 value）和一个布尔值（也就是 ok），可根据该布尔值判断 x 是否为 T 类型：  
1）如果 T 是具体某个类型，类型断言会检查 x 的动态类型是否等于具体类型 T。如果检查成功，类型断言返回的结果是 x 的动态值，其类型是 T。  
2）如果 T 是接口类型，类型断言会检查 x 的动态类型是否满足 T。如果检查成功，x 的动态值不会被提取，返回值是一个类型为 T 的接口值。  
无论 T 是什么类型，如果 x 是 nil 接口值，类型断言都会失败。

类型断言的例子：

```
func main() {
var x interface{}
x = 10
value, ok := x.(int)
fmt.Print(value, ",", ok)
}
```

结果：

```
10,true
```

断言失败的例子：

```
func main() {
    var x interface{}
    x = "Hello"
    value := x.(int)
    fmt.Println(value)
}
```

结果：

```
panic: interface conversion: interface {} is string, not int
```

断言还可以配合switch使用：

```
func main() {
    var a int
    a = 10
    getType(a)
}
func getType(a interface{}) {
    switch a.(type) {
    case int:
        fmt.Println("the type of a is int")
    case string:
        fmt.Println("the type of a is string")
    case float64:
        fmt.Println("the type of a is float")
    default:
        fmt.Println("unknown type")
    }
}
```

结果：

```
the type of a is int
```

## 8.4、排序

Go语言的sort 包内置的提供了根据一些排序函数来对任何序列排序的功能。

一个内置的排序算法需要知道三个东西：序列的长度，表示两个元素比较的结果，一种交换两个元素的方式；这就是 sort.Interface 的三个方法：

```
package sort
type Interface interface {
    Len() int            // 获取元素数量
    Less(i, j int) bool // i，j是序列元素的指数。
    Swap(i, j int)        // 交换元素
}
```

### 使用sort.Interface接口进行排序

对一系列字符串进行排序时，使用字符串切片（\[\]string）承载多个字符串。使用 type 关键字，将字符串切片（\[\]string）定义为自定义类型 MyStringList。为了让 sort 包能识别 MyStringList，能够对 MyStringList 进行排序，就必须让 MyStringList 实现 sort.Interface 接口。

排序例子：

```
// 将[]string定义为MyStringList类型
type MyStringList []string
// 实现sort.Interface接口的获取元素数量方法
func (m MyStringList) Len() int {
    return len(m)
}
// 实现sort.Interface接口的比较元素方法
func (m MyStringList) Less(i, j int) bool {
    return m[i] < m[j]
}
// 实现sort.Interface接口的交换元素方法
func (m MyStringList) Swap(i, j int) {
    m[i], m[j] = m[j], m[i]
}
func main() {
    // 准备一个内容被打乱顺序的字符串切片
    names := MyStringList{
        "3. Triple Kill",
        "5. Penta Kill",
        "2. Double Kill",
        "4. Quadra Kill",
        "1. First Blood",
    }
    // 使用sort包进行排序
    sort.Sort(names)
    // 遍历打印结果
    for _, v := range names {
            fmt.Printf("%s\n", v)
    }
}
```

结果：

```
1. First Blood
2. Double Kill
3. Triple Kill
4. Quadra Kill
5. Penta Kill
```

第 38 行，使用 sort 包的 Sort() 函数，将 names（MyStringList类型）进行排序。排序时，sort 包会通过 MyStringList 实现的 Len()、Less()、Swap() 这 3 个方法进行数据获取和修改。

### 常见类型的便捷排序

通过实现 sort.Interface 接口的排序过程具有很强的可定制性，可以根据被排序对象比较复杂的特性进行定制。例如，需要多种排序逻辑的需求就适合使用 sort.Interface 接口进行排序。但大部分情况中，只需要对字符串、整型等进行快速排序。Go语言中提供了一些固定模式的封装以方便开发者迅速对内容进行排序。

#### 1) 字符串切片的便捷排序

sort 包中有一个 StringSlice 类型，定义如下：

```
type StringSlice []string
func (p StringSlice) Len() int           { return len(p) }
func (p StringSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p StringSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
// Sort is a convenience method.
func (p StringSlice) Sort() { Sort(p) }
```

sort 包中的 StringSlice 的代码与 MyStringList 的实现代码几乎一样。因此，只需要使用 sort 包的 StringSlice 就可以更简单快速地进行字符串排序。将代码1中的排序代码简化后如下所示：

```
func main() {
names := sort.StringSlice{
"3. Triple Kill",
"5. Penta Kill",
"2. Double Kill",
"4. Quadra Kill",
"1. First Blood",
}
sort.Sort(names)

// 遍历打印结果
for _, v := range names {
fmt.Printf("%s\n", v)
}
}
```

结果：

```
1. First Blood
2. Double Kill
3. Triple Kill
4. Quadra Kill
5. Penta Kill
```

#### 2) 对整型切片进行排序

除了字符串可以使用 sort 包进行便捷排序外，还可以使用 sort.IntSlice 进行整型切片的排序。sort.IntSlice 的定义如下：

```
type IntSlice []int
func (p IntSlice) Len() int           { return len(p) }
func (p IntSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p IntSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
// Sort is a convenience method.
func (p IntSlice) Sort() { Sort(p) }
```

sort 包在 sort.Interface 对各类型的封装上还有更进一步的简化，下面使用 sort.Strings 继续对代码1进行简化，代码如下：

```
func main() {
names := []string{
"3. Triple Kill",
"5. Penta Kill",
"2. Double Kill",
"4. Quadra Kill",
"1. First Blood",
}
sort.Strings(names)
// 遍历打印结果
for _, v := range names {
fmt.Printf("%s\n", v)
}
}
```

结果同上

#### 3) sort包内建的类型排序接口一览

![在这里插入图片描述](https://img-blog.csdnimg.cn/c385f23b1c4849ab829f09a39a8fa2bb.png)

### 对结构体数据进行排序

除了基本类型的排序，也可以对结构体进行排序。结构体比基本类型更为复杂，排序时不能像数值和字符串一样拥有一些固定的单一原则。结构体的多个字段在排序中可能会存在多种排序的规则，例如，结构体中的名字按字母升序排列，数值按从小到大的顺序排序。一般在多种规则同时存在时，需要确定规则的优先度，如先按名字排序，再按年龄排序等。

#### 1) 完整实现sort.Interface进行结构体排序

排序时要求按照英雄的分类进行排序，相同分类的情况下按名字进行排序

```
// 声明英雄的分类
type HeroKind int

// 定义HeroKind常量, 类似于枚举
const (
None HeroKind = iota
Tank
Assassin
Mage
)

// 定义英雄名单的结构
type Hero struct {
Name string   // 英雄的名字
Kind HeroKind // 英雄的种类
}

// 将英雄指针的切片定义为Heros类型
type Heros []*Hero

// 实现sort.Interface接口取元素数量方法
func (s Heros) Len() int {
return len(s)
}

// 实现sort.Interface接口比较元素方法
func (s Heros) Less(i, j int) bool {
// 如果英雄的分类不一致时, 优先对分类进行排序
if s[i].Kind != s[j].Kind {
return s[i].Kind < s[j].Kind
}
// 默认按英雄名字字符升序排列
return s[i].Name < s[j].Name
}

// 实现sort.Interface接口交换元素方法
func (s Heros) Swap(i, j int) {
s[i], s[j] = s[j], s[i]
}
func main() {
// 准备英雄列表
heros := Heros{
&Hero{"吕布", Tank},
&Hero{"李白", Assassin},
&Hero{"妲己", Mage},
&Hero{"貂蝉", Assassin},
&Hero{"关羽", Tank},
&Hero{"诸葛亮", Mage},
}
// 使用sort包进行排序
sort.Sort(heros)
// 遍历英雄列表打印排序结果
for _, v := range heros {
fmt.Printf("%+v\n", v)
}
}
```

结果：

```
&{Name:关羽 Kind:1}
&{Name:吕布 Kind:1}
&{Name:李白 Kind:2}
&{Name:貂蝉 Kind:2}
&{Name:妲己 Kind:3}
&{Name:诸葛亮 Kind:3}
```

#### 2) 使用sort.Slice进行切片元素排序

从 Go 1.8 开始，Go语言在 sort 包中提供了 sort.Slice() 函数进行更为简便的排序方法。sort.Slice() 函数只要求传入需要排序的数据，以及一个排序时对元素的回调函数，类型为 func(i,j int)bool，sort.Slice() 函数的定义如下：

```
func Slice(slice interface{}, less func(i, j int) bool)
```

使用 sort.Slice() 函数，对代码2重新优化的完整代码如下：

```
type HeroKind int
const (
    None = iota
    Tank
    Assassin
    Mage
)
type Hero struct {
    Name string
    Kind HeroKind
}
func main() {
    heros := []*Hero{
        {"吕布", Tank},
        {"李白", Assassin},
        {"妲己", Mage},
        {"貂蝉", Assassin},
        {"关羽", Tank},
        {"诸葛亮", Mage},
    }
    sort.Slice(heros, func(i, j int) bool {
        if heros[i].Kind != heros[j].Kind {
            return heros[i].Kind < heros[j].Kind
        }
        return heros[i].Name < heros[j].Name
    })
    for _, v := range heros {
        fmt.Printf("%+v\n", v)
    }
}
```

## 8.5、接口的嵌套组合

在Go语言中，不仅结构体与结构体之间可以嵌套，接口与接口间也可以通过嵌套创造出新的接口。  
一个接口可以包含一个或多个其他的接口，这相当于直接将这些内嵌接口的方法列举在外层接口中一样。只要接口的所有方法被实现，则这个接口中的所有嵌套接口的方法均可以被调用。

### 系统包中的接口嵌套组合

Go语言的 io 包中定义了写入器（Writer）、关闭器（Closer）和写入关闭器（WriteCloser）3 个接口，代码如下：

```
type Writer interface {
    Write(p []byte) (n int, err error)
}
type Closer interface {
    Close() error
}
type WriteCloser interface {
    Writer
    Closer
}
```

type WriteCloser interface定义了写入关闭器（WriteCloser），这个接口由 Writer 和 Closer 两个接口嵌入。也就是说，WriteCloser 同时拥有了 Writer 和 Closer 的特性。

### 在代码中使用接口嵌套组合

在代码中使用 io.Writer、io.Closer 和 io.WriteCloser 这 3 个接口时，只需要按照接口实现的规则实现 io.Writer 接口和 io.Closer 接口即可。  
而 io.WriteCloser 接口在使用时，编译器会根据接口的实现者确认它们是否同时实现了 io.Writer 和 io.Closer 接口，详细实现代码如下：

```
import (
    "io"
)
// 声明一个设备结构
type device struct {
}
// 实现io.Writer的Write()方法
func (d *device) Write(p []byte) (n int, err error) {
    return 0, nil
}
// 实现io.Closer的Close()方法
func (d *device) Close() error {
    return nil
}
func main() {
    // 声明写入关闭器, 并赋予device的实例
    var wc io.WriteCloser = new(device)
    // 写入数据
    wc.Write(nil)
    // 关闭设备
    wc.Close()
    // 声明写入器, 并赋予device的新实例
    var writeOnly io.Writer = new(device)
    // 写入数据
    writeOnly.Write(nil)
}
```

## 8.6、接口和类型之间的转换

Go语言中使用接口断言（type assertions）将接口转换成另外一个接口，也可以将接口转换为另外的类型。接口的转换在开发中非常常见，使用也非常频繁。

### 类型断言的格式

类型断言是一个使用在接口值上的操作。

类型断言的基本格式如下：

```
t := i.(T)
```

其中，i 代表接口变量，T 代表转换的目标类型，t 代表转换后的变量。

这里有两种可能。第一种，如果断言的类型 T 是一个具体类型，然后类型断言检查 i 的动态类型是否和 T 相同。如果这个检查成功了，类型断言的结果是 i 的动态值，当然它的类型是 T。

例子：

```
var w io.Writer
w = os.Stdout
f := w.(*os.File) // 成功: f == os.Stdout
c := w.(*bytes.Buffer) // 死机：接口保存*os.file，而不是*bytes.buffer
```

第二种，如果相反断言的类型 T 是一个接口类型，然后类型断言检查是否 i 的动态类型满足 T。如果这个检查成功了，动态值没有获取到；这个结果仍然是一个有相同类型和值部分的接口值，但是结果有类型 T。

```
var w io.Writer
w = os.Stdout
rw := w.(io.ReadWriter) // 成功：*os.file具有读写功能
w = new(ByteCounter)
rw = w.(io.ReadWriter) // 死机：*字节计数器没有读取方法
```

如果断言操作的对象是一个 nil 接口值，那么不论被断言的类型是什么这个类型断言都会失败。

### 将接口转换为其他接口

实现某个接口的类型同时实现了另外一个接口，此时可以在两个接口间转换。

鸟和猪具有不同的特性，鸟可以飞，猪不能飞，但两种动物都可以行走。如果使用结构体实现鸟和猪，让它们具备自己特性的 Fly() 和 Walk() 方法就让鸟和猪各自实现了飞行动物接口（Flyer）和行走动物接口（Walker）。

将鸟和猪的实例创建后，被保存到 interface{} 类型的 map 中。interface{} 类型表示空接口，意思就是这种接口可以保存为任意类型。对保存有鸟或猪的实例的 interface{} 变量进行断言操作，如果断言对象是断言指定的类型，则返回转换为断言对象类型的接口；如果不是指定的断言类型时，断言的第二个参数将返回 false。例如下面的代码：

```
var obj interface = new(bird)
f, isFlyer := obj.(Flyer)
```

例子：

```
// 定义飞行动物接口
type Flyer interface {
    Fly()
}
// 定义行走动物接口
type Walker interface {
    Walk()
}
// 定义鸟类
type bird struct {
}
// 实现飞行动物接口
func (b *bird) Fly() {
    fmt.Println("bird: fly")
}
// 为鸟添加Walk()方法, 实现行走动物接口
func (b *bird) Walk() {
    fmt.Println("bird: walk")
}
// 定义猪
type pig struct {
}
// 为猪添加Walk()方法, 实现行走动物接口
func (p *pig) Walk() {
    fmt.Println("pig: walk")
}
func main() {
    // 创建动物的名字到实例的映射
    animals := map[string]interface{}{
        "bird": new(bird),
        "pig":  new(pig),
    }
    // 遍历映射
    for name, obj := range animals {
        // 判断对象是否为飞行动物
        f, isFlyer := obj.(Flyer)
        // 判断对象是否为行走动物
        w, isWalker := obj.(Walker)
        fmt.Printf("name: %s isFlyer: %v isWalker: %v\n", name, isFlyer, isWalker)
        // 如果是飞行动物则调用飞行动物接口
        if isFlyer {
            f.Fly()
        }
        // 如果是行走动物则调用行走动物接口
        if isWalker {
            w.Walk()
        }
    }
}
```

结果：

```
name: pig isFlyer: false isWalker: true
pig: walk
name: bird isFlyer: true isWalker: true
bird: fly
bird: walk
```

### 将接口转换为其他类型

在代码 1 中，可以实现将接口转换为普通的指针类型。例如将 Walker 接口转换为 \*pig 类型，请参考下面的代码：

```
p1 := new(pig)

var a Walker = p1
p2 := a.(*pig)

fmt.Printf("p1=%p p2=%p", p1, p2)
```

对代码的说明如下：  
第 3 行，由于 pig 实现了 Walker 接口，因此可以被隐式转换为 Walker 接口类型保存于 a 中。  
第 4 行，由于 a 中保存的本来就是 \*pig 本体，因此可以转换为 \*pig 类型。  
第 6 行，对比发现，p1 和 p2 指针是相同的。

如果尝试将上面这段代码中的 Walker 类型的 a 转换为 \*bird 类型，将会发出运行时错误，请参考下面的代码：

```
p1 := new(pig)
var a Walker = p1
p2 := a.(*bird)
```

运行时报错：

```
panic: interface conversion: main.Walker is *main.pig, not *main.bird
```

报错意思是：接口转换时，main.Walker 接口的内部保存的是 \*main.pig，而不是 \*main.bird。

因此，接口在转换为其他类型时，接口内保存的实例对应的类型指针，必须是要转换的对应的类型指针。

## 8.7、空接口类型（interface{}）

空接口是接口类型的特殊形式，空接口没有任何方法，因此任何类型都无须实现空接口。  
空接口类型类似于 Java 语言中的 Object

### 将值保存到空接口

```
var any interface{}
any = 1
fmt.Println(any)
any = "hello"
fmt.Println(any)
any = false
fmt.Println(any)
```

结果：

```
1
hello
false
```

### 从空接口获取值

保存到空接口的值，如果直接取出指定类型的值时，会发生编译错误，代码如下：

```
// 声明a变量, 类型int, 初始值为1
var a int = 1
// 声明i变量, 类型为interface{}, 初始值为a, 此时i的值变为1
var i interface{} = a
// 声明b变量, 尝试赋值i
var b int = i
```

第8行代码编译报错：

```
cannot use i (type interface {}) as type int in assignment: need type assertion
```

为了让第 8 行的操作能够完成，编译器提示我们得使用 type assertion，意思就是类型断言。  
可以这样改：

```
var b int = i.(int)
```

### 空接口的值比较

空接口在保存不同的值后，可以和其他变量值一样使用==进行比较操作。  
空接口的比较有以下几种特性：

#### 1）类型不同的空接口间的比较结果不相同

保存有类型不同的值的空接口进行比较时，Go语言会优先比较值的类型。因此类型不同，比较结果也是不相同的，代码如下：

```
// a保存整型
var a interface{} = 100
// b保存字符串
var b interface{} = "hi"
// 两个空接口不相等
fmt.Println(a == b)
```

结果：false

#### 2) 不能比较空接口中的动态值

当接口中保存有动态类型的值时，运行时将触发错误，代码如下：

```
// c保存包含10的整型切片
var c interface{} = []int{10}
// d保存包含20的整型切片
var d interface{} = []int{20}
// 这里会发生崩溃
fmt.Println(c == d)
```

结果：

```
panic: runtime error: comparing uncomparable type []int
```

这是一个运行时错误，提示 \[\]int 是不可比较的类型。下表中列举出了类型及比较的几种情况。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/aef538d5efd641a7b938231a9847d794.png)

## 8.8、类型分支（switch判断空接口中变量的类型）

type-switch 流程控制的语法或许是Go语言中最古怪的语法。 它可以被看作是类型断言的增强版。

类型断言的语法：

```
switch 接口变量.(type) {
    case 类型1:
        // 变量是类型1时的处理
    case 类型2:
        // 变量是类型2时的处理
    …
    default:
        // 变量不是所有case中列举的类型时的处理
}
```

对各个部分的说明：  
接口变量：表示需要判断的接口类型的变量。  
类型1、类型2……：表示接口变量可能具有的类型列表，满足时，会指定 case 对应的分支进行处理。

### 使用类型分支判断基本类型

```
func printType(v interface{}) {
switch v.(type) {
case int:
fmt.Println(v, "is int")
case string:
fmt.Println(v, "is string")
case bool:
fmt.Println(v, "is bool")
}
}
func main() {
printType(1024)
printType("pig")
printType(true)
}
```

结果：

```
1024 is int
pig is string
true is bool
```

## 8.9、error接口：返回错误信息

错误处理在每个编程语言中都是一项重要内容，通常开发中遇到的分为异常与错误两种，Go语言中也不例外。  
针对这样的情况，Go语言中引入 error 接口类型作为错误处理的标准模式，如果函数要返回错误，则返回值类型列表中肯定包含 error。

### error 基本用法

Go语言 error 类型是一个非常简单的接口类型，如下所示：

```
// The error built-in interface type is the conventional interface for
// representing an error condition, with the nil value representing no error.
type error interface {
    Error() string
}
```

error 接口有一个签名为 Error() string 的方法，所有实现该接口的类型都可以当作一个错误类型。Error() 方法给出了错误的描述，在使用 fmt.Println 打印错误时，会在内部调用 Error() string 方法来得到该错误的描述。

一般情况下，如果函数需要返回错误，就将 error 作为多个返回值中的最后一个（但这并非是强制要求）。

创建一个 error 最简单的方法就是调用 errors.New 函数，它会根据传入的错误信息返回一个新的 error，示例代码如下：

```
func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return -1, errors.New("math: square root of negative number")
    }
    return math.Sqrt(f), nil
}
func main() {
    result, err := Sqrt(-13)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(result)
    }
}
```

结果：

```
math: square root of negative number
```

### 自定义错误类型

```
type dualError struct {
    Num     float64
    problem string
}
func (e dualError) Error() string {
    return fmt.Sprintf("Wrong!!!,because \"%f\" is a negative number", e.Num)
}
func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return -1, dualError{Num: f}
    }
    return math.Sqrt(f), nil
}
func main() {
    result, err := Sqrt(-13)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(result)
    }
}
```

结果：

```
Wrong!!!,because "-13.000000" is a negative number
```

## 8.10、实现web服务器

Go语言里面提供了一个完善的 net/http 包，通过 net/http 包我们可以很方便的搭建一个可以运行的 Web 服务器。

### 搭建一个简单的 Web 服务器

```
import (
"fmt"
"log"
"net/http"
)

func main() {
http.HandleFunc("/", index) // index 为向 url发送请求时，调用的函数
log.Fatal(http.ListenAndServe("localhost:8000", nil))
}
func index(w http.ResponseWriter, r *http.Request) {
fmt.Fprintf(w, "Go语言网站")
}
```

运行后，用浏览器输入：http://localhost:8000/  
浏览器显示结果：

```
Go语言网站
```

## 九、Go语言包package

Go 语言的入口 main() 函数所在的包（package）叫 main，main 包想要引用别的代码，必须同样以包的方式进行引用。

Go 语言的包与文件夹一一对应，所有与包相关的操作，必须依赖于工作目录（GOPATH）

## 9.1、包的基本概念

Go语言的包借助了目录树的组织形式，一般包的名称就是其源文件所在目录的名称，虽然Go语言没有强制要求包名必须和其所在的目录名同名，但还是建议包名和所在目录同名，这样结构更清晰。

包名的定义是不包括目录路径的，但是包在引用时一般使用全路径引用。比如在GOPATH/src/a/b/ 下定义一个包 c。在包 c 的源码中只需声明为package c，而不是声明为package a/b/c，但是在导入 c 包时，需要带上路径，例如import “a/b/c”。

包的习惯用法：  
1）包名一般是小写的，使用一个简短且有意义的名称。  
2）包名一般要和所在的目录同名，也可以不同，包名中不能包含- 等特殊符号。  
3）包一般使用域名作为目录名称，这样能保证包名的唯一性，比如 GitHub 项目的包一般会放到GOPATH/src/github.com/userName/projectName 目录下。  
4）包名为 main 的包为应用程序的入口包，编译不包含 main 包的源码文件时不会得到可执行文件。  
5）一个文件夹下的所有源码文件只能属于同一个包，同样属于同一个包的源码文件不能放在多个文件夹下。

### 包的导入

要在代码中引用其他包的内容，需要使用 import 关键字导入使用的包。具体语法如下：

```
import "包的路径"
```

注意事项：  
1）import 导入语句通常放在源码文件开头包声明语句的下面；  
2）导入的包名需要使用双引号包裹起来；  
3）包名是从GOPATH/src/ 后开始计算的，使用/ 进行路径分隔。

包的导入有两种写法，分别是单行导入和多行导入。  
单行导入的格式如下：

```
import "包 1 的路径"
import "包 2 的路径"
```

多行导入的格式如下：

```
import (
    "包 1 的路径"
    "包 2 的路径"
)
```

#### 包的导入路径

包的引用路径有两种写法，分别是全路径导入和相对路径导入。

全路径导入：包的绝对路径就是GOROOT/src/或GOPATH/src/后面包的存放路径，如下所示：

```
import "lab/test"
import "database/sql/driver"
import "database/sql"
```

上面代码的含义如下：  
1）test 包是自定义的包，其源码位于GOPATH/src/lab/test 目录下；  
2）driver 包的源码位于GOROOT/src/database/sql/driver 目录下；  
3）sql 包的源码位于GOROOT/src/database/sql 目录下。

相对路径导入：  
相对路径只能用于导入GOPATH 下的包，标准包的导入只能使用全路径导入。  
例如包 a 的所在路径是GOPATH/src/lab/a，包 b 的所在路径为GOPATH/src/lab/b，如果在包 b 中导入包 a ，则可以使用相对路径导入方式。示例如下：

```
// 相对路径导入
import "../a"
```

### 包的引用格式

包的引用有四种格式：

#### 1) 标准引用格式

```
import "fmt"
```

#### 2) 自定义别名引用格式

```
import F "fmt"
```

其中 F 就是 fmt 包的别名，使用时我们可以使用F.来代替标准引用格式的fmt.来作为前缀使用 fmt 包中的方法。  
如：

```
package main
import F "fmt"
func main() {
    F.Println("C语言中文网")
}
```

#### 3) 省略引用格式

```
import . "fmt"
```

这种格式相当于把 fmt 包直接合并到当前程序中，在使用 fmt 包内的方法是可以不用加前缀fmt.，直接引用：

```
package main
import . "fmt"
func main() {
    //不需要加前缀 fmt.
    Println("C语言中文网")
}
```

#### 4) 匿名引用格式

在引用某个包时，如果只是希望执行包初始化的 init 函数，而不使用包内部的数据时，可以使用匿名引用格式

```
import _ "database/sql"
```

匿名导入的包与其他方式导入的包一样都会被编译到可执行文件中。

使用标准格式引用包，但是代码中却没有使用包，编译器会报错。如果包中有 init 初始化函数，则通过import \_ “包的路径” 这种方式引用包，仅执行包的初始化函数，即使包没有 init 初始化函数，也不会引发编译器报错。

例子：

```
package main
import (
    _ "database/sql"
    "fmt"
)
func main() {
    fmt.Println("aaa")
}
```

注意：  
1）一个包可以有多个 init 函数，包加载时会执行全部的 init 函数，但并不能保证执行顺序，所以不建议在一个包中放入多个 init 函数，将需要初始化的逻辑放到一个 init 函数里面。  
2）包不能出现环形引用的情况，比如包 a 引用了包 b，包 b 引用了包 c，如果包 c 又引用了包 a，则编译不能通过。  
3）包的重复引用是允许的，比如包 a 引用了包 b 和包 c，包 b 和包 c 都引用了包 d。这种场景相当于重复引用了 d，这种情况是允许的，并且 Go 编译器保证包 d 的 init 函数只会执行一次。

### 包加载

在执行 main 包的 mian 函数之前， Go 引导程序会先对整个程序的包进行初始化。整个执行的流程：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c10943ec68c34e868956f3db982ba548.png)  
Go语言包的初始化有如下特点：  
1）包初始化程序从 main 函数引用的包开始，逐级查找包的引用，直到找到没有引用其他包的包，最终生成一个包引用的有向无环图。  
2）Go 编译器会将有向无环图转换为一棵树，然后从树的叶子节点开始逐层向上对包进行初始化。  
3）单个包的初始化过程如上图所示，先初始化常量，然后是全局变量，最后执行包的 init 函数。

## 9.2、封装简介及实现细节

在Go语言中封装就是把抽象出来的字段和对字段的操作封装在一起，数据被保护在内部，程序的其它包只能通过被授权的方法，才能对字段进行操作。

封装的实现步骤：  
1）将结构体、字段的首字母小写；  
2）给结构体所在的包提供一个工厂模式的函数，首字母大写，类似一个构造函数；  
3）提供一个首字母大写的 Set 方法（类似其它语言的 public），用于对属性判断并赋值；  
4）提供一个首字母大写的 Get 方法（类似其它语言的 public），用于获取属性的值。

例子：对于员工，不能随便查看年龄，工资等隐私，并对输入的年龄进行合理的验证。  
1）创建model包，新建person.go

```
package model

import "fmt"

type person struct {
Name string
age  int //其它包不能直接访问..
sal  float64
}

//写一个工厂模式的函数，相当于构造函数
func NewPerson(name string) *person {
return &person{
Name: name,
}
}

//为了访问age 和 sal 我们编写一对SetXxx的方法和GetXxx的方法
func (p *person) SetAge(age int) {
if age > 0 && age < 150 {
p.age = age
} else {
fmt.Println("年龄范围不正确..")
//给程序员给一个默认值
}
}
func (p *person) GetAge() int {
return p.age
}
func (p *person) SetSal(sal float64) {
if sal >= 3000 && sal <= 30000 {
p.sal = sal
} else {
fmt.Println("薪水范围不正确..")
}
}
func (p *person) GetSal() float64 {
return p.sal
}
```

结果：

```
&{smith 18 5000}
smith  age = 18  sal =  5000
```

## 9.3、GOPATH（Go语言工作目录）

GOPATH 是 Go语言中使用的一个环境变量，它使用绝对路径提供项目的工作目录。

### 使用命令行查看GOPATH信息

```
go env
```

## 9.4、常用包简介

标准的Go语言代码库中包含了大量的包，并且在安装 Go 的时候多数会自动安装到系统中。我们可以在 $GOROOT/src/pkg 目录中查看这些包。

### 1) fmt

fmt 包实现了格式化的标准输入输出，这与C语言中的 printf 和 scanf 类似。其中的 fmt.Printf() 和 fmt.Println() 是开发者使用最为频繁的函数。

### 2) io

这个包提供了原始的 I/O 操作界面。它主要的任务是对 os 包这样的原始的 I/O 进行封装，增加一些其他相关，使其具有抽象功能用在公共的接口上

### 3) bufio

bufio 包通过对 io 包的封装，提供了数据缓冲功能，能够一定程度减少大块数据读写带来的开销。

在 bufio 各个组件内部都维护了一个缓冲区，数据读写操作都直接通过缓存区进行。当发起一次读写操作时，会首先尝试从缓冲区获取数据，只有当缓冲区没有数据时，才会从数据源获取数据更新缓冲。

### 4) sort

sort 包提供了用于对切片和用户定义的集合进行排序的功能。

### 5) strconv

strconv 包提供了将字符串转换成基本数据类型，或者从基本数据类型转换为字符串的功能。

### 6) os

os 包提供了不依赖平台的操作系统函数接口，设计像 Unix 风格，但错误处理是 go 风格，当 os 包使用时，如果失败后返回错误类型而不是错误数量。

### 7) sync

sync 包实现多线程中锁机制以及其他同步互斥机制。

### 8) flag

flag 包提供命令行参数的规则定义和传入参数解析的功能。绝大部分的命令行程序都需要用到这个包。

### 9) encoding/json

encoding/json 包提供了对 JSON 的基本支持，比如从一个对象序列化为 JSON 字符串，或者从 JSON 字符串反序列化出一个具体的对象等。

### 10) html/template

主要实现了 web 开发中生成 html 的 template 的一些函数。

### 11) net/http

net/http 包提供 HTTP 相关服务，主要包括 http 请求、响应和 URL 的解析，以及基本的 http 客户端和扩展的 http 服务。

通过 net/http 包，只需要数行代码，即可实现一个爬虫或者一个 Web 服务器，这在传统语言中是无法想象的。

### 12) reflect

reflect 包实现了运行时反射，允许程序通过抽象类型操作对象。通常用于处理静态类型 interface{} 的值，并且通过 Typeof 解析出其动态类型信息，通常会返回一个有接口类型 Type 的对象。

### 13) os/exec

os/exec 包提供了执行自定义 linux 命令的相关实现。

### 14) strings

strings 包主要是处理字符串的一些函数集合，包括合并、查找、分割、比较、后缀检查、索引、大小写处理等等。  
strings 包与 bytes 包的函数接口功能基本一致。

### 15) bytes

bytes 包提供了对字节切片进行读写操作的一系列函数。字节切片处理的函数比较多，分为基本处理函数、比较函数、后缀检查函数、索引函数、分割函数、大小写处理函数和子切片处理函数等。

### 16) log

log 包主要用于在程序中输出日志。

log 包中提供了三类日志输出接口，Print、Fatal 和 Panic。  
1）Print 是普通输出；  
2）Fatal 是在执行完 Print 后，执行 os.Exit(1)；  
3）Panic 是在执行完 Print 后调用 panic() 方法。

## 9.5、sync包与锁：限制线程对变量的访问

Go语言中 sync 包里提供了互斥锁 Mutex 和读写锁 RWMutex 用于处理并发过程中可能出现同时两个或多个协程（或线程）读或写同一个变量的情况。

锁是 sync 包中的核心，它主要有两个方法，分别是加锁（Lock）和解锁（Unlock）。

在并发的情况下，多个线程或协程同时其修改一个变量，使用锁能保证在某一时间内，只有一个协程或线程修改这一变量。

不使用锁时，在并发的情况下可能无法得到想要的结果，如下所示：

```
package main
import (
    "fmt"
    "time"
)
func main() {
    var a = 0
    for i := 0; i < 1000; i++ {
        go func(idx int) {
            a += 1
            fmt.Println(a)
        }(i)
    }
    time.Sleep(time.Second)
}
```

从理论上来说，上面的程序会将 a 的值依次递增输出，但实际上输出的a却不是有序的：

```
195
197
997
168
199
408
2
```

协程的执行顺序：  
1）从寄存器读取 a 的值；  
2）然后做加法运算；  
3）最后写到寄存器。

按照上面的顺序，假如有一个协程取得 a 的值为 3，然后执行加法运算，此时又有一个协程对 a 进行取值，得到的值同样是 3，最终两个协程的返回结果是相同的。  
而锁的概念就是，当一个协程正在处理 a 时将 a 锁定，其它协程需要等待该协程处理完成并将 a 解锁后才能再进行操作，也就是说同时处理 a 的协程只能有一个，从而避免上面示例中的情况出现。

### 1、互斥锁 Mutex

互斥锁中其有两个方法可以调用：

```
func (m *Mutex) Lock()
func (m *Mutex) Unlock()
```

将上面的代码略作修改：

```
func main() {
var a = 0
var lock sync.Mutex
for i := 0; i < 1000; i++ {
go func(idx int) {
lock.Lock()
defer lock.Unlock()
a += 1
fmt.Printf("goroutine %d, a=%d\n", idx, a)
}(i)
}
// 等待 1s 结束主程序
// 确保所有协程执行完
time.Sleep(time.Second)
}
```

结果：

```
...
goroutine 998, a=995
goroutine 993, a=996
goroutine 994, a=997
goroutine 996, a=998
goroutine 999, a=999
goroutine 1, a=1000
```

一个互斥锁只能同时被一个 goroutine 锁定，其它 goroutine 将阻塞直到互斥锁被解锁（重新争抢对互斥锁的锁定）

### 2、读写锁

读写锁有如下四个方法：  
1）写操作的锁定和解锁分别是func (\*RWMutex) Lock和func (\*RWMutex) Unlock；  
2）读操作的锁定和解锁分别是func (\*RWMutex) Rlock和func (\*RWMutex) RUnlock。

读写锁的区别在于：  
1）写锁：其他goroutine不可读也不可写；  
2）读锁：写锁阻塞等待；读锁可访问  
读和写是互斥的，读和读不互斥

例子：

```
import (
"fmt"
"math/rand"
"sync"
)

var count int
var rw sync.RWMutex

func main() {
ch := make(chan struct{}, 10)
for i := 0; i < 5; i++ {
go read(i, ch)
}
for i := 0; i < 5; i++ {
go write(i, ch)
}
for i := 0; i < 10; i++ {
<-ch
}
}
func read(n int, ch chan struct{}) {
rw.RLock()
fmt.Printf("goroutine %d 进入读操作...\n", n)
v := count
fmt.Printf("goroutine %d 读取结束，值为：%d\n", n, v)
rw.RUnlock()
ch <- struct{}{}
}
func write(n int, ch chan struct{}) {
rw.Lock()
fmt.Printf("goroutine %d 进入写操作...\n", n)
v := rand.Intn(1000)
count = v
fmt.Printf("goroutine %d 写入结束，新值为：%d\n", n, v)
rw.Unlock()
ch <- struct{}{}
}
```

结果：

```
goroutine 0 进入读操作...
goroutine 0 读取结束，值为：0
goroutine 4 进入写操作...
goroutine 4 写入结束，新值为：81
goroutine 1 进入读操作...
goroutine 1 读取结束，值为：81
goroutine 3 进入读操作...
goroutine 3 读取结束，值为：81
goroutine 4 进入读操作...
goroutine 4 读取结束，值为：81
goroutine 2 进入读操作...
goroutine 2 读取结束，值为：81
goroutine 0 进入写操作...
goroutine 0 写入结束，新值为：887
goroutine 1 进入写操作...
goroutine 1 写入结束，新值为：847
goroutine 2 进入写操作...
goroutine 2 写入结束，新值为：59
goroutine 3 进入写操作...
goroutine 3 写入结束，新值为：81
```

## 9.6、big包：对整数的高精度计算

实际开发中，对于超出 int64 或者 uint64 类型的大数进行计算时，如果对精度没有要求，使用 float32 或者 float64 就可以胜任，但如果对精度有严格要求的时候，我们就不能使用浮点数了，因为浮点数在内存中只能被近似的表示。

Go语言中 math/big 包实现了大数字的多精度计算，支持 Int（有符号整数）、Rat（有理数）和 Float（浮点数）等数字类型。

这些类型可以实现任意位数的数字，只要内存足够大，但缺点是需要更大的内存和处理开销，这使得它们使用起来要比内置的数字类型慢很多。

在 math/big 包中，Int 类型定义如下所示：

```
// An Int represents a signed multi-precision integer.
// The zero value for an Int represents the value 0.
type Int struct {
    neg bool // sign
    abs nat  // absolute value of the integer
}
```

生成 Int 类型的方法为 NewInt()，如下所示：

```
// NewInt allocates and returns a new Int set to x.
func NewInt(x int64) *Int {
    return new(Int).SetInt64(x)
}
```

注意：NewInt() 函数只对 int64 有效，其他类型必须先转成 int64 才行。

Go语言中还提供了许多 Set 函数，可以方便的把其他类型的整形存入 Int ，因此，我们可以先 new(int) 然后再调用 Set 函数，Set 函数有如下几种：

```
// SetInt64 函数将 x 转换为 z 并返回 z。
func (z *Int) SetInt64(x int64) *Int {
    neg := false
    if x < 0 {
        neg = true
        x = -x
    }
    z.abs = z.abs.setUint64(uint64(x))
    z.neg = neg
    return z
}

// SetUint64 函数将 x 转换为 z 并返回 z。
func (z *Int) SetUint64(x uint64) *Int {
    z.abs = z.abs.setUint64(x)
    z.neg = false
    return z
}

// Set 函数将 x 转换为 z 并返回 z。
func (z *Int) Set(x *Int) *Int {
    if z != x {
        z.abs = z.abs.set(x.abs)
        z.neg = x.neg
    }
    return z
}
```

示例代码如下所示：

```
import (
    "fmt"
    "math/big"
)
func main() {
    big1 := new(big.Int).SetUint64(uint64(1000))
    fmt.Println("big1 is: ", big1)
    big2 := big1.Uint64()
    fmt.Println("big2 is: ", big2)
}
```

结果：

```
big1 is:  1000
big2 is:  1000
```

## 9.7、time包：时间和日期

时间一般包含时间值和时区，可以从Go语言中 time 包的源码中看出：

```
type Time struct {
    // wall and ext encode the wall time seconds, wall time nanoseconds,
    // and optional monotonic clock reading in nanoseconds.
    //
    // From high to low bit position, wall encodes a 1-bit flag (hasMonotonic),
    // a 33-bit seconds field, and a 30-bit wall time nanoseconds field.
    // The nanoseconds field is in the range [0, 999999999].
    // If the hasMonotonic bit is 0, then the 33-bit field must be zero
    // and the full signed 64-bit wall seconds since Jan 1 year 1 is stored in ext.
    // If the hasMonotonic bit is 1, then the 33-bit field holds a 33-bit
    // unsigned wall seconds since Jan 1 year 1885, and ext holds a
    // signed 64-bit monotonic clock reading, nanoseconds since process start.
    wall uint64
    ext  int64
    // loc specifies the Location that should be used to
    // determine the minute, hour, month, day, and year
    // that correspond to this Time.
    // The nil location means UTC.
    // All UTC times are represented with loc==nil, never loc==&utcLoc.
    loc *Location
}
```

面代码中：  
1）wall：表示距离公元 1 年 1 月 1 日 00:00:00UTC 的秒数；  
2）ext：表示纳秒；  
3）loc：代表时区，主要处理偏移量，不同的时区，对应的时间不一样。

### 时间的获取

#### 1) 获取当前时间：time.Now()

```
import (
"fmt"
"time"
)

func main() {
now := time.Now() //获取当前时间
fmt.Printf("current time:%v\n", now)
year := now.Year()     //年
month := now.Month()   //月
day := now.Day()       //日
hour := now.Hour()     //小时
minute := now.Minute() //分钟
second := now.Second() //秒
fmt.Printf("%d-%02d-%02d %02d:%02d:%02d\n", year, month, day, hour, minute, second)
}
```

结果：

```
current time:2022-05-18 17:54:59.650928 +0800 CST m=+0.000096959
2022-05-18 17:54:59
```

#### 2) 获取时间戳

```
func main() {
now := time.Now()            //获取当前时间
timestamp1 := now.Unix()     //时间戳
timestamp2 := now.UnixNano() //纳秒时间戳
fmt.Printf("现在的时间戳：%v\n", timestamp1)
fmt.Printf("现在的纳秒时间戳：%v\n", timestamp2)
}
```

结果：

```
现在的时间戳：1652867789
现在的纳秒时间戳：1652867789215489000
```

使用 time.Unix() 函数可以将时间戳转为时间格式，示例代码如下：

```
func main() {
    now := time.Now()                  //获取当前时间
    timestamp := now.Unix()            //时间戳
    timeObj := time.Unix(timestamp, 0) //将时间戳转为时间格式
    fmt.Println(timeObj)
    year := timeObj.Year()     //年
    month := timeObj.Month()   //月
    day := timeObj.Day()       //日
    hour := timeObj.Hour()     //小时
    minute := timeObj.Minute() //分钟
    second := timeObj.Second() //秒
    fmt.Printf("%d-%02d-%02d %02d:%02d:%02d\n", year, month, day, hour, minute, second)
}
```

结果：

```
2022-05-18 18:00:04 +0800 CST
2022-05-18 18:00:04
```

## 9.8、os包

Go语言的 os 包中提供了操作系统函数的接口，是一个比较重要的包。顾名思义，os 包的作用主要是在服务器上进行系统的基本操作，如文件操作、目录操作、执行命令、信号与中断、进程、系统状态等等。

### os 包中的常用函数

#### 1) Hostname

```
func Hostname() (name string, err error)
```

Hostname 函数会返回内核提供的主机名。

#### 2) Environ

```
func Environ() []string
```

Environ 函数会返回所有的环境变量，返回值格式为“key=value”的字符串的切片拷贝。

#### 3) Getenv

```
func Getenv(key string) string
```

Getenv 函数会检索并返回名为 key 的环境变量的值。如果不存在该环境变量则会返回空字符串。

#### 4) Setenv

```
func Setenv(key, value string) error
```

Setenv 函数可以设置名为 key 的环境变量，如果出错会返回该错误。

#### 5）Exit

```
func Exit(code int)
```

Exit 函数可以让当前程序以给出的状态码 code 退出。一般来说，状态码 0 表示成功，非 0 表示出错。程序会立刻终止，并且 defer 的函数不会被执行。

#### 6) Getuid

```
func Getuid() int
```

Getuid 函数可以返回调用者的用户 ID。

#### 7) Getgid

```
func Getgid() int
```

Getgid 函数可以返回调用者的组 ID。

#### 8) Getpid

```
func Getpid() int
```

Getpid 函数可以返回调用者所在进程的进程 ID。

#### 9) Getwd

```
func Getwd() (dir string, err error)
```

Getwd 函数可以返回一个对应当前工作目录的根路径。如果当前目录可以经过多条路径抵达（因为硬链接），Getwd 会返回其中一个。

#### 10) Mkdir

```
func Mkdir(name string, perm FileMode) error
```

Mkdir 函数可以使用指定的权限和名称创建一个目录。如果出错，会返回 \*PathError 底层类型的错误。

#### 11）MkdirAll

```
func MkdirAll(path string, perm FileMode) error
```

MkdirAll 函数可以使用指定的权限和名称创建一个目录，包括任何必要的上级目录，并返回 nil，否则返回错误。权限位 perm 会应用在每一个被该函数创建的目录上。如果 path 指定了一个已经存在的目录，MkdirAll 不做任何操作并返回 nil。

#### 12) Remove

```
func Remove(name string) error
```

Remove 函数会删除 name 指定的文件或目录。如果出错，会返回 \*PathError 底层类型的错误。  
RemoveAll 函数跟 Remove 用法一样，区别是会递归的删除所有子目录和文件。

在 os 包下，有 exec，signal，user 三个子包：

### os/exec 执行外部命令

exec 包可以执行外部命令，它包装了 os.StartProcess 函数以便更容易的修正输入和输出，使用管道连接 I/O，以及作其它的一些调整。

```
func LookPath(file string) (string, error)
```

在环境变量 PATH 指定的目录中搜索可执行文件，如果 file 中有斜杠，则只在当前目录搜索。返回完整路径或者相对于当前目录的一个相对路径。

例子：

```
import (
    "fmt"
    "os/exec"
)
func main() {
    f, err := exec.LookPath("main")
    if err != nil {
        fmt.Println(err)
    }
    fmt.Println(f)
}
```

结果：

```
exec: "main": executable file not found in $PATH
```

### os/user 获取当前用户信息

可以通过 os/user 包中的 Current() 函数来获取当前用户信息，该函数会返回一个 User 结构体，结构体中的 Username、Uid、HomeDir、Gid 分别表示当前用户的名称、用户 id、用户主目录和用户所属组 id，函数原型如下：

```
func Current() (*User, error)
```

例子：

```
import (
"log"
"os/user"
)

func main() {
u, _ := user.Current()
log.Println("用户名：", u.Username)
log.Println("用户id", u.Uid)
log.Println("用户主目录：", u.HomeDir)
log.Println("主组id：", u.Gid)
// 用户所在的所有的组的id
s, _ := u.GroupIds()
log.Println("用户所在的所有组：", s)
}
```

结果：

```
2022/05/18 20:06:46 用户名： peng.shi
2022/05/18 20:06:46 用户id 502
2022/05/18 20:06:46 用户主目录： /Users/peng.shi
2022/05/18 20:06:46 主组id： 20
2022/05/18 20:06:46 用户所在的所有组： [20 501 12 61 79 80 81 98 502 702 701 33 100 204 250 395 398 399 400]
```

### os/signal 信号处理

一个运行良好的程序在退出（正常退出或者强制退出，如 Ctrl+C，kill 等）时是可以执行一段清理代码的，将收尾工作做完后再真正退出。  
一般采用系统 Signal 来通知系统退出，如 kill pid，在程序中针对一些系统信号设置了处理函数，当收到信号后，会执行相关清理程序或通知各个子进程做自清理。

Go语言中对信号的处理主要使用 os/signal 包中的两个方法，一个是 Notify 方法用来监听收到的信号，一个是 stop 方法用来取消监听。

```
func Notify(c chan<- os.Signal, sig ...os.Signal)
```

其中，第一个参数表示接收信号的 channel，第二个及后面的参数表示设置要监听的信号，如果不设置表示监听所有的信号。

例子：使用 Notify 方法来监听收到的信号：

```
import (
"fmt"
"os"
"os/signal"
)

func main() {
c := make(chan os.Signal, 0)
signal.Notify(c)
// Block until a signal is received.
s := <-c
fmt.Println("Got signal:", s)
}
```

通过Ctrl+C, 或者在goland中点方块键终止程序，结果:

```
Got signal: interrupt
```

例子：使用 stop 方法来取消监听：

```
import (
    "fmt"
    "os"
    "os/signal"
)
func main() {
    c := make(chan os.Signal, 0)
    signal.Notify(c)
    signal.Stop(c) //不允许继续往c中存入内容
    s := <-c       //c无内容，此处阻塞，所以不会执行下面的语句，也就没有输出
    fmt.Println("Got signal:", s)
}
```

因为使用 Stop 方法取消了 Notify 方法的监听，所以运行程序没有输出结果。

## 9.9、flag包：命令行参数解析

在编写命令行程序（工具、server）时，我们有时需要对命令参数进行解析，各种编程语言一般都会提供解析命令行参数的方法或库，以方便程序员使用。在Go语言中的 flag 包中，提供了命令行参数解析的功能。

### flag 包概述

Go语言内置的 flag 包实现了命令行参数的解析，flag 包使得开发命令行工具更为简单。  
flag 包支持的命令行参数类型有 bool、int、int64、uint、uint64、float、float64、string、duration，如下表所示：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/88547d75c3a44c1a8cd7d37b5d8508a0.png)

### flag 包基本使用

有以下两种常用的定义命令行 flag 参数的方法：

#### 1) flag.Type()

```
flag.Type(flag 名, 默认值, 帮助信息) *Type
```

Type 可以是 Int、String、Bool 等，返回值为一个相应类型的指针，例如我们要定义姓名、年龄、婚否三个命令行参数，我们可以按如下方式定义：

```
name := flag.String("name", "张三", "姓名")
age := flag.Int("age", 18, "年龄")
married := flag.Bool("married", false, "婚否")
delay := flag.Duration("d", 0, "时间间隔")
```

#### 2) flag.TypeVar()

```
flag.TypeVar(Type 指针, flag 名, 默认值, 帮助信息)
```

TypeVar 可以是 IntVar、StringVar、BoolVar 等，其功能为将 flag 绑定到一个变量上，例如我们要定义姓名、年龄、婚否三个命令行参数，我们可以按如下方式定义：

```
var name string
var age int
var married bool
var delay time.Duration
flag.StringVar(&name, "name", "张三", "姓名")
flag.IntVar(&age, "age", 18, "年龄")
flag.BoolVar(&married, "married", false, "婚否")
flag.DurationVar(&delay, "d", 0, "时间间隔")
```

#### flag.Parse()

通过以上两种方法定义好命令行 flag 参数后，需要通过调用 flag.Parse() 来对命令行参数进行解析。

支持的命令行参数格式有以下几种：  
\-flag：只支持 bool 类型；  
\-flag=x；  
\-flag x：只支持非 bool 类型。

其中，布尔类型的参数必须使用等号的方式指定。

flag 包的其他函数：

```
lag.Args()  //返回命令行参数后的其他参数，以 []string 类型
flag.NArg()  //返回命令行参数后的其他参数个数
flag.NFlag() //返回使用的命令行参 数个数
```

例子：

```
import (
"flag"
"fmt"
)

var Input_pstrName = flag.String("name", "gerry", "input ur name")
var Input_piAge = flag.Int("age", 20, "input ur age")
var Input_flagvar int

func Init() {
flag.IntVar(&Input_flagvar, "flagname", 1234, "help message for flagname")
}
func main() {
Init()
flag.Parse()
// After parsing, the arguments after the flag are available as the slice flag.Args() or individually as flag.Arg(i). The arguments are indexed from 0 through flag.NArg()-1
// Args returns the non-flag command-line arguments
// NArg is the number of arguments remaining after flags have been processed
fmt.Printf("args=%s, num=%d\n", flag.Args(), flag.NArg())
for i := 0; i != flag.NArg(); i++ {
fmt.Printf("arg[%d]=%s\n", i, flag.Arg(i))
}
fmt.Println("name=", *Input_pstrName)
fmt.Println("age=", *Input_piAge)
fmt.Println("flagname=", Input_flagvar)
}
```

结果：

```
args=[], num=0
name= gerry
age= 20
flagname= 1234
```

## 9.10、go mod包依赖管理工具

最早的时候，Go语言所依赖的所有的第三方库都放在 GOPATH 这个目录下面，这就导致了同一个库只能保存一个版本的代码。如果不同的项目依赖同一个第三方的库的不同版本，应该怎么解决？

go module 是Go语言从 1.11 版本之后官方推出的版本管理工具，并且从 Go1.13 版本开始，go module 成为了Go语言默认的依赖管理工具。

Modules 官方定义为：  
Modules 是相关 Go 包的集合，是源代码交换和版本控制的单元。Go语言命令直接支持使用 Modules，包括记录和解析对其他模块的依赖性，Modules 替换旧的基于 GOPATH 的方法，来指定使用哪些源文件。

### 如何使用 Modules？

1.  首先需要把 golang 升级到 1.11 版本以上（现在 1.13 已经发布了，建议使用 1.13）。
2.  设置 GO111MODULE。

#### GO111MODULE

在Go语言 1.12 版本之前，要启用 go module 工具首先要设置环境变量 GO111MODULE，不过在Go语言 1.13 及以后的版本则不再需要设置环境变量。通过 GO111MODULE 可以开启或关闭 go module 工具。

```
GO111MODULE=off 禁用 go module，编译时会从 GOPATH 和 vendor 文件夹中查找包；
GO111MODULE=on 启用 go module，编译时会忽略 GOPATH 和 vendor 文件夹，只根据 go.mod下载依赖；
GO111MODULE=auto（默认值），当项目在 GOPATH/src 目录之外，并且项目根目录有 go.mod 文件时，开启 go module。
```

在开启 GO111MODULE 之后就可以使用 go module 工具了，也就是说在以后的开发中就没有必要在 GOPATH 中创建项目了，并且还能够很好的管理项目依赖的第三方包信息。

常用的go mod命令如下表所示：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4612635987f54a16991de595727b804a.png)

#### GOPROXY

proxy 顾名思义就是代理服务器的意思。大家都知道，国内的网络有防火墙的存在，这导致有些Go语言的第三方包我们无法直接通过go get命令获取。GOPROXY 是Go语言官方提供的一种通过中间代理商来为用户提供包下载服务的方式。要使用 GOPROXY 只需要设置环境变量 GOPROXY 即可。

目前公开的代理服务器的地址有：  
1）goproxy.io；  
2）goproxy.cn：（推荐）由国内的七牛云提供。

设置 GOPROXY 的命令为：  
Windows 下设置 GOPROXY 的命令为：

```
go env -w GOPROXY=https://goproxy.cn,direct
```

MacOS 或 Linux 下设置 GOPROXY 的命令为：

```
export GOPROXY=https://goproxy.cn
```

Go语言在 1.13 版本之后 GOPROXY 默认值为 https://proxy.golang.org，在国内可能会存在下载慢或者无法访问的情况，所以十分建议大家将 GOPROXY 设置为国内的 goproxy.cn。

#### 使用go get命令下载指定版本的依赖包

执行go get 命令，在下载依赖包的同时还可以指定依赖包的版本。  
1）运行go get -u命令会将项目中的包升级到最新的次要版本或者修订版本；  
2）运行go get -u=patch命令会将项目中的包升级到最新的修订版本；  
3）运行go get \[包名\]@\[版本号\]命令会下载对应包的指定版本或者将对应包升级到指定的版本

提示：go get \[包名\]@\[版本号\]命令中版本号可以是 x.y.z 的形式，例如 go get foo@v1.2.3，也可以是 git 上的分支或 tag，例如 go get foo@master，还可以是 git 提交时的哈希值，例如 go get foo@e3702bed2。

### 如何在项目中使用

例子：创建一个新项目：

1.  在 GOPATH 目录之外新建一个目录，并使用go mod init初始化生成 go.mod 文件。  
    go mod init hello  
    go: creating new go.mod: module hello

go.mod 文件一旦创建后，它的内容将会被 go toolchain 全面掌控，go toolchain 会在各类命令执行时，比如go get、go build、go mod等修改和维护 go.mod 文件。

go.mod 提供了 module、require、replace 和 exclude 四个命令：  
1）module 语句指定包的名字（路径）；  
2）require 语句指定的依赖项模块；  
3）replace 语句可以替换依赖项模块；  
4）exclude 语句可以忽略依赖项模块。

初始化生成的 go.mod 文件如下所示：

```
module hello

go 1.13
```

2.  添加依赖。

新建一个 main.go 文件，写入以下代码：

```
package main
import (
    "net/http"
    "github.com/labstack/echo"
)
func main() {
    e := echo.New()
    e.GET("/", func(c echo.Context) error {
        return c.String(http.StatusOK, "Hello, World!")
    })
    e.Logger.Fatal(e.Start(":1323"))
}
```

执行go run main.go运行代码会发现 go mod 会自动查找依赖自动下载：

```
go run main.go
go: finding github.com/labstack/echo v3.3.10+incompatible
go: downloading github.com/labstack/echo v3.3.10+incompatible
go: extracting github.com/labstack/echo v3.3.10+incompatible
go: finding github.com/labstack/gommon v0.3.0
......
go: finding golang.org/x/text v0.3.0

   ____    __
  / __/___/ /  ___
/ _// __/ _ \/ _ \
/___/\__/_//_/\___/ v3.3.10-dev
High performance, minimalist Go web framework
https://echo.labstack.com
____________________________________O/_______
                                                      O\
⇨ http server started on [::]:1323
```

现在查看 go.mod 内容：

```
module hello

go 1.13

require (
    github.com/labstack/echo v3.3.10+incompatible // indirect
    github.com/labstack/gommon v0.3.0 // indirect
    golang.org/x/crypto v0.0.0-20191206172530-e9b2fee46413 // indirect
)
```

go module 安装 package 的原则是先拉取最新的 release tag，若无 tag 则拉取最新的 commit，详见 Modules 官方介绍。

go 会自动生成一个 go.sum 文件来记录 dependency tree：

```
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/labstack/echo v3.3.10+incompatible h1:pGRcYk231ExFAyoAjAfD85kQzRJCRI8bbnE7CX5OEgg=
github.com/labstack/echo v3.3.10+incompatible/go.mod h1:0INS7j/VjnFxD4E2wkz67b8cVwCLbBmJyDaka6Cmk1s=
github.com/labstack/gommon v0.3.0 h1:JEeO0bvc78PKdyHxloTKiF8BD5iGrH8T6MSeGvSgob0=
github.com/labstack/gommon v0.3.0/go.mod h1:MULnywXg0yavhxWKc+lOruYdAhDwPK9wf0OL7NoOu+k=
github.com/mattn/go-colorable v0.1.2 h1:/bC9yWikZXAL9uJdulbSfyVNIR3n3trXl+v8+1sx8mU=
... 省略很多行
```

再次执行脚本go run main.go发现跳过了检查并安装依赖的步骤。

可以使用命令go list -m -u all来检查可以升级的 package，使用go get -u need-upgrade-package升级后会将新的依赖版本更新到 go.mod \* 也可以使用go get -u升级所有依赖。

## 十、并发

Go 语言通过编译器运行时（runtime），从语言上支持了并发的特性。

Go 语言的并发通过 goroutine 特性完成。goroutine 类似于线程，但是可以根据需要创建多个 goroutine 并发工作。goroutine 是由 Go 语言的运行时调度完成，而线程是由操作系统调度完成。

Go 语言还提供 channel 在多个 goroutine 间进行通信。goroutine 和 channel 是 Go 语言秉承的 CSP（Communicating Sequential Process）并发模式的重要实现基础。

## 10.1、并发简述

有人把Go语言比作 21 世纪的C语言，这是因为：  
1）Go语言设计简单  
2）21 世纪最重要的就是并发程序设计，而 Go 从语言层面就支持并发  
3）实现了自动垃圾回收机制

Go语言的并发机制运用起来非常简便，在启动并发的方式上直接添加了语言级的关键字就可以实现，和其他编程语言相比更加轻量。

### 并发/并行

并发：多线程程序在单核的 cpu 上运行  
并行：多线程程序在多核的 cpu 上运行

### 协程/线程

线程：一个线程上可以跑多个协程，协程是轻量级的线程  
协程：拥有独立的栈空间，共享堆空间，调度由用户自己控制，本质上类似于用户级线程，这些用户级线程的调度也是由自己实现的。

### goroutine协程

goroutine 是一种轻量级的线程，可在单个进程里执行成并发任务，它是Go语言并发设计的核心。  
说到底 goroutine 其实就是线程，但是它比线程更小，十几个 goroutine 可能体现在底层就是五六个线程，而且Go语言内部也实现了 goroutine 之间的内存共享。

使用 go 关键字就可以创建 goroutine：将 go 声明放到一个需调用的函数之前运行这个函数，即可启动一个协程。

goroutine 的用法如下：

```
//go 关键字放在方法调用前新建一个 goroutine
go GetThingDone(param1, param2);

//新建一个匿名方法并执行
go func(param1, param2) {
}(val1, val2)

//直接新建一个 goroutine 并在 goroutine 中执行代码块
go {
    //do someting...
}
```

因为 goroutine 在多核 cpu 环境下是并行的，如果代码块在多个 goroutine 中执行，那么我们就实现了代码的并行。  
如果需要了解程序的执行情况，怎么拿到并行的结果呢？需要配合使用channel进行。

### channel

channel 是Go语言在语言级别提供的 goroutine 间的通信方式。我们可以使用 channel 在两个或多个 goroutine 之间传递消息。

channel 是类型相关的，一个 channel 只能传递一种类型的值，这个类型需要在声明 channel 时指定。可以将其认为是一种类型安全的管道。

#### 创建channel

定义一个 channel 时，也需要定义发送到 channel 的值的类型，注意，必须使用 make 创建 channel：

```
ci := make(chan int)
cs := make(chan string)
cf := make(chan interface{})
```

## 10.2、goroutine（轻量级线程）

goroutine 是 Go语言中的轻量级线程实现，由 Go 运行时（runtime）管理。Go 程序会智能地将 goroutine 中的任务合理地分配给每个 CPU。

Go 程序从 main 包的 main() 函数开始，在程序启动时，Go 程序就会为 main() 函数创建一个默认的 goroutine。

### 使用普通函数创建 goroutine

Go 程序中使用 go 关键字为一个函数创建一个 goroutine。一个函数可以被创建多个 goroutine，一个 goroutine 必定对应一个函数。  
为一个普通函数创建 goroutine 的写法如下：

```
go 函数名( 参数列表 )
```

使用 go 关键字创建 goroutine 时，被调用函数的返回值会被忽略。  
如果需要在 goroutine 中返回数据，需要通过channel把数据从 goroutine 中作为返回值传出。

goroutine例子：

```
import (
"fmt"
"time"
)

func running() {
var times int
// 构建一个无限循环
for {
times++
fmt.Println("tick", times)
// 延时1秒
time.Sleep(time.Second)
}
}
func main() {
// 并发执行程序
go running()

// 循环
var times int
// 构建一个无限循环
for {
times++
fmt.Println("main", times)
// 延时1秒
time.Sleep(time.Second)
}
}
```

结果：

```
main 1
tick 1
main 2
tick 2
main 3
tick 3
main 4
tick 4
...
```

### 使用匿名函数创建goroutine

go 关键字后也可以为匿名函数或闭包启动 goroutine。

```
go func( 参数列表 ){
    函数体
}( 调用参数列表 )
```

其中：  
1）参数列表：函数体内的参数变量列表。  
2）函数体：匿名函数的代码。  
3）调用参数列表：启动 goroutine 时，需要向匿名函数传递的调用参数。

例子：

```
func main() {
go func() {
var times int
for {
times++
fmt.Println("tick", times)
time.Sleep(time.Second)
}
}()

var times int
for {
times++
fmt.Println("main", times)
time.Sleep(time.Second)
}
}
```

结果：

```
main 1
tick 1
main 2
tick 2
main 3
tick 3
main 4
tick 4
...
```

所有 goroutine 在 main() 函数结束时会一同结束。

goroutine 虽然类似于线程概念，但是从调度性能上没有线程细致，而细致程度取决于 Go 程序的 goroutine 调度器的实现和运行环境。

## 10.3、并发通信

并发时线程的通信由两种方式：共享数据和消息  
共享数据是指多个并发单元分别保持对同一个数据的引用，被共享的数据可以放在内存、磁盘、网络等，最常见是放在内存中。

Go语言实现的通过共享数据方式：

```
import (
"fmt"
"runtime"
"sync"
)

var counter int = 0

func Count(lock *sync.Mutex) {
lock.Lock()
counter++
fmt.Println(counter)
lock.Unlock()
}
func main() {
lock := &sync.Mutex{}
for i := 0; i < 10; i++ {
go Count(lock)
}
for {
lock.Lock()
c := counter
lock.Unlock()

// 相当于java的yield，让出cpu给其他线程执行
runtime.Gosched()
if c >= 10 {
break
}
}
}
```

结果：

```
1
2
3
4
5
6
7
8
9
10
```

可以看出，共享数据的方式，需要在代码中加入互斥锁，代码比较繁琐。

所以Go语言推荐另一种通信模型：消息。  
通过消息来实现goroutine间的通信。

## 10.4、共享资源

如果两个或者多个 goroutine 在没有相互同步的情况下，访问某个共享的资源，比如同时对该资源进行读写时，会涉及到资源竞争。

为了保证线程安全，我们对于同一个资源的读写必须是原子的，也就是说，同一时间只能允许有一个 goroutine 对共享资源进行读写操作。

### 锁住共享资源：：原子函数或互斥锁

Go语言提供了传统的同步 goroutine 的机制，就是对共享资源加锁。  
atomic 和 sync 包里的一些函数就可以对共享的资源进行加锁操作。

#### 原子函数

原子函数能够以底层的加锁机制来同步访问整型变量和指针

```
var (
counter int64
wg      sync.WaitGroup
)

func main() {
wg.Add(2)
go incCounter(1)
go incCounter(2)
wg.Wait() //等待goroutine结束
fmt.Println(counter)
}
func incCounter(id int) {
defer wg.Done()
for count := 0; count < id; count++ {
atomic.AddInt64(&counter, 1) //安全的对counter加1
runtime.Gosched()
}
}
```

结果：3

上述代码中使用了 atmoic 包的 AddInt64 函数，这个函数会同步整型值的加法，方法是强制同一时刻只能有一个 gorountie 运行并完成这个加法操作。当 goroutine 试图去调用任何原子函数时，这些 goroutine 都会自动根据所引用的变量做同步处理。

另外两个有用的原子函数是 LoadInt64 和 StoreInt64。这两个函数提供了一种安全地读和写一个整型值的方式。下面是代码就使用了 LoadInt64 和 StoreInt64 函数来创建一个同步标志，这个标志可以向程序里多个 goroutine 通知某个特殊状态。  
例子：

```
import (
"fmt"
"sync"
"sync/atomic"
"time"
)

var (
shutdown int64
wg       sync.WaitGroup
)

func main() {
wg.Add(2)
go doWork("A")
go doWork("B")
time.Sleep(1 * time.Second)
fmt.Println("Shutdown Now")
atomic.StoreInt64(&shutdown, 1)
wg.Wait()
}
func doWork(name string) {
defer wg.Done()
for {
fmt.Printf("Doing %s Work\n", name)
time.Sleep(250 * time.Millisecond)
if atomic.LoadInt64(&shutdown) == 1 {
fmt.Printf("Shutting %s Down\n", name)
break
}
}
}
```

结果：

```
Doing B Work
Doing A Work
Doing A Work
Doing B Work
Doing B Work
Doing A Work
Doing A Work
Doing B Work
Shutdown Now
Shutting A Down
Shutting B Down

```

#### 互斥锁

另一种同步访问共享资源的方式是使用互斥锁。互斥锁用于在代码上创建一个临界区，保证同一时间只有一个 goroutine 可以执行这个临界代码。

```
var (
    counter int64
    wg      sync.WaitGroup
    mutex   sync.Mutex
)
func main() {
    wg.Add(2)
    go incCounter(1)
    go incCounter(2)
    wg.Wait()
    fmt.Println(counter)
}
func incCounter(id int) {
    defer wg.Done()
    for count := 0; count < 2; count++ {
        //同一时刻只允许一个goroutine进入这个临界区
        mutex.Lock()
        {
            value := counter
            runtime.Gosched()
            value++
            counter = value
        }
        mutex.Unlock() //释放锁，允许其他正在等待的goroutine进入临界区
    }
}
```

结果：4

## 10.5、通道channel – goroutine之间通信的管道

channel 是一个通信机制，它可以让一个 goroutine 通过它给另一个 goroutine 发送值信息。  
每个 channel 都有一个的类型，也就是 channels 可发送数据的类型。一个可以发送 int 类型数据的 channel 一般写为 chan int。

Go语言提倡使用通信的方法代替共享内存，当一个资源需要在 goroutine 之间共享时，通道在 goroutine 之间架起了一个管道，并提供了确保同步交换数据的机制。

声明通道时，需要指定将要被共享的数据的类型。  
channel类似于队列的方式，总是遵循先入先出（First In First Out）的规则，保证收发数据的顺序。

### 声明通道类型

```
var 通道变量 chan 通道类型
```

chan 类型的空值是 nil，声明后需要配合 make 后才能使用。

### 创建通道

通道是引用类型，需要使用 make 进行创建，格式如下：

```
通道实例 := make(chan 数据类型)
```

例子：

```
ch1 := make(chan int)                 // 创建一个整型类型的通道
ch2 := make(chan interface{})         // 创建一个空接口类型的通道, 可以存放任意格式
type Equip struct{ /* 一些字段 */ }
ch2 := make(chan *Equip)             // 创建Equip指针类型的通道, 可以存放*Equip
```

### 使用通道发送数据

通道创建后，就可以使用通道进行发送和接收操作。

#### 1) 通道发送数据的格式

```
通道变量 <- 值
```

#### 2) 通过通道发送数据的例子

```
// 创建一个空接口通道
ch := make(chan interface{})
// 将0放入通道中
ch <- 0
// 将hello字符串放入通道中
ch <- "hello"
```

#### 3) 发送将持续阻塞直到数据被接收

把数据往通道中发送时，如果接收方一直都没有接收，那么发送操作将持续阻塞。Go 程序运行时能智能地发现一些永远无法发送成功的语句并做出提示，代码如下：

```
func main() {
    // 创建一个整型通道
    ch := make(chan int)
    // 尝试将0通过通道发送
    ch <- 0
}
```

结果：

```
fatal error: all goroutines are asleep - deadlock!
```

报错的意思是：运行时发现所有的 goroutine（包括main）都处于等待 goroutine。也就是说所有 goroutine 中的 channel 并没有形成发送和接收对应的代码。

### 使用通道接收数据

通道的数据接收一共有以下 4 种写法。

#### 1) 阻塞接收数据

```
data := <-ch
```

执行该语句时将会阻塞，直到接收到数据并赋值给 data 变量。

#### 2) 非阻塞接收数据

```
data, ok := <-ch
```

data：表示接收到的数据。未接收到数据时，data 为通道类型的零值。  
ok：表示是否接收到数据。

非阻塞的通道接收方法可能造成高的 CPU 占用，因此使用非常少

#### 3) 接收任意数据，忽略接收的数据

```
<-ch
```

执行该语句时将会发生阻塞，直到接收到数据，但接收到的数据会被忽略。

例子：

```
func main() {
// 构建一个通道
ch := make(chan int)
// 开启一个并发匿名函数
go func() {
fmt.Println("start goroutine")
// 通过通道通知main的goroutine
ch <- 0
fmt.Println("exit goroutine")
}()
fmt.Println("wait goroutine")
// 等待匿名goroutine
<-ch
fmt.Println("all done")
}
```

结果：

```
wait goroutine
start goroutine
exit goroutine
all done
```

#### 4) 循环接收

通道的数据接收可以借用 for range 语句进行多个元素的接收操作，格式如下：

```
for data := range ch {
}
```

例子：

```
func main() {
// 构建一个通道
ch := make(chan int)
// 开启一个并发匿名函数
go func() {
// 从3循环到0
for i := 3; i >= 0; i-- {
// 发送3到0之间的数值
ch <- i
// 每次发送完时等待
time.Sleep(time.Second)
}
}()
// 遍历接收通道数据
for data := range ch {
// 打印通道数据
fmt.Println(data)
// 当遇到数据0时, 退出接收循环
if data == 0 {
break
}
}
}
```

结果：

```
3
2
1
0
```

## 10.6、单向通道

我们在将一个 channel 变量传递到一个函数时，可以通过将其指定为单向 channel 变量，比如只能往这个 channel 中写入数据，或者只能从这个 channel 读取数据。

单向 channel 变量的声明：只能写入数据的通道类型为chan<-，只能读取数据的通道类型为<-chan：

```
var 通道实例 chan<- 元素类型    // 只能写入数据的通道
var 通道实例 <-chan 元素类型    // 只能读取数据的通道
```

例子：

```
ch := make(chan int)
// 声明一个只能写入数据的通道类型, 并赋值为ch
var chSendOnly chan<- int = ch
//声明一个只能读取数据的通道类型, 并赋值为ch
var chRecvOnly <-chan int = ch
```

当然，使用 make 创建通道时，也可以创建一个只写入或只读取的通道：

```
ch := make(<-chan int)
var chReadOnly <-chan int = ch
<-chReadOnly
```

### 关闭 channel

```
close(ch)
```

这样看一个channel是否被关闭：

```
x, ok := <-ch
```

通过第二个返回bool值来看

## 10.7、无缓冲的通道 & 带缓冲的通道

Go语言中无缓冲的通道（unbuffered channel）是指在接收前没有能力保存任何值的通道。  
这种类型的通道要求发送 goroutine 和接收 goroutine 同时准备好，才能完成发送和接收操作。

有缓冲的通道（buffered channel）是一种在被接收前能存储一个或者多个值的通道。这种类型的通道并不强制要求 goroutine 之间必须同时完成发送和接收。  
只有在通道中没有要接收的值时，接收动作才会阻塞。只有在通道没有可用缓冲区容纳被发送的值时，发送动作才会阻塞。

有缓冲的通道和无缓冲的通道之间的一个很大的不同：  
无缓冲的通道保证进行发送和接收的 goroutine 会在同一时间进行数据交换；有缓冲的通道没有这种保证。

### 创建带缓冲通道

```
通道实例 := make(chan 通道类型, 缓冲大小)
```

带缓冲通道的例子：

```
func main() {
    // 创建一个3个元素缓冲大小的整型通道
    ch := make(chan int, 3)
    // 查看当前通道的大小
    fmt.Println(len(ch))
    // 发送3个整型元素到通道
    ch <- 1
    ch <- 2
    ch <- 3
    // 查看当前通道的大小
    fmt.Println(len(ch))
}
```

结果：

```
0
3
```

## 10.8、channel超时机制

可以用select来实现channel的超时结束机制：

```
func main() {
ch := make(chan int)
quit := make(chan bool)
//新开一个协程
go func() {
for {
select {
case num := <-ch:
fmt.Println("num = ", num)
case <-time.After(3 * time.Second):
fmt.Println("超时")
quit <- true
}
}
}() //别忘了()
for i := 0; i < 5; i++ {
ch <- i
time.Sleep(time.Second)
}
<-quit
fmt.Println("程序结束")
}
```

结果：

```
num =  0
num =  1
num =  2
num =  3
num =  4
超时
程序结束
```

## 10.9、等待组（sync.WaitGroup）

Go语言中除了可以使用通道（channel）和互斥锁进行两个并发程序间的同步外，还可以使用等待组进行多个任务的同步，**等待组可以保证在并发环境中完成指定数量的任务**

在 sync.WaitGroup（等待组）类型中，每个 sync.WaitGroup 值在内部维护着一个计数，此计数的初始默认值为零。

等待组的方法：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/5972cddcf66b435d98dba0ec4689da46.png)  
对于一个可寻址的 sync.WaitGroup 值 wg：  
1）我们可以使用方法调用 wg.Add(delta) 来改变值 wg 维护的计数。  
2）方法调用 wg.Done() 和 wg.Add(-1) 是完全等价的。  
3）如果一个 wg.Add(delta) 或者 wg.Done() 调用将 wg 维护的计数更改成一个负数，一个恐慌将产生。  
4）当一个协程调用了 wg.Wait() 时，  
<1> 如果此时 wg 维护的计数为零，则此 wg.Wait() 此操作为一个空操作（noop）；  
<2> 否则（计数为一个正整数），此协程将进入阻塞状态。当以后其它某个协程将此计数更改至 0 时（一般通过调用 wg.Done()），此协程将重新进入运行状态（即 wg.Wait() 将返回）。

例子：

```
import (
"fmt"
"net/http"
"sync"
)

func main() {
// 声明一个等待组
var wg sync.WaitGroup
// 准备一系列的网站地址
var urls = []string{
"http://www.github.com/",
"https://www.qiniu.com/",
"https://www.golangtc.com/",
}
// 遍历这些地址
for _, url := range urls {
// 每一个任务开始时, 将等待组增加1
wg.Add(1)
// 开启一个并发
go func(url string) {
// 使用defer, 表示函数完成时将等待组值减1
defer wg.Done()
// 使用http访问提供的地址
_, err := http.Get(url)
// 访问完成后, 打印地址和可能发生的错误
fmt.Println(url, err)
// 通过参数传递url地址
}(url)
}
// 等待所有的任务完成
wg.Wait()
fmt.Println("over")
}
```

结果：

```
https://www.qiniu.com/ <nil>
http://www.github.com/ <nil>
https://www.golangtc.com/ <nil>
over
```

## 十一、文件处理

## 11.1、JSON文件读写

写Json文件的demo：

```
import (
"encoding/json"
"fmt"
"os"
)

type Website struct {
Name   string `xml:"name,attr"`
Url    string
Course []string
}

func main() {
info := []Website{{"Golang", "http://c.biancheng.net/golang/", []string{"http://c.biancheng.net/cplus/", "http://c.biancheng.net/linux_tutorial/"}}, {"Java", "http://c.biancheng.net/java/", []string{"http://c.biancheng.net/socket/", "http://c.biancheng.net/python/"}}}
// 创建文件
filePtr, err := os.Create("info.json")
if err != nil {
fmt.Println("文件创建失败", err.Error())
return
}
defer filePtr.Close()
// 创建Json编码器
encoder := json.NewEncoder(filePtr)
err = encoder.Encode(info)
if err != nil {
fmt.Println("编码错误", err.Error())
} else {
fmt.Println("编码成功")
}
}
```

运行后，会生成一个json文件，内容为：

```
[{"Name":"Golang","Url":"http://c.biancheng.net/golang/","Course":["http://c.biancheng.net/cplus/","http://c.biancheng.net/linux_tutorial/"]},{"Name":"Java","Url":"http://c.biancheng.net/java/","Course":["http://c.biancheng.net/socket/","http://c.biancheng.net/python/"]}]
```

读json文件：

```
import (
"encoding/json"
"fmt"
"os"
)

type Website struct {
Name   string `xml:"name,attr"`
Url    string
Course []string
}

func main() {
filePtr, err := os.Open("./info.json")
if err != nil {
fmt.Println("文件打开失败 [Err:%s]", err.Error())
return
}
defer filePtr.Close()
var info []Website
// 创建json解码器
decoder := json.NewDecoder(filePtr)
err = decoder.Decode(&info)
if err != nil {
fmt.Println("解码失败", err.Error())
} else {
fmt.Println("解码成功")
fmt.Println(info)
}
}
```

结果：

```
解码成功
[{Golang http://c.biancheng.net/golang/ [http://c.biancheng.net/cplus/ http://c.biancheng.net/linux_tutorial/]} {Java http://c.biancheng.net/java/ [http://c.biancheng.net/socket/ http://c.biancheng.net/python/]}]
```

## 11.2、XML文件的读写

1、写XML文件：

```
import (
"encoding/xml"
"fmt"
"os"
)

type Website struct {
Name   string `xml:"name,attr"`
Url    string
Course []string
}

func main() {
//实例化对象
info := Website{"Go语言学习", "http://c.biancheng.net/golang/", []string{"Go语言入门教程", "Golang入门教程"}}
f, err := os.Create("./info.xml")
if err != nil {
fmt.Println("文件创建失败", err.Error())
return
}
defer f.Close()
//序列化到文件中
encoder := xml.NewEncoder(f)
err = encoder.Encode(info)
if err != nil {
fmt.Println("编码错误：", err.Error())
return
} else {
fmt.Println("编码成功")
}
}
```

结果：

```
编码成功
```

生成了info.xml，内容为：

```
<Website name="Go语言学习"><Url>http://c.biancheng.net/golang/</Url><Course>Go语言入门教程</Course><Course>Golang入门教程</Course></Website>% 
```

2、读xml文件

```
import (
"encoding/xml"
"fmt"
"os"
)

type Website struct {
Name   string `xml:"name,attr"`
Url    string
Course []string
}

func main() {
//打开xml文件
file, err := os.Open("./info.xml")
if err != nil {
fmt.Printf("文件打开失败：%v", err)
return
}
defer file.Close()
info := Website{}
//创建 xml 解码器
decoder := xml.NewDecoder(file)
err = decoder.Decode(&info)
if err != nil {
fmt.Printf("解码失败：%v", err)
return
} else {
fmt.Println("解码成功")
fmt.Println(info)
}
}
```

结果：

```
解码成功
{Go语言学习 http://c.biancheng.net/golang/ [Go语言入门教程 Golang入门教程]}
```

## 11.3、纯文本文件的读写

1、写文本文件

```
import (
    "bufio"
    "fmt"
    "os"
)
func main() {
    //创建一个新文件，写入内容
    filePath := "./output.txt"
    file, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE, 0666)
    if err != nil {
        fmt.Printf("打开文件错误= %v \n", err)
        return
    }
    //及时关闭
    defer file.Close()
    //写入内容
    str := "http://c.biancheng.net/golang/\n" // \n\r表示换行  txt文件要看到换行效果要用 \r\n
    //写入时，使用带缓存的 *Writer
    writer := bufio.NewWriter(file)
    for i := 0; i < 3; i++ {
        writer.WriteString(str)
    }
    //因为 writer 是带缓存的，因此在调用 WriterString 方法时，内容是先写入缓存的
    //所以要调用 flush方法，将缓存的数据真正写入到文件中。
    writer.Flush()
}
```

结果：生成了output.txt, 内容为：

```
http://c.biancheng.net/golang/
http://c.biancheng.net/golang/
http://c.biancheng.net/golang/
```

2、读文本文件

```
import (
    "bufio"
    "fmt"
    "io"
    "os"
)
func main() {
    //打开文件
    file, err := os.Open("./output.txt")
    if err != nil {
        fmt.Println("文件打开失败 = ", err)
    }
    //及时关闭 file 句柄，否则会有内存泄漏
    defer file.Close()
    //创建一个 *Reader ， 是带缓冲的
    reader := bufio.NewReader(file)
    for {
        str, err := reader.ReadString('\n') //读到一个换行就结束
        if err == io.EOF {                  //io.EOF 表示文件的末尾
            break
        }
        fmt.Print(str)
    }
    fmt.Println("文件读取结束...")
}
```

结果：

```
http://c.biancheng.net/golang/
http://c.biancheng.net/golang/
http://c.biancheng.net/golang/
文件读取结束...
```

## 11.4、文件的写入、追加、读取、复制操作

Go语言的 os 包下有一个 OpenFile 函数：

```
func OpenFile(name string, flag int, perm FileMode) (file *File, err error)
```

其中 name 是文件的文件名，如果不是在当前路径下运行需要加上具体路径；flag 是文件的处理参数，为 int 类型，根据系统的不同具体值可能有所不同，但是作用是相同的。

flag 文件处理参数：  
O\_RDONLY：只读模式打开文件；  
O\_WRONLY：只写模式打开文件；  
O\_RDWR：读写模式打开文件；  
O\_APPEND：写操作时将数据附加到文件尾部（追加）；  
O\_CREATE：如果不存在将创建一个新文件；  
O\_EXCL：和 O\_CREATE 配合使用，文件必须不存在，否则返回一个错误；  
O\_SYNC：当进行一系列写操作时，每次都要等待上次的 I/O 操作完成再进行；  
O\_TRUNC：如果可能，在打开时清空文件。

## 十二、编译和工具链

Go 语言的工具链非常丰富，从获取源码、编译、文档、测试、性能分析，到源码格式化、源码提示、重构工具等应有尽有。

在 Go 语言中可以使用测试框架编写单元测试，使用统一的命令行即可测试及输出测试报告。  
基准测试提供可自定义的计时器和一套基准测试算法，能方便快速地分析一段代码可能存在的 CPU 耗用和内存分配问题。  
性能分析工具可以将程序的 CPU 耗用、内存分配、竞态问题以图形化方式展现出来。

## 12.1、go build命令（go语言编译命令）

Go语言的编译速度非常快。Go 1.9 版本后默认利用Go语言的并发特性进行函数粒度的并发编译。  
Go语言的程序编写基本以源码方式，无论是自己的代码还是第三方代码，并且以 GOPATH 作为工作目录和一套完整的工程目录规则。  
因此Go语言中日常编译时无须像 C++ 一样配置各种包含路径、链接库地址等。

Go语言中使用 go build 命令主要用于编译代码。在包的编译过程中，若有必要，会同时编译与之相关联的包。

go build 有很多种编译方法，如无参数编译、文件列表编译、指定包编译等，使用这些方法都可以输出可执行文件。

### go build 无参数编译

如果源码中没有依赖 GOPATH 的包引用，那么源码可以使用无参数 go build。格式如下：

```
go build
```

### go build+文件列表

编译同目录的多个源码文件时，可以在 go build 的后面提供多个文件名，go build 会编译这些源码，输出可执行文件，“go build+文件列表”的格式如下：

```
go build file1.go file2.go……
```

### go build+包

“go build+包”在设置 GOPATH 后，可以直接根据包名进行编译，即便包内文件被增（加）删（除）也不影响编译指令。

```
go build -o main chapter11/goinstall
```

其中，-o main是指定输出文件为main, 后面跟要编译的包名 chapter11/goinstall

### go build 编译时的附加参数

go build 还有一些附加参数，可以显示更多的编译信息和更多的操作：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c09e8d175f0a46c081eeba13cf791eca.png)

## 12.2、go clean命令

go clean命令就像 Java 中的maven clean命令一样，会清除掉编译过程中产生的一些文件。

Go语言中go clean命令可以移除当前源码包和关联源码包里面编译生成的文件，这些文件包括以下几种：  
1）执行go build命令时在当前目录下生成的与包名或者 Go 源码文件同名的可执行文件。在 Windows 下，则是与包名或者 Go 源码文件同名且带有“.exe”后缀的文件。  
2）执行go test命令并加入-c标记时在当前目录下生成的以包名加“.test”后缀为名的文件。在 Windows 下，则是以包名加“.test.exe”后缀的文件。  
3）执行go install命令安装当前代码包时产生的结果文件。如果当前代码包中只包含库源码文件，则结果文件指的就是在工作区 pkg 目录下相应的归档文件。如果当前代码包中只包含一个命令源码文件，则结果文件指的就是在工作区 bin 目录下的可执行文件。  
4）在编译 Go 或 C 源码文件时遗留在相应目录中的文件或目录 。包括：“\_obj”和“\_test”目录，名称为“\_testmain.go”、“test.out”、“build.out”或“a.out”的文件，名称以“.5”、“.6”、“.8”、“.a”、“.o”或“.so”为后缀的文件。这些目录和文件是在执行go build命令时生成在临时目录中的。

通过上面的示例可以看出，go clean命令还可以指定一些参数。对应的参数的含义如下所示：  
\-i 清除关联的安装的包和可运行文件，也就是通过go install安装的文件；  
\-n 把需要执行的清除命令打印出来，但是不执行，这样就可以很容易的知道底层是如何运行的；  
\-r 循环的清除在 import 中引入的包；  
\-x 打印出来执行的详细命令，其实就是 -n 打印的执行版本；  
\-cache 删除所有go build命令的缓存  
\-testcache 删除当前包所有的测试结果

## 12.3、go run命令——编译并运行