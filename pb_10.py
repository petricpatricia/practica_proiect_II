def pb_10():
    f = open("matrice10.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    print(matrice)

    transpusa = [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]

    s = open('matrice10.out', 'w')
    for i in range(len(transpusa)):
        for j in range(len(transpusa)):
            s.write(str(transpusa[i][j]) + " ")
        s.write("\n")
    s.close()

    print(transpusa)


if __name__ == "__main__":
    pb_10()

