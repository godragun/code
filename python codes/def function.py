def marks (numofstu,numofsub):
    total=0
    while numofstu >= 1:
        name = input ("enter the studnt's name = ")
        a=x= numofsub
        y=1
        while x>=1:
            s=int(input('enter the marks = '))
            total =total +s
            x=x-1
        avg= total /a
        print (name , ':',"total is =",total,',avrage is =',avg)
        numofstu=numofstu-1
print (marks(3,3))        
