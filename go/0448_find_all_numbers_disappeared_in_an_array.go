func findDisappearedNumbers(nums []int) []int {
	nlen := len(nums)
	for i := 0; i < nlen; {
		if nums[i] != i+1 && nums[nums[i]-1] != nums[i] {
			nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
			continue
		}
		i++
	}

	var res []int
	for i := 0; i < nlen; i++ {
		if nums[i] != i+1 {
			res = append(res, i+1)
		}
	}
	return res
}