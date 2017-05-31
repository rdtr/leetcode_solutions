package main

func reverseString(s string) string {
	slen := len(s)
	if slen <= 1 {
		return s
	}

	bytes := []byte(s)
	for i := 0; i <= (slen/2)-1; i++ {
		bytes[i], bytes[slen-i-1] = bytes[slen-i-1], bytes[i]
	}
	return string(bytes)
}
