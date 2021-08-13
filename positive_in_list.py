##list1
n=int(input("Enter how many elements you want in list1 : "))
list1=[]
positive_list1=[]
list1.clear()
positive_list1.clear()
for i in range(n):
    x=int(input("Enter the element you want to add in the list1 :"))
    list1.append(x)
j=0
while j<=(len(list1)-1):
    if list1[j]>0:
        positive_list1.append(list1[j])
    j=j+1

##list2
m=int(input("Enter how many elements you want in list2 : "))
list2=[]
positive_list2=[]
list2.clear()
positive_list2.clear()
for i in range(m):
    y=int(input("Enter the element you want to add in the list2 :"))
    list2.append(y)
j=0
while j<=(len(list2)-1):
    if list2[j]>0:
        positive_list2.append(list2[j])
    j=j+1

    
## printing output
print("list1 :",list1)
print("list of positive elements in list1 :",positive_list1)
print("list2 :",list2)
print("list of positive elements in list2 :",positive_list2)