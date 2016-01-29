#include<iostream>
#include<vector>
using namespace std;

void disp(vector<int> a){
	for each (int i in a)
	{
		cout << i << " ";
	}
	cout << endl;
}

class Solution {
public:
	vector<int> plusOne(vector<int> &digits) {
		if (digits[digits.size() - 1] == 9){
			int d = 1;
			for (int i = digits.size() - 1; i >= 0; --i){
				digits[i] += d;
				d = digits[i] / 10;
				digits[i] %= 10;
			}
			if (d == 1){
				digits.push_back(0);
				for (int i = digits.size() - 1; i > 0; --i){
					digits[i] = digits[i-1];
				}
				digits[0] = 1;
			}
		}
		else{
			digits[digits.size() - 1] += 1;
		}
		return digits;
	}
};


void main(){
	vector<int> v = { 1, 9, 9 };
	Solution s;
	s.plusOne(v);
	disp(v);
}