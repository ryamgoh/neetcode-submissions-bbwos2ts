impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let length = nums.len();
        let length_half = length / 2;
        let mut res: HashMap<i32, i32> = HashMap::new();
        
        for num in nums {
            // Get current count or insert 0
            let count = res.entry(num).or_insert(0);
            *count += 1;  // Increment the count
            
            // Check if this element now has majority
            if *count > length_half as i32 {
                return num;
            }
        }
        
        // This should never be reached (majority element always exists)
        unreachable!()
    }
}