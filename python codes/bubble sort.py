def sequentialSearch(alist,item):
    pos=0
    found=False
    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    #output
    if found==True:
        return"%d was  found in indexed %d position."%(item,pos)
    else:
        return"%d was not found in the list."%(item)
testlist=[54,26,93,17,77,31,44,55,20,65]
print(sequentialSearch(testlist,17))
print(sequentialSearch(testlist,20))
