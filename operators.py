x = 15
y = 4

print('x + y =', x + y)  # x + y = 19

print('x - y =', x - y)  # x - y = 11

print('x * y =', x * y)  # x * y = 60

print('x / y =', x / y)  # x / y = 3.75

print('x // y =', x // y)  # x // y = 3

print('x ** y =', x ** y)  # x ** y = 50625

#   Karşılaştırma Operatörleri

x = 10
y = 12

print('x > y is', x > y)  # x > y is False

print('x < y is', x < y)  # x < y is True

print('x == y is', x == y)  # x == y is False

print('x != y is', x != y)  # x != y is True

print('x >= y is', x >= y)  # x >= y is False

print('x <= y is', x <= y)  # x <= y is True

# Mantık Operatörleri

x = True
y = False

print('x and y is', x and y)  # x and y is False

print('x or y is', x or y)  # x or y is True

print('not x is', not x)  # not x is False

# bitwise

x = 0b1010  # binary
y = 0b0101  # binary

print('x & y is', x & y)  # x & y is 0

print('x | y is', x | y)  # x | y is 15

print('x ^ y is', x ^ y)  # x ^ y is 15

# bitwise shift

x = 0b1010  # binary

print('x >> 2 is', x >> 2)  # x >> 2 is 0b101

print('x << 2 is', x << 2)  # x << 2 is 0b10100

# Assignment Operators

x = 10

x += 1  # x = x + 1

x -= 1  # x = x - 1

x *= 2  # x = x * 2

x /= 2  # x = x / 2

x %= 2  # x = x % 2

# Tanımlama Operatörleri

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Output: False
print(x1 is not y1)  # Output: True

print(x2 is y2)  # Output: True

print(x3 is y3)  # Output: False

# Üyelik Operatörleri

x = 'Hello world'
y = {1: 'a', 2: 'b'}

print('H' in x)  # Output: True

print('hello' not in x)  # Output: True

print(1 in y)  # Output: True

print('a' in y)  # Output: False
