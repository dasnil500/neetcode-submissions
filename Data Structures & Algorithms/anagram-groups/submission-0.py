class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = {}
        for item in strs:
            temp = Counter(item)
            key = tuple(sorted(temp.items()))

            if key not in temp_dict:
                temp_dict[key] = [item]
            else:
                temp_dict[key].append(item)

        return list(temp_dict.values())
