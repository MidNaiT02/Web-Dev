n = int(input())
students = {}

for _ in range(n):
    line = input().split()
    students[line[0]] = list(map(float, line[1:]))

query = input()
marks = students[query]
print("{:.2f}".format(sum(marks) / len(marks)))