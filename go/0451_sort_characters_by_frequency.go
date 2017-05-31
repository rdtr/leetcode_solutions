import "bytes"

func frequencySort(s string) string {
	m := make(map[byte]int)
	maxCount := 0
	for i := 0; i < len(s); i++ {
		if c, ok := m[s[i]]; !ok {
			m[s[i]] = 1
		} else {
			m[s[i]] = c + 1
		}

		if m[s[i]] > maxCount {
			maxCount = m[s[i]]
		}
	}

	buckets := make([][]byte, maxCount)
	for k, v := range m {
		if len(buckets[v-1]) == 0 {
			buckets[v-1] = []byte{k}
		} else {
			buckets[v-1] = append(buckets[v-1], k)
		}
	}

	var b bytes.Buffer
	for i := maxCount - 1; i >= 0; i-- {
		for _, ch := range buckets[i] {
			for j := 0; j < i+1; j++ {
				b.WriteByte(ch)
			}
		}
	}
	return b.String()
}