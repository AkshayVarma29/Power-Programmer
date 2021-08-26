# Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly increasing order.

head = [1, 5, 9, 9]

# def solve(head):
#     temp = head.next
#     last_element = head.val
#     while (temp!=None):
#         if temp.val <= last_element:
#             return False
#         else:
#             last_element = temp.val
#             temp = temp.next
#     return True

def solve(head):
    curr = head
    while curr.next:
        if curr.val >= curr.next.val:
            return False
        curr = curr.next
    return True