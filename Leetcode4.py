"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 """

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in range(1,len(strs)):
            if len(a) > len(strs[i]):
                a = a[0:len(strs[i])]
            for j in range(len(a)):
                if a[j] != strs[i][j]:
                    a = a[0:j]
                    break
        return a