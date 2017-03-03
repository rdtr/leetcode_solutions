package main

func permute(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{}
	}
	var res [][]int
	doPermute(&res, []int{}, nums)
	return res
}

func doPermute(res *[][]int, currentNums []int, remainingNums []int) {
	rlen := len(remainingNums)
	if rlen == 0 {
		*res = append(*res, currentNums)
		return
	}

	for i := 0; i < rlen; i++ {
		newRemaining := make([]int, rlen-1)
		copy(newRemaining[:i], remainingNums[:i])
		copy(newRemaining[i:], remainingNums[i+1:])

		newCurrent := make([]int, len(currentNums)+1)
		copy(newCurrent[:len(currentNums)], currentNums)
		newCurrent[len(currentNums)] = remainingNums[i]

		doPermute(res, newCurrent, newRemaining)
	}
}
