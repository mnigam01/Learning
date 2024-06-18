class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)

        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.counter[(x,y)]+=1
        

    def count(self, point: List[int]) -> int:
        x,y = point
        count = 0
        
        for X,Y in list(self.counter.keys()):
            if X==x:
                if x==X and y==Y:
                    continue
                # print(X,Y)
                length = abs(X-x) + abs(y-Y)
                for delta in [length,-length]:
                    count += self.counter[(x+delta,y)]*self.counter[(X+delta,Y)]*self.counter[(X,Y)]
            
        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


class DetectSquares:

    def __init__(self):
        self.points_xi = defaultdict(list)
        self.counter = defaultdict(int)

        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points_xi[x].append([x,y])
        self.counter[(x,y)]+=1
        

    def count(self, point: List[int]) -> int:
        x,y = point
        count = 0
        # print(self.points_xi[x])
        # print(self.counter)
        for X,Y in self.points_xi[x]:
            if x==X and y==Y:
                continue
            length = abs(X-x) + abs(y-Y)
            for delta in [length,-length]:
                count += self.counter[(x+delta,y)]*self.counter[(X+delta,Y)]
            
        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)