def listy(words):
    num=0
    list=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            num=num+1
            list.append(i)
    print("Words having same letters at the starting and ending are",list)
    return num
count=listy(["sanaya","anaaya","advika"])
