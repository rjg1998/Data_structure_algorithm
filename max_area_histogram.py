def max_area(arr):

    area=0


    for i in range (len(arr)):
        left_pointer = 0
        righ_pointer = len(arr) - 1
        for j in range (i-1,-1,-1):#check the index of smaller no. than ith no. in the left side of i
            if arr[j] < arr[i]:
                left_pointer = j + 1
                break

        for j in range(i+1,len(arr)):#check the index of smaller no. than ith no. in the right side of i
            if arr[j] < arr[i]:
                righ_pointer = j - 1
                break
        #calculate the area
        new_area= (righ_pointer-left_pointer+1)*arr[i]
        if new_area>area:
            area=new_area

    return area
arrs=[[2,4,3,6,1,5,8],[1,1,1,1],[1,0,1,0,1],[0,0,0,1],[1,2,3,4,5],[5,4,3,2,1]]
for arr in arrs:
    print(max_area(arr))

