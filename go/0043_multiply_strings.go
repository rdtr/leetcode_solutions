package main

import "bytes"

func multiply(num1 string, num2 string) string {
	num1, num2 = "0"+num1, "0"+num2 // sentinel to avoid special handling for the last carry over
	res := make([]byte, len(num1)+len(num2))
	for i, _ := range res { // initialize with byte character '0'
		res[i] = '0'
	}

	for i := 0; i < len(num2); i++ {
		pos2 := len(num2) - 1 - i
		ch2 := num2[pos2]
		co := 0
		for j := 0; j < len(num1); j++ {
			pos1 := len(num1) - 1 - j
			ch1 := num1[pos1]
			resPos := len(res) - 1 - (i + j)

			mul := int(ch1-'0')*int(ch2-'0') + int(res[resPos]-'0') + co
			res[resPos] = byte(mul%10 + '0')
			co = mul / 10
		}
	}

	var b bytes.Buffer
	firstZero := true
	for i := 0; i < len(res); i++ {
		c := res[i]
		if firstZero && c == '0' {
			continue
		}
		firstZero = false
		b.WriteByte(c)
	}

	resStr := b.String()
	if resStr == "" {
		return "0"
	}
	return resStr
}
