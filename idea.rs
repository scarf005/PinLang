// This is a comment.
/*
This is an block comment. /* Todo: make it nestable! */
*/

// imports are done by namespace.
// import std::random -> use like std::random::randint()
// import std::random::{ randint } -> use like randint()
// import std::random::* -> use like randint()
import std::cstring::{ cstrlen }
import std::cstdlib::{ ccalloc }

// typedef is done with: type TYPENAME = ...
type cstr = u8 ptr // ptr is explicit

// comptime: calculate expression at compile time (all values must be known)
// let: constants
// let mut: variables
comptime { 
  let STRING_INITIAL_SIZE: i32 = 20 
}

// structs
struct String {
  len: usize,
  data: cstr,
}

// traits define shared behavior an object does
trait ToString {
  fn to_cstr(&Self) -> cstr
}

// Add function bound within struct with impl keyword.
impl String {
  // member function if first argument is Self
  // myStr.len() is compiled to String__len_m(&myStr);
  fn len(&Self) -> { return Self.len }

  // static function
  // String::new() is compiled to String__new_s();
  fn new() -> String {
    return String {
      len=STRING_INITIAL_SIZE,
      data=ccalloc(u8, STRING_INITIAL_SIZE),
    } // named parameters
  }
  
  fn from(s: cstr) -> String {
    let len = cstrlen(s)
    let mut data: cstr = ccalloc(u8, len)

    for i in range(len) {
      data[i] = s[i]
    }

    return String {
      len, data,
    } // unnamed paramters
  }
}

// implement trait for struct
impl ToString for String {
  fn to_cstr(&self) -> cstr {
    return self.data
  }
}

fn main(argc: i32) -> i32 {
  let hello = String::from("Hello") // stack allocated
  let world = String::from("world")

  println!("{hello}, {world}!")
  
  // 'if' is an expression
  let spam = if 1 == 1 { 3 } else { 2 }
  // pattern matching is an expression too
  let egg = when (spam) {
    1 -> 11,
    2 -> 22,
    else -> 0,
  }
}
