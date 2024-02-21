from functools import reduce

l = [10,20,30,40,50]

l1 = reduce(lambda x,y:x+y,range(1,101))

print(l1)