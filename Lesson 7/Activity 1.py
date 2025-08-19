print("Enter marks of 5 subjects")
Mark1=int(input())
Mark2=int(input())
Mark3=int(input())
Mark4=int(input())
Mark5=int(input())
total=Mark1+Mark2+Mark3+Mark4+Mark5
average=total/5
if average>90 and average<100:
    print("Your grade is A1")
elif average>80 and average<90:
    print("Your grade is A2")
elif average>70 and average<80:
    print("Your grade is B1")
elif average>60 and average<70:
    print("Your grade is B2")
elif average>50 and average<60:
    print("Your grade is C1")
elif average>40 and average<50:
    print("Your grade is C2")
else: 
    print("You failed") 
