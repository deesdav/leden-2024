class Node:
    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None
        

class BinaryTree:
    def __init__(self):
        self._root = None

    def get_most_right_item(self, node):
        current_node = node
        while current_node._right is not None:
            current_node = current_node._right
        return current_node
    
    def get_most_left_item(self, node):
        current_node = node
        while current_node._left is not None:
            current_node = current_node._left
        return current_node

    def remove_value(self, value):
        if self._root is None:
            return
        
        if self._root._value == value:
            self.remove_root_node()
        else:
            self.remove_node(self._root, value)
    
    def remove_node(self, node):
        if node._left is None and node._right is None:
            node = None
            return

        if node._left is None:
           node = node._right
           return

        if node._left._right is None:
            node._left._right = node._right
            node = node._left
            return
        
        new_value = self.get_most_right_item(node._left)
        current_node = node._left
        while current_node._right is not new_value:
            current_node = current_node._right
        current_node._right = None
        node._value = new_value._value

    def remove_root_node(self):
        if self._root._left is None and self._root._right is None:
            node = None
            return
        
        if self._root._left is None:
           node = node._right
           return

        if self._root._left._right is None:
            self._root._left._right = self._root._right
            self._root = self._root._left
            return
    
        self.remove_node(self._root)
        


    def dfs(self):
        if self._root is None:
            return
        queue = [self._root]
        while len(queue) > 0:
            first_item = queue.pop()
            print(first_item._value)
            if first_item._right is not None:
                queue.append(first_item._right)
            if first_item._left is not None:
                queue.append(first_item._left)

    def bfs(self):
        if self._root is None:
            return
        queue = [self._root]
        while len(queue) > 0:
            first_item = queue[0]
            print(first_item._value)
            if first_item._left is not None:
                queue.append(first_item._left)
            if first_item._right is not None:
                queue.append(first_item._right)
            del queue[0]

    def add(self, number):
        if self._root is None:
            self._root = Node(number)
            return

        current_node = self._root
        while True:
            if current_node._value < number:
                if current_node._right is None:
                    current_node._right = Node(number)
                    return
                else:
                    current_node = current_node._right
            else:
                if current_node._left is None:
                    current_node._left = Node(number)
                    return
                else:
                    current_node = current_node._left
        

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(5)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(1)
    tree.add(10)
    tree.add(11)
    #tree.dfs()
    tree.remove_root_node()
    tree.remove_root_node()
    tree.remove_root_node()
    tree.dfs()