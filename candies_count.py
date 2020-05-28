def candies_count(a,b):
    x=((b*2)**(1/2))
    if x>int(x)+0.5:
        x=int(x)
        s=x
    else:
        x=int(x)
        s=x-1

    r=(s*(s+1))/2
    t=b-r#extra chocolate
    y=s//a#times
    m=s%a#extra
    l=[0]*a
    print(l)

    for i in range(a):
        l[i]=y*(i+1)+((y*(y-1))/2)*a

    for j in range (m):

        l[j]+=y*a+j+1

    l[m]+=t

    return l
result=candies_count(1000,1000)
print(result)