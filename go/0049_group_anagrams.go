package main

import "bytes"

func groupAnagrams(strs []string) [][]string {
	alphaBits := make([]string, len(strs))
	for i, str := range strs {
		alphaBits[i] = getAlphabetBit(str)
	}

	var res [][]string
	newIndex := 0
	mp := make(map[string]int)
	for bitIndex, alphaBit := range alphaBits {
		if mapIndex, ok := mp[alphaBit]; !ok {
			mp[alphaBit] = newIndex
			res = append(res, []string{strs[bitIndex]})
			newIndex++
			continue
		} else {
			res[mapIndex] = append(res[mapIndex], strs[bitIndex])
		}
	}
	return res
}

func getAlphabetBit(str string) string {
	res := make([]int, 26)
	for _, ch := range str {
		chInt := int(ch - 'a')
		res[chInt] += 1
	}

	var b bytes.Buffer
	for _, bit := range res {
		b.WriteByte(byte(int('0') + bit))
	}
	return b.String()
}
