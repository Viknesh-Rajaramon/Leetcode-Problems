package main

func aggregateTimeSeries(series1 [][]int, series2 [][]int) [][]int {
	result, m, n, i, j := make([][]int, 0), len(series1), len(series2), 0, 0
	for i < m && j < n {
		if series1[i][0] == series2[j][0] {
			result = append(result, []int{series1[i][0], series1[i][1] + series2[j][1]})
			i++
			j++
		} else if series1[i][0] < series2[j][0] {
			result = append(result, []int{series1[i][0], series1[i][1] + series2[j][1]})
			i++
		} else {
			result = append(result, []int{series2[j][0], series1[i][1] + series2[j][1]})
			j++
		}
	}

	for i < m {
		result = append(result, series1[i])
		i++
	}

	for j < n {
		result = append(result, series2[j])
		j++
	}

	return result
}
