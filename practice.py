def twoSum(items, target):
    sum = 0
    for i in range(len(items)-1):
        j = i+1
        while j<len(items):
            sum = items[i] + items [j]
            if sum == target:
                return [i,j]
            j+=1

# print(twoSum([5,2,6,4], 8))
# Time complexity O(n2)
# Space complexity O(1). Space required doesn't depend on size of input array.

#Two-pass hash table
def hashtwoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    # If no valid pair is found, return an empty list
    return []

# print(hashtwoSum([5,2,6,4], 8))
#Time complexity O(n)
#Space complexity O(n). Space required depends on number of items stored in hash table.

#One-pass hash table
def ohashtwoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    # If no valid pair is found, return an empty list
    return []

# print(ohashtwoSum([5,2,6,4], 8))
#Time complexity O(n)
#Space complexity O(n). Space required depends on number of items stored in hash table.

def rev_string(s):
    left = 0
    right = len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1

# Time complexity O(n/2) = O(n) where n is the length of the array
# Space complexity O(1). Regardless of input, only 2 points are used
# Modified in-place without creating another array or using additional memory
# Using slice object to creates a new array using O(n) extra memory