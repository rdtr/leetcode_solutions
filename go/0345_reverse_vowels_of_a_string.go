func reverseVowels(s string) string {
	bs := []byte(s)
	left, right := 0, len(s)-1

OUTER:
	for left < right {
		for !isVowel(bs[left]) {
			left++
			if left >= right {
				break OUTER
			}
		}

		for !isVowel(bs[right]) {
			right--
			if left >= right {
				break OUTER
			}
		}

		bs[left], bs[right] = bs[right], bs[left]
		left++
		right--
	}
	return string(bs)
}

func isVowel(b byte) bool {
	return b == 'a' || b == 'e' || b == 'i' || b == 'o' || b == 'u' || b == 'A' || b == 'E' || b == 'I' || b == 'O' || b == 'U'
}