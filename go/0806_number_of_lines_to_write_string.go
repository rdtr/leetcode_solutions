func numberOfLines(widths []int, S string) []int {
	curCount, lines := 0, 0
	for _, ch := range S {
		width := widths[int(ch)-int('a')]
		if curCount+width > 100 {
			lines++
			curCount = width
			continue
		}
		curCount += width
	}
	return []int{lines + 1, curCount}
}