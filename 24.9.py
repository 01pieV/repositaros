def schreder ():
    for i in range(1000,10000):
        posl_dve_c = i % 100
        prve_dve_c = i // 100
        if prve_dve_c ** 2 + posl_dve_c ** 2 == i:
            print(i)

#spocitanie cisel
def schreder2():
    tog = 0
    for i in range(1000,10000):
        tog = tog + i # tog += 1
    return tog

#faktorial
def fak(a):
    tog = 1
    for i in range(1, a+1):
        tog = tog * i
    return tog

print(fak(5))







# uloha 1.
def fun1():
    for i in range(1,11):
        print(i)
fun1()

# uhloha 2.
    # a.)
def fun2(a):
    for i in range(1, a+1):
        print(i)

fun2(5)
    # b.)
def fun2(a):
    for i in range(1, a+1):
        if i < a:
            print(i,end =',')
        else:
            print(i)
fun2(5)

# uloha 3.
def fun3(a):
    for i in range (5, a+1, 2):
        print(i)
fun3(15)

# uloha 4.

def fun4(a):
    for i in range(1, a+1):
        print(i, i**2 )
fun4(9)

# uloha 5.
import math
def fun5(a,b):
    for i in range(a,b+1):
        odmocninca = round(math.sqrt(i), 2)
        print(odmocninca)
fun5(1,6)
