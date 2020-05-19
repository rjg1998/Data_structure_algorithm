def sub_array(arr):
    x=[]
    for j in range (1,len(arr)):
        for i in range (len(arr)):
            if i+j<len(arr)+1:

                x.append(arr[i:i+j])

    return x
#result=sub_array([1,2,3,4,5])
#print(result)
def max_sum(arr):
    y=sub_array(arr)
    max=-10000000000
    for i in range (len(y)):
        m=0
        for j in range (len(y[i])):
            m=y[i][j]+m
            if max < m:
                max = m
    return max
result=max_sum([-2,1,-3,4,-1,2,1,-5,4])
print(result)

