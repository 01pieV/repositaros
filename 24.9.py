def schreder ():
    for i in range(1000,10000):
        posl_dve_c = i % 100
        prve_dve_c = i // 100
        if prve_dve_c ** 2 + posl_dve_c ** 2 == i:
            print(i)

schreder()
