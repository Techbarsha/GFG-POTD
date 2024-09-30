def LeftView(root):
    
    # code edutech barsha
    view, queue = [], [root] if root else []
    while queue:
        view.append(queue[0].data)
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return view
