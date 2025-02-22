x=""
for i in range(1,10):
    if i % 2==0:
        x=x+str(i);
print(x)
bn=""
r=0
y=int(input("Enter Number:"))
while(y>0):
    r=y % 2
    bn=str(r)+bn
    y=y//2
print(bn)
bn=""
r=0
y=int(input("Enter Number:"))
while(y>0):
    r=y % 8
    bn=str(r)+bn
    y=y//8
print(bn)
bn=""
r=0
y=int(input("Enter Number:"))
while(y>0):
    r=y % 16                   
    bn=str(r)+bn
    if r==10:
        bn="A"
    elif r==11:
        bn="B"
    elif r==12:
        bn="C"
    elif r==13:
        bn="D"
    elif r==14:
        bn="E"
    elif r==15:
        bn="F" 
    y=y//16
print(bn)
    
    
