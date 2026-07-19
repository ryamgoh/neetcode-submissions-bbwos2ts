impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut left = 0;
        let mut right = s.len();

        let bytes = s.as_bytes(); // More efficient for this problem

        while left < right {
            if !bytes[left].is_ascii_alphanumeric() {
                left += 1;
                continue;
            }
            
            if !bytes[right - 1].is_ascii_alphanumeric() {
                right -= 1;
                continue;
            }

            // Compare (case-insensitive)
            if left < right {
                if bytes[left].to_ascii_lowercase() != bytes[right - 1].to_ascii_lowercase() {
                    return false;
                }
                left += 1;
                right -= 1;
            }
        }

        true
    }
}