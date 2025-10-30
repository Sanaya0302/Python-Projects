test_dict={"codingal":2,"is":2,"for":2,"coding":1}
K=2
count=0
for i in test_dict:
    if test_dict[i]==2:
        count=count+1
print("count is",count)
print("original dictionary is",test_dict)