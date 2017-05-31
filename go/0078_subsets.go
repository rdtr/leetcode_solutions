package main

func subsets(nums []int) [][]int {
	res := [][]int{}
	backtrack([]int{}, nil, &res)
	for i, num := range nums {
		backtrack([]int{num}, nums[i+1:], &res)
	}
	return res
}

func backtrack(subset []int, nums []int, res *[][]int) {
	if len(nums) == 0 {
		*res = append(*res, subset)
		return
	}

	backtrack(subset, nil, res)
	for i, num := range nums {
		newSubset := make([]int, len(subset)+1)
		copy(newSubset[0:len(subset)], subset)
		newSubset[len(subset)] = num

		backtrack(newSubset, nums[i+1:], res)
	}
}
