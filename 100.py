def isSameTree(self, p, q):
        if not p and not q:
            return True
        if q and not p or p and not q:
            return False
        if p.val != q.val:
            return False
        if not p.left and not p.right and not q.left and not q.right and p.val == q.val:
            return True
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
