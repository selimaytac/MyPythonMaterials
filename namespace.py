# Note: You may get different values for the id
a = 2
print('id(2) =', id(2)) # 9302208

print('id(a) =', id(a)) # 9302208

# Namescape scopeları

# Built-in Namespaces
print('__builtins__ =', __builtins__) # <module 'builtins' (built-in)>

# Global Namepsaces (Modüller)
# Local Scopes (Fonksiyonlar)
def outer_function():
    b = 20
    def inner_func():
        c = 30
        print(b)  # 20
    print(c) # NameError: name 'c' is not defined


a = 10

print(a) # 10
print(b) # NameError: name 'b' is not defined
print(c) # NameError: name 'c' is not defined