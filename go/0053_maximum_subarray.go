package main

func maxSubArray(nums []int) int {
	nlen := len(nums)
	if nlen == 0 {
		return 0
	} else if nlen == 1 {
		return nums[0]
	}

	var num int
	max, curSum := nums[0], nums[0]
	if nums[0] < 0 {
		curSum = 0
	}
	for i := 1; i < nlen; i++ {
		num = nums[i]
		curSum += num
		if curSum > max {
			max = curSum
		}
		if curSum < 0 {
			curSum = 0
		}
	}
	return max
}
