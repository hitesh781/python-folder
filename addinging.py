#if the length of string is>3 add ing in last
#else same with out adding ing at last.
a=str(input("enter the string:"))
b="ing"
if len(a)>3:
    print(a+b)
else:
    print(a)    