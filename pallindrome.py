def palindrome(a):
    n=len(str(a))
    if n==1:
        print('its a palindrome')
    else:
        for i in range(n // 2):
            if (a // 10 ** (n - 1 - i)) % 10 == (a % 10 ** (i + 1) // 10 ** i):
                if i == (n // 2) - 1:
                    print('its a palindrome')
            else:
                print('not a palindrome')
                break


palindrome(121)