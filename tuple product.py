tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)
product=[]
for i in range(len(tuple1)):
    product.append(tuple1[i]*tuple2[i])
print(tuple(product))