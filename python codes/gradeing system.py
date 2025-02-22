n1=int(input("enter marks: "))
n=str(input('enter name : '))
if n1<0 and n1>100 :
    print('invalid number')
elif n1<=100 and n1>=75:
    print('very good an A:',n1,',',n)    
elif n1<=74 and n1>=65:
    print('good an B:',n1,',',n)
elif n1<=64 and n1>=55:
    print('can do better an C :',n1,',',n)
elif n1<=54 and n1>=35:
    print('improve an S:  ',n1,',',n)    
else :
    print('fail F:  ',n1,',',n)

