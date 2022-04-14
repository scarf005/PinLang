# Syntax

### Variables

```rs

let x := 1 // --> const int x = 1;
let y: int = 2 // --> const int y = 2;
let mut z = 3 // --> int z = 3;
let xPtr = &x // --> const int* xPtr = &x;
let yPtr: *int = &y // --> const int* yPtr = &y;
let zPtr: *mut int = &z // --> int* zPtr = &mut z;
```


```rs
type cstr *u8

struct String {
  len: usize,
  data: cstr,
}

impl String {
  fn empty() -> void {
    String {
      len: 0,
      data: 0x00,
    }
  }
  fn new(s: cstr) -> String {
    String {
      len: cstrlen(s),
      data: cstrdup(s),
    }
  }
  fn del(str: String) -> void {
    free(str.data)
  }
  fn len(&self) -> usize {
    self.len
  }
}

pub fn main() -> i32 {
  let s = String::new("Hello, world!")
  let size = s.len()

  println!(s)
  println!("length of above = {size}")

  String::del(s)
}
```
