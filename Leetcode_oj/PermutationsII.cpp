#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
	vector<vector<int>> permuteUnique(vector<int>& nums) {

		vector<vector<int> > res;
		if (nums.size() < 1){
			return res;
		}

		if (nums.size() == 1){
			res.push_back({ nums[0] });
			return res;
		}

		sort(nums.begin(), nums.end());

		vector<int> num_rest(nums.begin() + 1, nums.end());
		vector<vector<int>> res_rest = this->permuteUnique(num_rest);
		for (unsigned int j = 0; j < res_rest.size(); ++j){

			res_rest[j].insert(res_rest[j].begin(), nums[0]);
			
			res.push_back(res_rest[j]);
		}

		for (unsigned int i = 1; i < nums.size(); ++i){
			if (nums[i] == nums[i - 1]){
				continue;
			}
			else{
				vector<int> num_rest = nums;
				num_rest.erase(num_rest.begin() + i);
				vector<vector<int>> res_rest = this->permuteUnique(num_rest);
				for (unsigned int j = 0; j < res_rest.size(); ++j){
					res_rest[j].insert(res_rest[j].begin(), nums[i]);
					res.push_back(res_rest[j]);
				}
			}
		}
		return res;
	}
};


int main(int argc, char const *argv[]){
	vector<int> nums = { 1, 1, 1, 2 };

	cout << __FILE__ << " " << __LINE__ << endl;

	Solution s;
	vector<vector<int> > res = s.permuteUnique(nums);

	for each (vector<int> res_i in res)
	{
		for each (int i in res_i)
		{
			cout << i << " ";
		}
		cout << endl;
	}

	return 0;
}