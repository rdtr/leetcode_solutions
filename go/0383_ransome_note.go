package main

func canConstruct(ransomNote string, magazine string) bool {
	byteIndex := make([]int, 26)
	for _, letter := range magazine {
		byteIndex[int(letter-'a')]++
	}
	for _, ch := range ransomNote {
		byteIndex[int(ch-'a')]--
	}

	for i := range byteIndex {
		if byteIndex[i] < 0 {
			return false
		}
	}
	return true
}
