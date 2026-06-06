package main

func numberOfPairs(nums1 []int, nums2 []int, queries [][]int) []int {
	n := len(nums2)
	tree := make([]map[int]int, n<<2)
	lazy := make([]int, n<<2)

	merge := func(a, b map[int]int) map[int]int {
		res := make(map[int]int)
		for k, v := range a {
			res[k] = v
		}

		for k, v := range b {
			res[k] += v
		}

		return res
	}

	var build func(node, l, r int)
	build = func(node, l, r int) {
		if l == r {
			tree[node] = make(map[int]int)
			tree[node][nums2[l]] = 1
			return
		}

		mid := (l + r) >> 1
		build(node<<1, l, mid)
		build(node<<1|1, mid+1, r)
		tree[node] = merge(tree[node<<1], tree[node<<1|1])
	}

	apply := func(node, val int) {
		new_map := make(map[int]int)
		for k, v := range tree[node] {
			new_map[k+val] = v
		}

		tree[node] = new_map
		lazy[node] += val
	}

	var update func(node, l, r, L, R, val int)
	update = func(node, l, r, L, R, val int) {
		if L <= l && r <= R {
			apply(node, val)
			return
		}

		if lazy[node] > 0 {
			apply(node<<1, lazy[node])
			apply(node<<1|1, lazy[node])
			lazy[node] = 0
		}

		mid := (l + r) >> 1
		if L <= mid {
			update(node<<1, l, mid, L, R, val)
		}

		if R > mid {
			update(node<<1|1, mid+1, r, L, R, val)
		}

		tree[node] = merge(tree[node<<1], tree[node<<1|1])
	}

	query := func(target int) int {
		return tree[1][target]
	}

	build(1, 0, n-1)
	result := make([]int, 0)
	for _, q := range queries {
		if q[0] == 1 {
			update(1, 0, n-1, q[1], q[2], q[3])
		} else {
			count := 0
			for _, num := range nums1 {
				count += query(q[1] - num)
			}
			result = append(result, count)
		}
	}

	return result
}
