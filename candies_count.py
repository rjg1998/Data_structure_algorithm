def candies_count(children, candies):
    x=((candies * 2) ** (1 / 2))
    #s is total no. of times chocolate will be distributed
    if x>int(x)+0.5:
        x=int(x)
        s=x
    else:
        x=int(x)
        s=x-1
    # r is total chocolates in exact amount
    r=(s*(s+1))/2
    t= candies - r#extra chocolate after exact amount
    # y is no. of exact rounds 
    y= s // children#times
    # m is no. of students after exact rounds 
    m= s % children#extra student
    l= [0] * children
    print(l)

    for i in range(children):
        l[i]=y*(i+1)+ ((y*(y-1))/2) * children# sum of ap in exact rounds

    for j in range (m):

        l[j]+= y * children + j + 1# leftover students in last round

    l[m]+=t# extra chocolate to last student

    return l
result=candies_count(1000,4)
print(result)
