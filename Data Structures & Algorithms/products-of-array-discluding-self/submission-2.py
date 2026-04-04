class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 时间复杂度 O(n)
        # 空间复杂度 O(1) 因为output array不计入空间
        n = len(nums)
        res = [1] * n
        suffix = 1      # 用来存 prefix，最后也作为答案返回
        
        # ① 左边乘积：把 prefix 填进 res
        for i in range(1, n):                   # res[i] 存的是“i 左边所有数的乘积”
            res[i] = res[i - 1] * nums[i - 1]   # 更新 prefix：再乘上当前这个数

        # ② 右边乘积：用 suffix 变量从右往左乘进去
        for i in range(n - 1, -1, -1):
            res[i] *= suffix    # 再乘上“右边所有数的乘积”
            suffix *= nums[i]   # 更新 suffix：乘上当前这个数

        return res