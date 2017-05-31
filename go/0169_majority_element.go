func majorityElement(nums []int) int {
	res, cnt := nums[0], 1
	for i := 1; i < len(nums); i++ {
		if nums[i] != res {
			cnt--
			if cnt == 0 {
				res, cnt = nums[i], 1
			}
			continue
		}
		cnt++
	}
	return res
}