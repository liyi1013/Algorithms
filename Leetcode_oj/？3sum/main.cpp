// 3sum
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {

		unordered_multiset<int> set;
		int target = 0;
		vector<vector<int> > res;

		//sort(num.begin(), num.end());

		for (int i : num){
			set.insert(i);
		}
		for (auto i = num.begin(); i != num.end(); ++i){
			target -= *i;
			auto f = set.find(*i);
			if(f!=set.end()) set.erase(f);
			auto j = i;
			++j;
			for (; j != num.end(); ++j){
				auto f = set.find(*j);
				if (f != set.end()) set.erase(f);
				auto k=set.find(target - *j);
				if (k != set.end()){
					vector < int > r = { *i, *j, *k };
					sort(r.begin(),r.end());
					res.push_back(r);
				}
				//set.insert(*j);
			}
			target = 0;
		}
		return res;
    }
};

int  main(){
	vector<int> s{7, -1, 14, -12, -8, 7, 2, -15, 8, 8, -8, -14, -4, -5, 7, 9, 11, -4, -15, -6, 1, -14, 4, 3, 10, -5, 2, 1, 6, 11, 2, -2, -5, -7, -6, 2, -15, 11, -6, 8, -4, 2, 1, -1, 4, -6, -15, 1, 5, -15, 10, 14, 9, -8, -6, 4, -6, 11, 12, -15, 7, -1, -9, 9, -1, 0, -4, -1, -12, -2, 14, -9, 7, 0, -3, -4, 1, -2, 12, 14, -10, 0, 5, 14, -1, 14, 3, 8, 10, -8, 8, -5, -2, 6, -11, 12, 13, -7, -12, 8, 6, -13, 14, -2, -5, -11, 1, 3, -6};
	Solution t;
	vector<vector<int> > r=t.threeSum(s);
	for (vector<int> vi : r){
		for (int i : vi){
			cout << i << " ";
		}
		cout << endl;
	}
	return 0;
}