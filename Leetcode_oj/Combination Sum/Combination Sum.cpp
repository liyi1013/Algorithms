#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:

	vector<vector<int> > combinationSum_in(vector<int> &candidates, int target) {
		vector<vector<int> > res;
		if (candidates.size() <= 0 || target < candidates[0]){
			return res;
		}
		for (int i = 0; i < candidates.size(); ++i){

			vector<int>::iterator it = candidates.begin();// 选出后面的candidate，这样就不要剔除结果中的重复项；
			for (int k = 0; k < i; ++k) ++it;             // 若 combinationSum_in(candidates, target - candidates[i]);
			vector<int> candi(it,candidates.end());       // 则最后要剔除重复项

			vector<vector<int> > res_temp = combinationSum_in(candi, target - candidates[i]);
			if (!res_temp.empty()){
				for (int j = 0; j < res_temp.size(); ++j){
					
					//res_temp[j].push_back(candidates[i]);       // 在前面插入 与 查到最后面再排序 运行使时间差不多
					//sort(res_temp[j].begin(), res_temp[j].end());
					
					res_temp[j].insert(res_temp[j].begin(), candidates[i]);

					res.push_back(res_temp[j]);
				}
			}
			else if (target == candidates[i]){
				res.push_back({ target });
			}
		}
		return res;
	}

	vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
		sort(candidates.begin(), candidates.end());
		vector<vector<int> > res = combinationSum_in(candidates, target);
		return res;
	}

};


int main(){
	Solution s;
	//vector<int> candidates = {92, 71, 89, 74, 102, 91, 70, 119, 86, 116, 114, 106, 80, 81, 115, 99, 117, 93, 76, 77, 111, 110, 75, 104, 95, 112, 94, 73};
	vector<int> candidates = { 2,3,6,7 };
	vector<vector<int> > r = s.combinationSum(candidates, 7);
	
	// output:{[2,2,3],[7]}
	// f([2,3,6,7],7)={{2+f([2,3,6,7],5)},{3+f([3,6,7],4)},{6+f([6,7],1)},{7+f([7],0)}}

	//cout << "--------------------------------" << endl;
	for each (vector<int> v in r)
	{
		for each (int i in v)
		{
			cout << i << " ";
		}
		cout << endl;
	}
}