def median_3(arr1,arr2):
    n = len(arr1) + len(arr2)
    i,j,counter=0,0,0
    a,b=0,0
    if (n)%2==1:
        if counter<=n//2+1:
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<arr2[j]:
                    i=i+1
                    counter=counter+1
                    if counter == n//2+1:
                        return arr1[i-1]


                elif arr2[j] < arr1[i]:
                    j = j + 1
                    counter = counter + 1
                    if counter==n//2+1:
                        return arr2[j-1]
            while i<len(arr1):
                i=i+1
                counter=counter+1
                if counter == n//2+1:
                    return arr1[i-1]

            while j<len(arr2):

                j=j+1
                counter=counter+1
                if counter == n//2+1:
                    return arr2[j-1]


    if (n)%2==0:
        if counter<n//2+1:
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<arr2[j]:
                    i=i+1
                    counter=counter+1
                    if counter == n//2:
                        a= arr1[i-1]
                    if counter == n//2+1:
                        b= arr1[i-1]
                        break



                elif arr2[j] < arr1[i]:
                    j = j + 1
                    counter = counter + 1
                    if counter==n//2:
                        a= arr2[j-1]
                    if counter==n//2+1:
                        b= arr2[j-1]
                        break
            while i<len(arr1):
                i = i + 1
                counter = counter + 1
                if counter == n // 2:
                    a = arr1[i - 1]
                if counter == n // 2 + 1:
                    b = arr1[i - 1]
                    break
            while j<len(arr2):
                j = j + 1
                counter = counter + 1
                if counter == n // 2:
                    a = arr2[j - 1]
                if counter == n // 2 + 1:
                    b = arr2[j - 1]
                    break

            return (a+b)/2


arr1=[1,3,4,7,8,10]
arr2=[2,5,9,11]

result=median_3(arr1,arr2)
assert result==6.0
ar1 = [1]  # 15
ar2 = [2]
result=median_3(ar1,ar2)
assert result==1.5