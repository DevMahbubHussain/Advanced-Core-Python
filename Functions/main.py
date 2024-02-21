def calculate(a,b):
    print('The Sum',a+b)
    print('The Sub',a-b)
    print('The Mult',a*b)

calculate(10,20)


def wish(name):
    print("Hello",name,"Good Evening")
wish("Mahbub")


def square(num):
    sq = num*num
    print('The Square of {} is {}'.format(num,sq))

square(2)


def add(a,b):
    sums = a+b
    return sums

print(add(10,20))

def f1():
    print('Hello')

x = f1()

print('The return value',x)


#  Write a function to find  Factorial of given number

def fact(num):
    result = 1
    while num>=1:
        result = result*num
        num = num-1
    return result

for i in range(1,5):
   print('The Factorial of', i, 'is', fact(i))

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

x,y = sum_sub(10,20)

print('The sum is ',x)
print('The sub is ',y)


# Positional Arguments 

# keyword arguments 

def summa(a,b):
    print(a-b)

summa(b=500,a=300)

# variable lenght arguments 

def f1(*n):
    print('variable lenght arguments')
    print(type(n))
    print(n)

f1()
f1(10)
f1(10,20)

def sumq(*n):
    total= 0
    for x in n:
        total = total + x
    print('Summation',total)

sumq(10)
sumq(10,1)

def f2(s,*y):
    print(s)
    print(y)
f2(10,20,30,40)