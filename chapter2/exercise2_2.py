def weirdSubtract(n,k):
    while int(k) > 0:
        k -= 1
        if int(n) % 10 == 0 :
            n = n/10
        else:
            n -= 1
    return int(n)

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))