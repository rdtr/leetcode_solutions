import "math"

func longestConsecutive(nums []int) int {
	nlen := len(nums)
	if nlen == 0 {
		return 0
	} else if nlen == 1 {
		return 1
	}

	m := make(map[int]int)
	var val1, val2 int
	var ok1, ok2 bool
	for i := 0; i < nlen; i++ {
		val1, val2 = 0, 0
		ok1, ok2 = false, false
		num := nums[i]

		if _, ok := m[num]; ok {
			continue // redundant value
		}

		val := 1
		val1, ok1 = m[num+1]
		if ok1 {
			val += val1
		}

		val2, ok2 = m[num-1]
		if ok2 {
			val += val2
		}

		m[num] = val
		if ok1 {
			m[num+val1] = val
		}
		if ok2 {
			m[num-val2] = val
		}
	}

	max := math.MinInt32
	for _, v := range m {
		if v > max {
			max = v
		}
	}
	return max
}