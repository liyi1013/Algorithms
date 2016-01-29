# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    d=dict()
    def clone(self, old_node):
        if(old_node.label in self.d):
            return self.d[old_node.label]
        else:
            new_node=UndirectedGraphNode(old_node.label)
            self.d[new_node.label]=new_node
            for i in old_node.neighbors:
                new_node.neighbors.append(self.clone(i))
            return new_node

    def cloneGraph(self, node):
        if node == None:
        	return node
        else:
            return self.clone(node)

if __name__ == '__main__':
    s=Solution()
    root=UndirectedGraphNode(-1)
    r1=UndirectedGraphNode(1)
    r2=UndirectedGraphNode(3)
    root.neighbors.append(r1)
    r1.neighbors.append(root)

    node=s.cloneGraph(root)
    print node.label
    for i in node.neighbors:
        for j in i.neighbors:
            print j.label
        print i.label