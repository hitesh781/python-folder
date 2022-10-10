s=input("enter a string")
while True:
    print("  *CHANGE CASE*")
    print("1. sentence case")
    print("2. lower case")
    print("3. UPPEER CASE")
    print("4. Capitalze each word")
    print("5. toGGLE cASE")
    print("quit")
    choice=input("enter your choice(1-6 ")
    if choice=='1':
         result=s.capitalize()
    elif choice=='2':
         result=s.lower()
    elif choice=='3':
         result=s.upper()
    elif choice=='4':
         result=s.title()
    elif choice=='5':
         result=s.swapcase()
    else:
        break
    print(result)   
                 
  
        
       
              
                     
       
              
               
