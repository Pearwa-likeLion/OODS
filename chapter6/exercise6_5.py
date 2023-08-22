# def segment(text: str, language: list[str],word) -> bool:
#     if language == []:
#         return
#     else:
#         print(text) # Write here
#         print(language) 
#         if language[0] not in text:
#             print("False")   
#             return    
#         segment(text,language[1:],word)

# def converttolst(lst,l,output):
#     if lst == []:
#         return
#     else:
#         cleaned_item = lst[0].strip("' ").strip()
#         output.append(cleaned_item)
#         return converttolst(lst[1:],l-1,output)
        

# str = ""
# lst = []
# outputlst = []
# inp = input("Enter list[str]: ").split(",")
# str = inp[0]
# lst = inp[1:]
# word = ""
# converttolst(lst,len(lst),outputlst)
# # print(outputlst)
# segment(str,outputlst,word)

inp = input('Enter list[str]: ').split("'")[1::2]
word, parts = inp[0], inp[1:]

def segment(text, word_list):
    if not text:
        return True
    
    if not word_list:
        return False
    
    t = word_list[0]
    if t and t in text:
        remaining_text = text.replace(t, "", 1)
        # print(remaining_text)
        if segment(remaining_text, word_list) or segment(text, word_list[1:]):
            return True
        
    return segment(text, word_list[1:])

print(f"text: str = '{word}'")
print(f"lang: list[str] = {parts}")
print(f"segment(text, lang) -> {segment(word, parts)}")