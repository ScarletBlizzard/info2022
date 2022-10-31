class BinTree:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

    def __iter__(self):
        yield self
        if self.l is not None:
            for subtree in self.l:
                yield subtree
        if self.r is not None:
            for subtree in self.r:
                yield subtree

    def get_root_value(self):
        return self.val


if __name__ == "__main__":
    tree = BinTree(
            0,
            BinTree(1, BinTree(3), BinTree(4)),
            BinTree(2, BinTree(5), BinTree(6))
    )
    for subtree in tree:
        print(subtree.get_root_value())
