func lengthOfLongestSubstringKDistinct(s string, k int) int {
	mp := make(map[byte]int)
	res, left, right := 0, 0, 0

	slen := len(s)
	for right <= slen-1 {
		if mplen := len(mp); mplen <= k {
			if count, ok := mp[s[right]]; !ok {
				mp[s[right]] = 1
			} else {
				mp[s[right]] = count + 1
			}

			if len(mp) <= k && right-left+1 > res {
				res = right - left + 1
			}
			right++
		} else {
			count := mp[s[left]]
			if count == 1 {
				delete(mp, s[left])
			} else {
				mp[s[left]] = count - 1
			}
			left++
		}
	}
	return res
}