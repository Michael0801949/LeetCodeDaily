#Q1 Remove Linked List Elements https://leetcode.com/problems/remove-linked-list-elements/description/

'''
This Problem helps me be familiar with linked list gramma, to simplify the problem need to add a dummy node
'''

# Standard Answer 
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Create a dummy node and set its next pointer to head
        dummy_head = ListNode(0)
        dummy_head.next = head

        # Set cur to point to the dummy node
        cur = dummy_head

        # Traverse through the list
        while cur.next: # can use either 'cur.next is not None' or just 'cur.next' they are interchangeable 
            if cur.next.val == val:
                # Remove the node with the matching value
                cur.next = cur.next.next # I thought I can also do a cur = cur.next here, but it is wrong, becasue the next node can also be equal to val, then that val will be left off
            else:
                # Move cur to the next node
                cur = cur.next
        
        # Return the updated list, skipping the dummy node
        return dummy_head.next # need to get used to the linked list gramma, only the first value can be immidiately accessed
# Recurssion Answer
'''
Need to revisit how recurssion works
'''
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Base case: if the head is None (empty list), return None
        if head is None:
            return None

        # Recursive case
        if head.val == val:
            # If the current node's value matches, skip this node and call the function recursively
            new_head = self.removeElements(head.next, val)
            return new_head
        else:
            # Otherwise, proceed to the next node
            head.next = self.removeElements(head.next, val)
            return head

# Q2 Design Linked List: https://leetcode.com/problems/design-linked-list/description/
'''
Logic is not complex, get farmiliar with the data structure problem:
1. Init the data structure, think about what attribute need define for the specific instance to achive function required
2. Leverage the built in attribute from 1 write the logic
3. be careful about the index boundary see comment in line
'''
# Single linked list answer
# Single linked list answer
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        # to store instance specific info add self.xxx
        self.dummy_head = ListNode() # this dummy head helps adding or removing node (q1 as example), it is pointing to None at init, after we add node, it point to the head of node
        self.size = 0 # size here helps to retrive the length of the linked list but it is not 100% needed

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy_head.next # this is the current head, or None if we have not add any node to MyLinkedList
        for i in range(0, index): # I hesitate to use index or index + 1, should use index, becasue when i = index - 1, curr.next index is index. Again range is left close right open, so last i = index - 1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy_head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        self.size += 1     

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: # index here also need validation, when add it is > size becasue index can be equal = size to add to the very end
            return
        curr = self.dummy_head # dummy_head.next may be none if we have not add any node, there will be case add to the begining of the linkedlist, so curr must start with dummy
        for i in range(0, index): # i need to stop at index -1 to add the val at index, last run of this loop i = index - 1, curr move to curr next(with index equal given index), but we star at dummy node which is before index 0, so curr actual move to index - 1 not index 
            curr = curr.next
        temp = curr.next
        curr.next = ListNode(val, curr.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.dummy_head
        for i in range(0, index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1
        
# Q3 Reverse Linked List https://leetcode.com/problems/reverse-linked-list/description/

# 2 pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        pre = None # pre is just a pointer point to the previous node
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

# recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    def reverse(self, curr: ListNode, pre: ListNode) -> ListNode:
        if curr == None:
            return pre
        temp = curr.next
        curr.next = pre
        return self.reverse(temp, curr)
