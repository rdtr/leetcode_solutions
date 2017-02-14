package main

func removeElement(nums []int, val int) int {
	nlen := len(nums)
	reslen := nlen
	curIdx := 0
	for i := 0; i < nlen; i++ {
		if nums[i] == val {
			reslen--
			continue
		}
		nums[curIdx] = nums[i]
		curIdx++

	}
	return reslen
}
