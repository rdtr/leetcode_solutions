func removeDuplicateLetters(s string) string {
	hashMap := [26]int{}
	visited := [26]bool{}

	for i := range s {
		hashMap[int(s[i])-int('a')] = i
	}

	var res []byte
	for i := range s {
		ch := s[i]
		for len(res) > 0 {
			lastCh := res[len(res)-1]
			if ch <= lastCh && hashMap[int(lastCh)-int('a')] >= i && !visited[int(ch)-int('a')] {
				visited[int(lastCh)-int('a')] = false
				res = res[:len(res)-1]
				continue
			}
			break
		}

		if !visited[int(ch)-int('a')] {
			res = append(res, ch)
			visited[int(ch)-int('a')] = true
		}
	}
	return string(res)
}