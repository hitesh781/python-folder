lectur=int(input("enter total no of lecture:"))
atte=int(input("enter no of classes attend:"))
c=atte/lectur*100
print(c)
if c>75:
    print("aplicable for giving exam")
else:
    print("not aplicable for giving th exam" )    
    