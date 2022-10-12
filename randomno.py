import random
count=3
ans='y'
win=False
print("guess what number computer will generated between 20-30")
print("total 3 chance are there")
print("-------------------------let start the game----------------------------------")
while ans=='y':
    num1=random.randint(0,10)
    print("chance reamining:",count)
    guess=int(input("enter your answer:"))
    if num1==guess:
        print("congratulation! you gussed it right!you won $10")
        win=True
    else:
        print("worng! try again")
        count-=1
        if count==0:
            print("Oops! try again")
            print("number was:",num1)
    if win==True or count==0:
        ans==input("play Again ?")
        if ans=='y':
            count=3
            win=False
        

































        
