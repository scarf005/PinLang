# Syntax

### declarations

A variable or const is declared as:

```rust
foo := 10 // this is an variable of inferred type int
BAR :: 20 // this is an constant of inferred type int
spam : i32 = 10 // this is an variable of explicit type i32
EGG : i32 : 20 // this is an constant of explicit type i32
```

```c
int         foo;
const int   c_bar = 20; // due to norminette name restriction, no capitals
const i32_t c_spam = 10;
i32_t       egg;

foo = 10;
egg = 20;
```

note that constant expression is bound via `::` operator.

A struct:

```rust
point :: struct {
  x: i32,
  y: i32, // "," at the last is optional
}
```
```c
typedef s_point
{
  int x;
  int y;
} t_point;
```

An enum:
```rust
result :: enum {
  OK,
  FAIL = 3,
}
```
```c
typedef e_result
{
  OK,
  FAIL = 3,
} t_result;
```

### Functions
```rust
use core/print
;
main :: fn(ac: int, av: string[]) {
  spam := 10
  egg :: 20

  print!("{spam = } {egg = }")
}
```
```c
#include "pin.h"
#include "stdio.h"

int main(int ac, char *argv[])
{
  int       spam;
  const int egg = 20;

  spam = 10;
  printf("spam = %d egg = %d", spam, egg);
  return EXIT_SUCCESS;
}
```