impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let k = k as usize;
        let mut count = HashMap::new();
        let mut res = 0;
        let mut l = 0;

        for r in 0..s.len() {
            let e = count.entry(s[r]).or_insert(0usize);
            *e += 1;

            while (r - l + 1) - *count.values().max().unwrap_or(&0) > k {
                *count.get_mut(&s[l]).unwrap() -= 1;
                l += 1;
            }
            res = res.max(r - l + 1);
        }

        res as i32
    }
}