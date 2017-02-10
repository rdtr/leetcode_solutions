package main

func isValid(s string) bool {
	stack := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		switch c {
		case '(', '{', '[':
			stack = append(stack, c)
		default:
			if len(stack) == 0 {
				return false
			}
			switch last := stack[len(stack)-1]; {
			case c == ')' && last == '(',
				c == ']' && last == '[',
				c == '}' && last == '{':
				stack = stack[:len(stack)-1]
				break
			default:
				return false
			}
		}
	}
	return len(stack) == 0
}
