#[allow(dead_code)]
struct Card {
    front: String,
    back: String,
    img_path: Option<String>,
    notes: Option<String>,
}

#[allow(dead_code)]
// TODO: impl https://en.wikipedia.org/wiki/SuperMemo
impl Card {
    pub fn from(front: String, back: String) -> Card {
        Card {
            front,
            back,
            img_path: None,
            notes: None,
        }
    }
}
