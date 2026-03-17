a = int(input())
n = [0] * a
n = input().split()

for i in range(0, a):
    if int(n[i]) % 2 == 0:
        print(n[i], end=' ')