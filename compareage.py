per1=int(input("enter your age:"))
per2=int(input("enter your age:"))
per3=int(input("enter your age:"))
if per1<per2 and per1<per3:
    print("per1 is younger")
elif per2<per1 and per1<per3:
    print("per2 is younger")    
else:
    print("per3 is younger")
