func Constructor(capacity int) LRUCache {
	m := make(map[int]*CacheNode)
	c := LRUCache{
		Cap: capacity,
		Map: m,
	}
	return c
}

func (this *LRUCache) Get(key int) int {
	found, ok := this.Map[key]
	if !ok {
		return -1
	}
	if this.Head == found {
		return found.Val
	}
	if this.Tail == found {
		this.Tail = found.Prev
	}
	// move found to head
	if found.Next != nil {
		found.Next.Prev = found.Prev
	}
	if found.Prev != nil {
		found.Prev.Next = found.Next
	}
	this.Head.Prev, found.Nex = found, this.Head
	this.Head = found
	return found.Val
}

func (this *LRUCache) Put(key int, value int) {
	found, ok := this.Map[key]
	if ok {
		found.Val = value
		_ = this.Get(found.Key) // to move found node to head
		return
	}

	// add to head
	n := &CacheNode{Key: key, Val: value}

	if len(this.Map) == 0 {
		this.Tail = n
	} else {
		this.Head.Prev, n.Next = n, this.Head
	}
	this.Map[key], this.Head = n, n
	if this.Cap == this.Len {
		delete(this.Map, this.Tail.Key)
		this.Len, this.Tail = this.Len+1, this.Tail.Prev
	}
	this.Len++
}

type CacheNode struct {
	Next *CacheNode
	Prev *CacheNode
	Key  int
	Val  int
}

type LRUCache struct {
	Cap  int
	Len  int
	Head *CacheNode
	Tail *CacheNode
	Map  map[int]*CacheNode
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */