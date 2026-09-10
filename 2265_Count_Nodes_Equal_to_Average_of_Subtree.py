class Solution(object):
    def averageOfSubtree(self, root):
        self.matching_nodes_count = 0
        
        def dfs(node):
            if not node:
                return 0, 0 
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            if total_sum // total_count == node.val:
                self.matching_nodes_count += 1
                
            return total_sum, total_count

        dfs(root)
        return self.matching_nodes_count
