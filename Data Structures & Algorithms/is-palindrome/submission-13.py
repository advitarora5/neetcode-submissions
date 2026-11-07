class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=s.replace(" ", "")
        final=new.lower()

        leftptr = 0
        rightptr = len(final) - 1
        while leftptr < rightptr:
            while leftptr < rightptr and not final[rightptr].isalnum():
                rightptr = rightptr - 1
            while leftptr < rightptr and not final[leftptr].isalnum():
                leftptr = leftptr + 1

            if final[leftptr] != final[rightptr]:
                return False

            leftptr = leftptr + 1
            rightptr = rightptr - 1
        
        return True
