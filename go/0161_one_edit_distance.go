func isOneEditDistance(s string, t string) bool {
	slen, tlen := len(s), len(t)
	if slen == tlen {
		return checkSameLen(s, t)
	}

	if slen < tlen { // make sure s is the longer one
		s, t = t, s
		slen, tlen = tlen, slen
	}
	if slen-tlen > 1 {
		return false
	}
	return check(s, t)
}

// check for strings with same length
func checkSameLen(s, t string) bool {
	diff := 0
	for i := 0; i < len(s); i++ {
		if s[i] != t[i] {
			if diff > 0 {
				return false
			}
			diff++
		}
	}
	return diff == 1
}

// check for string s, t where len(s) = len(t) + 1
func check(s, t string) bool {
	sp, tp := 0, 0
	diff := 0
	for sp < len(s) && tp < len(t) {
		if s[sp] == t[tp] {
			sp++
			tp++
			continue
		}
		if diff > 0 {
			return false
		}
		diff++
		sp++
	}
	return true
}