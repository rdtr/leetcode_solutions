func partition(s string) [][]string {
	var res [][]string
	cache := make(map[string]bool)

	var curRes []string
	doPartition(s, &res, curRes, cache)
	return res
}

func doPartition(s string, res *[][]string, curRes []string, cache map[string]bool) {
	slen := len(s)
	if slen == 0 && len(curRes) > 0 {
		newRes := make([]string, len(curRes))
		copy(newRes, curRes)
		*res = append(*res, newRes)
		return
	}

	for i := 1; i <= slen; i++ {
		s1, s2 := s[:i], s[i:]
		if isParlindrome(s1, cache) {
			doPartition(s2, res, append(curRes, s1), cache)
		}
	}
}

func isParlindrome(s string, cache map[string]bool) bool {
	if len(s) == 1 {
		return true
	}

	if _, ok := cache[s]; ok {
		return true
	}

	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}

	cache[s] = true
	return cache[s]
}