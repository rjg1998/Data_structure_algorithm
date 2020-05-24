def sort(arr):
    l=0
    m=0
    r=len(arr)-1
    while m<=r:
        if arr[m]==0:
            arr[m],arr[l]=arr[l],arr[m]
            l=l+1
            m=m+1

        elif arr[m]==1:
            m=m+1
        elif arr[m]==2:
            arr[m],arr[r]=arr[r],arr[m]
            r=r-1
    return arr
arr=[0,1,0,1,1,0,2,1,0,2,0]
result=sort(arr)
print(result)