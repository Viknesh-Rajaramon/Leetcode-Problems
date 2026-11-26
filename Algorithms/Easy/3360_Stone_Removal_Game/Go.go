package main

func canAliceWin(n int) bool {
	result, take := false, 10
	for n >= take {
		n -= take
		take--
		result = !result
	}

	return result
}
