#include <vector>
#include <array>
#include<iostream>
#include <string>
using namespace std;

class Solution {
public:
	bool isValidSudoku(vector<string>& board) {
		const int NUM_rows = 9;
		const int NUM_cols = 9;
		array<int, 10> nums = {0,0,0,0,0,0,0,0,0,0};

		// 判断每行
		for (size_t i = 0; i < NUM_cols; i++)
		{
			for (size_t j = 0; j < NUM_rows; ++j)
			{
				if (board[i][j] != '.'){
					++nums[board[i][j] - '0'];
				}
			}
			for (size_t k = 0; k < 10; k++)
			{
				if (nums[k] > 1){ return false; }
			}
			nums.fill(0);
		}
		// 判断每列
		for (size_t i = 0; i < NUM_cols; ++i)
		{
			for (size_t j = 0; j < NUM_rows; ++j)
			{
				if (board[j][i] != '.' ){
					++nums[board[j][i] - '0'];
				}
			}
			for (size_t k = 0; k < 10; k++)
			{
				if (nums[k] > 1){ return false; }
			}
			nums.fill(0);
		}
		// 判断每列
		for (size_t i = 0; i < NUM_cols; i+=3)
		{
			for (size_t j = 0; j < NUM_rows; j+=3)
			{
				for (size_t p = i; p < 3+i; ++p)
				{
					for (size_t q = j; q < 3+j; ++q)
					{
						if (board[p][q] != '.' ){
							++nums[board[p][q] - '0'];
						}
					}
				}
				for (size_t k = 0; k < 10; k++)
				{
					if (nums[k] > 1){ return false; }
				}
				nums.fill(0);
			}
		}
		return true;
	}
};

int main(){
	Solution s;
	vector<string> ss = {"..4...63.", ".........", "5......9.", "...56....", "4.3.....1", "...7.....", "...5.....", ".........", "........."};
	cout << s.isValidSudoku(ss);
	return 0;
}