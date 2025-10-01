def con(decimal_num):
    if decimal_num == 0:
        return "0"
    binary_representation=""
    while decimal_num > 0:
        remainder = decimal_num % 2
        print("the remainder is ",remainder)
        binary_representation = str(remainder) + binary_representation
        print("the binary_representation is ",binary_representation)
        decimal_num //=2
        print("the decimal_num is ",decimal_num)
    return binary_representation

num=int(input("Enter a decimal number which you want to convert into a binary number: "))  
print( "The binary number is ",con(num))


