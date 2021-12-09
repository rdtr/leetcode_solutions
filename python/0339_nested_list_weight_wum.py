# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

from collections import deque


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        sumVal = 0
        que = deque([])
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                sumVal += nestedInteger.getInteger()
            else:
                que.extend([(2, elm) for elm in nestedInteger.getList()])

        while que:
            depth, nestedInteger = que.popleft()
            if nestedInteger.isInteger():
                sumVal += nestedInteger.getInteger() * depth
            else:
                que.extend([(depth + 1, elm) for elm in nestedInteger.getList()])

        return sumVal



