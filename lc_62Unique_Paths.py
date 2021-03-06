class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.mem = {}
        def f(x,y):
            if x < 0 or y < 0: return 0
            if x ==1 and y ==1:return 1
            if (x,y) in self.mem:
                return self.mem[(x,y)]
         
            self.mem[(x,y)] = f(x-1,y) + f(x,y-1)
            return self.mem[(x,y)]
        return f(m,n)