#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int reverse(int x) {
		vector<int> a;
		int y = 0;
		int sign = 1;
		if (x < 0){
			sign = -1;
			x = -x;
		}
		while (x / 10 != 0) {
			a.push_back(x % 10);
			x = x / 10;
		}
		a.push_back(x % 10);

		auto it = a.begin();
		for (; it != a.end();){
			cout << *it<<" ";
			++it;
		}

		while (!a.empty()) {
			y = a[0] + y * 10;
			vector<int>::iterator it=a.begin();
			a.erase(it);
		}
		return y*sign;
	}
};

int main(){
	Solution s ;
	int d=s.reverse(123);
	cout << d<<endl;
}