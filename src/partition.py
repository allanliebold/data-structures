"""Partition linked list."""

def partition(link_list, target):
    """Partition a linked list around value x."""
    curr = link_list.head
    new_list = LinkedList()
    first_half = []
    second_half = []
    while curr.next_node.data:
        if curr.data < target:
            first_half.append(curr)
        elif curr.data >= target:
            second_half.append(curr)
        curr = curr.next_node
    new_list.push(second_half)
    new_list.push(first_half)
    return new_list


partition(LinkedList([4, 3, 1, 2, 5]), 2.5)