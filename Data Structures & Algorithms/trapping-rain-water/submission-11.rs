impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();
        if n == 0 {
            return 0;
        }
        
        // Left pass (borrow instead of consume)
        let mut curr_left_max = i32::MIN;
        let left_max: Vec<i32> = height
            .iter()  // ✅ Borrow instead of consume
            .map(|&x| {
                curr_left_max = curr_left_max.max(x);
                curr_left_max
            })
            .collect();
        
        // Right pass - store in correct order
        let mut curr_right_max = i32::MIN;
        let mut right_max = vec![0; n];
        for i in (0..n).rev() {
            curr_right_max = curr_right_max.max(height[i]);
            right_max[i] = curr_right_max;
        }
        
        // Calculate trapped water
        let mut res = 0;  // ✅ Make mutable
        for i in 0..n {
            let max_height = left_max[i].min(right_max[i]);  // ✅ Use min, not max!
            if max_height > height[i] {
                res += max_height - height[i];
            }
        }
        
        res
    }
}