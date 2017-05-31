func reverseStr(s string, k int) string {
	sb := []byte(s)
	slen := len(sb)

	shouldReverse := true
	for i := 0; i < slen; i = i + k {
		if shouldReverse {
			end := i + k - 1
			if end >= slen-1 {
				end = slen - 1
			}
			reverseSb(sb, i, end)
		}
		shouldReverse = !shouldReverse
	}
	return string(sb)
}

func reverseSb(sb []byte, start, end int) {
	for start < end {
		sb[start], sb[end] = sb[end], sb[start]
		start++
		end--
	}
}