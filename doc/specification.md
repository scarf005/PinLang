# Specification

### Hello World

```rust
/* The main thing that this program does */
main :: () -> {
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

is compiled into

```cpp
#include <stdio.h>

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
    printf("element %zu is %g, \tits square is %g",
      i, A[i], A[i] * A[i]
    );
  }

  return EXIT_SUCCESS;
}
```