class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def dp(i):
            if i == 0:
                return [1]
            
            curRow = [1]
            prevRow = dp(i - 1)

            for j in range(1, i):
                curRow.append(prevRow[j - 1] + prevRow[j])

            curRow.append(1)

            return curRow



        return dp(rowIndex)