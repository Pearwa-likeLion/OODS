def bon(w):
	### Enter Your Code Here ###
    lst = []
    for i in w:
        if i in lst:
            one_based = ord(str(i)) - 96
            result = one_based * 4 
            break
        else:
            lst.append(i) 
    return result
secretCode = input("Enter secret code : ")
print(bon(secretCode))