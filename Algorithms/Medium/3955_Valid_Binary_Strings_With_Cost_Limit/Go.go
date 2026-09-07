package main

func generateValidStrings(n int, k int) []string {
	result := make([]string, 0)
	var dfs func(prev string, cost int, path string)
	dfs = func(prev string, cost int, path string) {
		if cost > k {
			return
		}

		if len(path) == n {
			result = append(result, path)
			return
		}

		dfs("0", cost, path+"0")
		if prev != "1" {
			dfs("1", cost+len(path), path+"1")
		}
	}

	dfs("0", 0, "")
	return result
}
