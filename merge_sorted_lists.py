# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

#Pseudocode:
# The lists are sorted, compare each value from the list, while either of the lists have items in them
# If one list is out of items, add the entire other list

def merge_sorted(lst1, lst2):
    sorted_lst=[]
    list1_idx=0
    list2_idx=0

    while len(sorted_lst)< len(lst1)+len(lst2):
      if not lst1 or (list1_idx==len(lst1)-1):
          sorted_lst.extend(lst2)

      if not lst2 or (list2_idx==len(lst2)-1):
          sorted_lst.extend(lst1)

      else:

        if lst1[list1_idx]> lst2[list2_idx]:
          sorted_lst.append(lst2[list2_idx])
          list2_idx+=1

        elif lst1[list1_idx]< lst2[list2_idx]:
          sorted_lst.append(lst1[list1_idx])
          list1_idx+=1

        elif lst1[list1_idx]==lst2[list2_idx]:
          sorted_lst.append(lst1[list1_idx])
          sorted_lst.append(lst2[list2_idx])
          list2_idx+=1
          list1_idx+=1

        return sorted_lst