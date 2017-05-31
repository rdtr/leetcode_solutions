package main

func isPalindrome(s string) bool {
	if s == "" {
		return true
	}
	for left, right := 0, len(s)-1; ; {
		if left == right {
			break
		}

		if !isAlphanumeric(s[left]) {
			left++
			continue
		}
		if !isAlphanumeric(s[right]) {
			right--
			continue
		}
		lch, rch := toLower(s[left]), toLower(s[right])

		if left+1 == right {
			if lch == rch {
				break
			}
			return false
		}
		if lch != rch {
			return false
		}
		left, right = left+1, right-1
	}
	return true
}

func isAlphanumeric(b byte) bool {
	return (b >= 'a' && b <= 'z') ||
		(b >= 'A' && b <= 'Z') ||
		(b >= '0' && b <= '9')
}

func toLower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + ('a' - 'A')
	}
	return b
}
