impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        // O(1) space
        // O(N)
        // Sorted numbers
        // Return only 2 numbers to equal to target
        // Only 1 exact Solution
        let mut right = numbers.len() - 1;
        let mut left = 0;
        while left < right {
            if numbers[left] + numbers[right] == target {
                return vec![(left + 1) as i32, (right + 1) as i32]
            } else if numbers[left] + numbers[right] > target {
                right -= 1;
            } else {
                left += 1;
            }
        }
        unreachable!()
    }
}
