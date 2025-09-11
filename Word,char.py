word=input("Enter a word: ")
char=input("Enter a char: ")
i=0
count=0
while i<len(word):
    if word[i]==char:
        count=count+1
    i=i+1
print("Total no: of times",char,"has occured is",count)