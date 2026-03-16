def reverse( x: int) -> int:
    m = 2147483647
    
    re = int(str(x)[::-1]) if x >= 0 else int("-"+str(abs(x))[::-1])
    if(re > m-1 or re < -m):
        return 0
    return re


print(reverse(123))