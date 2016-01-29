#include<iostream>
using namespace std;
class Solution{
public:
	int search(int A[], int n, int target) {
		if (A[0] <= A[n - 1] & (target < A[0] || target > A[n - 1])) return -1;
		if (A[0] >= A[n - 1] & (target < A[0] & target > A[n - 1])) return -1;

		int mid = n/2;
		if (A[mid] == target) return mid;

		else{
			int is_in_array1 = search(&A[0], mid, target);
			int is_in_array2 = search(&A[mid], n-mid, target);
			if (is_in_array2 != -1) return is_in_array2 + mid;
			return is_in_array1;
		}
	}
};

int main(){
	int a[] = { 4, 5, 6, 7,9, 0, 1, 2 };
	Solution s;
	cout << s.search(a, 8, 1);
}