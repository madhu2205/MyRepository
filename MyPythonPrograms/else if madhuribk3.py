#write a program to take
# acharacter input from user and check that whether that character is capital
#  letter,small case letter or a digit

ch=input("enter a char:")
x=ord(ch)
if x>=65 and x<=90:
    print("capital")
elif x>=90 and x<=122:
    print("small")
elif x>=48 and x<=57:
    print("digit")
else:
    print ("i dont know")