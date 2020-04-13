def middleNode(self, head: ListNode) -> ListNode:
    node_list = []
    current_node=head
    while current_node != None:
        node_list.append(current_node)
        current_node= current_node.next

    node_lst_len= len(node_list)-1
    if node_lst_len %2 ==0:
        middle_indx = int(node_lst_len/2)
        
    else:
        middle_indx = int((node_lst_len+1)/2)
        
    print (node_lst_len, middle_indx)
    
    mid_node = node_list[middle_indx]
    
    current_node=head
    while current_node != None:
        if current_node == mid_node:
            return current_node
        
        else:
            current_node= current_node.next