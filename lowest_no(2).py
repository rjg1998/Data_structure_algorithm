def lowest_no(arr):
    n = len(arr) // 2
    if len(arr)==2:
        return min(arr[0],arr[1])
    else:
        if arr[n - 1] > arr[n] and arr[n] < arr[n + 1]:
            return arr[n]
        if arr[n] < arr[0] and arr[n] < arr[len(arr) - 1]:
            return lowest_no(arr[:n])
        if arr[n] > arr[0] and arr[n] > arr[len(arr) - 1]:
            return lowest_no(arr[n:])
        if arr[n] > arr[0] and arr[n] < arr[len(arr) - 1]:
            return arr[0]





arr=[2]
result=lowest_no(arr)
print(result)