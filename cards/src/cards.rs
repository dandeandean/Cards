#[allow(dead_code)]
struct Card {
    front: String,
    back: String,
    img_path: Option<String>,
    notes: Option<String>,
    n_correct: usize,
    next_review: chrono::DateTime<chrono::Local>,
    easiness: f32,
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
            n_correct: 0,
            next_review: chrono::offset::Local::now(),
            easiness: 1.3,
        }
    }

    pub fn update_next_review(&mut self, n: usize) {
        self.next_review += chrono::Duration::days(n as i64);
    }
    pub fn sm2(&mut self, user_grade: usize) {
        if user_grade > 3 {
            match self.n_correct {
                0 => {
                    self.update_next_review(1);
                }
                1 => {
                    self.update_next_review(6);
                }
                _ => {
                    self.update_next_review(user_grade);
                }
            }
            self.n_correct += 1;
        } else {
            self.n_correct = 0;
            self.update_next_review(1);
        }
        let q = user_grade as f32;
        self.easiness += 0.1 - (5.0 - q) * (0.08 + (5.0 - q) * 0.02);
    }
}
