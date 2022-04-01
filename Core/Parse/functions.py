class Func_():

    def __init__(self,val) -> None:
        self.val = val

    def call(self,args):
        return(self.val(*args))

class BuiltInFunc(Func_):

    def __init__(self, val) -> None:
        super().__init__(val)


BUILTIN_FUNCTIONS = {
    "$add" : BuiltInFunc(lambda a, b : a + b),
    "$sub" : BuiltInFunc(lambda a, b : a - b),
    "$mul" : BuiltInFunc(lambda a, b : a * b),
    "$div" : BuiltInFunc(lambda a, b : a // b),
    }

print(BUILTIN_FUNCTIONS["$add"].call((1,2)))
print(BUILTIN_FUNCTIONS["$sub"].call((1,2)))
print(BUILTIN_FUNCTIONS["$mul"].call((1,2)))
print(BUILTIN_FUNCTIONS["$div"].call((1,2)))