s = lambda n:n*n
for i in range(1,11):
    print('The Square of {}'.format(i),s(i))


# Lambda function to find biggest of given Values
    
ss = lambda a,b:a if a>b else b
print('The  biggest number of 10,20',ss(10,20))