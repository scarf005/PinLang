# Pin Language Reference

- it's a tiny scripting language.
- keywords first so i don't have to write complex compiler
- control flow is expression that returns value
- supports generics, traits, and metaprogramming.
- compiles to C++ code.

## Basic Syntax

### Variables

- `let` declares a constant.
- `mut` declares a mutable variable.
- declaration and assignation must not be separated.
- types can be inferred.
- add ` : <type> ` to explicitly specify.

```rs
let a : i32 = 3
mut b = 4
let c // Error
mut d // error
```

### Control Flow

- control flow is expression that returns value.
- `if` , `else` works like in other languages

```rs
let a = 3
let b = if a > 3 {
  3
} else if a > 2 {
  2
} else {
  1
}

println!("{b}") // => 2
```

- `when` is pattern matching for given value
- `else` must be present
- can omit braces if expression is single-line
- value must be provided

```rs
let a = 3
let b = when a {
  3 -> {
    3
  }
  2 -> 2
  else -> 1
}

println!("{b}") // => 3
```

### Collections

- pin supports some of c++ collections, like vector, list, map, etc.
```rs
let a = List<i32>
a.append(3)
a.append(4)

let b = list!(3, 4)

let c = Map<String, i32>
c.set("a", 3)
c.set("b", 4)

let d = map!("a" -> 3, "b" -> 4)
```

- collections support helper functions for iteration
- some of the examples are `each`, `map`, `filter`, `reduce`

```rs
range(4)
  .to_list()
  .map(|i| i * 2)
  .filter(|i| i % 4)
// => List<i32> [0, 4]
vec!("a", "b", "c").each(|s| { print!("{!}") })
// => 1, 2, 3, %
let m = map!(
  "a" -> 1,
  "b" -> 2,
  "c" -> 3,
)
m.each((k, v) -> print!("{k}={v}, "))
// => a=1, b=2, c=3, %
m.each_keys(k -> print!("{k}, "))
// => a, b, c, %
```

### Functions
- can omit `()` if function has single parameter and has no default values.
- can omit `{}` if expression is single-line and has no provided explicit return type
- if parameter type is omitted, it can be only used as other function's parameter, which will set its types accordingly.

```rs
let isodd = i -> i % 2 == 1
let iseven = i -> bool { i % 2 == 0 }

let fib = (n: u32) -> u32 {
  when a {
    range(3) -> n
    else -> fib(n - 1) + fib(n - 2)
  }
}

let a = list!(1, 2, 3)
let b = a.filter(isodd) // => List<i32> [1, 3]
let c = a.map(i -> i * 2) // => List<i32> [2, 4, 6]
```

since `a` is collection List of type `i32`, parameter and return type of `i -> i * 2` is inferred to be `i32 -> i32`.

### Custom Types

```rs
type my_type = i32
type IntPoint = data {
  x: i32,
  y: i32,
}
type Point<T> = data {
  x: T,
  y: T,
}
type WeekOfDay = enum { Mon, Tue, Wed, Thu, Fri, Sat, Sun }

let a: my_type = 3
let b = 2
let c = a + b // error, my_type != i32
let day = WeekOfDay@Mon
```

### Traits, Impl

- `trait` declares a shared behavior(function) for a type.
- `self` is the value of the type itself, which is used to access its methods.
- `Self` as return means it returns the type itself.
- `impl` implements a trait for a type.
- types can be inferred from traits

```rs
trait Student {
  fn new(name: String, age: u16) -> Self
  fn study(self) -> unit
}

type Person = {
  name: String,
  age: u16,
}

impl Person -> Student {
  fn new(name = "hooman", age) -> Self {
    { name }
  }
  fn fly(self) -> unit {
    println!("{self.name} flies")
  }
}

impl Person {

}

let
```

