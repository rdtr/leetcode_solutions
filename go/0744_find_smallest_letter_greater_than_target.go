func nextGreatestLetter(letters []byte, target byte) byte {
	if target >= letters[len(letters)-1] {
		return letters[0]
	}

	l, h := 0, len(letters)
	for l < h {
		m := l + (h-l)/2 - 1
		if letters[m] > target {
			h = m
		} else {
			l = m + 1
		}
	}
	return letters[h]
}