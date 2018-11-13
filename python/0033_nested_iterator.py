# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        i = self.list.pop(-1)
        return i.getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.list:
            return False
        
        i = self.list[-1]
        while True:
            if i.isInteger():
                return True
            
            l = i.getList()
            self.list.pop(-1)
            if not l:
                if not self.list:
                    return False
            else:
                self.list.extend(l[::-1])
            i = self.list[-1]