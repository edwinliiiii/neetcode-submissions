# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
         given we are in a BST

         if p < node.val and q > node.val: WE ARE AT THE LCA!!!

         if p < node.val and q < node.val: ITER ON NODE.left

         if p > node.val and q > node.val: ITER ON NODE>RIGHT


        p = 3 q = 4         

        '''

        node = root

        while node and (p.val < node.val and q.val < node.val) or (p.val > node.val and q.val > node.val):
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
        
        return node





        '''
        recursion: 

        work on each node- am i an ancestor? answered by "looking for p and q"

        what that means: if p/q is lower    than current.val, call recursively on left
                         if p/q is greater  than current.val, call recursively on right

        base case: when to stop- if our value = p/q, return True (u are an ancestor!!!).
        
         when recursive call yields true on both sides, 
        '''