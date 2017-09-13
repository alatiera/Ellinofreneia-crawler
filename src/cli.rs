use structopt::StructOpt;
use loggerv;
use errors::*;

#[derive(StructOpt, Debug)]
#[structopt(name = "example", about = "An example of StructOpt usage.")]
struct Opt {
    /// A flag, true if used in the command line.
    // #[structopt(short = "d", long = "debug", help = "Activate debug mode")]
    // debug: bool,

    // ... Rustfmt hack
    /// Number of Episodes to be Downloaded
    #[structopt(short = "a", long = "amount", default_value = "10")]
    amount: i64,

    /// Enable logging, use multiple `v`s to increase verbosity
    #[structopt(short = "v", long = "verbose")]
    verbosity: u64,
}


pub fn run() -> Result<()> {
    let args = Opt::from_args();

    loggerv::init_with_verbosity(args.verbosity)?;

    // ...
    // let thing = "foobar";
    // debug!("Thing happened: {}", thing);
    // ...

    // info!("It's all good!");

    info!("Speed: {:?}", args.amount);
    ::crawler::latest_radio(args.amount as u64)?;
    // ::crawler::latest_tv(args.amount as u64)?;
    Ok(())
}