def problema13():
    f = open("medpoz.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    suma = 0
    nr = 0
    for i in range(n):
        for j in range(n):
            if (i > j) & (matrice[i][j] > 0):
                suma += matrice[i][j]
                nr += 1
    ma = suma/nr
    s = open('medpoz.out', 'w')
    s.write(format(ma, ".3f"))
    s.close()


if __name__ == "__main__":
    problema13()

