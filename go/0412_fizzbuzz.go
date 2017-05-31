package main

import "strconv"

func fizzBuzz(n int) []string {
	res, val := make([]string, n), ""
	for i := 1; i <= n; i++ {
		switch {
		case i%15 == 0:
			val = "FizzBuzz"
		case i%3 == 0:
			val = "Fizz"
		case i%5 == 0:
			val = "Buzz"
		default:
			val = strconv.Itoa(i)
		}
		res[i-1] = val
	}
	return res
}
