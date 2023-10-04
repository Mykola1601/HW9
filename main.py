#  HW9

import sys
import re

phone_book = {'Nik' :'+380935609516', 'Anna':'+380993331122'}   #some names
 
  
# =================================================

def normalize_phone(text=''):
    numbers = re.findall('\d+', text)
    phone = (''.join(numbers))
    iterator = re.finditer(r"0[\d]{9}", phone)
    if iterator:
        for match in iterator:
            phone = match.group()
            return "+38"+phone
    else:
        return None

# =================================================




# decor
def errors(func):
    def inner(*args):
        try:
            return func(*args)
        except :                  #any errors
            return "Give me name and phone please !!!"
    return inner


# =================================================


# greetings
def greeting(_):
    return ("How can I help you?")


# add contact
@errors
def add(text=""):
    text = text.removeprefix("add ")  #remove command
    name = text.split()[0].title()    #get Name
    text = text.removeprefix(name)    #remove Name
    if not len(text) >9:
        return 'Enter valid  phone'
    phone = normalize_phone(text)
    if not phone:
        return 'Enter valid phone'
    if not name in phone_book.keys():
        phone_book[name] = phone
        return name+" saved with number "+ phone
    else:
         return name+' allready exist in phone book'


# change contact if exist
@errors
def change(text=""):
    text = text.removeprefix("change ")
    name = text.split()[0].title()
    text = text.removeprefix(name)
    if not len(text) >9:
        return 'Enter valid name & phone'
    phone = normalize_phone(text)
    if not phone:
        return 'Enter valid phone'
    if name in phone_book.keys():
        phone_book[name] = phone
        return name+" change number to "+ phone
    else:
        return (f"no {name} in phone book")


# search contact 
def phone(text=""):
    text = text.removeprefix("phone ")
    name = text.split()[0].title()
    if name in phone_book.keys():
        return name+' -> '+phone_book[name] 
    else:
        return name+' not exist in phone book!!!' 


# show all
def show(_):
    list = ''
    for nam, ph in phone_book.items() :
        list += (f"{nam} --> {ph} \n")
    return list


# exit program
def exit(_):
    # print("Good bye!")
    return sys.exit('Good bye!\n')


# dict for commands
dic = { 
    "hello":greeting,
    "add ":add,
    "change ":change,
    "phone ":phone,
    "show all":show,
    "show":show,
    "exit":exit,
    "close":exit,
    "good bye":exit,
}


# find command in text > return dict key
def find_command(text=""): 
    text = text.lower()
    for kee in dic.keys():
        if kee in text:
            # func = dic[kee]
            return kee
    return None


def main():
    print("I'm Phone_Book_BOT, HELLO!!!")

    # loop forever
    while True:
        user_input =  (input(">>>"))
        comand = find_command(user_input)
        if not comand:
            print("Do not undestend, try again")
        else:
            out = dic[comand](user_input)
            print(out)




# ========================================
if __name__ == "__main__":
    main()



