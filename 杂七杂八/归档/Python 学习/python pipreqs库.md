> `pipreqs`可以帮你找到当前项目的所有组件及其版本，自动生成依赖清单。
### 安装
```
pip install pipreqs
```
### 使用步骤
```python
#1.在项目根目录下执行命令，生成requirements.txt
pipreqs ./
# 如果是Windows系统，会报编码错误 (UnicodeDecodeError: 'gbk' codec can't decode byte 0xa8 in position 24: illegal multibyte sequence)  
pipreqs ./ --encoding=utf-8
pipreqs ./ --force # 覆盖requirements.txt
#2.执行下面代码就会把项目用到的所有组件装上
pip3 install -r requirements.txt
```
### 文件`requirements.txt`
```
Flask_Migrate==2.3.1
redis==3.0.1
Flask==1.0.2
alembic==1.0.7
Flask_Script==2.0.6
Flask_SQLAlchemy==2.3.2
Flask_Session==0.3.1
SQLAlchemy==1.2.17
```