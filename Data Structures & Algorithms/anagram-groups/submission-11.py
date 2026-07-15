class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramToList = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagramToList[key].append(s)

        return list(anagramToList.values())