import "bytes"

func licenseKeyFormatting(S string, K int) string {
	var b bytes.Buffer
	cnt := 0
	for i := len(S) - 1; i >= 0; i-- {
		ch := S[i]
		if ch == '-' {
			continue
		} else if ch >= 'a' && ch <= 'z' {
			ch = byte(int(ch) + (int('Z') - int('z')))
		}
		b.WriteByte(ch)
		cnt++
		if cnt == K {
			cnt = 0
			b.WriteByte('-')
		}
	}

	res := b.Bytes()
	// we may have added unnecessary '-' to the last, so omit it if any
	if len(res) > 0 && res[len(res)-1] == '-' {
		res = res[:len(res)-1]
	}
	return reverse(res)
}

func reverse(b []byte) string {
	for l, r := 0, len(b)-1; l < r; l, r = l+1, r-1 {
		b[l], b[r] = b[r], b[l]
	}
	return string(b)
}