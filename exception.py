try:
    num=int(input("Enter a number: "))
    print("you have entered",num)
except ValueError as ex:
    print("exception",ex)

    