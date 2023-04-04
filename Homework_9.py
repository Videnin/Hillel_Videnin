n = 4
for i in range(1, n+1):
    print(' '.join(str(j) for j in range(i, i*2)))
for i in range(n-1, 0, -1):
    print(' '.join(str(j) for j in range(i, i*2)))
