package main

func repeatedStringMatch(a string, b string, x int, y int) bool {
	m, n := len(a), len(b)
	ta, tb := m*x, n*y
	if tb > ta {
		return false
	}

	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	temp := min(tb, (m*n)/gcd(m, n))
	for i := range m {
		if i+tb > ta {
			break
		}

		ok := true
		for j := range temp {
			if b[j%n] != a[(i+j)%m] {
				ok = false
				break
			}
		}

		if ok {
			return true
		}
	}

	return false
}
