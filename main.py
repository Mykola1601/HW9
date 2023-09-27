#  HW9

import sys
import re

phone_book = {
    'Nik' :'+380935609516',
    'Anna':'+380993331122',
}

def main():
    print("I'm Phone_Book_BOT, hello!!!")



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
        # text = text[text.find("add"):]
        text = text.removeprefix("add ")
        # print (text)
        phone = normalize_phone(text)
        if phone :
            words = text.split()
            name = words[0].title()
            phone_book[name] = phone
            print(name+" saved with number "+ phone)

    # change contact if exist
    def change(text=""):
        # text = text[text.find("change"):]
        text = text.removeprefix("change ")
        phone = normalize_phone(text)
        if not phone: return
        words = text.split()
        name = words[0].title()
        if name in phone_book.keys():
            phone_book[name] = phone
            print(name+" change number to "+ phone)
        else:
            print("no contact")

    # search contact 
    def phone(text=""):
        text = text.removeprefix("phone ")
        words = text.split()
        name = words[0].title()
        if name in phone_book.keys():
            print(name+' -> '+phone_book[name] )
        else:
            print(name,' not exist in phone book!!!')
            # name_input =  (input("Enter user name >>>"))
            # if not find_command(name_input):
            #     phone(text=name_input)


    # show all
    def show(text=""):
        for nam, ph in phone_book.items() :
            print(f"{nam} --> {ph} ")

    # exit program
    def exit(_):
        # print("Good bye!")
        sys.exit('Good bye!\n')

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

    # find command in text
    def find_command(text=""): 
        text = text.lower()
        for kee in dic.keys():
            if kee in text:
                func = dic[kee]
                return func(text)
        print("Do not undestend")
        return None



# loop forever
    while True:
        user_input =  (input(">>>"))
        find_command( user_input)




if __name__ == "__main__":
    main()
