import "container/heap"

func topKFrequent(nums []int, k int) []int {
	mp := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if cnt, ok := mp[nums[i]]; !ok {
			mp[nums[i]] = 1
		} else {
			mp[nums[i]] = cnt + 1
		}
	}

	myNums := make(MyNums, len(mp))
	i := 0
	for num, count := range mp {
		myNums[i] = MyNum{Val: num, Count: count}
		i++
	}

	heap.Init(&myNums)
	var res []int
	for i := 0; i < k; i++ {
		num := heap.Pop(&myNums).(MyNum)
		res = append(res, num.Val)
	}
	return res
}

// MyNum stores its value and frequency as Count.
type MyNum struct {
	Val   int
	Count int
}

type MyNums []MyNum

func (n MyNums) Len() int {
	return len(n)
}

func (n MyNums) Swap(i, j int) {
	n[i], n[j] = n[j], n[i]
}

func (n MyNums) Less(i, j int) bool {
	return n[i].Count >= n[j].Count
}

func (n *MyNums) Push(num interface{}) {
	myNum := num.(MyNum)
	*n = append(*n, myNum)
}

func (n *MyNums) Pop() interface{} {
	tmp := *n
	l := len(tmp)
	var res interface{} = tmp[l-1]
	*n = tmp[:l-1]
	return res
}
