from typing import Optional, List, Tuple
from math import inf, log2, log, sqrt, ceil
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop, heappushpop, heapify
import pandas as pd
from queue import PriorityQueue
import random
from itertools import accumulate
from sortedcontainers import SortedList
from random import randint
from functools import cache


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
