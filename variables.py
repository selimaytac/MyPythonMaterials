# Variable Tanımlama

# Değişkenler sayi ve keywords hariç her şey ile başlayabilir.

# Örneğin 1Users invalid, Users1 valid.

# Veya Global = 5 gibi değişkenleri kullanamayız çünkü global bir keyword.

# Global number = 5 gibi kullanılır.;

# Değişkenler özel karakterlerla başlayamaz !,@,#,$,% etc.

# Örneğin !Users, @ALL, #First gibi değişken isimleri tanımlanamaz.

numbers = 10

toplam = 10 + 13 + \
         11 + 21 + \
         59 + 23

# gibi tanımlamalar yapabiliriz.

isimler = ['ahmet', 'mehmet', 'veli', 'ali', 'veli']

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Yorum satırları

# böyle
# yazarak
# coklu
# yorum
# satırı kullanabiliriz

# veya

"""
buranın 
içine
yazılan
her şey
yorum olarak
sayılır
"""

number = 1231231
number = 321312.32
string = "Hello World"

# çoklu tanımlama

a1, a2, a3 = "ilk", 2, 3.0

a = b = c = 20

# sabitler

APIKEY = "12345"
APIURL = "https://TEST-API.com"

# literaller

a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2  # 1.5 x 10^2

# Complex Literal
x = 3.14j  # 3.14j is the complex number 3.14j

# strings

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

# bool

x = (1 == True)  # True
y = (1 == False)  # False
a = True + 4  # True + 4 = 5
b = False + 10  # False + 10 = 10

# ayrıca

noneVar = None


