# 1
def f(a,b):
    return 18*a*b
print(f(1,1))

# 2
summa = 0
for i in range(1,11):
    summa +=i
print(summa)

# 3
def is_even(n):
    if n % 2 == 0:
        return (n,' is even')
    else:
        return (n,' is odd')
print(is_even(4))

# 4
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# 5
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    return True

# 6
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result*a[i]
        return result
