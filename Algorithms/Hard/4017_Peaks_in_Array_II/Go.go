package main

import (
	"sort"
)

type Fenwick struct {
	n   int
	bit []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{
		n:   n,
		bit: make([]int, n+1),
	}
}

func (f *Fenwick) add(i, delta int) {
	i++
	for i <= f.n {
		f.bit[i] += delta
		i += i & -i
	}
}

func (f *Fenwick) sum(i int) int {
	if i < 0 {
		return 0
	}

	i++
	res := 0
	for i > 0 {
		res += f.bit[i]
		i -= i & -i
	}

	return res
}

func (f *Fenwick) range_sum(l, r int) int {
	if r < l {
		return 0
	}

	return f.sum(r) - f.sum(l-1)
}

func countOfPeaks(nums []int, queries [][]int) []int64 {
	n := len(nums)
	is_peak := func(i int) bool {
		return 0 < i && i < n-1 && nums[i] > nums[i-1] && nums[i] > nums[i+1]
	}

	f_len := func(L int) int {
		if L < 3 {
			return 0
		}

		return (L - 2) * (L - 1) / 2
	}

	bit, peaks, gap_val := NewFenwick(n), make([]int, 0), make(map[int]int)
	for i := 1; i < n-1; i++ {
		if is_peak(i) {
			peaks = append(peaks, i)
		}
	}

	compute_gap_val := func(leftPeak, rightPeak int) int {
		if rightPeak != 0 {
			return f_len(rightPeak - leftPeak + 1)
		}

		return 0
	}

	for i := 0; i < len(peaks)-1; i++ {
		val := compute_gap_val(peaks[i], peaks[i+1])
		gap_val[peaks[i]] = val

		if val != 0 {
			bit.add(peaks[i], val)
		}
	}

	if len(peaks) > 0 {
		gap_val[peaks[len(peaks)-1]] = 0
	}

	add_peak := func(p int) {
		if _, exists := gap_val[p]; exists {
			return
		}

		i := sort.SearchInts(peaks, p)
		var left *int
		var right *int

		if i-1 >= 0 {
			v := peaks[i-1]
			left = &v
		}

		if i < len(peaks) {
			v := peaks[i]
			right = &v
		}

		peaks = append(peaks, 0)
		copy(peaks[i+1:], peaks[i:])
		peaks[i] = p
		if left != nil {
			new_val := compute_gap_val(*left, p)
			prev := gap_val[*left]
			if new_val != prev {
				bit.add(*left, new_val-prev)
				gap_val[*left] = new_val
			}
		}

		right_val := 0
		if right != nil {
			right_val = *right
		}

		new_val_p := compute_gap_val(p, right_val)
		gap_val[p] = new_val_p
		if new_val_p != 0 {
			bit.add(p, new_val_p)
		}
	}

	remove_peak := func(p int) {
		if _, exists := gap_val[p]; !exists {
			return
		}

		i := sort.SearchInts(peaks, p)
		var left *int
		var right *int

		if i-1 >= 0 {
			v := peaks[i-1]
			left = &v
		}

		if i+1 < len(peaks) {
			v := peaks[i+1]
			right = &v
		}

		prev_p := gap_val[p]
		if prev_p != 0 {
			bit.add(p, -prev_p)
		}

		delete(gap_val, p)
		peaks = append(peaks[:i], peaks[i+1:]...)
		if left != nil {
			right_val := 0
			if right != nil {
				right_val = *right
			}

			new_val := compute_gap_val(*left, right_val)
			prev := gap_val[*left]
			if new_val != prev {
				bit.add(*left, new_val-prev)
				gap_val[*left] = new_val
			}
		}
	}

	total_subarrays_len_ge_3 := func(L int) int {
		if L < 3 {
			return 0
		}

		return L*(L+1)/2 - (2*L - 1)
	}

	result := make([]int64, 0)
	for _, q := range queries {
		if q[0] == 1 {
			total := total_subarrays_len_ge_3(q[2] - q[1] + 1)
			if total == 0 {
				result = append(result, int64(0))
				continue
			}

			Lidx := sort.Search(len(peaks), func(i int) bool {
				return peaks[i] >= q[1]+1
			})

			Ridx := sort.Search(len(peaks), func(i int) bool {
				return peaks[i] > q[2]-1
			}) - 1

			if Lidx > Ridx {
				result = append(result, int64(0))
				continue
			}

			internal_sum := 0
			if Lidx <= Ridx-1 {
				internal_sum = bit.range_sum(peaks[Lidx], peaks[Ridx-1])
			}

			no_peak_subarrays := f_len(peaks[Lidx]-q[1]+1) + internal_sum + f_len(q[2]-peaks[Ridx]+1)
			result = append(result, int64(total-no_peak_subarrays))
		} else {
			if nums[q[1]] == q[2] {
				continue
			}

			nums[q[1]] = q[2]
			for _, j := range []int{q[1] - 1, q[1], q[1] + 1} {
				if j <= 0 || j >= n-1 {
					continue
				}

				now := is_peak(j)
				_, was := gap_val[j]
				if now && !was {
					add_peak(j)
				} else if !now && was {
					remove_peak(j)
				}
			}
		}
	}

	return result
}
