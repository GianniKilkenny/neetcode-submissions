class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        heapq.heapify_max(stones)
        while len(stones) >= 3:
            x = stones[0]
            y = max(stones[1], stones[2])
            if x == y:
                heapq.heappop_max(stones)
                heapq.heappop_max(stones)
            else:
                new_x = x - y
                heapq.heappop_max(stones)
                heapq.heapreplace_max(stones, new_x)
        if len(stones) == 1:
            return stones[0]
        if stones[0] == stones[1]:
            return 0
        else:
            return stones[0] - stones[1]