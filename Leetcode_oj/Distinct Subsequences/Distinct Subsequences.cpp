/*  2015-2-15
Given a string S and a string T, count the number of distinct subsequences of T in S.
Here is an example:  S = "rabbbit", T = "rabbit"
*/
#include<iostream>
using std::cout;
using std::endl;

#include<string>
using std::string;

#include<vector>
using std::vector;

inline void disp(vector<vector<int>> &A){
	for (vector<int> i : A){
		for (int j : i){
			cout << j << " ";
		}
		cout << endl;
	}
}

class Solution {
public:

	// DP 
	// S = "rabbbit", T = "rabbit"
	// f(rabbbit,rabbit)=r+f(abbbit,abbit)
	// f(bbbit,bbit)=b+f(bbit,bit)
	// ACE ABCDE，
	// 借助背包问题的想法，（ABCDE）第i个元素（例如A放，B不放）要不要放进去

	int numDistinct_0(string S, string T) {

		int num_T = T.size(), num_S = S.size();
		//if (num_S < num_T){
		//	return 0;
		//}

		vector<vector<int>>  DP(num_T+1, vector<int>(num_S+1, 0));
		for (int i = 0; i < num_S ; ++i){        // S  //最后一个为0
			DP[0][i] = 1;
		}

		for (int j = 1; j < num_T+1; ++j){            // T
			for (int i = j; i < num_S+1; ++i){        // S
				if (T[j-1] == S[i-1]){ DP[j][i] = 1; }
			}
		}
		disp(DP);
		cout << endl;

		// 此方法需要递归的寻找路线，耗时很大
		//return is_the_way(DP, 0, 0, num_S); // 方法1，递归 ，递归到底，再回溯

		//可以换成 DP方法
		for (int j = num_T ; j > 0; --j){            // T
			int nn = 0;
			for (int i = num_S-(num_T-j) ; i > 0; --i){        // S
				nn += DP[j][i];
				if (DP[j - 1][i - 1] >= 1){
					DP[j - 1][i - 1] = nn;
				}
			}
		}
		cout << endl;
		disp(DP);
		/*
		if (DP.size() == 1){
			int res = 0;
			for (int i = 0; i < num_S; i++){
				res += DP[0][i];
			}
			return res;
		}
		else{
			for (int i = 0; i < num_S; i++){
				if (DP[0][i] != 0){
					return DP[0][i];
				}
			}
		}
		*/
		return DP[0][0];
		//return 0;
	}

	int is_the_way(vector<vector<int>> &DP, int i/*hang*/, int j/*lie*/, const int &n){
		int res = 0;
		if (i == DP.size() - 1){
			for (int k = j; k < n; ++k){
				if (DP[i][k] == 1){
					++res;
				}
			}
		}
		else{
			for (int k = j; k < n; ++k){
				if (DP[i][k] == 1){
					res += is_the_way(DP, i + 1, k + 1, n);
				}
			}
		}
		//cout <<"i:"<<i<<" j:"<<j<<" res:"<< res << endl;
		return res;
	}


	int numDistinct(string S, string T) {
		int num_T = T.size(), num_S = S.size();
		if (num_S < num_T) return 0;

		vector<vector<int>>  DP(num_T + 1, vector<int>(num_S + 1, 0));
		for (int i = 0; i < num_S; ++i){        // S，最后一个为0
			DP[0][i] = 1;
		}

		// DP
		for (int j = 1; j < num_T + 1; ++j){            // T
			for (int i = j; i < num_S + 1; ++i){        // S
				if (T[j - 1] == S[i - 1]){ DP[j][i] = 1; }
			}
		}
		//disp(DP); cout << endl;

		// 查表
		for (int j = num_T; j > 0; --j){                          // T
			int nn = 0;
			for (int i = num_S - (num_T - j); i > 0; --i){        // S
				nn += DP[j][i];
				if (DP[j - 1][i - 1] >= 1){
					DP[j - 1][i - 1] = nn;
				}
			}
		}
		disp(DP);
		return DP[0][0];
	}
};

int main(){
	Solution s;
	int r = s.numDistinct("rabbbit", "rabbit");
	//int r = s.numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa");
	//int r = s.numDistinct("bbb", "bb");
	//int r = s.numDistinct("", "a");
	//int r = s.numDistinct("bbb", "bbbb");
	cout << "r: " << r << endl;
}