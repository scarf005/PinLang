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
