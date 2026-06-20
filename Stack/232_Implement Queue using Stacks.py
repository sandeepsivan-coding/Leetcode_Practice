class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x):
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())

        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        x=self.stack1[-1]
        self.stack1.pop()
        return x

        """
        :rtype: int
        """
        

    def peek(self):
        return self.stack1[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.stack1)==0

        """
        :rtype: bool
        """
        