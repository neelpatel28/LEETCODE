# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k
        k = k % length
        if k == 0:
            return head

        # Step 3: Make circular list
        tail.next = head

        # Step 4: Find new tail
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head