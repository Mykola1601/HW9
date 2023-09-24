import re

text = 'add Mike   + 3 8 067 123 45-67'
#     result = []
# iterator = re.finditer(r"[add]+[www|/|:]+[.]{0,1}[\w]+\.[a-zA-Z]{2,7}", text)
# iterator = re.finditer(r"add+ \w+ +[+3|\d][\d| |\-|\(|\)]+", text)
# print ( iterator)
# for match in iterator:  
#     print(match.group())

numbers = re.findall('\d+', text)
phone = (''.join(numbers))  
phone = "+38"+phone[-10:]

print(phone)