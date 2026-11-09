class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        m = len(costs)//2
        total = 0
        
        #sort by the difference between cost to city A and city B 
        costs.sort(key=lambda x: x[0] - x[1])
        
        
        for i in range(m):
            total += costs[i][0]
        for i in range(m, 2*m):
            total += costs[i][1]
        return total
        # i cant think sort by differce costa city a-cityb so it can gaurantee half is city a is cheaper and half is city b is cheaper