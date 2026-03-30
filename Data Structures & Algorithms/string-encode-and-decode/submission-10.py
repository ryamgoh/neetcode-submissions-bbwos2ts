class Solution:

    def encode(self, strs) -> str:
        # O(n)
        res = ''.join(
            f'{len(s)}#{s}'
            for s in strs  
        )
        return res

    def decode(self, s: str) -> List[str]:
        idx = 0
        length = 0
        res = []
        while idx < len(s):
            if s[idx].isnumeric():
                start_num_idx = idx
                while s[idx].isnumeric():
                    idx += 1
                length = int(s[start_num_idx:idx])
            elif s[idx] == "#":
                idx += 1
                next_word = s[idx : idx + length]
                res.append(next_word)
                idx += length

        return res
            