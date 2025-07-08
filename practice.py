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

def delete_task(id):
    item_id = int(id)
    for i in task_list:
        if i["id"] == item_id:
            print(task_list.index(i))

task_list=[{"id":1,"task": "sleep"},{"id":2,"task": "play"} ]
# delete_task(2)


#A stack is a linear data structure that follow last-in-first-out principle. Elements are added (pushed)
#and removed (popped) from the same end, called the top

# stack = []
# stack.append(1)
# stack.pop() #Removes last element

s = '()'

def isValid(self, s: str) -> bool:
    hashmap = {')':'(', '}': '{', ']': '['}
    stack = []
    for i in s:
        if i not in hashmap:
            stack.append(i)
            continue
        if len(stack) ==0 or  hashmap[i] != stack[-1]:
            return False
        stack.pop()
    if len(stack) > 0:
        return False
    return True

#Valid Parentheses
# Time complexity O(n) = O(n) where n is the length of the inputarray
# Space complexity O(n). Storing number of opening brackets

#Linked list is a linear data structure where notes are stored in a sequence
#Each node contains data and a reference (pointer) to the next node
#Unlike arrays, linked lists don't use contiguous memory, allowing dynamic size changes.


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)  # Dummy node to anchor the merged list
    current = dummy  # Tracks the end of the merged list
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1  # Add list1’s node
            list1 = list1.next
        else:
            current.next = list2  # Add list2’s node
            list2 = list2.next
        current = current.next  # Move to the newly added node
    current.next = list1 if list1 else list2  # Append remaining nodes
    return dummy.next  # Return head of merged list



#Merge Two Sorted Lists
# Time complexity O(n) processing time increases with size n (strictly n+m)
# Space complexity O(1) constant because list1 and list2 pointers are updated in place. Don't have additional nodes