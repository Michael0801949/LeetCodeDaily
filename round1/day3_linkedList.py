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
