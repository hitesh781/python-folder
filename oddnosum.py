from operator import index


l1=eval(input("enter element list:"))
index=0
sum=0
while index<len(l1):
    if l1[index]%2==1:
        sum+=l1[index]
    index+=1
print("sum of all odd element in list:",sum)        
