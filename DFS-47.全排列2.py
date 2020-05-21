class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:return []
        def dfs(nums,n,u,path,res,used):
            if u==n:
                res.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    if i>0 and not used[i-1] and nums[i]==nums[i-1]:
                        continue
                    used[i]=True
                    path.append(nums[i])
                    dfs(nums,n,u+1,path,res,used)
                    used[i]=False
                    path.pop()
        n=len(nums)
        path=[]
        nums.sort()
        res=[]
        used=[False]*n
        dfs(nums,n,0,path,res,used)
        return res
