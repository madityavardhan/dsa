"""
I used a sliding window technique to solve this problem.

The idea is to keep track of all the encountered characters in a hash set within the current window.

If we encounter a character that is already present in the current window, then we shift the left pointer untill the window has all the unique characters so that the substring dosen't contain repeating characters.

We then update the maximum length of the window if the current window length is greater than the maximum length.

This approach solves the problem in O(n) time and because is uses a hash set, it also uses O(n) space.
"""


def length_of_longest_substring(s: str) -> int:
    # character set to keep track of encountered characters
    characterSet = set()
    # initialize maximum length found so far and left pointer to zero
    maxLength, left = 0, 0
    # Iterate through the string using right pointer
    for right in range(len(s)):
        # Remove characters untill there is no more repeated character
        while s[right] in characterSet:
            characterSet.remove(s[left])
            left += 1
        # Add the current character to the character set
        characterSet.add(s[right])
        # Calculate the current length of substring and update maxLength
        maxLength = max(maxLength, right - left + 1)
    return maxLength


# Example test cases
print(length_of_longest_substring("abcabcbb"))  # Expected output: 3
print(length_of_longest_substring("bbbbb"))  # Expected output: 1
print(length_of_longest_substring("pwwkew"))  # Expected output: 3
print(length_of_longest_substring(""))  # Expected output: 0
