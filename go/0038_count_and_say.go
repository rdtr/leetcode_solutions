package main

import "bytes"

func countAndSay(n int) string {
	if n == 0 {
		return ""
	}
	s := "1"
	for i := 1; i < n; i++ {
		s = calc(s)
	}
	return s
}

func calc(s string) string {
	count, start := 0, 0
	var ch byte
	var res bytes.Buffer
	for i := 0; i < len(s); i++ {
		start = i
		ch = s[i]
		count = 1
		for j := 1; start+j < len(s) && s[start+j] == ch; j++ {
			i++
			count++
		}
		res.WriteByte(byte(count) + '0')
		res.WriteByte(ch)
	}
	return res.String()
}
