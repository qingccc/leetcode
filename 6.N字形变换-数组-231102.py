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
        if numRows < 2:
            return s
        row = numRows
        sub_len = 2 * numRows-2
        n= len(s) % sub_len
        if n == 0:
            temp = 0
        elif n <= numRows:
            temp = 1
        else:
            temp = n - numRows + 1
        col_len = len(s)//sub_len * (numRows-1) + temp
        metric = [[0 for i in range(col_len)] for j in range(row)]
        indexi = 0
        indexj = 0
        for index,i in enumerate(s):
            if (index % sub_len) < (numRows-1):
                metric[indexi][indexj] = i
                indexi += 1
            else:
                metric[indexi][indexj] = i
                indexi -= 1
                indexj+=1
        rs_list = []
        for i in range(len(metric)):
            for j in range(len(metric[0])):
                if metric[i][j] !=0:
                    rs_list.append(metric[i][j])
        return "".join(rs_list)





if __name__ == '__main__':
    so = Solution()
    print(so.convert("PAYPALISHIRING", 2))







