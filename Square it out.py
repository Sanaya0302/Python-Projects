def square_odd_even(start,end):
    while start<end:
        squares=[]
        even_numbers=[]
        odd_number=[]
    for num in range(start,end+1):
        square=num*num
        squares.append(square)
        if square % 2==0:
            even_numbers.append(square)
        else:
            odd_number.append(square)
            print("Square:",square)
            print("Even squares:",even_numbers)
            print("Odd squares",odd_number)
        start=int(input("Enter start number: "))
        end=int(input("Enter end number: "))
        square_odd_even(start,end)

