l = [0,1,2,3,4,5,6,7,8,9,10]

def doubleit(n):
    return n*n

# l1 = list(map(doubleit,l))

l1 = list(map(lambda n:n*n,l))
print(l1)