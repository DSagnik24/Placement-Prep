def two_sum(nums,target):
    l=0
    r = len(nums)-1
    while l<r:
        sum = nums[l]+ nums[r]
        if sum == target:
            return [l,r]
        elif sum<target:
            l+=1
        else:
            r-=1

nums = [2,7,11,15]
target = 9

print(two_sum(nums,target))