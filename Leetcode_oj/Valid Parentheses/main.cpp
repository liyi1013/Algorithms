#include <iostream>
#include<string>
#include<unordered_set>
#include<stack>
using namespace std;


class Solution {
public:
    bool isValid(string s) {
        if(s.empty()){
			return false;
		}
		unordered_set<char> mappair_right={')',']','}'};
		auto search = mappair_right.find(s[0]);
		if(search != mappair_right.end()) {
			return false;
		}
		int len_s=s.length();
		if(len_s%2==1){
			return false;
		}
		
		stack<char> mystack;
		mystack.push(s[0]);
		int i=1;
		while(i<len_s){
			char second=mystack.top();
			mystack.push(s[i]);
			int num=mystack.size();
			if (num>1){
				if(isPair(&mystack.top(),&second)){
					mystack.pop();
					mystack.pop();
				}
			++i;
			}
		num=mystack.size();
		if(num>0)
			return false;
		else
			return true; 
		}
    }
    
    bool isPair(char *a,char *b){
    	if ((*a=='(' && *b==')')|| (*b=='(' && *a==')'))
    		return true;
    	if ((*a=='[' && *b==']')|| (*b=='[' && *a==']'))
    		return true;
    	if ((*a=='{' && *b=='}')|| (*b=='{' && *a=='}'))
    		return true;
    	else
    		return false;
    }
};

int main(int argc, char** argv) {
	Solution s;
	string ss;
	cin>>ss;
	cout<<s.isValid(ss)<<endl;
	return 0;
}
