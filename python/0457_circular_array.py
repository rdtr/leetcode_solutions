class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        for j in range(len(nums)):
            i = j 
            allVisited = set([i])
            visited = set([i])
            forward = nums[i] > 0            
            
            while True:
                if forward and nums[i] < 0:
                    forward = False
                    visited.clear()
                elif not forward and nums[i] > 0:
                    forward = True
                    visited.clear()
                
                tmp = i
                i = move(i, nums[i], nums)

                if i == tmp:
                    break
                if i in visited:
                    return True
                if i in allVisited:
                    break
            
                visited.add(i)
                allVisited.add(i)
        return False
            
def move(i, dist, nums):
    i += dist % len(nums)
    if i >= len(nums):
        return i - len(nums)
    if i < 0:
        return i + len(nums)
    return i
            