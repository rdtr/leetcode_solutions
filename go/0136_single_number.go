package main

func singleNumber(nums []int) int {
	var res int
	for _, num := range nums {
		res ^= num
	}
	return res
}

func singleNumber2(nums []int) int {
	m := make(map[int]int)
	for _, num := range nums {
		if mnum, ok := m[num]; !ok {
			m[num] = 1
		} else if mnum == 1 {
			delete(m, num)
		}
	}
	// only 1 element should be left
	for res := range m {
		return res
	}
	return 0
}
