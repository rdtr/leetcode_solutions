func checkRecord(s string) bool {
	acnt, lcnt := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'A' {
			acnt++
			if acnt > 1 {
				return false
			}
		} else if s[i] == 'L' {
			lcnt++
			if lcnt > 2 {
				return false
			}
			continue
		}
		lcnt = 0
	}
	return true
}