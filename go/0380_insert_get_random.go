import "math/rand"

type RandomizedSet struct {
	Index map[int]int
	Data  *[]int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	m := make(map[int]int)
	s := make([]int, 0)
	return RandomizedSet{Index: m, Data: &s}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.Index[val]; ok {
		return false
	}
	*this.Data = append(*this.Data, val)
	this.Index[val] = len(*this.Data) - 1
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	data := *this.Data
	if i, ok := this.Index[val]; !ok {
		return false
	} else {
		if i == len(data)-1 { // last index
			delete(this.Index, val)
			*this.Data = data[:i]
		} else {
			// swap i th element with the last one
			data[i], data[len(data)-1] = data[len(data)-1], data[i]
			delete(this.Index, val)
			this.Index[data[i]] = i
			*this.Data = data[:len(*this.Data)-1]
		}
		return true
	}
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	return (*this.Data)[rand.Intn(len(*this.Data))]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */