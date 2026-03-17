def my_power(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result

a,b =input().split()
a = float(a)
b=int(b)
print(my_power(a,b))