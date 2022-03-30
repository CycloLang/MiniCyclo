# MiniCyclo Docs

MiniCyclo is a subset of Cyclo. With the sole exception of the `$print()` function, all MiniCyclo code is valid Cyclo code. MiniCyclo removes almost all the syntaxtic sugar from Cyclo. A full grammar of Cyclo is avaible at `miniCyclo.bnf`

The full list of restrictions is as follows:

- No operators except from `=`, `:=`, `::=` and `.`
- No `elif`, `switch`, `for` or `foreach`
- No `import _ as` or `from _ import`
- Int or float literals must be base 10
- Only single character escape codes supported in strings
- No type checking is performed
- Parameters in macro definitions can only be referred to as `$0`...
- No pattern matching
- Function parameters cannot be given default values
- No formattted strings
- No slices or ranges
- No block comments
- Dicts and Structs
- Array and Tuple literals
- Semicolons are required

## Builtin functions

The following builtin functions are the only ones accessible:

- `$print(<value>)` not a function in standard Cyclo, `print()` is instead defined in the stdlib. The interpreter prints the value of the expression.
- `$add(a,b)` returns `a+b`
- `$sub(a,b)` returns `a-b`
- `$mul(a,b)` returns `a*b`
- `$div(a,b)` returns `a//b`
- `$mod(a,b)` returns `a%b`
- `$neg(a)` returns `-a`
- `$pos(a)` returns `+a`
- `$pow(a,b)` returns `a**b`
- `$shl(a,b)` returns `a<<b`
- `$shr(a,b)` returns `b>>a`
- `$not(a)` returns `not a`
- `$and(a,b)` returns `a and b`
- `$or(a,b)` returns `a or b`
- `$xor(a,b)` returns `a xor b`
- `$inv(a)` returns `~a`
- `$eq(a,b)` returns `a==b`
- `$neq(a,b)` returns `a!=b`
- `$int(a)` returns `int(a)`
- `$bool(a)` returns `bool(a)`
- `$str(a)` returns `str(a)`
- `$concat(a,b)` returns `a+b`
- `$in(a,b)` returns `a in b`
- `$index(a,b)` returns the index of `b` at which `a` first occurs
- `$delItem(a,b)` deletes `a[b]`
- `$setItem(a,b,c)` sets `a[b]` to `c`
- `$getItem(a,b)` returns the value of `a[b]`
- `$lt(a,b)` returns `a<b`
- `$le(a,b)` returns `a<=b`
- `$gt(a,b)` returns `a>b`
- `$ge(a,b)` returns `a>=b`