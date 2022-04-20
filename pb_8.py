def problema8():
    f = open("maxminmatrice.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    m = int(prima_linie[1])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    print(matrice)
    f.close()
    lista_minime_linii = []
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == min(matrice[i]):
                lista_minime_linii.append(matrice[i][j])
    for i in range(n):
        print(lista_minime_linii)
    maxim = max(lista_minime_linii)
    s = open('maxminmatrice.out', 'w')
    s.write(str(maxim))
    s.close()


if __name__ == "__main__":
    problema8()


