from typing import List, Tuple
from collections import defaultdict, Counter
from sortedcontainers import SortedList

class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        children = defaultdict(list)
        for child, p in enumerate(par):
            if p != -1:
                children[p].append(child)
        
        query_map = defaultdict(list)
        for parent, k in queries:
            query_map[parent].append(k)
        
        def merge(big_list, big_counter, small_list, small_counter) -> None:
            for val in small_list:
                if val not in big_counter:
                    big_list.add(val)
                
                big_counter[val] += small_counter[val]

        result = {}
        def dfs(parent: int, path_xor: int) -> Tuple[SortedList, Counter]:
            curr_xor = path_xor ^ vals[parent]
            big_list, big_counter = SortedList(), Counter()
            
            for child in children[parent]:
                small_list, small_counter = dfs(child, curr_xor)
                if len(small_list) > len(big_list):
                    big_list, small_list = small_list, big_list
                    big_counter, small_counter = small_counter, big_counter
                
                merge(big_list, big_counter, small_list, small_counter)
            
            big_counter[curr_xor] += 1
            if big_counter[curr_xor] == 1:
                big_list.add(curr_xor)
            
            for k in query_map[parent]:
                result[(parent, k)] = big_list[k-1] if k-1 < len(big_list) else -1
                
            return big_list, big_counter
        
        dfs(0, 0)
        return [result[(parent, k)] for parent, k in queries]
