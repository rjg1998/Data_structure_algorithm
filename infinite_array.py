def binary_search(arr,k,l,r):
    while l<r:
        mid=l+(l-r)//2
        if arr[mid]==k:
            return mid+1
        elif arr[mid]>k:
            return binary_search(arr,k,l,mid)
        elif arr[mid]<k:
            return binary_search(arr, k, mid+1,r)
    return -1    
        

    


def infinite_array(arr,k):
    i=0
    x=None
    while x!=k:
        if arr[2**i]==k:
            x=k
            return 2**i+1
        elif arr[2 ** i] > k:

            mid = (2 ** (i - 1) + 2 ** i) // 2
            if arr[mid] == k:
                x = k
                return mid+1
            elif arr[mid] > k:
                l=2**(i-1)+1
                r=mid-1
                return binary_search(arr, k,l,r)

            else:
                l=mid+1
                r=2**i
                return binary_search(arr, k, l,r)


        else:
            i = i + 1



arr=[2,3,4,7,9,11,13,17,18,20,21,23,26,28,50,100]
k=11
result=infinite_array(arr,k)
print(result)

