package main

import (
	"strconv"
)

func longestCommonPrefix(arr1 []int, arr2 []int) int {
	prefix_map := make(map[string]int)

	for _, num := range arr1 {
		str_num := strconv.Itoa(num)
		prefix := ""
		for _, c := range str_num {
			prefix += string(c)
			prefix_map[prefix]++
		}
	}

	result := 0
	for _, num := range arr2 {
		str_num := strconv.Itoa(num)
		prefix := ""
		for _, c := range str_num {
			prefix += string(c)
			if _, found := prefix_map[prefix]; found {
				if len(prefix) > result {
					result = len(prefix)
				}
			}
		}
	}

	return result
}
