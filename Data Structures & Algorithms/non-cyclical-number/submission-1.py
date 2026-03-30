class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        def recursion(n):
            if n in hashset:
                return False
            elif n == 1:
                return True
            else:
                hashset.add(n)
                new_number = 0
                while n > 0:
                    num = (n % 10)
                    new_number += num ** 2
                    n //= 10
                return recursion(new_number)

        return recursion(n)
