package main

import "bytes"

func longestCommonPrefix(strs []string) string {
	strslen := len(strs)
	if strslen == 0 {
		return ""
	}

	var b bytes.Buffer
	var ch string
	for i := 0; ; i++ {
		ch = ""
		for j := 0; j < strslen; j++ {
			if i >= len(strs[j]) {
				return b.String()
			}
			if ch == "" {
				ch = string(strs[j][i])
			} else if string(strs[j][i]) != ch {
				return b.String()
			}
		}
		b.WriteString(ch)
	}
}
