def problema7():
    f = open("matrice7.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    lista_suma_linii = []
    for i in range(n):
        suma_linie = 0
        for j in range(n):
            suma_linie += matrice[i][j]
        lista_suma_linii.append(suma_linie)
    lista_suma_coloane = []
    for j in range(n):
        suma_coloana = 0
        for i in range(n):
            suma_coloana += matrice[i][j]
        lista_suma_coloane.append(suma_coloana)
    C = 0
    for i in range(n):
        for j in range(n):
            if lista_suma_linii[i] == lista_suma_coloane[j]:
                C += 1
    s = open('matrice7.out', 'w')
    s.write(str(C))
    s.close()


if __name__ == "__main__":
    problema7()


