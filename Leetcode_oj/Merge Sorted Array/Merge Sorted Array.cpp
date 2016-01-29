#include<iostream>

class Solution {
public:
	void merge(int A[], int m, int B[], int n) {

		int i = n, j = 0;
		int k = 0;
		if (m == 0){
			while (j < n){
				A[k++] = B[j++];
			}
		}
		else if (n == 0){
			while (i < m){
				A[k++] = A[i++];
			}
		}
		else{

			for (k = n + m - 1; k > 0; --k){
				A[k] = A[k - n];
			}// 必须从后往前，从前往后有错误

			//for (size_t i = 0; i < n + m; ++i)
			//{
			//	std::cout << A[i] << " ";
			//}
			//std::cout << std::endl;

			k = 0;
			while (i < n + m && j < n){
				if (A[i] < B[j]){
					A[k++] = A[i++];
				}
				else{
					A[k++] = B[j++];
				}
			}
			while (i < n + m){
				A[k++] = A[i++];
			}
			while (j < n){
				A[k++] = B[j++];
			}
		}
	}

	void merge2(int A[], int m, int B[], int n) {
		int i = n, j = 0;
		int k = 0;
		for (k = n + m - 1; k > 0; --k){
			A[k] = A[k - n];
		}// 必须从后往前，从前往后有错误

		//for (size_t i = 0; i < n + m; ++i)
		//{
		//	std::cout << A[i] << " ";
		//}
		//std::cout << std::endl;

		k = 0;
		while (i < n + m && m != 0 && j < n){
			if (A[i] < B[j]){
				A[k++] = A[i++];
			}
			else{
				A[k++] = B[j++];
			}
		}
		while (i < n + m && m != 0){
			A[k++] = A[i++];
		}
		while (j < n){
			A[k++] = B[j++];
		}
	}
};


int main(){
	Solution s;
	const int m = 0, n = 5;
	int a[m + n] = {};
	int b[n] = { 1, 2, 3, 4, 5 };
	s.merge2(a, m, b, n);

	for (size_t i = 0; i < n + m; ++i)
	{
		std::cout << a[i] << " ";
	}
}