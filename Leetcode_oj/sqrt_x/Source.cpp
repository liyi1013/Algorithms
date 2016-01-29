#include <iostream>
#include <math.h>
using namespace std;


class Solution {
public:
	int sqrt(int x) {
		double x0 = 1;
		double y0 = 1 - x ;
		double z = x0 - y0 / 2*x0;
		while (abs(y0)>0.3 ){
			y0 = x0*x0 - x;
			z = x0 - y0/(2*x0);
			x0 = z;
			cout << z << endl;
		}
		return int(x0);
	}
};


int main()
{
	Solution s;
	cout << s.sqrt(2147395599);
}