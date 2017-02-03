package main

import "bytes"

func convert(s string, numRows int) string {
	var b bytes.Buffer
	slen := len(s)
	if numRows == 1 {
		return s
	}

	for row := 0; row < numRows; row++ {
		var step int

		i := row // first index
		if i >= slen {
			break
		}
		b.WriteByte(s[i])

		for {
			var distance int
			if step%2 == 0 {
				distance = 2 * (numRows - row - 1)
			} else {
				distance = 2 * row
			}

			step++
			if distance == 0 {
				continue
			}
			i += distance
			if i >= slen {
				break
			}
			b.WriteByte(s[i])
		}
	}
	return b.String()
}
