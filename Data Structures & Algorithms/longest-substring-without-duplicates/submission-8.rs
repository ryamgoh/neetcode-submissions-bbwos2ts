impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let s = s.as_bytes();
        let mut char_set = HashSet::new();
        let mut left = 0;
        let mut res = 0;

        for right in 0..s.len() {
            while char_set.contains(&s[right]) {
                char_set.remove(&s[left]);
                left += 1;
            }
            char_set.insert(&s[right]);
            res = res.max(right - left + 1);
        }

        res as i32
    }
}
