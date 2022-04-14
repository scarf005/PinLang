# Changes

Pin will be an alternative syntax for norminette C because reading norminette C physically hurts my eyes.

## Variables

```rs
let foo: int = 11
let mut bar: int = 3
```
```c
const int foo = 11;
int bar = 3;
```

## Functions

```rs
fn add(a: int, b:int) -> int {
  return a + b
}
```
```c
int add(int a, int b)
{
    return (a + b);
}
```

## Member Function
```rs
struct String { size: uint, data: char * }

impl String {
  fn new() -> String
  fn del() -> None
  fn len(&self) -> uint
}

fn main() -> int {
  let mut a: String = String::new("hello")
  let size: int = a.len()
  
  print!("string size is {size}")
  String::del(a)
}
```
```c
struct s_string { size: unsigned int; data: char * };
struct s_string string__new(const char* from);
unsigned int string__len(struct s_string);
void string__del(struct s_string);

int main(void)
{
  struct s_string a;
  int size;
  
  a = string__new("hello");
  size = string__len(a);
  printf("string size is %d", size);
  string__del(a);
}
```
## Loops
```rs
for (0..10) {}
```
```c
for (int i = 0; i < 10; i++) {}
```
with `--norminette`
```c
int i;
i = -1;
while (++i < 10) {}
```
