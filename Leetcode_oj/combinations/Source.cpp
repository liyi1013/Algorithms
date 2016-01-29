#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	vector<vector<int> > combine(int n, int k) {
		vector<vector<int> > results;
		int num_res = 1;
		for (int i = 0; i < k; ++i){
			num_res *= (n - i);
			num_res /= (i+1);
		}
		//cout << num_res;
		// 以上为计算组合个数。

		// 方法1：计算出所有组合，剔除重复项(不写)

		// 方法2：k个取值指针，,,不行
		/*
		int *p = new int[k];
		for (int i = 0; i< k; ++i){
			p[i] = i+1 ;
		}
		int end = n;
		for (int i = k - 1; i >= 0; --i){
			while (p[i] < n){
				vector<int> r;
				for (int t = 0; t < k; ++t){
					r.push_back(p[t]);
				}
				results.push_back(r);
				++p[i];
			}
			--end;
		}
		delete p;*/

		// 方法3：递归
		if (k == 1){
			for (int i = 1; i < n + 1; ++i){
				results.push_back({ i });
			}
			return results;
		}
		else{
			for (int i = 0; i < n - k +1; ++i){

				vector<vector<int>> r = combine(n-i-1,k-1);
				/*
				for each (vector<int> v in r) // for each gai 
				{
					vector<int> t = { i + 1 };
					for each(int j in v){
						t.push_back(j + i+1);
					}
					results.push_back(t);
				}
				*/
				for (int v = 0; v < r.size(); ++v){
					vector<int> t = { i + 1 };
					for (int j = 0; j < r[v].size(); ++j){
						t.push_back(r[v][j] + i + 1);
					}
					results.push_back(t);
				}
			}
		}

		return results;
	}
};

void main(){
	Solution s;
	vector<vector<int> >res = s.combine(4, 2);
	for each (vector<int> i in res)
	{
		cout << "[ ";
		for each(int j in i){
			cout << j << " ";
		}
		cout << "]"<<endl;
	}
}