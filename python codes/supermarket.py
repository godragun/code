n=int(input('enter number of products :'))
c=0
tot=0      
for i in range (c,n):
    c=+1
    u=int(input('enter unit price :'))
    q= int(input('enter quntity :'))
    tot= tot+(u*q)
if tot>=500:
    d=(5/100)*tot
    tot=tot-d
    print("total= ",tot,",","discount",d)

else:
    print('no discount')
    print("total= ",tot  )
