n = int(input())
s = set(map(int, input().split()))

m = int(input())
for _ in range(m):
    line = input().split()
    op = line[0]
    if op == 'pop':
        s.pop()
    elif op == 'remove':
        s.remove(int(line[1]))
    elif op == 'discard':
        s.discard(int(line[1]))

print(sum(s))