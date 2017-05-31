import "strconv"

func evalRPN(tokens []string) int {
	var queue []int
	for _, token := range tokens {
		switch token {
		default:
			i, _ := strconv.Atoi(token)
			queue = append(queue, i)
			continue
		case "+":
			queue[len(queue)-2] = queue[len(queue)-2] + queue[len(queue)-1]
		case "-":
			queue[len(queue)-2] = queue[len(queue)-2] - queue[len(queue)-1]
		case "*":
			queue[len(queue)-2] = queue[len(queue)-2] * queue[len(queue)-1]
		case "/":
			queue[len(queue)-2] = queue[len(queue)-2] / queue[len(queue)-1]
		}
		queue = queue[:len(queue)-1] // delete the last element after the calc
	}
	return queue[0]
}