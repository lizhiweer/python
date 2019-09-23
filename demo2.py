import decimal
import fractions

a = decimal.Decimal(10.0)
b = decimal.Decimal(3)

# 小数
print(a / b)
# 分数
print(fractions.Fraction(10, 3))

c = "abracadabra"
d = '''absentminded'''
e = '''哈哈哈哈哈哈哈哈哈哈或\
    或或或或或或或或或或或或或或或或或'''
print(type(c))
print(type(d))
print(e)

# 原始字符串
msg1 = r"G:\publish\codes\02\2.4"
print(msg1)