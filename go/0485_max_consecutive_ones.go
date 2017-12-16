func findMaxConsecutiveOnes(nums []int) int {
	curCnt := 0
	maxCnt := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			curCnt++
			if curCnt > maxCnt {
				maxCnt = curCnt
			}
		} else {
			curCnt = 0
		}
	}
	return maxCnt
}