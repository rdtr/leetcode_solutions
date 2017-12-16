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

func wordBreak(s string, wordDict []string) bool {
	dp := make([]bool, len(s)+1)
	dp[0] = true
	for i := 0; i < len(dp); i++ {
		if dp[i] {
			for _, word := range wordDict {
				if i+len(word) <= len(s) && s[i:i+len(word)] == word {
					dp[i+len(word)] = true
				}
			}
		}
	}
	return dp[len(s)]
}