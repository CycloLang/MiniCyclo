import Core.Tokens.token as token

AORU = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]

WHITESPACE = [" ","\t","\n","\r"]

BUILTINOPS = ["=",":=","::=","."]

SYMBOLS = ["(",")","{","}","=>","->",",",";"]

BUILTINKWDS = ["if","else","while","import","macro","infix","prefix","call","surround","me","super","static"]

LINE_COMMENT = ["//"]

STRING_DELIM = ["\""]

CHAR_DELIM = ["'"]

RESERVED_CHARS = ["(",")","{","}"]

def tokenise(text:str) -> list:

    textPos = 0
    text = text + " " #need to append a whitespace char for some reason
    targetLength = len(text)
    chunks = []

    #generate a full set of reserved chars
    reserved = RESERVED_CHARS
    for i in LINE_COMMENT:
        reserved.append(i[0])
    for i in STRING_DELIM:
        reserved.append(i[0])
    for i in CHAR_DELIM:
        reserved.append(i[0])

    operatorLike = reserved + SYMBOLS + BUILTINOPS

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
            return(isWhitespaceBlock,"WHITESPACE")
        elif isIdOrKw(char):    #used instead of isAlpha() as a $ is treated alphanumerically
            return(isIdOrKw,"ID")
        elif isDigit(char):
            return(isInt,"INT")
        elif isReserved(char):
            return(isReservedBlock,"RESERVED")
        else:
            return(isSymbolic,"SYMBOLIC")

    def scan(args):

        rule = args[0]
        name = args[1]

        nonlocal textPos
        currentStr = text[textPos]

        while textPos < targetLength and rule(currentStr):

            textPos += 1
            try:
                currentStr += text[textPos]
            except IndexError:
                return(("","EOF"))

        currentStr = currentStr[:-1]
        return(currentStr,name)

    def maxMunch(str:str,targets:list) -> str:

        retStr = ""

        def impossible():
            for i in targets:
                if i[:len(retStr)] == str[:len(retStr)] and len(retStr) <= len(i):
                    return(False)
            return(True)

        for i in str:
            retStr = retStr + i
            if impossible():
                retStr = retStr[:-1]
                break

        if retStr in targets:
            return(retStr)
        else:
            return("")

    #first tokenisation breaks into blocks

    while textPos < targetLength:

        currentChr = text[textPos]
        chunks.append(scan(charType(currentChr)))

    print(chunks)

    #TODO handle strings and comments

    tokens = []
    for i in chunks:

        if i[1] == "WHITESPACE":
            pass

        elif i[1] == "INT":
            tokens.append(token.IntLiteral(i[0]))

        elif i[1] == "ID":
            if i[0] in BUILTINKWDS:
                tokens.append(token.Keyword(i[0]))
            else:
                tokens.append(token.Identifier(i[0]))

        elif i[1] == "RESERVED" or i[1] == "SYMBOLIC":

            chunkText = i[0]
            while len(chunkText) > 0:

                #tokenText = ""
                tokenText = maxMunch(i[0],operatorLike)

                if tokenText == "(":
                    tokens.append(token.Delim("(","OPEN","PAREN"))
                elif tokenText == ")":
                    tokens.append(token.Delim(")","CLOSE","PAREN"))
                elif tokenText == "{":
                    tokens.append(token.Delim("{","OPEN","BRACE"))
                elif tokenText == "}":
                    tokens.append(token.Delim("}","CLOSE","BRACE"))
                elif tokenText == ",":
                    tokens.append(token.Delim(",","BREAK","COMMA"))
                elif tokenText == ";":
                    tokens.append(token.Delim(",","BREAK","SEMICOLON"))
                elif tokenText == "": #Undefined operator
                    tokens.append(token.Operator(chunkText))
                    tokenText = chunkText
                else:
                    tokens.append(token.Operator(tokenText))

                chunkText = chunkText[len(tokenText):]

    for i in tokens:
       print(f"{i.lex} ->> {i.val} |-> {i.cat}")
    return(tokens)