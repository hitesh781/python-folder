m= int(input("enter total number of row:"))
n=int(input("enter total no of column:"))
l=list(range(m*n))
k=0
print("input all matrix element one after other")
for i in range(n):
    for j in range(m):
        print("enter an element at index [",i,"][",j,"]:",end="")
        l[k]=input()
        k=k+1
print("list in matrix formate is")    
k=0
for i in range(n):
        for j in range(m):
            print(l[k],end=' ')
            k+=1
        print()    
