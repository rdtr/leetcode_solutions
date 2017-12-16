func lengthOfLongestSubstringTwoDistinct(s string) int {
	slen := len(s)
	if slen <= 2 {
		return slen
	}

	left, right, max := 0, 0, 0
	m := make(map[byte]int)
	for {
		if len(m) > 2 {
			for {
				count := m[s[left]]
				if count == 1 {
					delete(m, s[left])
					if len(m) <= 2 {
						left++
						break
					}
				} else {
					m[s[left]] = count - 1
				}
				left++
			}
		} else {
			count, ok := m[s[right]]
			if !ok {
				m[s[right]] = 1
			} else {
				m[s[right]] = count + 1
			}

			if len(m) <= 2 && right-left+1 > max {
				max = right - left + 1
			}
			right++
			if right == len(s) {
				break
			}
		}
	}
	return max
}