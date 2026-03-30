class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)

        L = 0
        R = len(people) - 1
        counter = 0

        while L <= R:
            if sorted_people[L] + sorted_people[R] <= limit:
                L += 1
            R -= 1
            counter += 1
        
        return counter