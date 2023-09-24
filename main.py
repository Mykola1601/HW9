#  HW9
import sys


phone_book = {
    'Nik':'0935609516',
    'Anna':'0993331122',
}


# greetings
def greeting(_):
    print("How can I help you?")

# add contact
def add(text=""):
    text = text[text.find("add"):]
    words = text.split()[1:3]
    phone_book[words[0].title()] = words[1]
    print(words[0].title()+" saved with number "+ words[1])

# change contact if exist
def change(text=""):
    text = text[text.find("change"):]
    words = text.split()[1:3]
    if words[0].title() in phone_book.keys():
        phone_book[words[0].title()] = words[1]
        print(words[0].title()+" change number to "+ words[1])
    else:
        print("no contact")

# search contact 
def phone(text=""):
    text = text[text.find("phone"):]
    words = text.split()[1:3]
    if words[0].title() in phone_book.keys():
        print(words[0].title()+' -> '+phone_book[words[0].title()] )
    else:
        print(words[0].title(),' not exist in phone book')

# show all
def show(text=""):
    print(phone_book)

# exit program
def exit(_):
    # print("Good bye!")
    sys.exit('Good bye!\n')


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
            p = (dic[kee])
            return p(text)
    return print("do not undestend")

print("I'm BOT, hello!!!")

while True:
    user_input =  (input(">>>"))
    find_command( user_input)



