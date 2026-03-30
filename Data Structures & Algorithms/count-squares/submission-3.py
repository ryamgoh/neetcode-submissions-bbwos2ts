from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.duplicatesByPoint = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        tup = tuple(point)
        self.duplicatesByPoint[tup] += 1
        self.points.append(tup)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        
        for x, y in self.points:
            # Check if (x,y) can be a diagonal corner
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
                
            # Check if the other two corners exist
            if (x, py) in self.duplicatesByPoint and (px, y) in self.duplicatesByPoint:
                res += self.duplicatesByPoint[(x, py)] * self.duplicatesByPoint[(px, y)]
        
        return res