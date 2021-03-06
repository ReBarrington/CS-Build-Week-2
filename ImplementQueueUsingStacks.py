# https://leetcode.com/problems/implement-queue-using-stacks/submissions/

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.items.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.items.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.items[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.items) > 0:
            return False
        return True