#  HW9

def gritting():
    print("How can I help you?")

def add():
    print("adding")

def change():
    print("chsnging")

def phone():
    print("phone read")

def show():
    print("showing")

def exit():
    print("good bye")


dic = {
    "hello":gritting,
    "add":add(),
    "change":change(),
    "phone":phone(),
    "exit":exit(),
    "close":exit,
    "good bye":exit,
}


def find_command(text=""): 
    text = text.lower()
    words = text.split()
    for word in words:
        # print(word)
        if word in dic:
            print("====",word)
            return dic[word]
        # else: 
        #     return print("error command")
    return 



find_command( "sz rtfgyd helLO ssr")





