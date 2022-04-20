def problema_serpuire():
    f = open("serpuire.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    z = 0
    s = open('serpuire.out', 'w')
    while z <= n*n:
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i+j == z+1:
                    if z % 2 == 0:
                        s.write(str(matrice[j-1][i-1]))
                    else:
                        s.write(str(matrice[i-1][j-1]))
                    s.write(str(" "))
        z += 1
    s.close()


if __name__ == "__main__":
    problema_serpuire()
