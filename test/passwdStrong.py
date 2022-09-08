regex = "fjd3IR9"


def search():
    strong = [False, False, False]
    for i in regex:
        if i.islower():
            strong[0] = True
        elif i.isupper():
            strong[1] = True
        elif i.isnumeric():
            strong[2] = True
    if len(regex) < 6 or False in strong:
        return False
    return True


search()
