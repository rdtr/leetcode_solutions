class Solution:
    def findContestMatch(self, n: int) -> str:
        nums = [i for i in range(1, n + 1)]

        while len(nums) > 2:
            newNums = []
            left, right = 0, len(nums) - 1
            while left < right:
                pair = '(' + str(nums[left]) + ',' + str(nums[right]) + ')'
                newNums.append(pair)
                left += 1
                right -= 1
            nums = newNums
        return '(' + str(nums[0]) + ',' + str(nums[1]) + ')'
