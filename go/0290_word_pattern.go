package main

import "strings"

func wordPattern(pattern string, str string) bool {
	strs := strings.Split(str, " ")
	if len(strs) == 0 {
		return false
	}
	if len(strs) != len(pattern) {
		return false
	}

	appearance := make(map[string]bool)
	mapping := make(map[byte]string)

	for i := 0; i < len(pattern); i++ {
		ch, str := pattern[i], strs[i]

		mapped, ok := mapping[ch]
		if ok {
			if mapped == str {
				continue
			}
			return false
		}

		appeared, ok := appearance[str]
		if ok && appeared {
			return false
		}

		mapping[ch] = str
		appearance[str] = true
	}
	return true
}
