import sys

class Solution(object):
    def __init__(self):
        self.shelfWidth = 0
        self.memo = {}

    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        self.shelfWidth = shelfWidth
        remainingW = shelfWidth

        return self.solve(books, 0, remainingW, 0)

    def solve(self, books, i, remainingW, maxH):
        if (i >= len(books)):
            return maxH
        
        if (i, remainingW) in self.memo.keys():
            return self.memo[(i, remainingW)]
        
        bookW = books[i][0]
        bookH = books[i][1]

        keepH = sys.maxsize
        skipH = sys.maxsize

        if bookW <= remainingW:
            keepH = self.solve(books, i+1, remainingW-bookW, max(maxH, bookH))
        
        skipH = maxH + self.solve(books, i+1, self.shelfWidth-bookW, bookH)

        self.memo[(i, remainingW)] = min(keepH, skipH)
        return self.memo[(i, remainingW)]

solution = Solution()
assert solution.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4) == 6
assert solution.minHeightShelves([[1,3],[2,4],[3,2]], 6) == 4
