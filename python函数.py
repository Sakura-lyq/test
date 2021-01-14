help(abs)
abs(-33)
max(12,77,34,56,33)
print(int(13.33))
print(float(13.33))
print(str(13.33))
print(bool(13.33))
print(bool(0))
print(hex(33))

from absert import my_abs
print(my_abs(-4))


def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError('bad operand type')
    if x>=0 :
        return x
    else:
        return -x
print(my_abs(88))

import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100, 100, 60, math.pi/6)
print(x,y)

import math
def quadratic(a,b,c):
    Z=b**2-4*a*c
    if Z==0:
        x=-c/b
        return x
    elif Z>=0:
        x1=(-b+math.sqrt(b**2-4*a*c))/2/a
        x2=(-b-math.sqrt(b**2-4*a*c))/2/a
        return x1,x2
    else:
        print("此方程无解")
print(quadratic(2,3,1))


##函数的参数
def students(age,name,height,weight):
    print('age:',age)
    print('name:',name)
    print('height:',height)
    print('weight:',weight)
students(11,'lisa',160,50)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1,2,3)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('lin',16,33,25,16,city='Nanjing',job='Teacher')

##递归函数
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
fact(4)
fact(100)