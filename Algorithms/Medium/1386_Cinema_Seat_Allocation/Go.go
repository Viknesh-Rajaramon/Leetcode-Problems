package main

func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
	rows := make(map[int]int)
	for _, seats := range reservedSeats {
		if 2 <= seats[1] && seats[1] <= 9 {
			rows[seats[0]] |= 1 << (seats[1] - 2)
		}
	}

	result, left, middle, right := 2*(n-len(rows)), 0b00001111, 0b00111100, 0b11110000
	for _, mask := range rows {
		if mask&left == 0 || mask&middle == 0 || mask&right == 0 {
			result++
		}
	}

	return result
}
