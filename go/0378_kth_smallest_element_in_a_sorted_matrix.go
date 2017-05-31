import "container/heap"

func kthSmallest(matrix [][]int, k int) int {
	mlen, nlen := len(matrix), len(matrix[0])
	var pq Elems
	for i := 0; i < mlen; i++ {
		pq = append(pq, Elem{m: i, n: 0, val: matrix[i][0]})
	}

	heap.Init(&pq)
	var res int
	for i := 0; i < k; i++ {
		e, _ := heap.Pop(&pq).(Elem)
		if e.n < nlen-1 {
			heap.Push(&pq, Elem{m: e.m, n: e.n + 1, val: matrix[e.m][e.n+1]})
		}
		res = e.val
	}
	return res
}

type Elem struct {
	m   int
	n   int
	val int
}

type Elems []Elem

func (pq Elems) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq Elems) Len() int {
	return len(pq)
}

func (pq Elems) Less(i, j int) bool {
	return pq[i].val < pq[j].val
}

func (pq *Elems) Pop() interface{} {
	vpq := *pq
	x := vpq[len(vpq)-1]
	*pq = vpq[:len(vpq)-1]
	return x
}

func (pq *Elems) Push(num interface{}) {
	numElm, _ := num.(Elem)
	*pq = append(*pq, numElm)
}