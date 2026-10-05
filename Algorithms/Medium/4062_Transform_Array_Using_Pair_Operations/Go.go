package main

func canTransform(source []int, target []int) bool {
	sum_ := 0
	for i := range len(source) {
		sum_ += source[i] - target[i]
	}

	return sum_ == 0
}
