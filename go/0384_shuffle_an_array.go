import "math/rand"

type Solution struct {
	Nums []int
}

func Constructor(nums []int) Solution {
	return Solution{Nums: nums}
}

/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
	return this.Nums
}

/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
	// rand.Seed(time.Now().UnixNano())
	shuffled := make([]int, len(this.Nums))
	copy(shuffled, this.Nums)

	for i := len(this.Nums) - 1; i > 0; i-- {
		r := rand.Intn(i + 1)
		shuffled[i], shuffled[r] = shuffled[r], shuffled[i]
	}
	return shuffled
}
