
    
    

#example 1
def fun():
    global x
    print('x is',x)
    x=2
    print('change local x to', x)
x=50
fun()
print ('value of x is a',x)


#example 2
global_var="hello"
def ex1():
    local_var='python'
    print(global_var)
    print(local_var)
ex1()
print(global_var)
print(local_var)

