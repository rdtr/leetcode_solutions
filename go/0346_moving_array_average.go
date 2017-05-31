type MovingAverage struct {
	Queue  []int
	Count  int
	Size   int
	CurSum int
}

/** Initialize your data structure here. */
func Constructor(size int) MovingAverage {
	ma := MovingAverage{
		Size:   size,
		CurSum: 0,
		Count:  0,
	}
	ma.Queue = make([]int, size)
	return ma
}

func (this *MovingAverage) Next(val int) float64 {
	if this.Count < this.Size {
		this.CurSum = this.CurSum + val
		this.Queue[this.Count] = val
		this.Count += 1
		return float64(this.CurSum) / float64(this.Count)
	}

	i := this.Count % this.Size
	this.CurSum = this.CurSum - this.Queue[i] + val
	this.Queue[i] = val
	this.Count += 1
	return float64(this.CurSum) / float64(this.Size)
}
