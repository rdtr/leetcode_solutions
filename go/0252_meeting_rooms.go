import "sort"

func canAttendMeetings(intervals []Interval) bool {
	ivs := MyIntervals(intervals)
	sort.Sort(ivs)
	for i := 0; i < len(ivs)-1; i++ {
		if ivs[i].End > ivs[i+1].Start {
			return false
		}
	}
	return true
}

// followings are just a boilerplate to suffice sort interface for []Interval
type MyIntervals []Interval

func (ivs MyIntervals) Len() int {
	return len(ivs)
}

func (ivs MyIntervals) Swap(i, j int) {
	ivs[i], ivs[j] = ivs[j], ivs[i]
}

func (ivs MyIntervals) Less(i, j int) bool {
	return ivs[i].Start < ivs[j].Start
}