def  asc_dsc(arr):
    if len(arr)<3:
        print('invalid input')
    if len(arr)==3:




    if len(arr)>3:
        for i in range(3):

            if arr[i] < arr[i + 1] < arr[i + 2]:
                print("asc_rotated")
                break
            if arr[i] > arr[i + 1] > arr[i + 2]:
                print("dsc_rotated")
                break


arr=[1,7,6]
asc_dsc(arr)