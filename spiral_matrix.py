def spiralOrder(A):
    S = []
    top= 0

    m = len(A)
    n = len(A[0])
    bottom = m - 1
    right = n - 1
    left = 0
    direction = 0
    while (top <= bottom and left <= right):
        if (direction == 0):
            for i in range(left, right + 1):
                S.append(A[top][i])
            top = top + 1

        if (direction == 1):
            for i in range(top, bottom + 1):
                S.append(A[i][right])
            right = right - 1

        if (direction == 2):
            for i in range(right, left - 1, -1):
                S.append(A[bottom][i])
            bottom = bottom - 1

        if (direction == 3):
            for i in range(bottom, top - 1, -1):
                S.append(A[i][left])
            left = left + 1
        direction = direction + 1
        if direction > 3:
            direction = 0
    return S
#A=[[1,2,3],[5,6,7],[13,11,12]]
#A=[[1,9,11,2],[6,7,0,13],[5,9,10,17]]
A=[[1,9,11,2],[6,7,0,13],[5,9,10,17],[8,5,12,7]]
result=spiralOrder(A)
print(result)
