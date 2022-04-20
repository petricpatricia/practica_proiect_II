def problema12():
    f = open("matrice12.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n=int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    suma_deasupra = 0
    suma_dedesubt = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                suma_deasupra += matrice[i][j]
            if i > j:
                suma_dedesubt += matrice[i][j]
    while suma_deasupra != suma_dedesubt:
        if suma_deasupra > suma_dedesubt:
            suma_deasupra -= suma_dedesubt
        else: suma_dedesubt -= suma_deasupra
    D = suma_deasupra
    s = open('matrice12.out', 'w')
    s.write(str(D))
    s.close()


if __name__ == "__main__":
    problema12()

