class pairs:
    def twosum(self,nums,target):
        lookout={}
        for i,num in enumerate(nums):
            if target-num in lookout:
                return lookout[target-num],i
            lookout[num]=i
target=int(input("Enter a num between 10 and 130: "))
print("index1=%d index2=%d" % pairs().twosum((10,20,30,40,50,60,70),target))