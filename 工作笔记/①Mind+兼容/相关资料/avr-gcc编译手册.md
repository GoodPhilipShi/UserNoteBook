> 调整一下参数后，运行脚本就可以了

```shell
#!/bin/bash

# http://www.nongnu.org/avr-libc/user-manual/install_tools.html

# 为了获得最佳编译时间，这通常应设置为您的机器具有的 CPU 内核数
JOBCOUNT=$(getconf _NPROCESSORS_ONLN)

# 为 Linux 构建
# 构建 Windows 工具链需要 Linux AVR-GCC 工具链
# 如果 Linux 工具链已经构建，那么你可以将它设置为 0
FOR_LINUX=1

# 为 32 位 Windows 构建
FOR_WINX86=0

# 为 32 位 Windows 构建
FOR_WINX64=0


# --------- 编译选项 ----------

# 为选定的操作系统构建 Binutils
BUILD_BINUTILS=1

# 为选定的操作系统构建 GCC（需要 AVR-Binutils）
BUILD_GCC=1

# 为选定的操作系统构建 GDB
BUILD_GDB=1

# 构建 AVR-LibC（需要 AVR-GCC）
BUILD_LIBC=1

# 构建 AVRDUDE
BUILD_AVRDUDE=1

# 构建 SIMULAVR
#todo 这个目前存在问题....
BUILD_SIMULAVR=0

NAME_BINUTILS="binutils-2.36.1"
NAME_GCC="gcc-11.1.0"
NAME_GDB="gdb-10.2"
NAME_LIBC="avr-libc3.git" # https://github.com/stevenj/avr-libc3
COMMIT_LIBC="d09c2a61764aced3274b6dde4399e11b0aee4a87"
NAME_AVRDUDE="avrdude-6.3"
NAME_SIMULAVR="simulavr" # https://github.com/Traumflug/simulavr

# 构建工具链的输出位置
BASE=`pwd`/
PREFIX_GCC_LINUX=${BASE}avr-${NAME_GCC}-linux
PREFIX_GCC_WINX86=${BASE}avr-${NAME_GCC}-x86-windows
PREFIX_GCC_WINX64=${BASE}avr-${NAME_GCC}-x64-windows
PREFIX_LIBC=${BASE}avr-libc # The contents of the avr-libc directory will need to be copied/merged with each of the target toolchain directories

HOST_WINX86="i686-w64-mingw32"
HOST_WINX64="x86_64-w64-mingw32"

OPTS_BINUTILS="
	--target=avr
	--disable-nls
	--disable-werror
"

OPTS_GCC="
	--target=avr
	--enable-languages=c,c++
	--disable-nls
	--disable-libssp
	--disable-libada
	--with-dwarf2
	--disable-shared
	--enable-static
	--enable-mingw-wildcard
	--enable-plugin
	--with-gnu-as
"

OPTS_GDB="
	--target=avr
	--with-static-standard-libraries
"

OPTS_AVRDUDE=""

OPTS_LIBC=""

# 安装包
if hash apt-get 2>/dev/null; then
	# 这适用于 Debian 8 和 Ubuntu 16.04
	apt-get install wget make mingw-w64 gcc g++ bzip2 git autoconf texinfo
elif hash yum 2>/dev/null; then
	# 这适用于 CentOS 7
	yum install wget git texinfo
	rpm -q epel-release-7-6.noarch >/dev/null
	if [ $? -ne 0 ]; then
		# EPEL 适用于 MinGW 的东西
		rm -f epel-release-7-6.noarch.rpm
		wget https://www.mirrorservice.org/sites/dl.fedoraproject.org/pub/epel//7/x86_64/e/epel-release-7-6.noarch.rpm
		rpm -Uvh epel-release-7-6.noarch.rpm
	fi
	yum install make mingw64-gcc mingw64-gcc-c++ mingw32-gcc mingw32-gcc-c++ gcc gcc-c++ bzip2 autoconf
elif hash pacman 2>/dev/null; then
	# Arch 的情况发生了变化，现在它被打破了 :/
	pacman -S --needed wget make mingw-w64-binutils mingw-w64-gcc mingw-w64-crt mingw-w64-headers mingw-w64-winpthreads gcc bzip2 git autoconf texinfo
fi

# 停止错误
set -e

TIME_START=$(date +%s)

makeDir()
{
	rm -rf "$1/"
	mkdir -p "$1"
}

fixGCCAVR()
{
	# In GCC 7.1.0 there seems to be an issue with INT8_MAX and some other things being undefined in /gcc/config/avr/avr.c when building for Windows.
	# Adding '#include <stdint.h>' doesn't fix it, but manually defining the values does the trick.

	echo "修复缺少的定义(defines)..."

	DEFSFIX="
		#if (defined _WIN32 || defined __CYGWIN__)
		#define INT8_MIN (-128)
		#define INT16_MIN (-32768)
		#define INT8_MAX 127
		#define INT16_MAX 32767
		#define UINT8_MAX 0xff
		#define UINT16_MAX 0xffff
		#endif
	"

	ORIGINAL=$(cat ../gcc/config/avr/avr.c)
	echo "$DEFSFIX" > ../gcc/config/avr/avr.c
	echo "$ORIGINAL" >> ../gcc/config/avr/avr.c
}

echo "清除输出目录..."
[ $FOR_LINUX -eq 1 ] && makeDir "$PREFIX_GCC_LINUX"
[ $FOR_WINX86 -eq 1 ] && makeDir "$PREFIX_GCC_WINX86"
[ $FOR_WINX64 -eq 1 ] && makeDir "$PREFIX_GCC_WINX64"
[ $BUILD_LIBC -eq 1 ] && makeDir "$PREFIX_LIBC"

echo "清除以前的下载..."
rm -f $NAME_BINUTILS.tar.xz
rm -rf $NAME_BINUTILS/
rm -f $NAME_GCC.tar.xz
rm -rf $NAME_GCC/
rm -f $NAME_GDB.tar.xz
rm -rf $NAME_GDB/
rm -f $NAME_LIBC.tar.bz2
rm -rf $NAME_LIBC/
rm -rf $NAME_AVRDUDE.tar.gz
rm -rf $NAME_AVRDUDE/

echo "下载源代码..."
[ $BUILD_BINUTILS -eq 1 ] && wget https://mirrors.ustc.edu.cn/gnu/binutils/$NAME_BINUTILS.tar.xz
[ $BUILD_GCC -eq 1 ] && wget https://mirrors.ustc.edu.cn/gnu/gcc/$NAME_GCC/$NAME_GCC.tar.xz
[ $BUILD_GDB -eq 1 ] && wget https://mirrors.ustc.edu.cn/gnu/gdb/$NAME_GDB.tar.xz
[ $BUILD_AVRDUDE -eq 1 ] && wget https://mirrors.ustc.edu.cn/gnu/gdb/$NAME_AVRDUDE.tar.gz
if [ $BUILD_LIBC -eq 1 ]; then
	if [ "$NAME_LIBC" = "avr-libc3.git" ]; then
		git clone https://github.com/stevenj/$NAME_LIBC "$NAME_LIBC"
	else
		wget http://download.savannah.gnu.org/releases/avr-libc/$NAME_LIBC.tar.bz2
	fi
fi

PATH="$PREFIX_GCC_LINUX"/bin:"$PATH"
export PATH

CC=""
export CC

confMake()
{
	../configure --prefix=$1 $2 $3 $4
	make -j $JOBCOUNT
	make install-strip
	rm -rf *
}

confMakeGDB()
{
	# install-strip doesn't work properly with GDB, so we have to manually strip the massive 100MB+ executable down to ~5MB then do a normal install
	../configure --prefix=$2 $3 $4 $5
	make -j $JOBCOUNT
	$1
	make install
	rm -rf *
}

# Make AVR-Binutils
if [ $BUILD_BINUTILS -eq 1 ]; then
	echo "编译 Binutils..."
	echo "提取..."
	tar xf $NAME_BINUTILS.tar.xz
	mkdir -p $NAME_BINUTILS/obj-avr
	cd $NAME_BINUTILS/obj-avr
	[ $FOR_LINUX -eq 1 ] && confMake "$PREFIX_GCC_LINUX" "$OPTS_BINUTILS"
	[ $FOR_WINX86 -eq 1 ] && confMake "$PREFIX_GCC_WINX86" "$OPTS_BINUTILS" --host=$HOST_WINX86 --build=`../config.guess`
	[ $FOR_WINX64 -eq 1 ] && confMake "$PREFIX_GCC_WINX64" "$OPTS_BINUTILS" --host=$HOST_WINX64 --build=`../config.guess`
	cd ../../
else
	echo "跳过 Binutils..."
fi

# Make AVR-GCC
if [ $BUILD_GCC -eq 1 ]; then
	echo "编译 GCC..."
	echo "提取..."
	tar xf $NAME_GCC.tar.xz
	mkdir -p $NAME_GCC/obj-avr
	cd $NAME_GCC
	chmod +x ./contrib/download_prerequisites
	./contrib/download_prerequisites
	cd obj-avr
	# fixGCCAVR
	[ $FOR_LINUX -eq 1 ] && confMake "$PREFIX_GCC_LINUX" "$OPTS_GCC"
	[ $FOR_WINX86 -eq 1 ] && confMake "$PREFIX_GCC_WINX86" "$OPTS_GCC" --host=$HOST_WINX86 --build=`../config.guess`
	[ $FOR_WINX64 -eq 1 ] && confMake "$PREFIX_GCC_WINX64" "$OPTS_GCC" --host=$HOST_WINX64 --build=`../config.guess`
	cd ../../
else
	echo "跳过 GCC..."
fi

# Make GDB
if [ $BUILD_GDB -eq 1 ]; then
	echo "编译 GDB..."
	echo "提取..."
	tar xf $NAME_GDB.tar.xz
	mkdir -p $NAME_GDB/obj-avr
	cd $NAME_GDB/obj-avr
	[ $FOR_LINUX -eq 1 ] && confMake "strip gdb/gdb" "$PREFIX_GCC_LINUX" "$OPTS_GDB"
	[ $FOR_WINX86 -eq 1 ] && confMakeGDB "$HOST_WINX86-strip gdb/gdb.exe" "$PREFIX_GCC_WINX86" "$OPTS_GDB" --host=$HOST_WINX86 --build=`../config.guess`
	[ $FOR_WINX64 -eq 1 ] && confMakeGDB "$HOST_WINX64-strip gdb/gdb.exe" "$PREFIX_GCC_WINX64" "$OPTS_GDB" --host=$HOST_WINX64 --build=`../config.guess`
	cd ../../
else
	echo "跳过 GDB..."
fi

# Make AVR-LibC
if [ $BUILD_LIBC -eq 1 ]; then
	echo "编译 AVR-LibC..."
	if [ "$NAME_LIBC" = "avr-libc3.git" ]; then
		echo "准备中..."
		cd $NAME_LIBC
		git checkout $COMMIT_LIBC
		./bootstrap
		cd ..
	else
		echo "提取..."
		bunzip2 -c $NAME_LIBC.tar.bz2 | tar xf -
	fi
	mkdir -p $NAME_LIBC/obj-avr
	cd $NAME_LIBC/obj-avr
	confMake "$PREFIX_LIBC" "$OPTS_LIBC" --host=avr --build=`../config.guess`
	cd ../../
else
	echo "跳过 AVR-LibC..."
fi

# Make AVRDUDE
if [ $BUILD_AVRDUDE -eq 1 ]; then
	echo "编译 AVRDUDE..."
	echo "提取..."
	tar xf $NAME_AVRDUDE.tar.xz
	mkdir -p $NAME_AVRDUDE/obj-avr
	cd $NAME_AVRDUDE/obj-avr
	[ $FOR_LINUX -eq 1 ] && confMake "strip gdb/gdb" "$PREFIX_GCC_LINUX" "$OPTS_AVRDUDE"
	[ $FOR_WINX86 -eq 1 ] && confMakeGDB "$HOST_WINX86-strip gdb/gdb.exe" "$PREFIX_GCC_WINX86" "$OPTS_AVRDUDE" --host=$HOST_WINX86 --build=`../config.guess`
	[ $FOR_WINX64 -eq 1 ] && confMakeGDB "$HOST_WINX64-strip gdb/gdb.exe" "$PREFIX_GCC_WINX64" "$OPTS_AVRDUDE" --host=$HOST_WINX64 --build=`../config.guess`
	cd ../../
else
	echo "跳过 AVRDUDE..."
fi

TIME_END=$(date +%s)
TIME_RUN=$(($TIME_END - $TIME_START))

echo ""
echo "完成花费 $TIME_RUN 秒"

exit 0
```