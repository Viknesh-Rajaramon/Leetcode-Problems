package main

func minQueenMoves(source []int, target []int) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	if source[0] == target[0] && source[1] == target[1] {
		return 0
	}

	if source[0] == target[0] || source[1] == target[1] || abs(source[0]-target[0]) == abs(source[1]-target[1]) {
		return 1
	}

	return 2
}
