package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int) // key: number, value: index
	for i, num := range nums {
		if index, ok := m[target-num]; ok {
			return []int{index, i}
		}
		m[num] = i
	}
	return nil
}
