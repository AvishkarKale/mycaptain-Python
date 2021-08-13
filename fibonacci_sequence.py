n=int(input("enter how many fibonacci do you want :"))
i=0
j=1
k=0
Fn=[0,1]
m=n-3
while k<=m:
    c=i+j
    Fn.append(c)
    i=j
    j=c
    k=k+1
print("Fn =",Fn)