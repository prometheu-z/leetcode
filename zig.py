def convert(s: str, numRows: int) -> str:

    t = ""
    p = 2* numRows -2
    atual = 0
    prox = 0
    c = 0
    l = 1
    while l <= numRows:
        if numRows == 1 or numRows >= len(s):
            return s
        if(prox >= len(s)):
            l += 1
            c = 0
            atual += 1
            prox = atual

        if l > 1:
            if c == 0:
                c = 1
            else:
                c = 0
            if c == 0:
                p = abs(2*numRows -2 - p)
                if p == 0:
                    p = 2*numRows - 2
            else:
                p = 2*numRows - 2*l
                if p == 0:
                    p = 2*numRows - 2

                    
        if l > numRows:
            break
        
        if numRows == 1 or (prox >= len(s)):
            t = s
            break
        
        t = t+s[prox]

        

        prox += p
            
            
        

    return t


print(convert("PAYPALISHIRING", 3))