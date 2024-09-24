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
        print()
fun2(5)
