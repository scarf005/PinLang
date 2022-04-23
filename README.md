# Pin

since i was always having hard time with lua in modding, i decided to write my own tiny language (in the following decades)

## How it looks like

```rs
let main = () -> i32 {
  println!("Hello, world!")
  0
}
```

## Some Features
- variable is default `const`. add `mut` for mutables.
- functions are default `static`. add `pub` to unhide it.
- `->` and `.` keyword is merged to `.`.

## Goal

Pin is merely a toy project

### Features
- [ ] variable declaration
- [ ] function declaration
- [ ] loops
- [ ] structs
- [ ] arrays

### Long Term Goals
- [ ] enums
- [ ] macros
