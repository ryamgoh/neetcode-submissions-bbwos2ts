class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def dfs(start_index):
            # Base case: reached end of string - return list with empty path
            if start_index == len(s):
                return [[]]  # List of paths, each path is a list of words
            
            # Check memoization
            if start_index in memo:
                return memo[start_index]
            
            # Initialize answer as empty list of paths
            all_paths = []
            
            # Try all possible words starting at start_index
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                
                if word in word_set:
                    # Get all paths from the remaining string
                    next_paths = dfs(end_index)
                    
                    # Prepend current word to each path
                    for path in next_paths:
                        all_paths.append([word] + path)
            
            # Memoize and return
            memo[start_index] = all_paths
            return all_paths
        
        # Convert list of word lists to strings
        paths = dfs(0)
        return [' '.join(path) for path in paths]