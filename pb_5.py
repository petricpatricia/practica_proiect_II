def problema5():
    f = open("colzero.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    m = int(prima_linie[0])
    n = int(prima_linie[1])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    NR = 0
    for j in range(n):
        ok = 1
        for i in range(m):
            if matrice[i][j] != 0:
                ok = 0
        if ok == 1:
            NR += 1
    s = open('colzero.out', 'w')
    s.write(str(NR))
    s.close()


if __name__ == "__main__":
    problema5()