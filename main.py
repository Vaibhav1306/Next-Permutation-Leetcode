class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        c = 0
        for i in range(len(nums)-1,0,-1): #finding the point of change
            if nums[i-1]<nums[i]:
                k = i
                c =1
                break
        if c==0:
            return nums.sort()  #return if no change occurs
        p=[]
        u = 100000000 #INT_MAX
        for j in range(k,len(nums)): #finding next greater then value at k-1
            if nums[j]>nums[k-1]:
                if nums[j]<u:
                    u=nums[j]
                    w = j
        #sorting the remaining array on it's place
        nums[k-1],nums[w]=nums[w],nums[k-1]
        y = nums[k:]
        y.sort()
        o = 0
        for h in range(k,len(nums)):
            nums[h]=y[o]
            o+=1
        
