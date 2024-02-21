def isEven(n):
    if n%2==0:
        return True
    else:
        return False

l = [0,1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(lambda n:n%2==0,l))

# l1 = list(filter(isEven,l))

print(l1)

