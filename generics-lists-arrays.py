# collections

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

# type kontrolü

a = 5
print(a, "is of type", type(a))  # is of type <class 'int'>

a = 2.0
print(a, "is of type", type(a))  # is of type <class 'float'>

a = 1 + 2j
print(a, "is complex number?", isinstance(1 + 2j, complex))  # is complex number? True

# listeler

list = [1, 2, 3, 4, 5]

a = [5, 10, 15, 20, 25, 30, 35, 40]

print("a[2] = ", a[2])  # a[2] = 15

print("a[0:3] = ", a[0:3])  # a[0:3] = [5, 10, 15]

print("a[5:] = ", a[5:])  # a[5:] = [30, 35, 40]

# tuple


t = (5, 'program', 1 + 3j)

print("t[1] = ", t[1])  # t[1] = 'program'

print("t[0:3] = ", t[0:3])  # t[0:3] = (5, 'program', (1+3j))

# t[0] = 10 # tuple'lar değişemeyeceği için böyle bir şey yaparsak compiler hata verecektir.  TypeError: 'tuple' object does not support item assignment

# sets

a = {5, 2, 3, 1, 4}

print(type(a))  # <class 'set'>

a = {1, 2, 2, 3, 3, 3}
print(a)  # {1, 2, 3} Duplicate olanları otomatik siler

# a[1]  # setlerde order olmadığı için bu işlem hata verecektir => TypeError: 'set' object does not support indexing

# dictionary

d = {1: 'value', 'key': 2}

type(d)  # <class 'dict'>

# ornek kullanim
d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# print("d[2] = ", d[2]) # key burda 'key' ama biz 2 yani value değeri üzerinden çağırmaya çalışıyoruz, bu işlem hata verecektir.
