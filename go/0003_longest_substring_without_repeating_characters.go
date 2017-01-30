package main

func lengthOfLongestSubstring(s string) int {
	m := make(map[rune]int)
	start := 0
	l := 0
	for i, ch := range s {
		if preIdx, ok := m[ch]; ok && m[ch] >= start {
			start = preIdx + 1
			m[ch] = i
			continue
		}

		if dist := i - start + 1; dist > l {
			l = dist
		}
		m[ch] = i
	}
	return l
}
