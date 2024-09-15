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
      
