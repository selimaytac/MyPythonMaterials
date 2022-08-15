print(1, 2, 3, 4, sep='*')  # sep='*' ile sep değişkeni ile * karakteri arasına yazılır. Output = 1*2*3*4
print(1, 2, 3, 4, sep='#', end='&')  # end='&' ile bitirme işlemi yapılır. Output = 1#2#3#4&

x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))  # The value of x is 5 and y is 10
print('The value of x is {1} and y is {0}'.format(x, y))  # The value of x is 10 and y is 5
print('Hello {name}, {greeting}'.format(greeting='Goodmorning', name='John'))  # Hello John, Goodmorning

x = 12.3456789
print('The value of x is %3.2f' %x)  # The value of x is 12.35

# input işlemleri

num = input('Enter a number: ')

print('The number is', num) # The number is 12

# import işlemleri

from math import pi

print(pi) # 3.141592653589793