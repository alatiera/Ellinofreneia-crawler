#![recursion_limit = "1024"]

#[macro_use]
extern crate log;
extern crate loggerv;
#[macro_use]
extern crate error_chain;
extern crate ellinofreneia;
extern crate structopt;

// use error_chain::example_generated::Result;
use structopt::StructOpt;

use ellinofreneia::cli;

quick_main!(|| -> Result<()> {
    let args = cli::Cli::from_args();

    loggerv::init_with_verbosity(args.verbosity)?;

    // ...
    let thing = "foobar";
    debug!("Thing happened: {}", thing);
    // ...

    info!("It's all good!");
    Ok(())
});

error_chain! {
    foreign_links {
        Log(::log::SetLoggerError);
    }
}
