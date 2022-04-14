# Pin

Pin is a dialect of C language.
Its goal is to be compiled into norminette-compatible C code.
The syntax will be terse and consistent to go easy with parsing.

## How it looks like

```rs
pub fn main() -> i32 {
  println!("Hello, world!")
  0
}
```

## Some changes
- variable is default `const`. add `mut` for mutables.
- functions are default `static`. add `pub` to unhide it.
- `->` and `.` keyword is merged to `.`.

## Goal

Pin is merely a toy project; its features will be a fraction of C.

### Features
- [ ] variable declaration
- [ ] function declaration
- [ ] loops
- [ ] structs
- [ ] arrays

### Long Term Goals
- [ ] enums
- [ ] macros
