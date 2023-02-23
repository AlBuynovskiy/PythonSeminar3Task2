N = abs(int(input()))
A_entered = input().split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print()
else:
    X = int(input())
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'{A_num[index]}')