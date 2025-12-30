class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, head1, head2):
        # Reverse both lists
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        # Add digits
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = Node(total % 10)
            curr = curr.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        # Reverse result
        result = self.reverse(dummy.next)

        # Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next

        return result

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
