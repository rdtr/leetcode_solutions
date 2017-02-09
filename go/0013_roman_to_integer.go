package main

import "bytes"

func romanToInt(s string) int {
	b := []byte(s)
	i := [][]byte{[]byte("IX"), []byte("VIII"), []byte("VII"), []byte("VI"), []byte("V"), []byte("IV"), []byte("III"), []byte("II"), []byte("I")}
	x := [][]byte{[]byte("XC"), []byte("LXXX"), []byte("LXX"), []byte("LX"), []byte("L"), []byte("XL"), []byte("XXX"), []byte("XX"), []byte("X")}
	c := [][]byte{[]byte("CM"), []byte("DCCC"), []byte("DCC"), []byte("DC"), []byte("D"), []byte("CD"), []byte("CCC"), []byte("CC"), []byte("C")}
	m := [][]byte{[]byte("MMM"), []byte("MM"), []byte("M")}

	var res int
	digitLists := [][][]byte{m, c, x, i}
	base := 1000
	for _, digitList := range digitLists {
		for j, val := range digitList {
			if idx := bytes.Index(b, val); idx == 0 {
				res += base * (len(digitList) - j)
				b = b[len(val):]
				break
			}
		}
		base /= 10
	}
	return res
}
