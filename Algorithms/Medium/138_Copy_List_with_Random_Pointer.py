from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {None: None}
        
        ptr = head
        while ptr:
            new_node = Node(ptr.val)
            hash_map[ptr] = new_node
            ptr = ptr.next
        
        ptr = head
        while ptr:
            hash_map[ptr].next = hash_map[ptr.next]
            hash_map[ptr].random = hash_map[ptr.random]
            ptr = ptr.next
        
        return hash_map[head]
