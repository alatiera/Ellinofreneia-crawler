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

    let radio_links = get_radio_shows(&document);
    let tv_links = get_tv_shows(&document1);

    println!("{:#?}", radio_links);
    println!("{:#?}", tv_links);

    let limit = page_limit(&document);
    let limit1 = page_limit(&document1);
    println!("{:?}", limit);
    println!("{:?}", limit1);

    Ok(())
}

fn get_radio_shows(document: &Document) -> Vec<&str> {

    let radio_links: Vec<_> = document
        .find(Class("my-item"))
        .filter_map(|x| x.attr("href"))
        .collect();

    radio_links
}

fn get_tv_shows(document: &Document) -> Vec<&str> {

    let tv_links: Vec<_> = document
        .find(Class("yendif-thumbnail"))
        .filter_map(|x| x.attr("href"))
        .collect();

    tv_links
}

fn page_limit(document: &Document) -> Option<i32> {
    let limit = document.find(Attr("title", "Τέλος")).next();

    // println!("{:?}", limit);
    match limit {
        Some(foo) => {
            // It feels like regex
            let stop = foo.attr("href").unwrap();
            let mut bar: Vec<_> = stop.split("=").collect();
            bar.reverse();
            let num = bar.first().unwrap().parse().unwrap();

            // println!("{:?}", num);
            return Some(num);
        } 
        _ => None,
    }
}