import "bytes"

func repeatedStringMatch(A string, B string) int {
	alen, blen := len(A), len(B)
	var a bytes.Buffer
	res := 0
	shouldBreak := false
	for !shouldBreak {
		if res*alen > blen {
			shouldBreak = true
		}
		a.WriteString(A)
		res++

		if isMatch(a.String(), B) {
			return res
		}
	}
	return -1
}

func isMatch(haystack, needle string) bool {
	if len(needle) > len(haystack) {
		return false
	}
	table := make(map[byte]int)
	for i, dist := len(needle)-1, 0; i >= 0; i, dist = i-1, dist+1 {
		if _, ok := table[needle[i]]; !ok {
			table[needle[i]] = dist
		}
	}

	for i := len(needle) - 1; i < len(haystack); {
		for diff := 0; diff < len(needle); diff++ {
			if haystack[i-diff] == needle[len(needle)-1-diff] {
				if diff == len(needle)-1 {
					return true
				}
				continue
			}
			slide, ok := table[haystack[i-diff]]
			if !ok {
				slide = len(needle)
			}
			if next := i + (slide - diff); next > i {
				i = next
			} else {
				i++
			}
			break
		}
	}
	return false
}