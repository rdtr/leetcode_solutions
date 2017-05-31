func wordBreak(s string, wordDict []string) bool {
	dlen := len(wordDict)
	if dlen == 0 {
		return false
	}
	mp := make(map[string]bool) // caching

	var que []string
	word := ""
	for {
		for i := 0; i < dlen; i++ {
			newWord := word + wordDict[i]
			if _, ok := mp[newWord]; ok {
				continue
			}

			if newWord == s {
				return true
			}
			if nlen := len(newWord); nlen >= len(s) || newWord != s[:nlen] {
				continue
			}

			mp[newWord] = true
			que = append(que, newWord)
		}

		if len(que) == 0 {
			break
		}
		word = que[0]
		que = que[1:]
	}
	return false
}
