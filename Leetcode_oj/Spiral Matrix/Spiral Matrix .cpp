#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	vector<int> spiralOrder(vector<vector<int> > &matrix) {
		vector<int> res;
		int num_row = 0, num_column = matrix.size();
		if (num_column > 0){
			num_row = matrix[0].size();
			int row_begin = 0, row_end = num_row - 1;  // 行遍历
			int col_begin = 0, col_end = num_column - 1;// 列遍历
			while (row_begin <= row_end && col_begin <= col_end){ //一次循环执行一个逆时针 

				for (int i = row_begin; i <= row_end; ++i){
					res.push_back(matrix[col_begin][i]);
				}
				++col_begin;

				for (int j = col_begin; j <= col_end; ++j){
					res.push_back(matrix[j][row_end]);
				}
				--row_end;

				for (int i = row_end; i >= row_begin && (col_end >= col_begin); --i){
					res.push_back(matrix[col_end][i]);
				}
				--col_end;

				for (int j = col_end; j >= col_begin && (row_begin <= row_end); --j){
					res.push_back(matrix[j][row_begin]);
				}
				++row_begin;
			}
		}
		return res;
	}
};

int main(){
	Solution s;
	vector<vector<int>> m0 = { { 1, 2, 3, 4, 5 } };

	vector<vector<int>> m2 = { { 1, 2, 3 }, { 4, 5, 6 } };

	vector<vector<int>> m = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

	vector<vector<int>> m1 = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 }, { 13, 14, 15, 16 } };

	vector<vector<int>> mt = { { 3 }, { 2 }, { 8 } };

	vector<vector<int>> m3 = { { 1, 2 }, { 3, 4 } };

	vector<int> r = s.spiralOrder(m1);
	cout << endl << r.size() << endl;
	for each (int i in r)
	{
		cout << i << " ";
	}
	cout << endl;
	return 1;
}