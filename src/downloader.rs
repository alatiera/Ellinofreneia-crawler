use reqwest;
use select::document::Document;
use select::predicate::{Class, Attr};
use errors::*;

pub fn youtube_dl(url: &str) -> Result<()> {
    let res = reqwest::get(url)?;

    let doc = Document::from_read(res)?;

    Ok(())
}

fn get_youtube_url(document: &Document) -> Result<String> {
    let tv_link: Vec<_> = document
        .find(Attr("type", "video/youtube"))
        .filter_map(|x| x.attr("src"))
        .collect();
    // println!("{:#?}", tv_link);

    // FIXME: compiler dsnt like &&str :3, and with good reason prolly
    // let foo = tv_link.first()?.to_string();
    let foo = tv_link.first().unwrap().to_string();

    Ok(foo)
}

#[cfg(test)]
#[test]
fn test_youtube_url() {
    let doc = Document::from(include_str!("../tests/tv_episode.html"));
    let url = String::from("http://www.youtube.com/watch?v=xwAkcgkhiak");
    let foo = get_youtube_url(&doc).unwrap();
    assert_eq!(foo, url);
}