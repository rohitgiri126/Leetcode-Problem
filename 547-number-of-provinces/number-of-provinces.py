class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        self.visited=set()
        def dfs(city):
            self.visited.add(city)
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and neighbour not in self.visited:
                    dfs(neighbour)
        self.provinces=0
        for city in range(n):
            if city not in self.visited:
                self.provinces+=1
                dfs(city)
             
        return self.provinces                