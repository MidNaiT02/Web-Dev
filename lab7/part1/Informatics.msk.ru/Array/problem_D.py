a = int(input())
n = list(map(int, input().split()))

count = 0
for i in range(1, a):
    if n[i] > n[i-1]:
        count += 1

print(count)