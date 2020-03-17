## I didn't end up finishing the problem in the hour, but my idea is to create a tree based on places the rabbit can visit.  Then the possible places are the children of the start node, add the largest of these, and stop when there are no more nodes to visit.

class Node(object):
    """Node in a tree."""
    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children
    def __repr__(self):
        """Reader-friendly representation."""
        return "<Node {data}>".format(data=self.data)

class Tree(object):
    """Tree."""
    def __init__(self, root):
        self.root = root
    def __repr__(self):
        """Reader-friendly representation."""
        return "<Tree root={root}>".format(root=self.root)
    def get_nodes(self, data):
        to_visit= [self.root]
        node_list=[]
    
        while to_visit:
            current= to_visit.pop(0)
            if current.data == data:
                node_list.append(current)
                to_visit.extend(current.children)

            else:
                to_visit.extend(current.children)
        return node_list

b1 = Node("B")
b2 = Node("B")
e = Node("E")
c = Node("C", [ b1, e])
a = Node("A", [b2, c])
tree = Tree(a)
result = tree.get_nodes("B")
print(result)



garden = [
[2, 3, 1, 4, 2, 2, 3],
[2, 3, 0, 4, 0, 3, 0],
[1, 7, 0, 2, 1, 2, 3],
[9, 3, 0, 4, 2, 0, 3],]

def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid
    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns
    nrows = len(garden)
    ncols = len(garden[0])
    carrot_sum=0

    def starting_pos(nrorc):
        if nrorc % 2==0:
          first_num= int(nrorc)
          second_num= int(nrorc) + 1
          highest_num = max (garden[first_num], garden[second_num])
          return highest_num

        else:
            return (nrorc/2) 
            poss_starting_norc= (((nrorc+1)/2), ((nrorc-1)/2))
            return poss_starting_norc

    srow= starting_pos(nrows)
    scol= starting_pos(ncols)
    start=(srow, scol)

    start=Node(start, (garden[start[0]][start[1]]))

# getting the starting position
    start_row= starting_pos(nrows)
    start_col= starting_pos(ncols)
    if (start_row is tuple) or (start_col is tuple):
      return True

    else:
      start_pos=start_row, start_col
      return False

print(lunch_count(garden))


