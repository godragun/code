a=['dog','cat','dog',100,56,78,78,78]
print(a[:2]+['parrot',89,'cow',2*2])
print(a)


print(3*a)
print(3*a[:2]+['hello'])
for x in range(0,1):
    t=int(input('enter number'))
    a.append(t)
print(a)
#count

print(a.count(78))

#index

print(a.index(78))

#insert

a.insert(2,100)
print(a)

#remove
a.remove(100)
print(a)

##pop
a.pop()
print(a)

a.pop(3)
print(a)


#reverse

a.reverse()
print(a)



#sort

b=[78,67,98,987]
b.sort()
print(b)
b.reverse()
print(b)

c=['cow','can','pappy','paty','antyh']
c.sort()
print(c)


#extend
h=[]
h.extend('cat')
print(h)





































