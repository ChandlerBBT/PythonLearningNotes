# encoding:utf-8
# project: PythonLearningNotes
# author: chandler
# file: Rule3_Strings.py
# create_time: 2020/4/19
# IDE: Pycharm


"""
在Python3中，只有bytes和str两种表示字符序列的类型
因此，需要编写接受str或bytes，并且总是返回str的方法
"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value  # str的实例


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value