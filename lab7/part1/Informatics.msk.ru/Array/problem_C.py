a= int(input())
arr=[0]*a
arr=input().split()
c=0
for i in range(0,a):
    if int(arr[i])>0:
        c+=1
print(c)