print(float(20))  # 20.0
print(int(20.5))  # 20

print(int(True))  # 1

print(int(-14.9))  # -14

print(float('-5'))  # -5.0

# print(float('ahmet'))  # ValueError: could not convert string to float: 'ahmet'

print(set([1, 2, 3]))  # {1, 2, 3} listeyi set'e çevirir

print(tuple({5, 6, 7}))  # (5, 6, 7) seti tuple'a çevirir

print(list('hello'))  # ['h', 'e', 'l', 'l', 'o'] stringi liste'ye çevirir

# print(dict([[1,2],[3,4]])) # liste'yi dictionary'e çevirir ama bu işlem hata verecektir çünkü pairleri yok..

print(dict([(3, 26), (4,
                      44)]))  # {3: 26, 4: 44} liste'yi dictionary'e çevirir, Not: dict çevirisi yapılırken her bir elemanı key:value şeklinde yapılır.

## 2 Çeşit çevirme vardır

# Örtük (Implicit) ve Açık (Explicit) çevirme

# Örtük (Implicit)

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))  # datatype of num_int: <class 'int'>
print("datatype of num_flo:", type(num_flo))  # datatype of num_flo: <class 'float'>

print("Value of num_new:", num_new)  # Value of num_new: 126.23
print("datatype of num_new:", type(num_new))  # datatype of num_new: <class 'float'>

# bunları otomatik olarak python compilerı değerlere göre çevirecektir

# hata verebilecek kısımlar

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))  # Data type of num_int: <class 'int'>
print("Data type of num_str:", type(num_str))  # Data type of num_str: <class 'str'>

# print(num_int + num_str)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Açık (Explicit)

# bu çevirmeyi yapmak için int() ve float() gibi fonksiyonları kullanılırız, tipi özel olarak belirtiriz.

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:",
      type(num_str))  # Data type of num_str before Type Casting: <class 'str'>

num_str = int(num_str)
print("Data type of num_str after Type Casting:",
      type(num_str))  # Data type of num_str after Type Casting: <class 'int'>

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)  # Sum of num_int and num_str: 479
print("Data type of the sum:", type(num_sum))  # Data type of the sum: <class 'int'>

# Python avoids the loss of data in Implicit Type Conversion.

# Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.

# In Type Casting, loss of data may occur as we enforce the object to a specific data type.