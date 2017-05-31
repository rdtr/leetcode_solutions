func titleToNumber(s string) int {
	res, base := 0, 1
	for i := len(s) - 1; i >= 0; i-- {
		res += base * (int(s[i]-'A') + 1)
		base *= 26
	}
	return res
}