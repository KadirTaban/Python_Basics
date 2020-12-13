from functools import  wraps

def log_data(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """wrapper hakkında bilgilendir."""
        print(f"çağırdığınız metot ismi: {fn.__name__}")
        print(f"metot bilgisi : {fn.__doc__}")

        return fn(*args,**kwargs)
    return wrapper
@log_data
def add(x,y):
    """fonksiyona gönderilen iki sayıyı toplar """
    return x+y
"""
print(add(10,20))

print(add.__name__)
print(add.__doc__)
"""
@log_data

def carp(a,b):
    """fonksiyona gönderilen iki sayıyı çarpar"""
    return a*b
print(carp(4,5))
print(carp.__name__)
print(carp.__doc__)
