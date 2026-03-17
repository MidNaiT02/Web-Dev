a = int(input())
n = list(map(int, input().split()))

for i in range(a//2):
    n[i], n[a-i-1]=n[a-i-1], n[i]

print(*n)