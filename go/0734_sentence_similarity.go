package main

func areSentencesSimilar(words1 []string, words2 []string, pairs [][]string) bool {
	wlen := len(words1)
	if wlen != len(words2) {
		return false
	}

	// setup map
	pairMap := make(map[string]map[string]int8)
	for _, pair := range pairs {
		if existing, ok := pairMap[pair[0]]; !ok {
			pairMap[pair[0]] = make(map[string]int8)
		}
		pairMap[pair[0]][pair[1]] = 1
	}

	// compare
	for i := 0; i < wlen; i++ {
		w1, w2 := words1[i], words2[i]
		if w1 == w2 {
			continue
		}
		if inner, ok := pairMap[w1]; ok {
			if _, ok := inner[w2]; ok {
				continue
			}
		}
		if inner, ok := pairMap[w2]; ok {
			if _, ok := inner[w1]; ok {
				continue
			}
		}
		return false
	}
	return true
}
