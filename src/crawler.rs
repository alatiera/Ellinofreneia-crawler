use select::document::Document;
use select::predicate::{Attr, Class};
use reqwest;
use errors::*;

const BASE_URL: &str = "http://ellinofreneianet.gr/";
const _RADIO_SHOWS: &str = "radio/radio-shows-2.html";
const _TV_SHOWS: &str = "television/tv-shows.html";
const _RADIO_ARGS: &str = "?limit=11&start=";
const _TV_ARGS: &str = "?limit=21&start=";

#[derive(Debug, Clone)]
enum Show {
    Radio,
    Tv,
}

pub fn latest_radio(limit: u64) -> Result<Vec<String>> {
    let url = format!("{}{}{}", BASE_URL, _RADIO_SHOWS, _RADIO_ARGS);
    let links = backlog(&url, limit, Show::Radio);

    links
}

pub fn latest_tv(limit: u64) -> Result<Vec<String>> {
    let url = format!("{}{}{}", BASE_URL, _TV_SHOWS, _TV_ARGS);
    let links = backlog(&url, limit, Show::Tv);

    links
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

fn page_limit(document: &Document) -> Option<u64> {
    let limit = document.find(Attr("title", "Τέλος")).next();

    match limit {
        Some(foo) => {
            // It feels like regex
            let stop = foo.attr("href").unwrap();
            let mut bar: Vec<_> = stop.split("=").collect();
            bar.reverse();
            let num = bar.first().unwrap().parse().unwrap();

            info!("Page Limit Returned: {:?}", num);
            return Some(num);
        } 
        _ => None,
    }
}

// TODO: Refactor into an Iterator.
fn backlog(url: &str, limit: u64, show_step: Show) -> Result<Vec<String>> {
    let mut count = 0;
    let mut links: Vec<String> = vec![];

    let _res = reqwest::get(&format!("{}0", url))?;
    let _doc = Document::from_read(_res)?;
    let plimit = page_limit(&_doc).unwrap();

    // ensure that you dont fetch the whole backlog if not needed
    while count < limit && count <= plimit {
        info!("Count: {:?}", count);
        info!("Limit: {:?}", limit);

        let foo = format!("{}{}", url, count);
        info!("Calling {}", foo);

        let res = reqwest::get(&foo)?;
        let doc = Document::from_read(res)?;

        let l = match show_step {
            Show::Radio => get_radio_shows(&doc),
            Show::Tv => get_tv_shows(&doc),
        };

        debug!("Links Received: {:?}", l);
        for f in l {

            if links.len() >= limit as usize {
                break;
            }
            debug!("{:?}", f);
            debug!("{}{}", BASE_URL, f.to_string());
            links.push(format!("{}{}", BASE_URL, f.to_string()));
        }

        match show_step {
            Show::Radio => count += 11, 
            Show::Tv => count += 21, 
        };
    }
    Ok(links)
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn page_limit_test() {
        let radio = Document::from(include_str!("../tests/radio-shows-2.html"));
        assert_eq!(page_limit(&radio).unwrap(), 1221);

        let tv = Document::from(include_str!("../tests/tv-shows.html"));
        assert_eq!(page_limit(&tv).unwrap(), 231);
    }

    #[test]
    fn get_radio_test() {
        let radio = Document::from(include_str!("../tests/radio-shows-2.html"));
        let correct = vec![
            "/radio/radio-shows-2/1599-2017-09-08.html",
            "/radio/radio-shows-2/1596-2017-09-07.html",
            "/radio/radio-shows-2/1595-2017-09-06.html",
            "/radio/radio-shows-2/1594-2017-09-05.html",
            "/radio/radio-shows-2/1593-2017-09-04.html",
            "/radio/radio-shows-2/1592-2017-07-14.html",
            "/radio/radio-shows-2/1589-2017-07-13.html",
            "/radio/radio-shows-2/1588-2017-07-12.html",
            "/radio/radio-shows-2/1587-2017-07-11.html",
            "/radio/radio-shows-2/1586-2017-07-10.html",
            "/radio/radio-shows-2/1585-2017-07-07b.html",
        ];
        assert_eq!(get_radio_shows(&radio), correct);
    }

    #[test]
    fn get_tv_test() {
        let tv = Document::from(include_str!("../tests/tv-shows.html"));
        let correct = vec![
            "/television/tv-shows/video/301-20-06-2017.html",
            "/television/tv-shows/video/300-19-06-2017.html",
            "/television/tv-shows/video/299-13-06-2017.html",
            "/television/tv-shows/video/298-12-06-2017.html",
            "/television/tv-shows/video/297-06-06-2017.html",
            "/television/tv-shows/video/296-05-06-2017.html",
            "/television/tv-shows/video/295-30-05-2017.html",
            "/television/tv-shows/video/294-29-05-2017.html",
            "/television/tv-shows/video/293-23-05-2017.html",
            "/television/tv-shows/video/292-22-05-2017.html",
            "/television/tv-shows/video/291-16-05-2017.html",
            "/television/tv-shows/video/290-15-05-2017.html",
            "/television/tv-shows/video/289-09-05-2017.html",
            "/television/tv-shows/video/288-08-05-2017.html",
            "/television/tv-shows/video/287-02-05-2017.html",
            "/television/tv-shows/video/286-01-05-2017.html",
            "/television/tv-shows/video/285-25-04-201.html",
            "/television/tv-shows/video/284-24-04-2017.html",
            "/television/tv-shows/video/282-04-04-2017.html",
            "/television/tv-shows/video/281-03-04-2017.html",
            "/television/tv-shows/video/280-28-03-2017.html",
        ];

        assert_eq!(get_tv_shows(&tv), correct);
    }
}