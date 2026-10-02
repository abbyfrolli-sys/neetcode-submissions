class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        
        pdt =1
        pdt2= 1
        for i in range(len(nums)):
            output[i] = pdt
            pdt *= nums[i]
    
        for j in range(len(nums)-1, -1, -1):
            output[j] *= pdt2
            pdt2 *= nums[j]
        return output
            
          
            
