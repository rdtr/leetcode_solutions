class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nlen = len(nums)
        if nlen <= 1:
            return nums
        
        k = k % nlen
        if k == 0:
            return nums

        count = 0
        start_idx = 0
        while count < nlen:
            cur_idx = start_idx
            cur = nums[start_idx]

            while True:
                new_idx = (cur_idx + k) % nlen
                cur, nums[new_idx] = nums[new_idx], cur
                cur_idx = new_idx
                count += 1
                
                if new_idx == start_idx:
                    break
            start_idx += 1
        
        return nums
