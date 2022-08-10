class Tree:

    def __init__(self, elem=None):
        self.left = None
        self.right = None
        self.elem = elem

    def insert(self, elem):
        if not self.elem:
            self.elem = elem
        else:
            if elem < self.elem:
                if not self.left:
                    self.left = Tree(elem)
                else:
                    self.left.insert(elem)
            else:
                if not self.right:
                    self.right = Tree(elem)
                else:
                    self.right.insert(elem)

    def tree_search(self, x):
        if x < self.elem:
            if self.left is None:
                return False
            return self.left.tree_search(x)
        elif x > self.elem:
            if self.right is None:
                return False
            return self.right.tree_search(x)
        else:
            return True

    @staticmethod
    def minimum_tree(tree):
        while tree.left:
            tree = tree.left
        return tree.elem

    @staticmethod
    def maximum_tree(tree):
        while tree.right:
            tree = tree.right
        return tree.elem

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.elem, "->", end=' '),
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.elem, "->", end=' '),

    def print_preorder(self):
        print(self.elem, "->", end=' '),
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def max_depth(self, tree):
        if tree is None:
            return 0
        else:
            return 1 + max(self.max_depth(tree.left), self.max_depth(tree.right))

    def min_depth(self, tree):
        if tree is None:
            return 0
        else:
            return 1 + min(self.min_depth(tree.left), self.min_depth(tree.right))

    def is_balanced(self):
        return self.max_depth() - self.min_depth() <= 1


if __name__ == "__main__":
    root = Tree(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    print("Min Tree", root.minimum_tree(root))
    print("Max Tree", root.maximum_tree(root))
    print("Print Tree in order")
    print(root.print_inorder())
    val = 31
    if root.tree_search(val):
        print("{} is found".format(val))
    else:
        print("{} is not found".format(val))

    print("Max depth : {}".format(root.max_depth(root)))
    print("Min depth : {}".format(root.min_depth(root)))
