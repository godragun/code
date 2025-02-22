a = {1:'tomato', 2:'potato', 3:'banana',4:'fish', 5:'egg', 6:'applesoda'}
print(a.keys())
print(a.items())
print(a.values())
print(a[3])

#copy
b=a.copy()
print(b)

#pop
a.pop(2)
print(a)

a.popitem()
print(a)



