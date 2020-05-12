def non_repeated_no(arr):

    for i in range (0,len(arr),2):
        if i==len(arr)-1:
            return arr[len(arr)-1]
        else:

            if arr[i]!=arr[i+1]:
                return arr[i]
arr1=[1,1,2,3,3,4,4,5,5]
arr2=[2,3,3,5,5,6,6]
arr3=[2,2,4,4,5,5,7]
arr4=[3,3,5,5,6,7,7,8,8,9,9]
assert non_repeated_no(arr1)==2
assert non_repeated_no(arr2)==2
assert non_repeated_no(arr3)==7
assert non_repeated_no(arr4)==6