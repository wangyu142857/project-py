"""
Syntax Basics
"""

#######################
# int
a = 10
b = -5

# float
x = 3.14

# complex
c = 1 + 2j

# str
st = "Hello"

# list
arr = [1, 2, 3]

# tuple
t = (1, 2, 3)

# range
r = range(0, 10)

# dict
d = {"name": "张三"}

# set
s = {1, 2, 3}

# frozenset
fr_set = frozenset([1, 2, 3])

# bool
b = True
b = 2

# if
if b:
    print("b is True")
elif b == 0:
    print("b is 0")
else:
    print("b is False")

# match
status_code = 200
match status_code:
    case 200:
        print("OK")
    case 401 | 403 | 404:
        print("Not All")
    case 500 | 503:
        print("Internal Server Error")
    case _:
        print("Unknown")

# for
total = 0
for i in range(10):
    total += i
print(total)

# while
i = 1
while i < 10:
    print(i)
    total += i
    if total > 50:
        break
    i += 1
    if i % 2 == 0:
        continue
print(total)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}×{j}={i * j}", end="\t")
    print()

# 佩波那契数列
a, b = 0, 1
while b < 100:
    print(b, end=" ")
    a, b = b, a + b
print()

# 列表
arr = [1, 2, 3, 4, 5]
arr2 = list[int](range(10))
arr3 = list[str]("Hello, World!")

# 列表运算
arr4 = arr + arr2
print(arr4)
arr5 = arr * 2
print(arr5)
print(1 in arr)
print(10 not in arr)
print(arr[0])
print(arr[-1])
# 切片 [start:end:stride]
print(arr[1:3])  # 从索引1开始，到索引3结束，不包括索引3
print(arr[:3])  # 从索引0开始，到索引3结束，不包括索引3
print(arr[1:])  # 从索引1开始，到末尾
print(arr[:])  # 从索引0开始，到末尾
print(arr[::2])  # 从索引0开始，到末尾，步长为2
print(arr[::-1])  # 从末尾开始，到索引0结束，不包括索引0

# 遍历下标
for index in range(len(arr)):
    print(arr[index])

# 遍历元素
for item in arr:
    print(item)

# 列表api
arr.append(6)  # 添加元素到末尾
arr.insert(0, 0)  # 添加元素到指定位置,
arr.remove(0)  # 删除元素,只删除第一个出现的元素
arr.pop()  # 删除末尾元素
arr.reverse()  # 反转列表
arr.sort()  # 排序列表
arr.sort(reverse=True)  # 排序列表，倒序
arr.index(1)  # 返回元素的索引
arr.count(1)  # 返回元素的个数
arr.copy()  # 复制列表
arr.extend(arr2)  # 添加列表到末尾
arr.extend(arr2)  # 添加列表到末尾
# arr.clear()  # 清空列表
arr6 = [i for i in range(10) if i % 2 == 0]
print(arr6)
arr7 = [i * 2 for i in arr]
print(arr7)

# 元组
t = (1, 2, 3)
t = (1,)  # 元组中只有一个元素时，需要加逗号
t = 1, 2, 3  # 打包成元组
i, j, k = t  # 解包成变量,解包出来的元素个数和变量个数必须一致
i, *t2 = t  # 解包变量少时，使用 * 解包剩余元素, * 修饰的变量是一个列表
