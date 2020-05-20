'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,u,n,st,path,ans):
            if u==n:
                ans.append(path[:])
                return
            for i in range(n):
                if not st[i]:
                    st[i] = True
                    path.append(nums[i])
                    dfs(nums,u+1,n,st,path,ans)
                    path.pop()
                    st[i] = False
        ans=[]        
        n = len(nums)
        st=[False]*n
        path=[]
        dfs(nums,0,n,st,path,ans)
        return ans




