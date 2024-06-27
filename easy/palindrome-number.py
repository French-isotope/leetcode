def isPalindrome(x: int) -> bool:
    if( x < 0):
        return False
    num = x
    reversed_num = 0
    while num != 0:
        reversed_num *= 10
        reversed_num += (num % 10)
        num //= 10
    return x == reversed_num


print(isPalindrome(101))