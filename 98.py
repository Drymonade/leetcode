class Solution: 
    def isValidBST(self, root):
        def _check(root, _min, _max):
            if not root.left and not root.right:
                if _min is not None and _max is not None:
                    return root.val > _min and root.val < _max
                if _min is not None:
                    return root.val > _min
                if _max is not None:
                    return root.val < _max
                return True
                
            if not root.left:
                if root.right.val <= root.val:
                    return False
                return _check(root.right, root.val, _max)

            if not root.right:
                if root.left.val >= root.val:
                    return False
                return _check(root.left, _min, root.val)

            if root.left.val >= root.val or root.right.val <= root.val:
                return False

            return _check(root.left, _min, root.val) and _check(root.right, root.val, _max)

        return _check(root, None, None) 
