func partition(s string) [][]string {
	slen := len(s)
	if slen == 0 {
		return [][]string{}
	}

	var res [][]string
	if isPalindrome(s) {
		res = append(res, []string{s})
	}
	doPartition(&res, []string{s})
	return res
}

func doPartition(res *[][]string, strs []string) {
	slen := len(strs)
	lastStr := strs[slen-1]
	if len(lastStr) == 1 {
		return // no new partition can be created
	}

	for i := 0; i < len(lastStr)-1; i++ {
		splitted0, splitted1 := lastStr[0:i+1], lastStr[i+1:]
		if !isPalindrome(splitted0) {
			continue
		}
		newStrs := make([]string, slen+1)
		copy(newStrs[:slen-1], strs[:slen-1])
		newStrs[slen-1], newStrs[slen] = splitted0, splitted1

		if isPalindrome(splitted1) {
			*res = append(*res, newStrs)
		}
		doPartition(res, newStrs)
	}
}

func isPalindrome(s string) bool {
	slen := len(s)
	for i, j := 0, slen-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}