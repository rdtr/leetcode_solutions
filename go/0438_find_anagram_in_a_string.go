func findAnagrams(s string, p string) []int {
	slen, plen := len(s), len(p)
	if slen < plen {
		return []int{}
	}

	var table [26]int
	for i := 0; i < plen; i++ {
		table[int(p[i])-int('a')]++
		table[int(s[i])-int('a')]--
	}

	var res []int
	if check(table) {
		res = append(res, 0)
	}

	for i := plen; i < slen; i++ {
		table[int(s[i])-int('a')]--
		table[int(s[i-plen])-int('a')]++
		if check(table) {
			res = append(res, i-plen+1)
		}
	}
	return res
}

func check(arr [26]int) bool {
	for i := 0; i < len(arr); i++ {
		if arr[i] != 0 {
			return false
		}
	}
	return true
}