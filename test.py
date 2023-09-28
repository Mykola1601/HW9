import re

text = 'add Mike   + 3 8 067 123 45-67'
#     result = []
# iterator = re.finditer(r"[add]+[www|/|:]+[.]{0,1}[\w]+\.[a-zA-Z]{2,7}", text)
# iterator = re.finditer(r"add+ \w+ +[+3|\d][\d| |\-|\(|\)]+", text)
# print ( iterator)
# for match in iterator:  
#     print(match.group())

# numbers = re.findall('\d+', text)
# phone = (''.join(numbers))  
# phone = "+38"+phone[-10:]

# print(phone)


# text = text[text.find("add"):]
# print (text)
# text = text.removeprefix("add ")
# print (text)

text = '+3-8 0 97 (333) 44 - 22'
numbers = re.findall('\d+', text)
# print(numbers)
phone = (''.join(numbers))  
# print ( (phone))

# if   12 >= len(phone) >= 10:
#     return "+380"+phone[-9:]
# else:
#     # print('Phone number ERROR')
#     return None

iterator = re.finditer(r"0[\d]{9}", phone)
if ( iterator):
    for match in iterator:  
        print(match.group())


