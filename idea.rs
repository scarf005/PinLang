type cstr = *const u8

pub struct String {
  len: usize,
  data: cstr,
}

trait Printable {
  fn to_cstr(&self) -> cstr;
}

impl String {
  pub fn len(&self) -> { return self.len }

  pub fn new() -> String {
    return String {
      len: 0,
      data: ptr,
    }
  }

  pub fn from(s: cstr) -> String {
    let len = cstrlen(s)
    let data: cstr = allocate!(u8, len)

    for i in 0..len {
      data[i] = s[i]
    }

    return String {
      len: len,
      data: data,
    }
  }
}

impl String::Printable {
  fn to_cstr(&self) -> cstr {
    return self.data
  }
}

pub fn main(argc: i32) -> i32 {
  let hello = String::from("Hello") // stack allocated
  let world = String::from("world")

  println!("{hello}, {world}!")
}
