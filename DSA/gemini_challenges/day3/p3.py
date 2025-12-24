# Problem 3: The Unique DNA Sequence (Variable Window + Set)
# Scenario: You are scanning a DNA string for unique markers.
# Requirement: Find the length of the longest substring without repeating characters.
# Input: "abcabcbb"
# Expected Output: 3 (The answer is "abc", with length 3).
# Input: "bbbbb" -> Output: 1
# Hint: Use a set to track what is currently in your window. If you see a duplicate, 
# shrink the window from the left until the duplicate is gone.