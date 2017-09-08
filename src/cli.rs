// use structopt::StructOpt;
// use error_chain::example_generated::Result;

// Hello world.
#[derive(StructOpt, Debug)]
#[structopt(name = "foo", about = "An example of StructOpt.")]
pub struct Cli {
    /// Enable logging, use multiple `v`s to increase verbosity
    #[structopt(short = "v", long = "verbose")]
    pub verbosity: u64,
}