package main

func lengthOfLastWord(s string) int {
	slen := len(s)
	if slen == 0 {
		return 0
	}

	var cnt int
	lastwordExist := false
	for i := slen - 1; i >= 0; i-- {
		c := s[i]
		if !lastwordExist && c != ' ' {
			lastwordExist = true
			cnt = 1
			continue
		}

		if lastwordExist && c != ' ' {
			cnt++
			continue
		}

		if lastwordExist && c == ' ' {
			break
		}
	}
	return cnt
}
