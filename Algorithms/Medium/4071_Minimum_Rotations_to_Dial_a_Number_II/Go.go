package main

func minRotations(n int, s string) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	dist := func(a, b int) int {
		d := abs(a - b)
		return min(d, 10-d)
	}

	base := dist(0, int(s[0]-'0'))
	for i := range n - 1 {
		base += dist(int(s[i]-'0'), int(s[i+1]-'0'))
	}

	result := min(base, base-dist(0, int(s[0]-'0'))+dist(0, int(s[n-1]-'0')))
	for k := range n - 1 {
		result = min(result, base-dist(int(s[k]-'0'), int(s[k+1]-'0'))+dist(int(s[k]-'0'), int(s[n-1]-'0')))
	}

	return result
}
