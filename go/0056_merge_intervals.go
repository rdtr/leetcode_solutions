import "sort"

func merge(intervals []Interval) []Interval {
	sort.Sort(ByStart(intervals))
	interLen := len(intervals)

	for i := 0; i < interLen-1; {
		cur, next := intervals[i], intervals[i+1]
		if next.Start <= cur.End {
			if next.End > cur.End {
				intervals[i].End = intervals[i+1].End
			}
			intervals = append(intervals[:i+1], intervals[i+2:]...)
			interLen--
			continue
		}
		i++
	}
	return intervals
}

type ByStart []Interval

func (bs ByStart) Len() int {
	return len(bs)
}
func (bs ByStart) Swap(i, j int) {
	bs[i], bs[j] = bs[j], bs[i]
}
func (bs ByStart) Less(i, j int) bool {
	return bs[i].Start < bs[j].Start
}