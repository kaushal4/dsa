class Solution:

    def findK(self, start:ListNode, k:int):
        while start != None and k > 1:
            start = start.next
            k -= 1
        return start

    def reverse(self, start:ListNode, end: ListNode):
        prev = None
        cur = start
        while cur != end:
            temp = cur.next 
            cur.next = prev
            prev = cur 
            cur = temp
        end.next = prev
        return start


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        wait_pointer = ListNode(-1, None) 
        first_head = ListNode(-1, self.findK(head, k))

        while True:
            k_node = self.findK(head, k)
            if k_node == None:
                wait_pointer.next = head
                break
            wait_pointer.next = k_node
            next_group = k_node.next
            wait_pointer = self.reverse(head, k_node)
            head = next_group

        return first_head.next