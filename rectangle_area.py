class points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def rect_area(l1,l2,r1,r2):
    a=[l1.x,l2.x,r1.x,r2.x]
    b=[l1.y,l2.y,r1.y,r2.y]
    a.sort()
    b.sort()
    area=(a[2]-a[1])*(b[2]-b[1])
    return area
if __name__=="__main__":
    l1=points(0,10)
    l2=points(10,0)
    r1=points(5,5)
    r2=points(15,0)

    result=rect_area(l1,l2,r1,r2)
    print(result)

