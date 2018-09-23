func isPowerOfFour(num int) bool {
	return num == 1 || num == 1<<2 || num == 1<<4 || num == 1<<6 || num == 1<<8 || num == 1<<10 ||
		num == 1<<12 || num == 1<<14 || num == 1<<16 || num == 1<<18 || num == 1<<20 || num == 1<<22 ||
		num == 1<<24 || num == 1<<26 || num == 1<<28 || num == 1<<30 || num == 1<<32
}