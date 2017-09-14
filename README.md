# Ellinofreneia-crawler
dler of ellinofreneianet.gr website

## Info:
Unoficial crawler meant for offline content consumption.

There also 2 hidden rss feeds on the site but they link to soundcloud/youtube.

[radio](http://www.ellinofreneianet.gr/radio/radio-shows-2.feed?type=rss)

[tv](http://www.ellinofreneianet.gr/television/tv-shows.feed?type=rss)


## Cargo Dependancies:

* [error-chain](https://github.com/rust-lang-nursery/error-chain)

* [reqwests](https://github.com/seanmonstar/reqwest)

* [structopt](https://github.com/TeXitoi/structopt)

* [structopt-derive](https://github.com/TeXitoi/structopt)

* [log](https://github.com/rust-lang/log)

* [loggerv](https://github.com/clux/loggerv)

* [rafy](https://github.com/ritiek/rafy-rs)

## Build:

```
git clone https://github.com/alatiera/Ellinofreneia-crawler.git
git checkout rust-rewrite
cargo build --release
cargo run -- --help
```

## Stuff Not yet in Feature-Parity with the python version. WIP.

* Proper StructOpt menu.

* Soundcloud ripper, There doesnt seem to be a crate to do that atm.

* Specified File-Save Path.

* Not sure if a file renamer/organizer will be needed.