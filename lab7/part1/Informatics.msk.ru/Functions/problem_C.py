def XOR(x,y):
    if x==y:
        return 0
    else:
        return 1
    
a,b=input().split()
a=int(a)
b=int(b)
print(XOR(a,b))