#example 1

def a():
    print('hello world')
a()    
print('hi')
a()
print('example of function')
a()


#example 2

def sum(x,y):
    tot=x+y
    print('total is',tot)
sum(6,5)
a=int(input ('enter number one :'))
b=int(input ('enter number two :'))
sum(a,b)

#example 3 (can be use at any place)
a=int(input ('enter number one :'))
b=int(input ('enter number two :'))
sum(a,b)


#example 4
def example(x,y):
    tot=x+y
    return tot
a=10
b=8
print(example(a,b))


#example 5

def example(x,y):
    return x+y
a=10
b=5
c=example(6,8)
print(c)
print(example(a,b))

#example 6

def arg(word,number=3):
    print(word*number)
arg("hello")
arg('hi ',5)



#example 7

def fun(a,b=5,c=10):
    print('a is',a,",","b is",b,",",'and c is',c)
fun(3,7,)
fun(25,c=24)


#example 8
def getmax(a,b):
    if a>b:
        return a
    else:
        return b
x=getmax(4,7)
print(x)
print(getmax(-3,-4))





    






































