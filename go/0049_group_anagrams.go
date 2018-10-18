func groupAnagrams(strs []string) [][]string {
	m := make(map[[26]int][]string)
	for i := 0; i < len(strs); i++ {
		str := strs[i]

		var k [26]int
		for j := 0; j < len(str); j++ {
			k[(str[j]-'a')]++
		}

		if _, ok := m[k]; ok {
			m[k] = append(m[k], str)
		} else {
			m[k] = []string{str}
		}
	}

	var res [][]string
	for _, v := range m {
		res = append(res, v)
	}
	return res
}