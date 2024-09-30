#User function Template for python3


#Function to find the vertical width of a Binary Tree.
def verticalWidth(root):
    # code here
    if not root:
        return 0
    
    from collections import defaultdict, deque
    
    # Dictionary to store nodes at each vertical line
    vertical_map = defaultdict(list)
    
    # Using a deque for BFS
    queue = deque()
    queue.append((root, 0))  # (node, vertical line offset from root)
    
    # BFS traversal to fill vertical_map
    while queue:
        node, vertical_line = queue.popleft()
        
        # Store the current node in the vertical_map
        vertical_map[vertical_line].append(node.data)
        
        # Queue left child with decreased vertical line
        if node.left:
            queue.append((node.left, vertical_line - 1))
        
        # Queue right child with increased vertical line
        if node.right:
            queue.append((node.right, vertical_line + 1))
    
    # Calculate the number of unique vertical lines
    return len(vertical_map)
