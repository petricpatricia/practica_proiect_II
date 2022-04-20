def problema4():
    smax = -100001
    indice = 0
    f = open("sumcolmax.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    m = int(prima_linie[1])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    for j in range(m):
        suma = 0
        for i in range(n):
            suma += matrice[i][j]
        if suma > smax:
            smax = suma
            indice = j
    scriere_fisier = open("sumcolmax.out", 'w')
    for i in range(n):
        scriere_fisier.write(str(matrice[i][indice]))
        scriere_fisier.write(' ')
    scriere_fisier.close()


if __name__ == "__main__":
    problema4()


