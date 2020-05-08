def low_no(arr):
    if len(arr)==1:
        return arr[0]
    elif len(arr)==0:
        return 'no number in array'
    else:
        for i in range (len(arr)-1):
            if arr[i]>arr[i+1]:
                x= arr[i+1]
                break
            else :
                x= arr[0]
    return x
arr=[2,3,4,0,1]
result=low_no(arr)
print(result)