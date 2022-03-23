# Syntax

### Lexical elements and literals

```c
// A comment

my_integer_variable: int // A comment for documentation

/*
multi-line comment work too
*/
```

### String and character literals

```c

"A string"
"안녕 세계"
'\n' // newline char

"hello".len() // builtin method returns 5
```

```py
str :: "world"
fmt"hello {str}"

/*
string formatting is allowed
only when its type can be inferred in compile-time
*/
```