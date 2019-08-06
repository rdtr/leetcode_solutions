package main

func combinationSum(candidates []int, target int) [][]int {
	var res [][]int
	for i, cand := range(candidates) {
		helper(target, i, candidates[i], []int{cand}, &res, candidates)
	}
	return res
}

func helper(target, curIndex, curSum int, cur []int, res *[][]int, candidates []int) {
	if curSum == target {
		ans := make([]int, len(cur))
		copy(ans, cur)
		*res = append(*res, ans)
	} else if curSum < target {
		for i := curIndex; i < len(candidates); i++ {
			cur = append(cur, candidates[i])
			helper(target, i, curSum + candidates[i], cur, res, candidates)
			cur = cur[:len(cur) - 1]
		}
	}
}

