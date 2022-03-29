AORU = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]

WHITESPACE = [" ","\t","\n","\r"]

BUILTINOPS = ["=",":=","::=","."]

SYMBOLS = ["(",")","{","}","=>","->",","]

BUILTINKWDS = ["if","else","while","import","macro","infix","prefix","call","surround","me","super"]

LINE_COMMENT = ["//"]

BLOCK_COMMENT = [("/\"","\"/")]

STRING_DELIM = ["\""]

CHAR_DELIM = ["'"]

RESERVED_CHARS = ["(",")","{","}"]

def tokenise(text:str) -> list:

    textPos = 0
    targetLength = len(text)
    chunks = []

    #generate a full set of reserved chars
    reserved = RESERVED_CHARS
    for i in LINE_COMMENT:
        reserved.append(i[0])
    for i in BLOCK_COMMENT:
        for j in i:
            reserved.append(j[0])
    for i in STRING_DELIM:
        reserved.append(i[0])
    for i in CHAR_DELIM:
        reserved.append(i[0])


    def isAorU(char:str) -> bool:
        return(char in AORU)

    def isDigit(char:str) -> bool:
        return(char in DIGITS)

    def isWhitespace(char:str) -> bool:
        return(char in WHITESPACE)

    def isReserved(char:str) -> bool: #cannot appear in operators
        return(char in reserved)

    def isSymbol(char:str) -> bool:
        return(not(isAorU(char) or isDigit(char) or isWhitespace(char) or isReserved(char)))

    def isIdOrKw(testStr:str) -> bool:
        firstChar = testStr[0]

        if firstChar == "$" or isAorU(firstChar):

            for i in testStr[1:]:
                if not(isAorU(i) or isDigit(i)):
                    return(False)

            return(True)

        else:
            return(False)

    def isInt(testStr:str) -> bool:
        for i in testStr:
            if not(isDigit(i)):
                return(False)

        return(True)

    def isReservedBlock(testStr:str) -> bool:
        for i in testStr:
            if not(isReserved(i)):
                return(False)

        return(True)

    def isSymbolic(testStr:str) -> bool:
        for i in testStr:
            if not(isSymbol(i)):
                return(False)

        return(True)

    def isWhitespaceBlock(testStr:str) -> bool:
        for i in testStr:
            if not(isWhitespace(i)):
                return(False)

        return(True)

    def charType(char:str) -> bool:
        if isWhitespace(char):
            return(isWhitespaceBlock)
        elif isIdOrKw(char):    #used instead of isAlpha() as a $ is treated alphanumerically
            return(isIdOrKw)
        elif isDigit(char):
            return(isInt)
        elif isReserved(char):
            return(isReservedBlock)
        else:
            return(isSymbolic)

    def scan(rule):

        nonlocal textPos
        currentStr = text[textPos]

        while textPos < targetLength and rule(currentStr):

            textPos += 1
            try:
                currentStr += text[textPos]
            except IndexError:
                return(None)

        currentStr = currentStr[:-1]
        return(currentStr)



    #first tokenisation breaks into blocks

    while textPos < targetLength:

        currentChr = text[textPos]
        chunks.append(scan(charType(currentChr)))

    print(chunks)
