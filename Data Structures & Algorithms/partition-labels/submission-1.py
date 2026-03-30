class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count = Counter(s)            

        L = 0
        curr_set = set()
        res = []
        no_zero = 0
        for R in range(len(s)):
            curr_set.add(s[R])
            # decrement count
            if s[R] in count:
                count[s[R]] -= 1
                if count[s[R]] == 0:
                    no_zero += 1
            if no_zero == len(curr_set):
                curr_set.clear()
                res.append(R - L + 1)
                no_zero = 0
                L = R + 1

        return res