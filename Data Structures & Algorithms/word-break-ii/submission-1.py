class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        result = []  # ans
        
        def dfs(start_index, path):  # path is current_words
            # Base case: reached end of string
            if start_index == len(s):
                result.append(path[:])  # add a copy of the path
                return
            
            # Try all possible edges (words)
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                
                # Prune if word not in dictionary
                if word not in word_set:
                    continue
                
                # Add edge to path
                path.append(word)
                
                # Recurse
                dfs(end_index, path)
                
                # Backtrack
                path.pop()
        
        dfs(0, [])
        return [' '.join(words) for words in result]