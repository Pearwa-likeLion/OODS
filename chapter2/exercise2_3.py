def odd_even(type, data, mode):
    d = []
    result = []
    str1 = ''
    if type == "S":
        for l in data:
            d.append(l)
    if type == "L":
        d = data.split(" ")
    if mode == "Odd":
        for i in range(0, len(d), 2):
            result.append(d[i])
    elif mode == "Even":
        for i in range(1, len(d), 2):
            result.append(d[i])
    
    if type == "S":
        for l in result:
            str1 += l
        return str1
    else:
        return result
    # elif type == "S":
print("*** Odd Even ***")
t, d, m = input("Enter Input : ").split(',')
print(odd_even(t,d,m))