def merge(arr1,arr2):
    arr3=[None]*(len(arr1)+len(arr2))
    i,j,k=0,0,0
    while i< len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3[k] = arr1[i]
            i=i+1
            k=k+1

        else:
            arr3[k] = arr2[j]
            j = j + 1
            k = k + 1
    while i<len(arr1):
        arr3[k]=arr1[i]
        i=i+1
        k=k+1
    while j<len(arr2):
        arr3[k]=arr2[j]
        j=j+1
        k=k+1
    mid = (len(arr3)) // 2
    if len(arr3) % 2 == 0:
        median = (arr3[mid] + arr3[mid-1]) / 2
    else:
        median = arr3[mid]
    return median
arr1=[1,12,15,26,38]
arr2=[2,13,17,30,45,100,200]

result=merge(arr1,arr2)
print(result)
