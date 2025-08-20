class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head: Optional[ListNode]):
            if head == None:
                return head
            prev = None

            while(head != None):
                temp = head.next
                head.next = prev
                prev = head
                head = temp

            return prev
        
        if head == None:
            return
        
        og_head = head
        fast = head
        slow = head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        
        
        to_insert = reverse(slow.next)
        slow.next = None

        head = og_head
        while head != None and to_insert != None:
            temp = head.next
            temp2 = to_insert.next
            head.next = to_insert
            to_insert.next = temp
            to_insert = temp2
            head = temp