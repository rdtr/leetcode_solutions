func maxProduct(words []string) int {
	wlen := len(words)
	wtables := make([]int32, wlen)

	for i := 0; i < wlen; i++ {
		wtables[i] = helper(words[i])
	}

	max := 0
	for i := 0; i < wlen; i++ {
		for j := i + 1; j < wlen; j++ {
			if wtables[i]&wtables[j] == 0 {
				if prod := len(words[i]) * len(words[j]); prod > max {
					max = prod
				}
			}
		}
	}
	return max
}

func helper(word string) int32 {
	var res int32
	for i := 0; i < len(word); i++ {
		res |= 1 << uint(26-(int(word[i])-int('a')))
	}
	return res
}