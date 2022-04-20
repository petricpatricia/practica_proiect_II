def problema_spirala():
    f = open("spirala.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    k = n//2
    s = open('spirala.out', 'w')
    for p in range(1, k+1):
        for j in range(p, n+2-p):
            s.write(str(matrice[p-1][j-1]))
            s.write(str(" "))
        for i in range(p+1, n+2-p):
            s.write(str(matrice[i-1][n-p]))
            s.write(str(" "))
        for j in range(n-p, p, -1):
            s.write(str(matrice[n-p][j-1]))
            s.write(str(" "))
        for i in range(n-p+1, p, -1):
            s.write(str(matrice[i-1][p-1]))
            s.write(str(" "))

    if n % 2 != 0:
        s.write(str(matrice[n//2+1][n//2+1]))


if __name__ == "__main__":
    problema_spirala()
