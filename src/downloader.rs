use reqwest;
use select::document::Document;
use select::predicate::Attr;
use rafy::Rafy;
use errors::*;

pub fn from_youtube(url: &str) -> Result<()> {
    info!("Calling {}", url);
    let res = reqwest::get(url)?;

    let doc = Document::from_read(res)?;
    let yt = get_youtube_url(&doc)?;
    rafy_dl(&yt)?;

    Ok(())
}

fn rafy_dl(yt_url: &str) -> Result<()> {
    info!("Starting download of: {:?}", yt_url);
    // Copied directly from the Raffy Example.
    let content = Rafy::new(yt_url).unwrap();
    // Rafy::Error dsnt impl Send yet I think so it cant be added to error-chain
    // let content = Rafy::new(yt_url)?;
    let title = content.title;
    info!("Video title: {:?}", title);
    let streams = content.streams;
    // Debug not implemented for stream structs
    // info!("Rafy streams Struct: {:?}", streams);
    let ref stream = streams[0];
    // stream.download(&title)?;
    info!("Downloading {:?}", title);
    stream.download(&title).unwrap();
    Ok(())
}

fn get_youtube_url(document: &Document) -> Result<String> {
    let tv_link: Vec<_> = document
        .find(Attr("type", "video/youtube"))
        .filter_map(|x| x.attr("src"))
        .collect();
    info!("Found video(s): {:?}", tv_link);

    // FIXME: compiler dsnt like &&str :3, and with good reason prolly
    // let foo = tv_link.first()?.to_string();
    let foo = tv_link.first().unwrap().to_string();
    debug!("Returned youtube url: {}", foo);

    Ok(foo)
}

// TODO: make it a test and check for the downloaded file
pub fn to_be_made_into_test() -> Result<()> {
    let f = "http://www.ellinofreneianet.gr/television/tv-shows/video/301-20-06-2017.html";
    from_youtube(f)?;
    Ok(())
}

#[cfg(test)]
#[test]
fn test_youtube_url() {
    let doc = Document::from(include_str!("../tests/tv_episode.html"));
    let url = String::from("http://www.youtube.com/watch?v=xwAkcgkhiak");
    let foo = get_youtube_url(&doc).unwrap();
    assert_eq!(foo, url);
}
