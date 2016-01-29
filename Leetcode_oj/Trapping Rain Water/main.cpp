#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    int trap(int A[], int n) {
    	if (n<3){
    		return 0;
    	}
    	stack<int> water_stack;
    	int begin=0;
    	int res=0;
    	for (int i =0;i<n;++i){
    		if (A[i]>0 && water_stack.empty()){
    			water_stack.push(A[i]);
    			begin=A[i];
    			continue;
    		}
    		if (A[i]<begin){
				water_stack.push(A[i]);
				continue;
    		}
    		if (A[i]>=begin && begin!=0){
    			while(!water_stack.empty()){
					cout<<"A"<<i<<": "<<A[i];
					cout<<" begin: "<<begin;
    				cout<<" top: "<<water_stack.top()<<endl;
    				
    				res+=begin-water_stack.top();
    				water_stack.pop();

    			}
				water_stack.push(A[i]);
				begin=A[i];
    		}
    		cout<<"res: "<<res<<endl;
    	}
    	int end=0;
    	while(!water_stack.empty()){
    		if(water_stack.top()>=end){
    			end=water_stack.top();
    			water_stack.pop();
    		}
    		else{
    			res+=end-water_stack.top();
    			water_stack.pop();
    		}
    	}
    	return res;
    }
};


int main(int argc, char** argv) {
	Solution s;
	int A[]={0,1,0,2,1,0,1,3,2,1,2,1};
	//int A[]={0,0,0,0};
	cout<<s.trap(A,12);
	return 0;
}
