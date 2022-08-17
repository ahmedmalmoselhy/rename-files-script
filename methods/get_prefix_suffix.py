def get_text(placement):
    text = input("Type your " + placement + ": ")
    if text == "":
        return get_text(placement)

    return text
