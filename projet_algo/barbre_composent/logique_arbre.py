class BTreeNode:
    def __init__(self, t):
        self.t = t  
        self.keys = [] 
        self.children = []  
        self.leaf = True 

    def is_full(self):
        return len(self.keys) == 2 * self.t - 1

    def split(self, parent, index):
        """Divise le nœud actuel et ajuste le parent."""
        new_node = BTreeNode(self.t)
        mid_index = len(self.keys) // 2
        split_key = self.keys[mid_index]

        new_node.keys = self.keys[mid_index + 1:]
        self.keys = self.keys[:mid_index]

        if not self.leaf:
            new_node.children = self.children[mid_index + 1:]
            self.children = self.children[:mid_index + 1]
            new_node.leaf = False

        parent.keys.insert(index, split_key)
        parent.children.insert(index + 1, new_node)

    def insert_non_full(self, key):
        """Insère une clé dans un nœud non plein."""
        if self.leaf:
            self.keys.append(key)
            self.keys.sort()
        else:
            index = len(self.keys) - 1
            while index >= 0 and key < self.keys[index]:
                index -= 1
            index += 1

            if self.children[index].is_full():
                self.children[index].split(self, index)
                if key > self.keys[index]:
                    index += 1

            self.children[index].insert_non_full(key)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def insert(self, key):
        if self.root.is_full():
            new_root = BTreeNode(self.t)
            new_root.children.append(self.root)
            new_root.leaf = False
            self.root.split(new_root, 0)
            self.root = new_root

        self.root.insert_non_full(key)
