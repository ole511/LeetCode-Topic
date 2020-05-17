# 17. 电话号码的字母组合
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        chars=['abc','def','ghi','jkl','mno','qprs','tuv','wxyz']
        res=['']
        for i in digits:
            now=[]
            for j in chars[int(i)-2]:
                for k in res:
                    now.append(k+j)
            res=now
        return res
