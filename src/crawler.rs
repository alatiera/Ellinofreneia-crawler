use select::document::Document;
use select::predicate::{Attr, Class, Name};
use reqwest;
use Result;

pub fn main() -> Result<()> {
    let res = reqwest::get("http://www.ellinofreneianet.gr/radio/radio-shows-2.html")?;
    let res1 = reqwest::get("http://www.ellinofreneianet.gr/television/tv-shows.html")?;

    // let document = Document::from(include_str!("../ell.html"));
    let document = Document::from_read(res)?;
    let document1 = Document::from_read(res1)?;

    let radio_links: Vec<_> = document
        .find(Class("my-item"))
        .filter_map(|x| x.attr("href"))
        .collect();

    let tv_links: Vec<_> = document1
        .find(Class("yendif-thumbnail"))
        .filter_map(|x| x.attr("href"))
        .collect();

    println!("{:#?}", radio_links);
    println!("{:#?}", tv_links);

    Ok(())
}