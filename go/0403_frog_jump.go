func canCross(stones []int) bool {
	slen := len(stones)
	if slen == 0 {
		return true
	}
	if stones[1] != 1 {
		return false
	}

	mp := make(map[int]int)
	for i := 0; i < slen; i++ {
		mp[stones[i]] = i
	}

	var res bool
	visited := make(map[[2]int]bool)

	jump(1, 1, mp, slen-1, visited, &res)
	return res
}

func jump(curStone int, prevStep int, stoneMap map[int]int, targetIndex int, visitedMap map[[2]int]bool, res *bool) {
	if stoneMap[curStone] == targetIndex {
		*res = true
	}
	if *res {
		return
	}
	if _, ok := visitedMap[[2]int{curStone, prevStep}]; ok {
		return
	}
	visitedMap[[2]int{curStone, prevStep}] = true

	if _, ok := stoneMap[curStone+prevStep]; ok {
		jump(curStone+prevStep, prevStep, stoneMap, targetIndex, visitedMap, res)
	}
	if _, ok := stoneMap[curStone+prevStep+1]; ok {
		jump(curStone+prevStep+1, prevStep+1, stoneMap, targetIndex, visitedMap, res)
	}
	if prevStep > 1 {
		if _, ok := stoneMap[curStone+prevStep-1]; ok {
			jump(curStone+prevStep-1, prevStep-1, stoneMap, targetIndex, visitedMap, res)
		}
	}
}