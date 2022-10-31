def CalcSeparators(userID,details):
    separators = []
    for index in range (len(details)):
        if details[index] == "|":
            separators.append(index)
    return separators