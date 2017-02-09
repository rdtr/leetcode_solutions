package main

func letterCombinations(digits string) []string {
	m := map[byte][]string{
		'0': []string{"0"},
		'1': []string{"1"},
		'2': []string{"a", "b", "c"},
		'3': []string{"d", "e", "f"},
		'4': []string{"g", "h", "i"},
		'5': []string{"j", "k", "l"},
		'6': []string{"m", "n", "o"},
		'7': []string{"p", "q", "r", "s"},
		'8': []string{"t", "u", "v"},
		'9': []string{"w", "x", "y", "z"},
	}

	var res []string
	if digits == "" {
		return res
	}
	backtrack("", &res, 0, digits, m)
	return res
}

func backtrack(curStr string, res *[]string, index int, digits string, digitsMap map[byte][]string) {
	if index == len(digits) {
		*res = append(*res, curStr)
		return
	}
	for _, ch := range digitsMap[digits[index]] {
		backtrack(curStr+ch, res, index+1, digits, digitsMap)
	}
}
