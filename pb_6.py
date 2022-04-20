def problema6():
    f = open("matrice6.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    m = int(prima_linie[1])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    nr_pozitive = 0
    nr_negative = 0
    nr_nule = 0
    for i in range(n):
        for j in range(m):
            if matrice[i][j] > 0:
                nr_pozitive += 1
            else:
                if matrice[i][j] < 0:
                    nr_negative += 1
                else: nr_nule += 1
    s = open('matrice6.out','w')
    s.write("{} {} {}\n".format(nr_nule,nr_negative,nr_pozitive))
    s.close()


if __name__ == "__main__":
    problema6()