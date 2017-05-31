import "strconv"

func findMissingRanges(nums []int, lower int, upper int) []string {
	nlen := len(nums)
	var res []string

	if nlen == 0 {
		return []string{getMissingRange(lower-1, upper+1)}
	} else if nlen == 1 {
		appendIfNotEmpty(&res, getMissingRange(lower-1, nums[0]))
		appendIfNotEmpty(&res, getMissingRange(nums[0], upper+1))
		return res
	}

	for i := 0; i < nlen; i++ {
		if i == 0 {
			appendIfNotEmpty(&res, getMissingRange(lower-1, nums[i]))
			continue
		}
		appendIfNotEmpty(&res, getMissingRange(nums[i-1], nums[i]))

		if i == nlen-1 {
			appendIfNotEmpty(&res, getMissingRange(nums[i], upper+1))
		}
	}
	return res
}

func getMissingRange(a, b int) string {
	if b-a <= 1 {
		return ""
	} else if b-a == 2 {
		return strconv.Itoa(a + 1)
	} else {
		left, right := strconv.Itoa(a+1), strconv.Itoa(b-1)
		return left + "->" + right
	}
}

func appendIfNotEmpty(list *[]string, s string) {
	if s != "" {
		*list = append(*list, s)
	}
}