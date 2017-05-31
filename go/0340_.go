func lengthOfLongestSubstringKDistinct(s string, k int) int {
	if k == 0 {
		return 0
	}

	left, right := 0, 0
	res := 0
	distMap := make(map[byte]int)
	for right < len(s) {
		ch := s[right]
		if cnt, ok := distMap[ch]; ok {
			distMap[ch] = cnt + 1
		} else {
			distMap[ch] = 1
		}

		if len(distMap) <= k {
			if right-left+1 > res {
				res = right - left + 1
			}
		} else {
			for len(distMap) > k {
				ch = s[left]
				distMap[ch] -= 1
				if distMap[ch] == 0 {
					delete(distMap, ch)
				}
				left++
			}
		}
		right++
	}
	return res
}