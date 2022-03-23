# Specification

### Hello World

```rust
/* The main thing that this program does */
main :: () -> Unit {
  // Declarations
  A : [5]f64 : [
    0: 9.0,
    1: 2.9,
    4: 3.E+25,
    3: .0007,
  ]

  // Doing Some Work
  A.each((v, i) -> {
    print(fmt"element {i} is {v}, \tits square is {v * v}")
  })
}
```
into readable c.

```cpp
#include <pin/std/format.h>

int main(void) {
  // Declarations
  const double A[5] = {
    [0] = 9.0,
    [1] = 2.9,
    [4] = 3.E+25,
    [3] = .0007,
  };

  // Doing Some Work
  for (int i = 0; i < 5; i++) {
    printf("element %zu is %g, \tits square is %g\n",
      i, A[i], A[i] * A[i]
    );
  }

  return EXIT_SUCCESS;
}
```

### RAII

```rust
use std/io::stdin, std/string
; // makes md syntax highlight happy

foo :: () -> {
  str := stdin.readline()

  when (str) {
    "hello" -> print("Nice to meet you")
    "bye" -> print("Goodbye")
  }
}

main :: () -> {
  foo()
}
```

is compiled into pin IR

```ts
var str
try:
  str = readline(stdin)
  when str
  "hello" -> print(1, "Nice to meet you")
  "bye" -> print(1, "Goodbye")
  else -> Unit
finally:
  [[destroy]](str)

```

is compiled into

```cpp
#include <pin/std/memory.h>
#include <pin/std/string.h>
#include <stdlib.h>

//typedef char* cstr_t
cstr_t foo(void) {
  const cstr_t CONST_STR = "This is an const string."
  cstr_t str = "This is a stack string"

  cstr_t heapStr;
  {
    cstr_t __PIN_TMP_VAR_0 = "This is a heap string";
    heapStr = malloc(22);
    strcpy(heapStr, __PIN_TMP_VAR_0);
    heapStr[21] = '\0';
  }
  return heapStr;
}

int main(void) {

  // Doing Some Work
  for (int i = 0; i < 5; i++) {
    printf("element %zu is %g, \tits square is %g\n",
      i, A[i], A[i] * A[i]
    );
  }

  return EXIT_SUCCESS;
}
```