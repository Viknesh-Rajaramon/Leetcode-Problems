package main

func minimumPushes(word string) int {
	n := len(word)
	m := (n-1)/8 + 1
	return m * (n - 4*(m-1))
}
