def max_area(arr):

    area=0
    x=0
    y=0

    for i in range (len(arr)):
        for j in range (i-1,-1,-1):
            x=i
            if j==0:
                if arr[j]<arr[i]:
                    x=1
                else:
                    x=0
            else:
                if arr[j] < arr[i]:
                    x = j + 1
                    break

        for j in range(i+1,len(arr)):
            y=i
            if j==len(arr)-1:
                if arr[j]<arr[i]:
                    y=len(arr)-2
                else:
                    y=len(arr)-1
            else:
                if arr[j] < arr[i]:
                    y = j - 1
                    break
        new_area= (y-x+1)*arr[i]
        if new_area>area:
            area=new_area

    return area
arr=[2,4,3,6,1,5,8,12]
print(max_area(arr))

