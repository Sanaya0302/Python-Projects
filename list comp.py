num=int(input("enter a number: "))
even=[x for x in range(1,num+1)if x%2==0]
odd=[x for x in range(1,num+1)if x%2!=0]
print("Even numbers are",even)
print("Odd numbers are",odd)
fruit_list=["apple","banana","cherry","kiwi"]
new=map(str.title,fruit_list)
print(list(new))