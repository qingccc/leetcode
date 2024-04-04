'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
思路：
按照字面意思，就是按照Z字型排列，然后按照从上到下，从左到右的顺序读取
所以可以看做一个个z字形的迭代  每个的长度是2n-2
但是要考虑边界条件 n=1时  2n-2 = 0 ; n=2时，
1. 分析问题
2. 边界条件
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # n+n-2  2n-2
        if numRows < 2:
            return s
        i = 0
        j = 0
        sub_len = 2 * numRows - 2
        index = 0
        temp_key = len(s) % sub_len
        if temp_key == 0:
            col_len = int(len(s) / sub_len) * (numRows - 1)
        else:
            col_len = int(len(s) / sub_len * (numRows - 1)) + (temp_key % numRows + 1)
        print(col_len)
        rs_matrics = [[0 for _ in range(col_len)] for j in range(numRows)]

        for index in range(len(s)):
            rs_matrics[i][j] = s[index]
            key = index % sub_len
            if key < numRows - 1:
                i += 1
            else:
                j += 1
                i -= 1

        rs_list = []
        print(rs_matrics)
        for row in range(len(rs_matrics)):
            for col in range(len(rs_matrics[0])):
                if rs_matrics[row][col] != 0:
                    rs_list.append(rs_matrics[row][col])
        return "".join(rs_list)
if __name__ == '__main__':
    so = Solution()
    print(so.convert("PAYPALISHIRING", 2))







