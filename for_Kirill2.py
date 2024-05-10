a, b, c, d = map(int, input().split())
if (a, b, c, d < 10) or (a <= b) or (c <= d):
    print('', end='\t')
    for i in range(c, d + 1):
        print(i, end='\t')
    print()
    for j in range(a, b + 1):
        print(j, end='\t')
        for k in range(c, d + 1):
            print(j * k, end='\t')
        print()