package main

import "sort"

func combinationSum(candidates []int, target int) [][]int {
	var res [][]int
	sort.Ints(candidates)
	doCombinationSum(&res, candidates, []int{}, target, 0, 0)
	return res
}

func doCombinationSum(res *[][]int, candidates []int, currentCandidates []int, target int, currentSum int, index int) {
	if currentSum == target {
		*res = append(*res, currentCandidates)
		return
	} else if currentSum > target {
		return
	}

	for i := index; i < len(candidates); i++ {
		newCandidates := make([]int, len(currentCandidates)+1)
		copy(newCandidates[:len(currentCandidates)], currentCandidates)
		newCandidates[len(newCandidates)-1] = candidates[i]

		doCombinationSum(res, candidates, newCandidates, target, currentSum+candidates[i], i)
	}
}
