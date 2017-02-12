package main

func strStr(haystack string, needle string) int {
	hlen, nlen := len(haystack), len(needle)
	if nlen == 0 {
		return 0
	}

OUTER:
	for i := 0; i < hlen; i++ {
		if haystack[i] == needle[0] && i+nlen-1 < hlen {
			for j := 0; j < nlen; j++ {
				if haystack[i+j] != needle[j] {
					continue OUTER
				}
			}
			return i
		}
	}
	return -1
}
