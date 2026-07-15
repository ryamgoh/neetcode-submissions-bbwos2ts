impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hash_map: HashMap<String, Vec<String>> = HashMap::new();
        for s in &strs {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort();
            let sorted_s: String = chars.into_iter().collect();
            hash_map.entry(sorted_s).or_default().push(s.clone());
        }
        hash_map.into_values().collect()
    }
}
