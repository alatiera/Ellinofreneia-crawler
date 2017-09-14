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
enum Opt1 {
    #[structopt(name = "download")]
    /// Download latest Episodes!
    Download {
        #[structopt(long = "tv", conflicts_with = "radio")]
        tv: bool,
        #[structopt(long = "radio", conflicts_with = "tv")]
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
    info!("{:?}", foo);

    match foo {
        Opt1::Download {
            tv,
            radio,
            all,
            amount,
        } => placeholder(tv, radio, all, amount),
        _ => (),
    };

    Ok(())
}

fn placeholder(tv: bool, radio: bool, all: bool, amount: Option<i64>) {

    // Check if either radio or tv flag is present
    // If not default to dl all

    if tv == true {
        ::download_tv(amount.unwrap() as u64).unwrap();
    }

    if radio == true {

        // Not implemented yet
        // ::download_radio(amount.unwrap() as u64);}
    }

    if all == true {
        //do both
    }

}