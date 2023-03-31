# **<font color=#01A0B3>"笨方法"学</font> <font color=#A9A9A9>Python 3</font>**

<font color=#A9A9A9 size=3>Learn PYTHON 3 the</font> <font color=#01A0B3 size=3>HARD WAY</font>

<img src="https://img-blog.csdnimg.cn/img_convert/7b0d6ba5dcce6ce6b2e732fdffde6496.gif" alt="">

## 前言

​:exclamation:​​​:exclamation:​​  ==**PS: 初学不要用IDE!!** 就用文本编辑器==.
| 编辑器名称 | 支持平台 |
| --- | --- |
|**Visual Studio Code** <svg class="icon svg-icon" aria-hidden="true"><use xlink:href="#icon-tubiaozhizuomoban"></use></svg>|Windows, macOS, Linux|
|NotePad++|Windows|
|gEdit|Linux, macOS, Windows|
|Textmate|macOS|
|SciTe|Windows, Linux|
|jEdit|Linux, macOS, Windows|
|Atom|Windows, macOS, Linux|

:pushpin:书中代码放在[github](https://github.com/QSanSi/LearnPython3theHardWay)上了.

- [Python官方文档](https://docs.python.org/zh-cn/3/index.html)
- [Python 语言参考手册](https://docs.python.org/zh-cn/3/reference/index.html)
- [Python基础教程，Python入门教程（非常详细）](http://c.biancheng.net/python/)

## 习题1 第一个程序

```python
print("Hello World!")
```

## 习题2 注释和#号

```python
print("This will run.") # Anything after "#" is ignored by python.
# print("This won't run.")
```

1. 多行注释每行前加`#`;
2. 记住它的名字(octothorpe或者pound character).

## 习题3 数字和数学计算

- +: 加号; -: 减号; *: 乘; /: 除(得浮点数商); //: 除(得整数商); **: 幂运算
- %: ==取模==
  - C/C++, Java为**取余**, Python为**取模**
  - **区别:**
    > 第一步：求整数商c：
    > 进行求模运算时：c = a / b = -7 / 4 = -2（向负无穷方向舍入）
    > 进行求余运算时：c = a / b = -7 / 4 = -1（向0方向舍入）
    > 第二步：计算模和余数的公式相同，但因c的值不同，
    > 求模时：r = a - c \* b = -7 - (-2) \* 4 = 1
    > 求余时：r = a - c \* b = -7 - (-1) \* 4 =-3
  - **归纳：** 当a和b正负号一致时，求模运算和求余运算所得的c的值一致，因此结果一致。当正负号不一致时，结果不一样。
- <: 小于; \>: 大于; <=: 小于等于; >=: 大于等于
- 浮点数四舍五入`round() 函数`, 例: `round(3.1415)`

## 习题4 变量和命名

- 不用显式指定数据类型, 命名一个变量定义赋值直接用. 变量名以"字母"或"_"开头

```python
cars = 100
_drivers = 30
```

## 习题5 更多的变量和打印

- **格式化字符串(f-string)** 字符串以f开头, 变量放在{}中。
  
```python
my_name = 'Zed A. Shaw'
print(f"Let's talk about {my_name}.")
# Let's talk about Zed A. Shaw.
```

## 习题6 字符串和文本

- 字符串以`" "`、`' '`、`''' '''`或`""" """`标识, 三连的引号可以多行表示字符串。
- 拼接字符串

```python
a = "kg"
b = "nb"
print(a + b)
# kgnb
```

- ==重点：== 格式化字符串[f-string拓展](https://www.cnblogs.com/qsswxm/p/17263280.html)。

## 习题7 更多打印

- 字符串后`*`加数字(n)可以重复该字符串n次。

```python
print("." * 10)
# ..........
```
  
- `end`可以将`print()`函数末尾给字符串添加的换行符替换为指定字符。
  
```python
print("ABC")
print("DEF")
# ABC
# DEF
print("ABC", end='')
print("DEF")
# ABCDEF
print("ABC", end=' ')
print("DEF")
# ABC DEF
print("ABC", end='123')
print("DEF")
# ABC123DEF
```

## 习题8 打印，打印
