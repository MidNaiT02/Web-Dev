a=input()
b=reversed(a)
inx=0
num=0
for i in b:
    if(i=="1"):
        num+=2**inx
    inx+=1
print(num)