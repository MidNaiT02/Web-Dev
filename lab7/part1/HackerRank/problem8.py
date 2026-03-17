n = int(input())
students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

lowest = min(s[1] for s in students)
second_lowest = min(s[1] for s in students if s[1] != lowest)

for name in sorted(s[0] for s in students if s[1] == second_lowest):
    print(name)