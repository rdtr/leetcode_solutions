func totalFruit(tree []int) int {
	res := 0
	m := make(map[int]int)

	for left, right := 0, 0; right < len(tree); right++ {
		if cnt, ok := m[tree[right]]; ok {
			m[tree[right]] = cnt + 1
		} else {
			m[tree[right]] = 1
		}

		for len(m) > 2 {
			if cnt, ok := m[tree[left]]; ok {
				m[tree[left]] = cnt - 1
				if cnt == 1 {
					delete(m, tree[left])
				}
			}
			left++
		}

		if dist := right - left + 1; dist > res {
			res = dist
		}
	}
	return res
}