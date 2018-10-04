func decodeString(s string) string {
	stack := []*Item{&Item{}}
	counting := false
	var numStart int
    
	for i, ch := range s {
		switch {
		case ch >= '0' && ch <= '9':
			if !counting {
				var newBuf bytes.Buffer
				item := &Item{Val: newBuf}
				stack = append(stack, item)
				numStart = i
				counting = true
			}
		case ch == '[':
            counting = false
			numStr := s[numStart:i]
			numInt64, _ := strconv.ParseInt(numStr, 10, 32)
			stack[len(stack)-1].Num = int(numInt64)
		case ch == ']':
			tmpNum, tmpVal := stack[len(stack)-1].Num, stack[len(stack)-1].Val.Bytes()
			stack = stack[:len(stack)-1]
			for j := 0; j < tmpNum; j++ {
				stack[len(stack)-1].Val.Write(tmpVal)
			}
		default:
			stack[len(stack)-1].Val.WriteRune(ch)
		}
	}
	return stack[0].Val.String()
}

type Item struct {
	Num int
	Val bytes.Buffer
}