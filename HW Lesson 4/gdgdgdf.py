class roman_numeral:
    def __init__(self):
        self.roman_dict={
            1000: "M",
            900: "CM",
            500: "D",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
    def convert(self,num):
        if num in self.roman_dict:
            return self.roman_dict[num]
        else:
            print("Not Found")
num=int(input("Enter a Number: "))
obj=roman_numeral()
print("roman numeral:",obj.convert(num))