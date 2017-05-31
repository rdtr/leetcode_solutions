func wordBreak(s string, wordDict []string) []string {
	var res []string
	visited := make(map[string]bool)

	for _, w := range wordDict {
		backtrack(w, w, &res, visited, wordDict, s)
	}
	return res
}

func backtrack(word, wordSpace string, res *[]string, visited map[string]bool, wordDict []string, target string) {
	if len(word) > len(target) || target[:len(word)] != word {
		return
	}

	if _, ok := visited[wordSpace]; ok {
		return
	}
	visited[wordSpace] = true

	if word == target {
		*res = append(*res, wordSpace)
		return
	}

	for i := 0; i < len(wordDict); i++ {
		backtrack(word+wordDict[i], wordSpace+" "+wordDict[i], res, visited, wordDict, target)
	}
}