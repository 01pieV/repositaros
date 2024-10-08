def jano():
    return "ahoj svet"
def jozo():
    print("ahoj svet")
jozo() # napíše ahoj svet
c = jano() # z c sa stane "ahoj svet"
print(c)


def colatz(n):
    while n!=1:
        if n%2 ==0:
            n//=2 # n = n//2
            print(n, end=",")
        else:
            n = n*3+1
            print(n, end=",")
    print()
for i in range (1,101):
    colatz(i)

def deli(a):
    dela = 2
    while a!= 1:
        if a % dela ==0:
            print(dela)
            a = a // dela
        else:
            dela += 1
deli(12)

def sucdel(a):
    b = 0
    for i in range(1,a+1):
        if a % i ==0:
            b +=i
    return b

print(sucdel(6))

def is_perfect(a):
    if sucdel(a) == a*2:
        return True
    else:
        return False
for i in range(1,101):
    print(i, end=",")
    print(is_perfect(i))
