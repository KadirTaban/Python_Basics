"""
sonsuz sayıda  sayının karesini alma
def sonsuz_sayi_uret():
    sayi = 0

    while True:

        yield sayi**2
        sayi+=1

generator = sonsuz_sayi_uret()

print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)
"""
"""
fibonacci
def fibonacci(max):
    sayilar =[]
    a, b = 0, 1
    while len(sayilar)<max:
        sayilar.append(b)
        a, b = b, a+b
    return sayilar


print(fibonacci(100))

"""
"""
fibonacci 
def fib_gen(max):
    count=0

    a, b = 0, 1
    while count < max :
        a, b = b, a+b
        yield b
        count +=1
for i in fib_gen(10):
    print(i)
    
"""
"""
def iki_kat(max):
    sayilar=[]
    a=2
    count=0 
    while count < max:
        a=a*2
        yield a
        count +=1

for i in iki_kat(10):
    print(i)
"""
import time
list_start_time = time.time()
print([i**2 for i in range (1000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
print(i**2 for i in range (1000))
gen_stop = time.time() - gen_start_time
print(list_stop, gen_stop)