from curses.ascii import isalpha

   
num1=int(input("enter  first no:"))
num2=int(input("enter second no:"))
if num1>num2:
    print("num1 is greater")
elif num1<num2:
    print("num2 is greater")    
else:
    print("both are same")    