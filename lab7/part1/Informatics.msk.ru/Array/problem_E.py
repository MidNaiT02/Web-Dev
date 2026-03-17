a = int(input())
n = list(map(int, input().split()))

found = False
for i in range(1, a):
    if n[i] * n[i-1] > 0:
        found = True
        break

print("YES" if found else "NO")