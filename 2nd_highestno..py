def second_highest(arr):
    if len(arr)<2:
        return ('invalid input')
    else:
        for i in range(2):
            max_ind = i
            for j in range(i + 1, (len(arr))):
                if arr[max_ind] < arr[j]:
                    max_ind = j
            arr[max_ind], arr[i] = arr[i], arr[max_ind]
        return arr[1]

arr=[23,45,67,12,36,90]

result=second_highest(arr)
print(result)