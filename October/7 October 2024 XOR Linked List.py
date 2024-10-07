nodes = dict()    
def insert(head, data):
    NEW = Node(data)
    NEW.npx = None
    nodes[id(NEW)] = NEW
    
    if head:
        NEW.npx = id(head)
        
        if head.npx:
            head.npx = id(NEW) ^ head.npx
        else:
            head.npx = id(NEW)
            
    return NEW

def getList(head):
    ans = []
    prvs = 0
    curr = head
    
    while curr:
        ans.append(curr.data)
        if curr.npx:
            npx = prvs ^ curr.npx
        else:
            break
        
        if npx not in nodes:
            break
        
        NEXT = nodes[npx]
        prvs = id(curr)
        curr = NEXT
        
    return ans
