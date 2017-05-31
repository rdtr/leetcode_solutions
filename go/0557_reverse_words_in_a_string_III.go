import "strings"

func reverseWords(s string) string {
	start := 0
	for {
		if i := strings.Index(s[start:], " "); i == -1 {
			break
		} else {
			s = reverse(s, start, start+i-1)
			start = start + i + 1
		}
	}

	if start < len(s) {
		s = reverse(s, start, len(s)-1)
	}
	return s
}

func reverse(s string, start, end int) string {
	sb := []byte(s)
	for start < end {
		sb[start], sb[end] = sb[end], sb[start]
		start, end = start+1, end-1
	}
	return string(sb)
}