func minEnergy(n int, brightness int, intervals [][]int) int64 {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	var time int64 = 0
	start := intervals[0][0]
	end := intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] <= end {
			end = max(end, intervals[i][1])
		} else {
			time += int64(end - start + 1)
			start = intervals[i][0]
			end = intervals[i][1]
		}
	}

	time += int64(end - start + 1)
	return time * int64((brightness+2)/3)
}
