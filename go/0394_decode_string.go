import (
	"bytes"
	"strconv"
)

func decodeString(s string) string {
	res, _ := doDecodeString(s)
	return res
}

func doDecodeString(s string) (string, int) {
	slen := len(s)
	if slen == 0 {
		return "", 0
	}

	var res bytes.Buffer
	for i := 0; i < slen; {
		if !isNumber(s[i]) {
			res.WriteByte(s[i])
			i++
			continue
		}

		var newRes string
		newRes, i = extract(s, i)
		res.WriteString(newRes)
	}
	return res.String(), 0
}

func extract(s string, i int) (string, int) {
	var b bytes.Buffer

	// extract number
	var numBuf bytes.Buffer
	for s[i] != '[' {
		numBuf.WriteByte(s[i])
		i++
	}
	i++ // skip '['

	num, _ := strconv.ParseInt(numBuf.String(), 10, 32)
	// extract string
	for s[i] != ']' {
		if isNumber(s[i]) {
			newRes, newI := extract(s, i)
			b.WriteString(newRes)
			i = newI
			continue
		}
		b.WriteByte(s[i])
		i++
	}

	var res bytes.Buffer
	for j := 0; j < int(num); j++ {
		res.WriteString(b.String())
	}
	return res.String(), i + 1 // skip ']'
}

func isNumber(ch byte) bool {
	return ch >= '0' && ch <= '9'
}