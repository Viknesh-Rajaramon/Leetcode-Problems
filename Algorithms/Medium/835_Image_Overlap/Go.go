package main

func largestOverlap(img1 [][]int, img2 [][]int) int {
	type RC struct {
		r int
		c int
	}

	n, img1_points, img2_points, d := len(img1), make([]RC, 0), make([]RC, 0), make(map[RC]int)
	for r := range n {
		for c := range n {
			if img1[r][c] == 1 {
				img1_points = append(img1_points, RC{r: r, c: c})
			}

			if img2[r][c] == 1 {
				img2_points = append(img2_points, RC{r: r, c: c})
			}
		}
	}

	for i := range img1_points {
		for j := range img2_points {
			key := RC{r: img2_points[j].r - img1_points[i].r, c: img2_points[j].c - img1_points[i].c}
			if _, exists := d[key]; !exists {
				d[key] = 0
			}

			d[key]++
		}
	}

	result := 0
	for _, val := range d {
		result = max(result, val)
	}

	return result
}
