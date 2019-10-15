func mirrorReflection(p int, q int) int {
	x, y := 0, 0
	direction := 1
	for {
		if direction == 1 {
			y += q
			if y > p {
				direction = -1
				y = 2*p - y
			}
		} else {
			y -= q
			if y < 0 {
				direction = 1
				y = -y
			}
		}

		if x == p {
			x = 0
		} else {
			x = p
		}

		if x == p && y == 0 {
			return 0
		} else if x == p && y == p {
			return 1
		} else if x == 0 && y == p {
			return 2
		}
	}
}