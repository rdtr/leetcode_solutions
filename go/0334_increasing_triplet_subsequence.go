import "math"

func increasingTriplet(nums []int) bool {
	nlen := len(nums)
	if nlen < 3 {
		return false
	}

	smallest, secondSmallest := nums[0], math.MaxInt32
	for i := 1; i < nlen; i++ {
		switch num := nums[i]; {
		case num < smallest:
			smallest = num
		case num > smallest && num < secondSmallest:
			secondSmallest = num
		case num > secondSmallest:
			return true
		}
	}
	return false
}