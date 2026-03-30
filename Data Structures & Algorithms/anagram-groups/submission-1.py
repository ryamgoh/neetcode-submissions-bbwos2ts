class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            anagrams[tuple(sorted(string))].append(string)

        return [ls for ls in anagrams.values()]