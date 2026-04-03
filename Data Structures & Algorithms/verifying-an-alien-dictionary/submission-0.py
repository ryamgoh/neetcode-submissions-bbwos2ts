class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # alien dictionary
        orderInd = { c: i for i, c in enumerate(order)}

        # outer for loop to look thru each pair
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]

            for j in range(len(word_1)):
                if j == len(word_2):
                    return False # This means that word_2 is a prefix of word_1

                if word_1[j] != word_2[j]:
                    if orderInd[word_1[j]] > orderInd[word_2[j]]:
                        return False
                    break

        return True