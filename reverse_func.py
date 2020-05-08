arr=[23,45,67,12,36]
def reverse_func(arr):
    n=len(arr)
    for i in range (n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    return arr
result = reverse_func(arr)
print(result)