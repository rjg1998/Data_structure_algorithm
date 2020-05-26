def next_no(arr):
    n=len(arr)-1
    if arr[-1]==9:
        
        for i in range (n,-1,-1):
            if i>0:
                if arr[i]==9:
                    arr[i]=0
                else:
                    arr[i]=arr[i]+1
                    break
            else:
                if arr[i]!=9:
                    arr[i] = arr[i] + 1
                    return arr
                else:
                    arr[0]=1
                    arr.append(0)
                    return arr
    else :
        arr[-1]=arr[-1]+1
    return arr
#arr=[1,9,9]
arrs=[[9,9,9],[1,2,9],[1,0,0,0],[1,9,9],[9],[0],[1,1,1,9,9],[9,9]]
for arr in arrs:
    result=next_no(arr)
    print(result)