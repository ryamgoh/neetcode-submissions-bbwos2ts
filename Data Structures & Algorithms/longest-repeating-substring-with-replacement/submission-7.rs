impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let k = k as usize;
        let mut res = 0;

        for i in 0..s.len() {
            let mut count = HashMap::new();
            let mut maxf = 0;
            for j in i..s.len() {
                let e = count.entry(s[j]).or_insert(0);
                *e += 1;
                maxf = maxf.max(*e);
                if (j - i + 1) - maxf <= k {
                    res = res.max(j - i + 1);
                }
            }
        }

        res as i32
    }
}