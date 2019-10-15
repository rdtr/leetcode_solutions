func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	var requirements [26]int
	for _, ch := range s1 {
		requirements[int(ch)-int('a')]++
	}
	var appearance [26]int
	for i := 0; i < len(s1); i++ {
		appearance[int(s2[i])-int('a')]++
	}

	count := compare(requirements, appearance)
	if count == 26 {
		return true
	}

	l, r := 0, len(s1)-1
	for {
		wasMatch := requirements[int(s2[l])-int('a')] == appearance[int(s2[l])-int('a')]
		appearance[int(s2[l])-int('a')]--
		nowMatch := requirements[int(s2[l])-int('a')] == appearance[int(s2[l])-int('a')]

		if wasMatch && !nowMatch {
			count--
		} else if !wasMatch && nowMatch {
			count++
		}

		if l += 1; l == len(s2) {
			break
		}
		if r += 1; r == len(s2) {
			break
		}

		wasMatch = requirements[int(s2[r])-int('a')] == appearance[int(s2[r])-int('a')]
		appearance[int(s2[r])-int('a')]++
		nowMatch = requirements[int(s2[r])-int('a')] == appearance[int(s2[r])-int('a')]

		if wasMatch && !nowMatch {
			count--
		} else if !wasMatch && nowMatch {
			count++
		}

		if count == 26 {
			return true
		}
	}
	return false
}

func compare(a1, a2 [26]int) int {
	var res int
	for i := 0; i < 26; i++ {
		if a1[i] == a2[i] {
			res++
		}
	}
	return res
}