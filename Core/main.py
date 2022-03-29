from Core.Tokens.tokeniser import tokenise

def runFile(fileName,args=[]):
    fileText = fileName.read()
    print(fileText)
    tokenise(fileText)