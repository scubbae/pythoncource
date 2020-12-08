formError = 0
userName = True
msg =""


def form():
    if formError == 0 and userName == True:
        msg = "Congrats! you have no errors"
        print(msg)
    else:
        msg = "Oh no, u have some errors"
        print(msg)


form()

