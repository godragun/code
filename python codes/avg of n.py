tot= 0
count=1
while count <=10:
    num = float(input('Enter number: '))
    if num>=0 and num<=100:
        tot += num
        count +=1
    else:
        print('error')


avg = tot / 10
print('Average of numbers:  ', avg)
