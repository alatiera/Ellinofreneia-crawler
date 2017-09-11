#![recursion_limit = "1024"]

#[macro_use]
extern crate error_chain;
extern crate ellinofreneia;


use ellinofreneia::cli::run;

quick_main!(run);
