def get_text(placement):
    text = input("Type your " + placement + ": ")
    if text == "":
        get_text(placement)

    return text
