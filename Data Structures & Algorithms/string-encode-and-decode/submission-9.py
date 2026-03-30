class Solution:

    def encode(self, strs) -> str:
        # O(n)
        res = ''.join(
            f'{len(s)}#{s}'
            for s in strs  
        )
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        length = 0
        while l < len(s):
            if s[l].isnumeric():
                curr_i = l
                while s[l].isnumeric():
                    l += 1
                length = int(s[curr_i:l])
            elif s[l] == "#":
                l += 1
                next_word = s[l : l + length]
                res.append(next_word)
                l += length
            print(l)

        return res
            