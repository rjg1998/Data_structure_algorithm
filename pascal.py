def pascal(A):
    if A <= 0:
        return []
    result = [[1]]
    for r in range(1, A):
        row = [1]
        for i in range(1, r):
            row.append(result[r - 1][i - 1] + result[r - 1][i])
        row.append(1)
        result.append(row)
    for i in range (len(result)):
        m=str(result[i])
        print(m[1:len(m)-1])


pascal(3)
