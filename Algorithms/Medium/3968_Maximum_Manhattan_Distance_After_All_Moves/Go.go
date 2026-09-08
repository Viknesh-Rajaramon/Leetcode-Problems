package main

func maxDistance(moves string) int {
	x, y, extra := 0, 0, 0
	for _, c := range moves {
		if c == 'R' {
			x++
		} else if c == 'L' {
			x--
		} else if c == 'U' {
			y++
		} else if c == 'D' {
			y--
		} else {
			extra++
		}
	}

	return max(x, -x) + max(y, -y) + extra
}
