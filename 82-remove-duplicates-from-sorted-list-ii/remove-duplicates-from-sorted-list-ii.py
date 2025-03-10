class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(-101, head)
        prev = fake_head
        dupli_val = -101

        while head != None:
            if head.val == dupli_val:
                prev.next = head.next
                head = head.next
            elif head.next and head.val == head.next.val:
                dupli_val = head.val
            else:
                prev = head
                head = head.next

        return fake_head.next