class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=s.replace(" ", "")
        final=new.lower()
        count = 0
        for i in range(0, len(final)):
            if not final[i].isalnum():
                count = count + 1

        if count == len(final):
            return True

        leftptr = 0
        rightptr = len(final) - 1
        while leftptr < rightptr:
            while not final[rightptr].isalnum():
                rightptr = rightptr - 1
            while not final[leftptr].isalnum():
                leftptr = leftptr + 1

            if final[leftptr] != final[rightptr]:
                return False

            leftptr = leftptr + 1
            rightptr = rightptr - 1
        
        return True
