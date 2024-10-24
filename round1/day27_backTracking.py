
# Q1 77. Combinations: https://leetcode.com/problems/combinations/description/

# back tracking:
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backTracking(self, n: int, k: int, s: int):
        # base case / stop condition: if path length == k, append the path to result and return nothing
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        # current level logic: iterate each number from 1 to n
        for i in range(s, n + 1):
            self.path.append(i)
            # recursion logic: go to the next level repeat current level logic and check base case
            self.backTracking(n, k, i + 1)
            # backtracking: backtrack path to before append i
            self.path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backTracking(n, k, 1)
        return self.result
    
# optimized with branch trimed
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backTracking(self, n: int, k: int, s: int):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        # use n - (k - len(self.path)) + 1 substitute n, this is the last i which can finish a k elements path ( then + 1 because range higher boundary is not inclusive)
        for i in range(s, n - (k - len(self.path)) + 2):
            self.path.append(i)
            self.backTracking(n, k, i + 1)
            self.path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backTracking(n, k, 1)
        return self.result

# Q2 216. Combination Sum III: https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def backtracking(self, k , n, s):
        if len(self.path) == k and sum(self.path) == n:
            self.result.append(self.path[:])
            return
        elif len(self.path) == k and sum(self.path) != n:
            return
        # trim branch if > n return 
        elif sum(self.path) > n:
            return
        # use 9 - (k - len(self.path)) + 1 substitute 9, this is the last i which can finish a k elements path ( then + 1 because range higher boundary is not inclusive)
        # use 9 not n  becasue n could be > 9
        for i in range(s, 9 - (k - len(self.path)) + 2):
            self.path.append(i)
            self.backtracking(k, n, i + 1)
            self.path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.result

# Q3 17. Letter Combinations of a Phone Number: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# my answer:

class Solution:
    def __init__(self):
        self.path = ""
        self.result = []
        self.dic = {'0': [''], '1': [''], '2':['a','b','c'], '3':['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def backTracking(self, l: list, s: int):
        # stop condition: when start index > len(l) - 1, we already have a long enough string
        if s == len(l):
            self.result.append(self.path)
            return
        # operation on the level: 
        # get the leters for this start index
        letters = self.dic[l[s]]
        # iterate each letter in the letter list, perform recursion and backtrac
        for i in letters:
            self.path += i
            self.backTracking(l, s + 1)
            self.path = self.path[:-1] # remove last element in the string
        
    def letterCombinations(self, digits: str) -> List[str]:
        # input validation
        if len(digits) == 0:
            return self.result
        l = list(digits)
        self.backTracking(l,0)
        return self.result