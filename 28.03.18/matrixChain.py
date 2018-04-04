import sys;

def matrixChaninMul(p, n):

    m = [[0 for x in range(n)]for x in range(n)]
    s = [[0 for y in range(n)]for y in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i + l -1
            m[i][j] = 1000000
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + (p[i-1] * p[k] * p[j])
                if(q < m[i][j]):
                    m[i][j] = q
                    s[i][j] = k


    print("Minimum multiplications : {} " .format(m[1][n-1]))
    print("m matrix is")
    print(m)
    return s


def printOptimalParan(s, i, j):
    if(i == j):
        print("A {}" .format(i))
    else:
        print("(", end='')
        printOptimalParan(s, i, s[i][j])
        printOptimalParan(s, s[i][j]+1, j)
        print(")", end='')


p = []
n = int(input("Enter number of elements in size matrix : "))
for i in range(0,n):
    x = int(input("Enter the size {} : " .format(i)))
    p.append(x)

u = []
u = matrixChaninMul(p, n)
print("Order of multiplication : \n")
printOptimalParan(u, 1, n-1)
print("\n")
print(u)
