# Q1 Swap Nodes in Pairs: https://leetcode.com/problems/swap-nodes-in-pairs/description/

'''
They key of this problem is:
1. the logic of switch order
    a. Pointer should be pointing to the node before 2 swaping node
    b. The order of swapping node, saving nodes which will be isolated during swapping
2. boundary:
    a. the boundary of start and stop swapping iteration
    b. the boundary of pointer next node (curr.next, curr.next.next, curr.next.next.next)
'''

# answer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None,head)
        curr = dummy_head # curr is the pointer to the node before 2 swap nodes, use it allow use to have access to curr.next and curr.next.next as while condition
        while curr.next and curr.next.next:
            temp1 = curr.next # isolate node1
            temp2 = curr.next.next.next # isolate node2
            # this is the most repeatable swap order, more detail see: https://programmercarl.com/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html#%E6%80%9D%E8%B7%AF
            curr.next = curr.next.next # current node next next node become the next node
            curr.next.next = temp1 # revert the pointer between the old next node(temp1) and new next node
            temp1.next = temp2 # point the new next next node next pointer to the temp2
            curr = curr.next.next # move forward to the next swap if there are still 2 or 2+ node left
        return dummy_head.next

# Q2 Remove Nth Node From End of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

'''
The key points of this problem:
1. Slow pointer need to stop at N-1th node at the end not the Nth node backward to delete Nth node backward
2. Boundary of moving is critical
'''

# Answer 1: move fast pointer first for n + 1 step then move slow pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize dummy node, which simplifies edge cases (e.g., removing the first node)
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        # Two pointers: i and j, both start at dummy_head
        i = dummy_head
        j = dummy_head
        
        # Move i forward by n+1 steps so that when i reaches the end,
        # j will be right before the node to remove.
        for _ in range(n + 1): # can not use i here for index becasue i already mena something, to stop at N-1, diff between i and j is N+1
            i = i.next
        
        # Move both pointers until i reaches the end of the list
        while i: # while i not while i.next to make sure j stop at N-1th Node, if use i.next here, line 61 need to change to range(n)
            i = i.next
            j = j.next
        
        # j is now just before the node to remove, so skip it
        j.next = j.next.next
        
        # Return the next node of dummy_head (which is the real head unless we removed the first node)
        return dummy_head.next



# Answer 2: move slow pointer while fast pointer, use diff to track the difference between them

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        i = dummy_head
        j = dummy_head
        diff = 0
        while i: # same here, if use i.next need to change line 93 to diff - n > 0
            diff += 1
            i = i.next
            while diff - n - 1  > 0:  # Inner while loop move slow pointer, diff > n + 1 to make sure slow pointer stop before N+1th node backward
                j = j.next
                diff -= 1
        j.next = j.next.next
        return dummy_head.next

# Q3 Intersection of Two Linked Lists https://leetcode.com/problems/intersection-of-two-linked-lists/description/

'''
1. The problem requires "return the node at which the two lists intersect". It means we need to compare the node (including val and memory address) not just node.value
2. It was a bit confuse about the input skipA and skipB, they are not actual input of the function which is a bit missleading
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Answer1 find the size of both linked list then move one pointer by the diff then move the slow pointer: 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i = headA
        a = headA
        sizeA = 0
        j = headB
        b = headB
        sizeB = 0
        while i:
            i = i.next
            sizeA += 1
        while j:
            j = j.next
            sizeB += 1
        if sizeA > sizeB:
            for _ in range(sizeA-sizeB):
                a = a.next
        elif sizeB > sizeA:
            for _ in range(sizeB-sizeA):
                b = b.next
        while a and b: # here compare a and b nodes not just nodes value
            if a == b:
                return a
            else:
                a = a.next
                b = b.next
        return None
        
# Answer 2: begin moving 2 pointers at the same time, code reusable

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dis = self.getLength(headA) - self.getLength(headB)
        
        # move at the longer linked list to make both linked list the same length
        if dis > 0:
            headA = self.moveForward(headA, dis)
        else:
            headB = self.moveForward(headB, abs(dis))
        
        # move 2 pointers unit they reach each other
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
    
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head
