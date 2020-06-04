def duplicate(arr):
    x = 0
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            x = x + 1
            arr[x] = arr[i + 1]

    for j in range(x + 1, (len(arr))):
        arr[j] = 0
    return arr,x+1


arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6]
a,b = duplicate(arr)
print(a)
print(b)
