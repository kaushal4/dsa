class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        even = []
        odd = []
        
        head_pointer = ListNode(-1, head)

        count = 0
        while head != None:
            even.append(head)
            head = head.next
            count += 1

        odd = even[::-1]

        i = 0
        even_pointer = 0
        odd_pointer = 0
        prev = head_pointer
        while count:
            pointer = None 
            if i % 2 == 0:
                pointer = even[even_pointer]
                even_pointer += 1
            else:
                pointer = odd[odd_pointer]
                odd_pointer += 1
            
            prev.next = pointer
            pointer.next = None
            prev = pointer

            i += 1
            count -= 1

        return head_pointer.next