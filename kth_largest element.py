def partition(arr,low,high):
    pi=arr[high]
    j=low-1
    for i in range (low,high):
        if arr[i]<=pi:
            j=j+1
            arr[j],arr[i]=arr[i],arr[j]



    arr[j+1],arr[high]=arr[high],arr[j+1]
    return (j+1)
def k_element(arr,k,low,high):


        pi = partition(arr,low,high)

        if k<pi+1:
            return k_element(arr,k,low,pi-1)
        elif k==pi+1:
            return arr[pi]
        elif k>pi+1:
            return k_element(arr, k, pi+1,high)
arr=[2,4,6,3,9,1,0,2,1]
result =k_element(arr,3,0,8)
print(result)