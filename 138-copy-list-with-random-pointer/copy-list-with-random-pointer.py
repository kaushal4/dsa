class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        head_pointer = Node(-1, head)
        duplicates = []

        while head != None:
            copy = Node(head.val, None)
            duplicates.append(copy)
            copy.next = head.next 
            head.next = copy
            head = copy.next

        head = head_pointer.next

        while head != None and head.next != None:
            if head.random != None:
                head.next.random = head.random.next
            head = head.next.next

        for i in range(0, len(duplicates)):
            duplicates[i].next = duplicates[i + 1] if i + 1 < len(duplicates) else None

        return duplicates[0]