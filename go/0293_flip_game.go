package main

func generatePossibleNextMoves(s string) []string {
	slen := len(s)
	res := []string{}

	if slen < 2 {
		return res
	}
	for i := 1; i < slen; i++ {
		if s[i] == '+' && s[i] == s[i-1] {
			res = append(res, s[:i-1]+"--"+s[i+1:])
		}
	}
	return res
}
