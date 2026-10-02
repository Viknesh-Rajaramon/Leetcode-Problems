package main

func generateParenthesis(n int) []string {
	result := make([]string, 0)
	var dfs func(left, right int, s string)
	dfs = func(left, right int, s string) {
		if len(s) == 2*n {
			result = append(result, s)
			return
		}

		if left < n {
			dfs(left+1, right, s+"(")
		}

		if right < left {
			dfs(left, right+1, s+")")
		}
	}

	dfs(0, 0, "")
	return result
}
