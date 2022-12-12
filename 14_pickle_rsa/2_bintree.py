import pickle


class TreeNode:

    def __init__(self, val=None, parent=None, l=None, r=None):
        self._val = val
        self._parent = parent
        self._l = l
        self._r = r

    def add(self, val):
        if self._val is None:
            self._val = val
            return True

        if val < self._val:
            if self._l is None:
                self._l = TreeNode(val, self)
                return True
            else:
                return self._l.add(val)
        elif val > self._val:
            if self._r is None:
                self._r = TreeNode(val, self)
                return True
            else:
               return self._r.add(val)

        return False

    def find(self, val):
        if val == self._val:
            return True
        if val < self._val and self._l is not None:
            return self._l.find(val)
        elif val > self._val and self._r is not None:
            return self._r.find(val)
        return False

    def delete(self, val):
        if self._val is None:
            return False

        if val == self._val:
            if self._parent is not None:
                if self._l is not None and self._r is None:
                    if val < self._parent._val:
                        self._parent._l = self._l
                    else:
                        self._parent._r = self._l
                elif self._r is not None and self._l is None:
                    if val < self._parent._val:
                        self._parent._l = self._r
                    else:
                        self._parent._r = self._r
                elif self._r is not None and self._l is not None:
                    node = self._r
                    while node._l is not None:
                        node = node._l
                    self._val = node._val
                    node.delete(node._val)
                else:
                    if val < self._parent._val:
                        self._parent._l = None
                    else:
                        self._parent._r = None
            else:
                if self._l is not None and self._r is None:
                    self.__dict__.update(self._l.__dict__)
                    self._parent = None
                elif self._r is not None and self._l is None:
                    self.__dict__.update(self._r.__dict__)
                    self._parent = None
                elif self._r is not None and self._l is not None:
                    node = self._r
                    while node._l is not None:
                        node = node._l
                    self._val = node._val
                    node.delete(node._val)
                else:
                    self._val = None
            return True
        if val < self._val:
            return self._l.delete(val)
        elif val > self._val:
            return self._r.delete(val)
        return False


    def __iter__(self):
        yield self
        if self._l is not None:
            for subtree in self._l:
                yield subtree
        if self._r is not None:
            for subtree in self._r:
                yield subtree


    def __str__(self):
        return str(sorted([node._val for node in self]))

if __name__ == "__main__":
    tree = TreeNode()
    try:
        with open('tree.pickle', 'rb') as f:
            data = pickle.load(f)
            if data is not None:
                tree = data
            print("Loaded tree from file")
    except FileNotFoundError:
        print("Created empty tree")
    except ValueError:
        print("Tree file was damaged. Created empty tree")
    while (cmd := input()) != "exit":
        if cmd.startswith("add"):
            val = int(cmd.split()[1])
            print(tree.add(val))
        elif cmd.startswith("find"):
            val = int(cmd.split()[1])
            print(tree.find(val))
        elif cmd.startswith("delete"):
            val = int(cmd.split()[1])
            print(tree.delete(val))
        elif cmd == "print":
            print(tree)
        elif cmd == "clear":
            tree = TreeNode()
        elif cmd == "dump":
            with open('tree.pickle', 'wb') as f:
                pickle.dump(tree, f, pickle.HIGHEST_PROTOCOL)
