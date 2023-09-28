#  Sort by alphabet
def Alphabetword(word):
    for w in word:
        if w >= "a" and w <= "z":
            return ord(w)

def SortByAlphabet(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if Alphabetword(l[j]) > Alphabetword(l[j+1]):
                l[j] , l[j+1] = l[j+1] , l[j]
    return l

inp = input("Enter Input : ").split(" ")
print(" ".join(SortByAlphabet(inp)))

# Enter Input : 932c 832u32 2344b
# 2344b 932c 832u32

# Enter Input : 99a 78b c2345 11d
# 99a 78b c2345 11d


# Enter Input : 572z 5y5 304q2
# 304q2 5y5 572z

