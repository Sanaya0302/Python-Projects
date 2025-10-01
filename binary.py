def convert(number):
    if number == 0:
      return 0  
    binary=""
    while number > 0:
        remainder=number%2
        binary= str(remainder)+binary   
        number //=2
    return binary

decimalNum=int(input("Enter a decimal number which you want to convert into a binary number: "))  
print( "The binary number is ",convert(decimalNum))