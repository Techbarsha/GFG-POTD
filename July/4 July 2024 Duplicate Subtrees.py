class Solution:
    def printAllDups(self, root):
        # code here
        from collections import defaultdict
        
        def serialize(node, lookup, result):
            if not node:
                return "#"
            serial = "{},{},{}".format(node.data, serialize(node.left, lookup, result), serialize(node.right, lookup, result))
            lookup[serial].append(node)
            if len(lookup[serial]) == 2:
                result.append(node)
            return serial
        
        lookup = defaultdict(list)
        result = []
        serialize(root, lookup, result)
        result.sort(key=lambda x: x.data)
        return result
