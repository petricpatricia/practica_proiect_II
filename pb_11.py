def pb_11():
    f = open("matrice11.in",'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    matrice1 = []
    matrice2 = []
    linie = []
    for i in range(n):
        linie.append(matrice[i])
        linie[i].sort(key=int)
        matrice1.append(linie[i])
    rez = [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]
    for row in rez:
        matrice2.append(row)
    for i in range(len(matrice2)):
        matrice2[i].sort(key=int)
    rez = [[matrice2[j][i] for j in range(len(matrice2))] for i in range(len(matrice2[0]))]
    s = open('matrice11.out', 'w')
    for i in range(len(rez)):
        for j in range(len(rez)):
            s.write(str(rez[i][j])+" ")
        s.write("\n")
    s.close()


if __name__ == "__main__":
    pb_11()
    # 2877

