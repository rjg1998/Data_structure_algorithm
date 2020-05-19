def max_sum_v2(arr):
    max=-100000000000
    s=[]
    for i in range (len(arr)):

        for j in range (i+1,len(arr)+1):

            s.append(arr[i:j])

            l=sum(s[0])
            if l>max:
               max=l
            s=[]

    return max
result=max_sum_v2([-2,1,-3,4,-1,2,1,-5,4])
print(result)