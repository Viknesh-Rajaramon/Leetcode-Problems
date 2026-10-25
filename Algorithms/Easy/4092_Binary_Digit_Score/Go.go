package main

func calculateScore(a int, b int) int {
	bits := func(x int) int {
		res := 0
		for x > 0 {
			res += x % 2
			x >>= 1
		}

		return res
	}

	s1, s2 := bits(a), bits(b)
	if s1 >= s2 {
		return s1 * s2
	}

	return s2 / s1
}
