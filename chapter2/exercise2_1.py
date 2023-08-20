# M=1000    CM=900    D=500    CD=400,
# C=100    XC=90    L=50    XL=40,
# X=10    IX=9    V=5    IV=4    I=1
# เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I
#____________________________________________________________#

class translator:

    def deciToRoman(self, num):
        lst = []
        lt = ''
        n = int(num)
        while n > 0:
            if n - 1000 >= 0 :
                n -= 1000
                lt += 'M'

            elif n - 900 >= 0:
                n -= 900
                lt += 'CM'

            elif n - 500 >= 0:
                n -= 500
                lt += 'D'
            elif n - 400 >= 0:
                n -= 400
                lt += 'CD'

            elif n - 100 >= 0:
                n -= 100
                lt += 'C'
            elif n - 90 >= 0:
                n -= 90
                lt += 'XC'

            elif n - 50 >= 0:
                n -= 50
                lt += 'L'
            elif n - 40 >= 0:
                n -= 40
                lt += 'XL'

            elif n - 10 >= 0:
                n -= 10
                lt += 'X'
            elif n - 9 >= 0:
                n -= 9
                lt += 'IX'
            
            elif n - 5 >= 0:
                n -= 5
                lt += 'V'
            elif n - 4 >= 0 :
                n -= 4
                lt += 'IV'

            elif n - 1 >= 0 :
                n -= 1
                lt += 'I'
                
        return lt
    def romanToDeci(self, s):
        number = 0
        c=0
        for i in s:
            if i == 'M' :
                number += 1000
            elif i == 'C' :
                if c +1 <= len(s)-1:
                    if s[c+1] == 'M' :
                        number -= 100
                    elif s[c+1] == 'D':
                        number -= 100
                    else:
                        number += 100
                else:
                        number += 100
            elif i == 'D':
                number += 500
            elif i == 'L':
                number += 50
            elif i == 'X':
                if c +1 <= len(s)-1:
                    if s[c+1] == 'C':
                        number -= 10
                    elif s[c+1] == 'L':
                        number -= 40
                    else:
                        number += 10
                else:
                        number += 10
            elif i == 'V':
                number += 5
            elif i == 'I':
                if c + 1 <= len(s)-1:
                    if s[c+1] == 'V':
                        number -= 1
                    elif s[c+1] == "X":
                        number -= 1
                    else:
                        number += 1
                else:
                        number += 1
            c += 1
        return number

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))