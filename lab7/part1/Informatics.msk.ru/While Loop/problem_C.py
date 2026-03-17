n = int(input())
i = 0
while i <= n:
    c=2**i
    if c > n:
        break
    print(str(c)+" ", end="")
    i += 1