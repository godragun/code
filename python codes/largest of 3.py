n1=int(input("enter number: "))
n2=int(input("enter number: "))
n3=int(input("enter number: "))
if n1==n2 and n3==n2 :
    print('all nunbers are eaual')
elif n1<n2 and n3<n2:
    print('the largest number is :  ',n2)    
elif n1<n3 and n2<n3:
    print('the largest number is :  ',n3)

else:
    print('the largest number is :  ',n1)
    
