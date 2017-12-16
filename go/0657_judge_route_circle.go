func judgeCircle(moves string) bool {
	if len(moves) == 0 {
		return false
	}

	x, y := 0, 0
	for i := 0; i < len(moves); i++ {
		m := moves[i]
		switch m {
		case 'R':
			x += 1
		case 'L':
			x -= 1
		case 'U':
			y += 1
		case 'D':
			y -= 1
		}
	}
	return x == 0 && y == 0
}