use structopt::StructOpt;
use loggerv;

// Hello world.
#[derive(StructOpt, Debug)]
#[structopt(name = "foo", about = "An example of StructOpt.")]
struct Cli {
    /// Enable logging, use multiple `v`s to increase verbosity
    #[structopt(short = "v", long = "verbose")]
    verbosity: u64,
}

pub fn run() -> Result<()> {
    let args = Cli::from_args();

    loggerv::init_with_verbosity(args.verbosity)?;

    // ...
    let thing = "foobar";
    debug!("Thing happened: {}", thing);
    // ...

    info!("It's all good!");
    Ok(())
}

error_chain! {
    foreign_links {
        Log(::log::SetLoggerError);
    }
}