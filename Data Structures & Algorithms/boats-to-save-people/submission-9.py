class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = Counter(people)
        sorted_people = []
        print(counter)
        for i in range(limit + 1):
            if i in counter:
                sorted_people.extend([i] * counter[i])        
        L = 0
        R = len(sorted_people) - 1
        counter = 0

        while L <= R:
            if sorted_people[L] + sorted_people[R] <= limit:
                L += 1
            R -= 1
            counter += 1
        
        return counter