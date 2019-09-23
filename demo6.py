# list 列表
arr = ['哈哈', '呵呵', '嘻嘻', '你大爷']

# tuple 元组
arr_source = ('大姨妈', '二姨妈', '八大姨', '七大舅')

aarr = list(arr_source)

arr.append("cao")
arr.append(arr_source)

arr.extend(arr_source)

del arr[len(arr) - 1]

print(arr)
print(arr_source)
print(aarr)

del arr

# dic 字典
map = dict()
map['a'] = 1
map['b'] = 2
map['c'] = 3

print(map)

print(map.items())

print(map.keys())

print(map.values())

