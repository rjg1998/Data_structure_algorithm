def total_water(arr):
    start=0
    extra_brick=0
    total_water=0
    #to get the index of maximum no.
    max_no_index=arr.index(max(arr))
    #total_water will be 0 if len of arr is less than 2
    if len(arr)>2:
        #total water till max no's index
        for i in range (1,max_no_index+1):
            if arr[start]>arr[i]:
                #to subtract the extra brick
                extra_brick=extra_brick-arr[i]

            if arr[start]<=arr[i]:
                #to add total water and subtracting the units of brick
                total_water=extra_brick+(i-start-1)*arr[start]+total_water
                extra_brick=0
                start=i

        start = len(arr)-1
        extra_brick = 0
        #total water from last to max no's index
        for j in range(len(arr) - 2, max_no_index-1 , -1):
            if arr[start] > arr[j]:
                extra_brick = extra_brick - arr[j]

            if arr[start] <= arr[j]:
                total_water = extra_brick + (start - j - 1) * arr[start] + total_water
                extra_brick=0
                start = j

    return total_water
arrs=[[4,3,2,1],[1,2,3,4],[1,0,1,0,2],[4,3,2,1,0,1,2,1],[4,3,2,1,0,1,2,3,4],[1,2,3,0,3,2,5],[1,1,1,1,1],[1,2,3,5,3,2,1]]
for arr in arrs:
    result=total_water(arr)
    print(result)
