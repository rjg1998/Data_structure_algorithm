def palindrome(a):
    if str(a)[::]==str(a)[::-1]:
        return True
    else:
        return False
result=palindrome(12345543218)
print(result)