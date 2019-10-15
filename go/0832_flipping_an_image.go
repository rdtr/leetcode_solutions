package main

func flipAndInvertImage(A [][]int) [][]int {
	mlen := len(A)
	if mlen == 0 {
		return [][]int{}
	}
	nlen := len(A[0])

	for i := 0; i < mlen; i++ {
		left, right := 0, nlen-1
		for left <= right {
			A[i][left], A[i][right] = (A[i][right]+1)%2, (A[i][left]+1)%2
			left, right = left+1, right-1
		}
	}
	return A
}
