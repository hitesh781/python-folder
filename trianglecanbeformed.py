a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if a+b>c:
    print("triangle an be formed")
elif a+c>b:
        print("triangle an be formed")
elif b+c>a:
    print("triangle an be formed")      
elif a==b==c:
    print("triangle an be formed")      
else:
    print("can not form triangle")    