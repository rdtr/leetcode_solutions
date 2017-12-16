func reverseVowels(s string) string {
	slen := len(s)
	if slen == 0 {
		return ""
	}

	b := []byte(s)
	left, right := 0, slen-1
OUTER:
	for left < right {
		for !isVowel(b[right]) {
			right--
			if left >= right {
				break OUTER
			}
		}

		for !isVowel(b[left]) {
			left++
			if left >= right {
				break OUTER
			}
		}

		b[left], b[right] = b[right], b[left]
		left++
		right--
	}
	return string(b)
}

func isVowel(b byte) bool {
	return b == 'a' || b == 'e' || b == 'o' || b == 'i' || b == 'u' ||
		b == 'A' || b == 'E' || b == 'O' || b == 'I' || b == 'U'
}

