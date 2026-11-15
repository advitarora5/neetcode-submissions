class Solution:
    def climbStairs(self, n: int) -> int:
        #after every step you have 2 choices, climb with 1 step at a time or            2       steps at a time
        #recursive binary tree
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        