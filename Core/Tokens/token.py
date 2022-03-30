class Token():

    def __init__(self,lex,val,cat) -> None:
        self.lex = lex
        self.val = val
        self.cat = cat

class IntLiteral(Token):

    def __init__(self, lex) -> None:
        super().__init__(lex, int(lex), "INT_LITERAL")

class Keyword(Token):

    def __init__(self, lex) -> None:
        super().__init__(lex, lex, "KEYWORD")

class Identifier(Token):

    def __init__(self, lex) -> None:
        super().__init__(lex, lex, "IDENTIFIER")

class Operator(Token):

    def __init__(self, lex) -> None:
        super().__init__(lex, lex, "OPERATOR")

class EOF(Token):

    def __init__(self) -> None:
        super().__init__("", "EOF", "EOF")

class Delim(Token):

    def __init__(self, lex, val,cat) -> None:
        super().__init__(lex, val, cat)