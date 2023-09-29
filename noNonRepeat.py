'''you are given a string str consisting english lowercase alphabet only. Let brr be anoter string that is made by first taking all the even indexed charecter of the str and then odd indexed charecter of str.

for example: input = "abc" output = "a"
example: input = "aabbcc" output = -1
if there is no non repeat charecter then print -1 other wise print the first non repeat charecter.
'''

class Solution(object):
    def nonRepeat(self, input):
        even = input[::2]
        odd = input[1::2]
        brr = even + odd

        count = {}

        for c in input:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        for c in brr:
            if count[c] == 1:
                return c
        return -1

s = Solution()
# res = s.nonRepeat("abc")
res = s.nonRepeat("aabbcc")
print(res)

# the time complexity of this code is O(n)