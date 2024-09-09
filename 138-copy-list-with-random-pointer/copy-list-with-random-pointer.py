class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        head_pointer = Node(-1, head)

        while head != None:
            copy = Node(head.val, None)
            copy.next = head.next 
            head.next = copy
            head = copy.next

        head = head_pointer.next
        sol_pointer = Node(-1, head.next)

        while head != None and head.next != None:
            if head.random != None:
                head.next.random = head.random.next
            head = head.next.next

        head = head_pointer.next

        while head != None:
            temp = head.next.next
            if temp != None:
                head.next.next = temp.next
            else:
                head.next.next = None
            head = temp

        return sol_pointer.next
