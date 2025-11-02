from typing import Optional, List, Tuple
from math import inf, log2, log, sqrt, ceil, comb, gcd, lcm, prod
from collections import deque, Counter, defaultdict, OrderedDict
from heapq import heappush, heappop, heappushpop, heapify, nlargest
import pandas as pd
from queue import PriorityQueue
import random
from itertools import accumulate, product, combinations
from sortedcontainers import SortedList
from random import randint
from functools import cache, lru_cache
import string
from bisect import bisect_left, bisect_right, insort
import re
from datetime import datetime


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

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
