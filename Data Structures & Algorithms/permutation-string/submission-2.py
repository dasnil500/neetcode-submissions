class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)

        ws = len(s1)

        l = 0
        r = ws - 1
        substring_count = Counter(s2[:r+1])

        while r < len(s2):

            if substring_count == s1_dict:
                return True

            substring_count[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                substring_count[s2[r]] += 1

        return False