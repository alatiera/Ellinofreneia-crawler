#![recursion_limit = "1024"]

extern crate structopt;
#[macro_use]
extern crate structopt_derive;
#[macro_use]
extern crate error_chain;
#[macro_use]
extern crate log;
extern crate loggerv;
extern crate select;
extern crate reqwest;
extern crate rafy;

pub mod cli;
pub mod crawler;
pub mod downloader;

pub mod errors {

    use reqwest;
    use std::io;

    error_chain! {
        foreign_links {
            ReqError(reqwest::Error);
            IoError(io::Error);
            Log(::log::SetLoggerError);
        }
    }
}