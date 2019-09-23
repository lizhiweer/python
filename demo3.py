import sys

# 获取默认编码
print(sys.getdefaultencoding())

# 字符与编码转换
print(ord("我"))
print(chr(25105))

# 通过b前缀指定hello是bytes类型的值
a = b'hello'
b = bytes("我是谁", encoding='utf-8')
print(a)
print(b)
print(b.decode('utf-8'))
#
print(sys.getwindowsversion())
