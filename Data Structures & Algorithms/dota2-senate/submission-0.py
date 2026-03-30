class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q, dire_q = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant_q.append(i)
            else:
                dire_q.append(i)
            
        while radiant_q and dire_q:
            radiant_head = radiant_q.popleft()
            dire_head = dire_q.popleft()

            if radiant_head < dire_head:
                radiant_q.append(radiant_head + len(senate))
            else:
                dire_q.append(dire_head + len(senate))
        
        return "Radiant" if radiant_q else "Dire"