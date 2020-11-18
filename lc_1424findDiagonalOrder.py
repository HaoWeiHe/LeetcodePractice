class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        [[1,2,3], 
         [4,5,6],
         [7,8,9]]
         
         
        (0,0) / (1,0) (0,1) /  (2,0)(1,2)(0,2) / (2,1) (1,2) / (2,2)
         0            1          2                  3           4
        tuple = (sum,row, val)
        row max = len(nums) -1
        """
        tuples = []
    
        for i,row in enumerate(nums):
            for j in range(len(row)):
                tuples.append((i+j,i,j))
                
        sort_res = sorted(tuples, key = lambda (s,r,c): (s,-r))
        res =[]
        for ele in sort_res:
            s,i,j = ele
            res.append(nums[i][j] )
        return res
        