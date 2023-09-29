'''You are given a string str that contain lowercase english alphabets only. for each charecter in the string. your task is to find the number of occurences of that charecter on the side of the sting

for example: input = "abcd" then the output = "0 0 0 0"
example: input = "abaab" then the output = "2 1 1 0 0"
'''
class Solution(object):
    def occurance(self, input):
        occur = []
        for i in range(len(input)):
            c = input[i]
            rightSide = input[i+1:]
            occur.append(rightSide.count(c))
        return occur
    
s = Solution()
# res = s.occurance("abcd")
res = s.occurance("abaab")
result = " ".join(map(str, res))
print(result)

# the time complexity of this code is O(n^2).

 

