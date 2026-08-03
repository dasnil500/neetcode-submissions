class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)

        ws = len(s1)

        l = 0
        r = ws - 1

        while r < len(s2):
            substring = s2[l:r+1]
            substring_count = Counter(substring)

            if substring_count == s1_dict:
                return True
            else:
                r += 1
                l += 1
        return False