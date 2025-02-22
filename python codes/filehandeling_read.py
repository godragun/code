#example 1
fp=open('1.txt',"r")
data=fp.read(1)
print(data)
fp.close()

#example 2
fp=open('1.txt','r')
data=fp.read(6)
print(data)
fp.close()

#example 3
fp=open('1.txt','r')
data=fp.readline()
print(data)
fp.close()


#example 4
fp=open('1.txt','r')
line=fp.readline()
while line:
    print(line)
    line=fp.readline()
fp.close()


#example 5
fp=open('1.txt','r')
for i in fp:
    print(i)
fp.close()


#example 6
fp=open('1.txt','r')
data=fp.readlines()
print(data)
fp.close()

#example 7
fp=open('1.txt','r')
data=fp.readline()
for i in data:
    print(i)
fp.close()

#example 8
fp=open('1.txt','r')
data=fp.readlines()
for i in data:
    print(i)
fp.close()



















