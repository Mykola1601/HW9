#  HW9
import sys
import re

phone_book = {
    'Nik':'0935609516',
    'Anna':'0993331122',
}

def normalize_phone(text = ''):
    numbers = re.findall('\d+', text)
    phone = (''.join(numbers))  
    if   12 >= len(phone) >= 10:
        return "+38"+phone[-10:]
    else:
        print('Phone number ERROR')
        return None


# greetings
def greeting(_):
    print("How can I help you?")

# add contact
def add(text=""):
    text = text[text.find("add"):]
    phone = normalize_phone(text)
    words = text.split()[1:]
    name = words[0].title()
    phone_book[name] = phone
    print(name+" saved with number "+ phone)

# change contact if exist
def change(text=""):
    text = text[text.find("change"):]
    phone = normalize_phone(text)
    words = text.split()[1:]
    name = words[0].title()
    if name in phone_book.keys():
        phone_book[name] = phone
        print(name+" change number to "+ phone)
    else:
        print("no contact")

# search contact 
def phone(text=""):
    text = text[text.find("phone"):]
    words = text.split()[1:]
    name = words[0].title()
    if name in phone_book.keys():
        print(name+' -> '+phone_book[name] )
    else:
        print(name,' not exist in phone book')

# show all
def show(text=""):
    print(phone_book)

# exit program
def exit(_):
    # print("Good bye!")
    sys.exit('Good bye!\n')

# dict for commands
dic = { 
    "hello":greeting,
    "add":add,
    "change":change,
    "phone":phone,
    "show all":show,
    "show":show,
    "exit":exit,
    "close":exit,
    "good bye":exit,
}

# find command in text
def find_command(text=""): 
    text = text.lower()
    for kee in dic.keys():
        if kee in text:
            # print("====",kee)
            func = dic[kee]
            return func(text)
    return print("do not undestend")

print("I'm BOT, hello!!!")

while True:
    user_input =  (input(">>>"))
    find_command( user_input)



