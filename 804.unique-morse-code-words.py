#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#
# https://leetcode.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (76.61%)
# Likes:    602
# Dislikes: 622
# Total Accepted:    134.6K
# Total Submissions: 175.8K
# Testcase Example:  '["gin", "zen", "gig", "msg"]'
#
# International Morse Code defines a standard encoding where each letter is
# mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps
# to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
#
#
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# Now, given a list of words, each word can be written as a concatenation of
# the Morse code of each letter. For example, "cba" can be written as
# "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call
# such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
#
#
# Note:
#
#
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.
#
#
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        return len({"".join(morse[ord(c) - ord("a")] for c in word) for word in words})
        #  for word in words:
        #      s = ""
        #      for c in word:
        #          s += morse[ord(c) - ord("a")]
        #      seen_codes.add(s)
        #  return len(seen_codes)


# @lc code=end
