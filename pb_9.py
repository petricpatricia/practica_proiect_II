def problema9():
    f = open("matrice9.in", 'r')
    prima_linie = f.readline().strip().split(' ')
    matrice = []
    n = int(prima_linie[0])
    for linie in f.readlines():
        matrice.append([int(x) for x in linie.strip().split(' ')])
    f.close()
    suma_dp = 0
    suma_ds = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                suma_dp += matrice[i][j]
            if i+j == n-1:
                suma_ds += matrice[i][j]
    if suma_dp >= suma_ds:
        D = suma_dp-suma_ds
    else: D = suma_ds-suma_dp
    s = open('matrice9.out', 'w')
    s.write(str(D))
    s.close()


if __name__ == "__main__":
    problema9()


