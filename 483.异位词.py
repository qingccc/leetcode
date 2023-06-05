from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        rs_list = []
        map_p = {}
        tmp_map = {}
        left = 0
        if s == p:
            return [0]
        if len(s) == 1 and len(p) == 1 and s != p:
            return []
        for letter in p: 
            map_p[letter] = map_p.get(letter, 0) + 1
            left = 0
        for r in range(len(p) - 1, len(s)):

            i = left
            while i < r:
                if s[i] not in map_p:
                    # left 应该移动到i的下一位
                    tmp_map = {}
                    left = i + 1
                    break
                if s[i] in map_p and tmp_map.get(s[i], 0) < map_p.get(s[i]):
                    tmp_map[s[i]] = tmp_map.get(s[i], 0) + 1
                else:
                    # tmp_map[s[i]] = tmp_map.get(s[i]) - 1
                    # 需要把前面的都删除
                    for j in range(left, i + 1):
                        tmp_map = {}
                        if s[j] == s[i]:
                            left = j + 1
                            break
                    break
                i += 1
            print(left, r)
            if i == r:
                # print(left,r)
                rs_list.append(r - len(p) + 1)
                tmp_map[s[left]] = tmp_map.get(s[left]) - 1
                left = left + 1
        return rs_list
if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    so = Solution()
    print(so.findAnagrams(s,p))
