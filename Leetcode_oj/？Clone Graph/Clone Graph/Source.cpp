#include<unordered_map>
#include<vector>

using namespace std;

/* Definition for undirected graph.*/
struct UndirectedGraphNode {
	int label;
	vector<UndirectedGraphNode *> neighbors;
	UndirectedGraphNode(int x) : label(x) {};
};


class Solution {
	unordered_map<int, UndirectedGraphNode*> map;
public:

	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
		if (!node){
			return node;
		}
		else{
			return clone(node);
		}
	}

	UndirectedGraphNode *clone(UndirectedGraphNode *old_node) {
		auto p = map.find(old_node->label);
		if (p == map.end()){
			UndirectedGraphNode *new_node = new UndirectedGraphNode(old_node->label);
			map.insert({ new_node ->label,new_node});
			for (size_t i = 0; i < old_node->neighbors.size(); i++)
			{
				new_node->neighbors.push_back(clone( old_node->neighbors[i] ));
			}
		}
		else{
			return map[old_node->label];
		}
	}
};

void main(){

}