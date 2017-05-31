func minWindow(s string, t string) string {
	requirements := make(map[byte]int)
	for i := range t {
		ch := t[i]
		if cnt, ok := requirements[ch]; !ok {
			requirements[ch] = 1
		} else {
			requirements[ch] = cnt + 1
		}
	}

	apperances := make(map[byte]int)
	counter := len(t)
	minLen := len(s) + 1
	resLeft, resRight := 0, 0
	for left, right := 0, 0; right < len(s); {
		rch, lch := s[right], s[left]

		if _, ok := requirements[rch]; ok {
			if cnt, ok := apperances[rch]; !ok {
				apperances[rch] = 1
			} else {
				apperances[rch] = cnt + 1
			}

			if apperances[rch] <= requirements[rch] && counter != 0 {
				counter--
			}
		}

		if counter == 0 {
			for {
				_, ok := requirements[lch]

				if !ok || apperances[lch] > requirements[lch] {
					if apperances[lch] > requirements[lch] {
						apperances[lch]--
					}

					left++
					lch = s[left]
				} else {
					break
				}
			}

			if right-left+1 < minLen {
				resLeft, resRight = left, right+1
				minLen = right - left + 1
			}
		}
		right++
	}

	if resLeft == 0 && resRight == 0 {
		return ""
	}
	return s[resLeft:resRight]
}