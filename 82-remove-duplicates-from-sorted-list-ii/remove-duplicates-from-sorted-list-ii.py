class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(-101, head)
        prev = fake_head
        dupli_set = set()
        while(head != None):
            if head.val == prev.val:
                dupli_set.add(head.val)
            prev = head
            head = head.next
        
        head = fake_head.next
        prev = fake_head
        while(head != None):
            if head.val in dupli_set:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next

        return fake_head.next