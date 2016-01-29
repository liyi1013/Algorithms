/* ����x^n
   2015-2-17
*/

#include<iostream>
using std::cout;
using std::endl;

class Solution {
public:
	double pow(double x, int n) {

		// ���ֲ���Ҫ��������
		if (n == 0||x==1){ return 1; }
		
		if (x == -1){
			if (n % 2 == 0)
				return 1;
			else
				return -1;}
		
		if (n == 1) return x;
		
		// ���ټ������
		if (n < 0){ 
			return 1/pow(x, -n); }
		else{
			if (n % 2 == 0){
				double res = pow(x, n / 2);
				return res*res;
			}
			else{
				double res = pow(x, (n - 1) / 2);
				return res*res*x;
			}
		}
	}
};


int main(){
	Solution s;
	cout << s.pow(8.88023, 3) << endl;
}