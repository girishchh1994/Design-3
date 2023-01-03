# T.C: For next()-> O(1)
#      For hasNext()-> worst case: O(h) where h is the max depth of the recursion. Avg case it will be O(1)
# S.C: For next()-> O(1)
#      For hasNext()-> O(h) where h is the max depth of the recursion

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = []
        self.st.append(iter(nestedList))
        self.ne = None
        
    
    def next(self) -> int:
        return self.ne
        
    
    def hasNext(self) -> bool:
        while self.st:
            val = next(self.st[-1],None)
            if not val:
                self.st.pop()
            elif val.isInteger():
                self.ne = val
                return True
            else:
                self.st.append(iter(val.getList()))
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
