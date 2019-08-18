import "fmt"

func getHint(secret string, guess string) string {
	b, c := 0, 0

	ms, mg := make(map[byte]int), make(map[byte]int)
	for i := 0; i < len(secret); i++ {
		if cnt, ok := ms[secret[i]]; ok {
			ms[secret[i]] = cnt + 1
		} else {
			ms[secret[i]] = 1
		}

		if cnt, ok := mg[guess[i]]; ok {
			mg[guess[i]] = cnt + 1
		} else {
			mg[guess[i]] = 1
		}
	}

	for k, v := range ms {
		if cnt, ok := mg[k]; ok {
			c += min(cnt, v)
		}
	}

	for i := 0; i < len(secret); i++ {
		if secret[i] == guess[i] {
			b += 1
			c -= 1
		}
	}
	return fmt.Sprintf("%dA%dB", b, c)
}

func min(a, b int) int {
	if a >= b {
		return b
	}
	return a
}