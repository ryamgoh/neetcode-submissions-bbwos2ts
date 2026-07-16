impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        // We might have to look through all combinations
        // But this would be too much time O(N^2) actually
        // In this case, we should go for a two pointer approach
        // Where at any point in time, we try to keep the tallest bar
        // In the event we find another taller bar, we can keep hold onto that
        // At each movement, we just calculate the max_area!
        // Intuition: We calculate Breath * Height for the area, and we want to keep a taller bar,
        // because a tall bar and another tall bar would lead to a long height of area, giving us a chance
        // to upsert the max_area
        let mut left = 0;
        let mut right = heights.len() - 1;
        let mut best = 0;

        while left < right {
            // Calculate the current area
            let length = (right - left) as i32;
            let height = heights[left].min(heights[right]);
            best = best.max(length * height);
            if heights[left] > heights[right] {
                right -= 1;
            } else {
                left += 1
            }
        }
        best
    }
}
