

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        ptd = {}

        for i in range(len(points)):
            distance = math.sqrt((points[i][0] ** 2) + (points[i][1] **2))
            distances.append(distance)
            if distance not in ptd:
                ptd[distance] = []
                ptd[distance].append(points[i])
            else:
                ptd[distance].append(points[i])
        heapq.heapify(distances)
        res = []
        while len(res) < k:
            distance = heapq.heappop(distances)
            res.append(ptd[distance][0])
            ptd[distance].remove(ptd[distance][0])
        return res
        
        

        

            