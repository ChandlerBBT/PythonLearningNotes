# encoding:utf-8
# project: PythonLearningNotes
# author: chandler
# file: Rule2_ObeyPep8.py
# create_time: 2020/4/19
# IDE: Pycharm


"""命名规范"""
# 函数、变量、属性应该用小写字母和下划线
lower_case = None

# 受保护的实例属性，应该以单个下划线开头
_leading_undersocre = None

# 私有的实例属性，应该以双下划线开头
__double_dunder_variable = None

# 类、异常，应该以首字母大写的形式书写
class PublicParameter(object):
    try:
        pass
    except KeyError:
        pass

# 模块级别的常量，应该全部采用大写字母书写
GLOBAL_VARAIABLE = 0

# 类中的实例方法，应该把首个参数命名为self，以表示该类自身
class Model(object):
    def function(self):
        pass

# 类方法的首个参数应该命名为cls
class Trunk(object):
    @classmethod
    def function(cls):
        pass


"""表达式和语句中的注意事项"""
# 采用联形式的否定词
# 好的写法
if a is not b:pass
# 坏的写法
if not a is b:pass

# 不要通过判断长度来检查对象是否为空
# 好的写法
if not somelist:pass
# 坏的写法
if len(somelist) == 0:pass