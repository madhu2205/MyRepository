#write a program to calculate gross salary
#da is 20% of basic salary
#hra is 40% of basic salary
#gross salary=basic salary+da+hra

bs=input("enter basic salary")
bs=float(bs)
da=bs*0.2
hra=bs*0.4
gs=bs+da+hra
print ("total salary is:",gs)