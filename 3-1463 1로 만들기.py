N = int(input())
make_1 = [0 for _ in range(N+1)]

for i in range(2, N+1):
    make_1[i] = make_1[i-1] + 1
    if i % 2 == 0:
        if make_1[i//2] + 1 < make_1[i-1] + 1:
            make_1[i] = make_1[i//2] + 1
    if i % 3 == 0:
        if make_1[i//3] + 1 < make_1[i-1] + 1:
            make_1[i] = make_1[i//3] + 1

print(make_1[N])