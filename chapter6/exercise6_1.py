def print1ToN(n):
    #code here
    if n <= 1:
        return 1
    else:
        return f"{print1ToN(n-1)} {n}"
    

def printNto1(n):
    if n <= 1:
        return 1
    # print(n , end=" ")
    return f"{n} {printNto1(n-1)}"
    

n = int(input("Enter Input : "))

print(print1ToN(n),end=" ")
print(printNto1(n))