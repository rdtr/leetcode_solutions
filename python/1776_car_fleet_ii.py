class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = [-1.0] * len(cars)
        stack = []
        
        for i in range(len(cars) - 1, -1, -1):

            pos, speed = cars[i]
            
            while stack:
                if speed <= cars[stack[-1]][1]:
                    stack.pop()
                elif res[stack[-1]] > 0 and (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1]) >= res[stack[-1]]:
                    stack.pop()
                else:
                    break
            
            if stack:
                res[i] = (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1])
            stack.append(i)
        
        return res