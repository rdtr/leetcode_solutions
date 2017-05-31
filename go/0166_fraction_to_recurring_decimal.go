import "strconv"

func fractionToDecimal(numerator int, denominator int) string {
	flag := ""
	switch {
	case numerator < 0 && denominator < 0:
		numerator, denominator = -numerator, -denominator
	case numerator > 0 && denominator < 0:
		denominator, flag = -denominator, "-"
	case numerator < 0 && denominator > 0:
		numerator, flag = -numerator, "-"
	}

	qua, rem := numerator/denominator, numerator%denominator
	res := []byte(strconv.FormatInt(int64(qua), 10))
	if rem == 0 {
		return flag + string(res)
	}

	res = append(res, '.')
	m, curIndex := make(map[int]int), len(res)-1
	for rem != 0 {
		numerator = rem * 10
		qua, rem = numerator/denominator, numerator%denominator

		if index, ok := m[numerator]; ok {
			res = append(res, ')', ' ')
			copy(res[index+1:], res[index:])
			res[index] = '('
			break
		}

		res = append(res, digitToByte(qua))
		curIndex++
		m[numerator] = curIndex
	}
	return flag + string(res)
}

func digitToByte(digit int) byte {
	return byte('0' + digit)
}