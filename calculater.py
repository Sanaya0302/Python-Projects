def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("please choose an operation")
print("a. addition\n b. subtraction\n c. multiplication\n d. division")
choice=input("Enter an option a,b,c or d: ")
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid choice!")