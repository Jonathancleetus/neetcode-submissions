class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_final = []
        visited = set()

        for i in range(len(strs)):
            if strs[i] not in visited:
                sublist = [strs[i]]
                visited.add(strs[i])
                for j in range(len(strs)):
                    if i != j and ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                        sublist.append(strs[j])
                        visited.add(strs[j])
                out_final.append(sublist)     

        return out_final