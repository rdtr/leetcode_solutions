package main

func backspaceCompare(S string, T string) bool {
	slen, tlen := len(S), len(T)
	if slen == 0 && tlen == 0 {
		return true
	}
	scur, tcur := slen-1, tlen-1
	sbs, tbs := 0, 0

	for {
		// for each strings, check '#' and skips characters
		for scur >= 0 && (S[scur] == '#' || sbs > 0) {
			if S[scur] == '#' {
				sbs++
			} else {
				sbs--
			}
			scur--
		}
		for tcur >= 0 && (T[tcur] == '#' || tbs > 0) {
			if T[tcur] == '#' {
				tbs++
			} else {
				tbs--
			}
			tcur--
		}

		if (scur == 0 && tcur == 0) || (scur < 0 && tcur < 0) {
			return true
		} else if (scur >= 0 && tcur < 0) || (scur < 0 && tcur >= 0) || S[scur] != T[tcur] {
			return false
		}
		scur--
		tcur--
	}
}
