#  HW9

def gritting(_):
    print("How can I help you?")

def add(text=""):
    print(text)
    print("adding")

def change(text=""):
    print("chsnging")

def phone(text=""):
    print("phone read")

def show(text=""):
    print("showing")

def exit(_):
    print("Good bye!")


dic = {
    "hello":gritting,
    "add":add,
    "change":change,
    "phone":phone,
    "exit":exit,
    "close":exit,
    "good bye":exit,
}

# find command in text
def find_command(text=""): 
    text = text.lower()
    for kee in dic.keys():
        if kee in text:
            print("====",kee)
            p = (dic[kee])
            return p(text)
    return print("waiting")



find_command( " first seKOnd hello mister")





