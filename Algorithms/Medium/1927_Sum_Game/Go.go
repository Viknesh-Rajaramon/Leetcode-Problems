package main

func sumGame(num string) bool {
	n := len(num)
	get := func(s string) (int, int) {
		nn, qq := 0, 0
		for _, c := range s {
			if c == '?' {
				qq++
			} else {
				nn += int(c - '0')
			}
		}

		return nn, qq
	}

	n0, q0 := get(num[:n/2])
	n1, q1 := get(num[n/2:])
	return (q0+q1)%2 == 1 || (n0-n1)*2 != (q1-q0)*9
}
