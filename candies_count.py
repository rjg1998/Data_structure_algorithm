def candies_count(children, candies):
    x=((candies * 2) ** (1 / 2))
    if x>int(x)+0.5:
        x=int(x)
        s=x
    else:
        x=int(x)
        s=x-1

    r=(s*(s+1))/2
    t= candies - r#extra chocolate
    y= s // children#times
    m= s % children#extra student
    l= [0] * children
    print(l)

    for i in range(children):
        l[i]=y*(i+1)+ ((y*(y-1))/2) * children

    for j in range (m):

        l[j]+= y * children + j + 1

    l[m]+=t

    return l
result=candies_count(1000,4)
print(result)