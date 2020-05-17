'''
顺序：
1. 枚举起点
2. 依次搜索下一个点的位置
3. 在枚举过程中，实时判断当前路径和目标单词是否匹配。
时间复杂度：nm*3^k     nm是二维矩阵的长和宽，代表起点的个数
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(i,j,board,word,0,m,n):
                    return True
        return False
    
    def dfs(self,x,y,board,word,u,m,n):
        if board[x][y] != word[u]: return False
        if u == len(word)-1: return True

        dx,dy=[-1,0,1,0],[0,1,0,-1]
        board[x][y] = '.'
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a>=0 and a<m and b>=0 and b<n:
                if self.dfs(a,b,board,word,u+1,m,n):
                    return True
        board[x][y]=word[u]
        return False
