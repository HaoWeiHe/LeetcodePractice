class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        while(self.s1):
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
        
        #can improve code here
        while(self.s2):
            self.s1.append(self.s2.pop())     
        
        return res
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        
        return self.s1[0]
        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.s1) > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()