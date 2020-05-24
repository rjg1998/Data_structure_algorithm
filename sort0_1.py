def sort(arr):
   left=0
   right=len(arr)-1
   i=0
   #for i in range (len(arr)):
   while left < right :

       if arr[left]==0:
           left=left+1


       elif arr[left]==1 and arr[right]==0:
           arr[left]=0
           arr[right]=1
           left=left+1
           right=right-1



       elif arr[right]==1:
           right=right-1








   return arr
arr=[0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1]
result=sort(arr)
print(result)