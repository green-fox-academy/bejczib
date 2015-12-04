def reverse2(nums):
   output = []
   i = len(nums)-1
   while i >= 0:
       output.append(nums[i])
       i -= 1
   return output
