package main

func minBishopMoves(source []int, target []int) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	if (source[0]+source[1])%2 != (target[0]+target[1])%2 {
		return -1
	}

	if abs(source[0]-target[0]) == abs(source[1]-target[1]) {
		return 1
	}

	return 2
}
