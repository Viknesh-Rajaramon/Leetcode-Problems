package main

func secondsBetweenTimes(startTime string, endTime string) int {
	f := func(c byte) int {
		return int(c - '0')
	}

	diff := func(i int) int {
		return 10*(f(endTime[i])-f(startTime[i])) + f(endTime[i+1]) - f(startTime[i+1])
	}

	return 60*(60*(diff(0))+diff(3)) + diff(6)
}
