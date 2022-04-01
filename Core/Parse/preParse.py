def preParse(tokens:list) -> list:

    retList = []
    curList = []

    for i in tokens:

        if i.cat == "SEMICOLON":
            retList.append(curList)
            curList = []

        else:

            curList.append(i)
