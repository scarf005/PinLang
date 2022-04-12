# Pin Cheatsheet

pin is a c dialect with none of its syntax. it is mostly for preparing a bigger language someday, `quilt` that has generics.

## Features
- Everything is an expression
- All functions are anonymous
- Terse syntax

## Semantic Symbols

all symbolic tokens have consistent meaning across syntax. A `{}` will always used to denote a scope. a `()` will always denote a parameter.

| token | means                                                             |
| :---: | :---------------------------------------------------------------- |
|  `:`  | type indicator.                                                   |
|  `=`  | assignment.                                                       |
|  `*`  | pointer.                                                          |
|  `&`  | reference.                                                        |
| `{}`  | A scope. Acessing scoped values require scope resoution operator. |
| `()`  | A parameter. () means empty parameter.                            |
| `<>`  | Generic type.                                                     |
| `::`  | Scope resolution operator. Use it to restrict specific scope.     |
|  `!`  | Macro.                                                            |
| `->`  | If then operator. left expression results in expression in right. |

## Keywords

```rs
```

### `let [mut] IDENTIFIER [: type] [= VALUE | TYPE]`
`let`: runtime constant assignment.
`mut`: runtime mutable variable assignment.
`ref`: runtime reference variable assignment.

types can be inferred.

```rs
let mut spam = 12 // ok
let usize8 : type = u8 // ok
let spam = &spam // converts into const std::unique_ptr<int> spamPtr(&foo);
let egg = &spam // converts into std::unique_ptr<int> eggPtr(&spam);
let a = 1, b = 2, c: string = "hello" // multiple assignments
```

### `if COND { ... } [else if COND { ... }]* [else { ... }]`
conditional expression

```rs
let a = 1
let b = if a > 10 { 10 } else if a > 5 { 5 } else { 1 }
// b = 1
```

### `when [VALUE] { [CASE -> ...,]* else -> DEFAULT [,] }`
pattern match expression. default non-fallthrough. if value is not provided, every case must be an boolean expression. if else is not provided, the default return value is None.

```rs

let a = "hello world"
let b = when a {
  "hello world" -> 1,
  "bye world" -> 2,
  else -> 3
}
// 1
```

### `for [COND | IDENTIFIER in ITERABLE] { ... }`
loop expression. pin only has for loop. for iterables, use `each` method in `Iterable` trait instead.
if used as `for {...}`, the loop will be infinite. for always returns `None`.

```rs
// usu. used to implement iterator
let a = 0
for a < 10 {
  a += 1
}

let arr: int[] = { 1, 2, 3, 4, 5 }
arr.each((_, i) -> {
  println!("{i}")
})
```

###  `([IDENTIFIER [: TYPE]]*) -> [TYPE] { ... }`
pin only has anonymous function. assign to a variable or use as lambda.
if the type variable in parameter can be clearly inferred, it can be skipped.
the same applies to return type.

```rs
let a = (x: int, y: int) -> int {
  x + y
}

let b = a(1, 2) // b == 3

let arr  = [1, 2, 3, 4, 5]
let new_arr = arr.map((e) -> {e * 2})
```

### `struct IDENTIFIER { [IDENTIFIER: TYPE, ]* IDENTIFIER: TYPE }`
a struct is a custom value type.

```rs
struct Point {
  x: int,
  y: int,
}

let my_pos := Point { x=1, y=2 }
```

### `enum IDENTIFIER { [IDENTIFIER [= VALUE] [,]* ]* }`
an enum is a custom type.

```rs
enum Color {
  Red,
  Green,
  Blue,
}

let red := Color::Red
```

### `trait IDENTIFIER { [IDENTIFIER [: TYPE] [-> TYPE] [,]* ]* }`
```rs
trait Printable {
  let to_string = () -> string
}

trait Iterable<T> {
  let Item: type

  let each = (f: (value: T) -> Any) -> None
  let map = (f: (value: T) -> T) -> T[]
  let filter = (f: (value: T) -> bool) -> T[]
  let enumerate = (f: (i: usize, value: T) -> Any) -> None
  ...
}
```

### `impl IDENTIFIER[::TRAIT] { ... }`
implement a trait or method.

```rs
struct Array {
  len: int,
  data: int[],
}

impl Array<T>::Iterable {
  let Item = T

  let each = (&self, f: (value: T) -> Any) -> None {
    for i in 0..self.len {
      f(data[i])
    }
  }

  let map = (&self, f: (value: T) -> T) -> T[] {
    let mut new_arr = T[]
    for i in 0..self.len {
      new_arr[i] = f(data[i])
    }
    new_arr
  }
}

impl Array<T>::Printable {
  let to_string = (&self) -> String {
    let mut s = "".to_string()
    self.data.each((v) -> {
      s += v.to_string()
    })
    s
  }
}

let a = Array<int>::new(3, {1, 2, 3})
let b = array!(1, 2, 3) // macro equivalent
assert_eq!(a, b)
```
