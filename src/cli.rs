use structopt::StructOpt;
use loggerv;
use errors::*;

#[derive(StructOpt, Debug)]
#[structopt(name = "example", about = "An example of StructOpt usage.")]
struct Opt {
    /// Enable logging, use multiple `v`s to increase verbosity
    #[structopt(short = "v", long = "verbose")]
    verbosity: u64,

    #[structopt(subcommand)]
    dl: Opt1,
}

#[derive(StructOpt, Debug)]
#[structopt(name = "Ellinofreneia-Crawler")]
/// the stupid content tracker
enum Opt1 {
    #[structopt(name = "download")]
    /// Download latest Episodes!
    Download {
        #[structopt(long = "tv")]
        tv: bool,
        #[structopt(long = "radio")]
        radio: bool,

        #[structopt(short = "a", long = "all", default_value = "true")]
        all: bool,

        /// Number of Episodes to be Downloaded
        #[structopt(default_value = "10")]
        amount: Option<i64>,
    },
}

pub fn run() -> Result<()> {
    let args = Opt::from_args();

    loggerv::init_with_verbosity(args.verbosity)?;

    let foo = args.dl;
    // This works
    info!("{:?}", foo);

    // This dsnt and I hate everything
    // info!("{:?}", foo.all);

    // ::crawler::latest_radio(args.amount as u64)?;
    // ::crawler::latest_tv(am as u64)?;
    Ok(())
}