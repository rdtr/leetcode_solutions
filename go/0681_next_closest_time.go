import "math"

func nextClosestTime(time string) string {
	digits := [4]byte{
		time[0],
		time[1],
		time[3],
		time[4],
	}

	// It looks if 4 digits are all the same, we need to return itself
	if digits[0] == digits[1] && digits[0] == digits[2] && digits[0] == digits[3] {
		return time
	}

	mindist := math.MaxInt32
	t, res := "", ""
	for i := 0; i < 4; i++ {
		d1 := string(digits[i])
		for j := 0; j < 4; j++ {
			d2 := string(digits[j])
			for k := 0; k < 4; k++ {
				d3 := string(digits[k])
				for l := 0; l < 4; l++ {
					d4 := string(digits[l])
					t = d1 + d2 + ":" + d3 + d4
					if !isValidTime(t) || t == time {
						continue
					}

					dist := getDistance(time, t)
					if dist < mindist {
						mindist = dist
						res = t
					}
				}
			}
		}
	}
	return res
}

func isValidTime(time string) bool {
	if time[3] > '5' {
		return false
	}
	if time[0] > '2' {
		return false
	} else if time[0] == '2' && time[1] > '3' {
		return false
	}
	return true
}

func getDistance(time1 string, time2 string) int {
	one1 := int(time1[0]) - int('0')
	two1 := int(time1[1]) - int('0')
	three1 := int(time1[3]) - int('0')
	four1 := int(time1[4]) - int('0')

	one2 := int(time2[0]) - int('0')
	two2 := int(time2[1]) - int('0')
	three2 := int(time2[3]) - int('0')
	four2 := int(time2[4]) - int('0')

	hr1 := one1*10 + two1
	min1 := three1*10 + four1
	hr2 := one2*10 + two2
	min2 := three2*10 + four2

	if hr1 < hr2 {
		return (60 - min1) + min2 + 60*(hr2-hr1)
	} else if hr1 == hr2 {
		if min1 <= min2 {
			return min2 - min1
		}
		return 24*60 - (min1 - min2)
	} else {
		diff := (24 - (hr1 - hr2)) * 60
		if min1 <= min2 {
			return diff + min2 - min1
		} else if min1 == min2 {
			return diff
		}
		return diff - (min1 - min2)
	}
}