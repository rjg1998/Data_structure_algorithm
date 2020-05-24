def ap_miss(arr):
    n=len(arr)
    mid=n//2
    diff=(arr[-1]-arr[0])/n
    if arr[mid] - arr[mid - 1] != diff:
        return arr[mid - 1] + diff
    if arr[mid + 1] - arr[mid] != diff:
        return arr[mid] + diff
    if arr[mid] == arr[0] + mid * diff:
        return ap_miss(arr[mid + 1:])
    if arr[mid] > arr[0] + mid * diff:
        return ap_miss(arr[:mid])




arr=[33,30,27,21,18,15,12]
result=ap_miss(arr)
print(result)