def fibbonacci(n):
    a=[None]*n
    if n>=1:

        a[0]=0
    if n>=2:

        a[1]=1
    if n>2:

         for i in range (1,n-1):
            a[i+1]=a[i-1]+a[i]
    return a
result =fibbonacci(7)
print(result)