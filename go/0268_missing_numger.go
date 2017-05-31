func missingNumber(nums []int) int {
	nlen := len(nums)
	if nlen == 0 {
		return 0
	}

	res := nums[0]
	for i := 0; i < nlen+1; i++ {
		if i == 0 || i == nlen {
			res = res ^ i
			continue
		}
		res = res ^ i ^ nums[i]
	}
	return res
}