class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l, r = 0, 0
        count = Counter() # Do not take this counter inside the while loop

        while r < len(s):
            count[s[r]] += 1 # because 'r' runs the whole string 
            max_count = max(count.values())

            if (r-l+1) - max_count <= k:
                maxLen = max(maxLen, r - l + 1)
                r += 1 # Expanding the window
            else:
                count[s[l]] -= 1 # Shrinking the window
                l += 1 # Shrinking the window
                r += 1

        return maxLen
            

