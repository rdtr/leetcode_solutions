package main

func addBinary(a string, b string) string {
	alen, blen := len(a), len(b)
	if alen == 0 && blen == 0 {
		return "0"
	} else if alen == 0 {
		return b
	} else if blen == 0 {
		return a
	}

	// ensure a is the longer one
	if alen < blen {
		a, b = b, a
		alen, blen = blen, alen
	}

	var res []byte
	var co byte = '0'
	var sum byte
	for i, j := alen-1, blen-1; i >= 0; i, j = i-1, j-1 {
		var ach, bch byte
		if j >= 0 {
			bch = b[j]
		} else {
			bch = '0'
		}
		ach = a[i]

		sum, co = calc(ach, bch, co)
		res = append([]byte{sum}, res...)
	}
	// handle the last carry over
	if co == '1' {
		res = append([]byte{'1'}, res...)
	}
	return string(res)
}

func calc(ach, bch, co byte) (res byte, newco byte) {
	switch {
	case ach == '0' && bch == '0':
		res = co
		newco = '0'
	case ach == '0' && bch == '1',
		ach == '1' && bch == '0':
		if co == '0' {
			res = '1'
			newco = '0'
		} else {
			res = '0'
			newco = '1'
		}
	case ach == '1' && bch == '1':
		if co == '0' {
			res = '0'
		} else {
			res = '1'
		}
		newco = '1'
	}
	return res, newco
}
