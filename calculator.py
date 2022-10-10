while True:
    print("simple caculator")
    print("...........")
    print("1. ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.QUIT")
    print("......................")
    ch=int(input("enter your choice(1-5):"))
    if ch==5:
        break 
    n1=int(input("enter first no.:"))
    n2=int(input("enter second no.:"))
    reasult=0
    if ch==1:
        result=n1+n2
    elif ch==2:
        result=n1-n2
    elif ch==3:
        result=n1*n2
    elif ch==4:
        result=n1/n2
    print("result of calculation=",result)
    print()
    print("progam terminated....")