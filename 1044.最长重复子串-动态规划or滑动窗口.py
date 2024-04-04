class Solution:
    # def longestDupSubstring(self, s: str) -> str:
    #     max_str = ""
    #     i = 0
    #     for index in range(len(s)):
    #         # 在前面存在
    #         tmp_len = 0
    #
    #         if s[index] in s[i:index]:
    #             # print(i)
    #             # 找到具体的位置
    #             start = s[i:index].find(s[index])
    #             begin = start
    #             # temp_str = s[i:]
    #             tmp_index = index
    #             print(tmp_index, s[i], s[tmp_index])
    #             while (tmp_index < len(s) and start < len(s) and s[start] == s[tmp_index]):
    #                 start += 1
    #                 tmp_index += 1
    #                 tmp_len += 1
    #             print(tmp_len)
    #
    #             max_str = max_str if len(max_str) > tmp_len else s[begin:begin + tmp_len]
    #             i += start
    #         # if tmp_len!=0:
    #         #     index += tmp_len
    #     return max_str
    def longestDupSubstring(self, s: str) -> str:
        max_str = ""
        # if len(s) <= 2:
        #     if s[0] == s[1]:
        #         return s[0]
        #     else:
        #         return ""
        for i in range(len(s)):

            if i > 0 and s[i] in s[:i]:
                tmp_len = 0
                index = i
                while (index < len(s) and (s[i:index+1] in s[:index])):
                    tmp_len += 1
                    index += 1
                max_str = max_str if len(max_str) >= tmp_len else s[i:i + tmp_len]
        return max_str

if __name__ == '__main__':
    so = Solution()
    # print(so.longestDupSubstring("banana"))
    print(so.longestDupSubstring("nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"))
    print(so.longestDupSubstring("zxcvdqkfawuytt"))