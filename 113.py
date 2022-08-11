# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        
        def _pathSum(node, targetSum, result, results):   
            if not node:
                return
            if not node.left and not node.right:
                if targetSum == node.val:
                    results.append(result + [node.val])
            if node.left: 
                _pathSum(node.left, targetSum - node.val, result + [node.val], results)
            if node.right:
                _pathSum(node.right, targetSum - node.val, result + [node.val], results)
        
        _pathSum(root, targetSum, [], results)
        
        return results
