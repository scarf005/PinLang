# Specification

## Hello World

```rust
use core/print
;
main :: fn() -> i32 {
  spam :: "hello"
  egg :: "world"

  // print! is a macro that is same as printf(fmt!"...")
  print!("{hello} {world}")
}
```

is compiled to

```c
#include <stdio.h>

int main(void)
{
  const char* spam = "hello";
  const char* egg = "world;
  printf("%s %s", hello, world);
}
```

## Rules

along with general C limitations:

#### declarations
only static

#### functions
max **4** parameter variables
max **5** variable declarations
max **25** lines
