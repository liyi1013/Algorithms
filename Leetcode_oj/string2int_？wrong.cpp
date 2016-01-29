#include <iostream>
#include <iomanip>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
    	int res=0;
    	int d=1;
    	int i=0;
    	for (; i < str.size(); ++i)
    	{
    		if (str[i]==' ')
        		continue;
        	else
        		break;
    	}
    	if(str[i]=='-'){d=-1;++i;}
    	else if(str[i]=='+'){++i;}
        for (; i < str.size(); ++i)
        {
        	int r=(str[i]-'0');
        	if(r>9 ||r<0 ){
        		break;
        	}else{
        		res=res*10+r;
                if(res >= INT_MAX/10){
                    if(i+1 < str.size()){
                        r=(str[i+1]-'0');
                        if(r>9 ||r<0 ){
                            break;
                        }else{
                            if(d==1&& r>=7){return INT_MAX;}
                            else{return d*(res*10+r);}
                            if(d==-1&&r>=8){return INT_MIN;}
                            else{return d*(res*10+r);}
                        }
                    }
                }
        	}
        }
        return int(res*d);
    }
};
int main()
{
	Solution s;
	//cout<<"   "<<s.myAtoi("2147483648")<<endl;
	//cout<<"  "<<s.myAtoi("-2147483647")<<endl;
    //cout<<"  "<<s.myAtoi("-21474899999")<<endl;
    cout<<"  "<<s.myAtoi("      -11919730356x")<<endl;

	cout<<"max: "<<INT_MAX<<endl;
	cout<<"min:"<<INT_MIN;
}