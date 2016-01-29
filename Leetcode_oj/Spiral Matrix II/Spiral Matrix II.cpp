#include<vector>
using std::vector;
#include<iostream>
using std::cout;
using std::endl;


class Solution {
public:
	vector<vector<int> > generateMatrix(int n) {
		vector<vector<int> > res = vector<vector<int> >(n, vector<int>(n, 0));

		int num_row = 0, num_column = res.size();
		if (num_column > 0){
			num_row = res[0].size();
			int k = 0;
			int row_begin = 0, row_end = num_row - 1;  // 行遍历
			int col_begin = 0, col_end = num_column - 1;// 列遍历
			while (row_begin <= row_end && col_begin <= col_end){

				for (int i = row_begin; i <= row_end; ++i){

					res[col_begin][i]=(++k);
				}
				++col_begin;

				for (int j = col_begin; j <= col_end; ++j){

					res[j][row_end] = (++k);
				}
				--row_end;

				for (int i = row_end; i >= row_begin && (col_end >= col_begin); --i){

					res[col_end][i] = (++k);
				}
				--col_end;

				for (int j = col_end; j >= col_begin && (row_begin <= row_end); --j){

					res[j][row_begin] = (++k);
				}
				++row_begin;
			}
		}
		return res;
	}
};

int main(){
	Solution s;
	vector<vector<int> > r = s.generateMatrix(5);

	for each (vector<int> v in r)
	{
		for each (int i in v)
		{
			cout << i << " ";
		}
		cout << endl;
	}
}