""""Add two linked lists together."""


    def add_lists(list1, list2):
        """."""
        curr_1 = list1.head
        curr_2 = list2.head
        holder_1 = []
        holder_2 = []
        while curr_1.next_node is not None:
            holder_1.append(curr_1)
            curr_1 = curr_1.next_node
        while curr_2.next_node is not None:
            holder_2.append(curr_2)
            curr_2 = curr_2.next_node
        final_1 = holder_1[::-1]
        final_2 = holder_1[::-1]
        sum_list = [x.data + y.data for x, y in zip(final_1, final_2)]
        return LinkedList(sum_list)
