import heapq

class Node:
    def __init__(self, d, i, left=None, right=None):
        self.data = d          
        self.index = i         
        self.left = left
        self.right = right

def preOrder(root, ans, curr):
    if root is None:
        return

    # leaf node
    if root.left is None and root.right is None:
        ans.append(curr if curr else "0")
        return

    preOrder(root.left, ans, curr + "0")
    preOrder(root.right, ans, curr + "1")

class Solution:
    def huffmanCodes(self, s, freq):
        # code here
        # This code implemented by Barsha Saha
        n = len(s)
        pq = []
        for i in range(n):
            tmp = Node(freq[i], i)
            heapq.heappush(pq, (tmp.data, tmp.index, tmp))

        # single character case
        if n == 1:
            return ["0"]

        # build huffman tree
        while len(pq) >= 2:
            f1, i1, l = heapq.heappop(pq)
            f2, i2, r = heapq.heappop(pq)

            newNode = Node(
                l.data + r.data,
                min(l.index, r.index),
                l,
                r
            )

            heapq.heappush(pq, (newNode.data, newNode.index, newNode))

        root = pq[0][2]
        ans = []
        preOrder(root, ans, "")
        return ans
        
        
        
