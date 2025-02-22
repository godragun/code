n=int(input('enter no of students:'))
c=0
x=0
while n>0:
    add=int(input('entr admisioon:'))
    m=int(input('enter  avg marks;'))
    if c<m:
        c=m
        x=add
    if 100>=m>=90:
        print(add,m,"gold")
    elif 89>=m>=85:
        print(add,m,"silver")
    elif 84>=m>=80:
        print(add,m,"bronze")
    elif 79>=m>=75:
        print(add,m,"merit")
    else:
        print('no medal')
    n=n-1
print('special medal',c,x)    
    
    
