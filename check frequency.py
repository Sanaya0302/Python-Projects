dict1={"codingal":1,"is":2,"fun":3}
print(dict1)
word=input("enter a word to search in dictionary: ")
if word in dict1:
    print("The frequency of",word,"is",dict1[word])
    