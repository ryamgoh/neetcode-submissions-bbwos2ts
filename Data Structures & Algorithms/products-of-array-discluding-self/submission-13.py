class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = [0] * len(nums)

        temp = 1
        for i in range(len(nums)):
            prefix[i] = temp * nums[i]
            temp = prefix[i]

        temp = 1
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = temp * nums[j]
            temp = postfix[j]

        print(prefix)
        print(postfix)

        for i in range(len(nums)):
            # if i == 0:
            #     output[i] = postfix[i + 1]
            # if i == len(nums) - 1:
            #     output[i] = prefix[i - 1]
            left = prefix[i - 1] if (i - 1) >= 0 else 1
            right = postfix[i + 1] if (i + 1) < len(nums) else 1
            output[i] = left * right

        return output