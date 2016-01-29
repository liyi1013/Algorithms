#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        string res(num1.size()+num2.size(),'0');
        for (int i = num1.size()-1; i >=0 ; --i){
            int carry=0;
            for (int j = num2.size()-1; j >=0 ; --j)
            {
                int temp=(res[i+j+1]-'0')+(num1[i]-'0')*(num2[j]-'0')+carry;
                res[i+j+1]=temp%10+'0';
                carry=temp/10;
            }
            res[i]+=carry;
        }
        cout<<res<<endl;
        int begin=0;
        for (int i = 0; i < res.size(); ++i)
        {
            begin=i;
            if(res[i]!='0'){
                break;
            }
        }
        return res.substr(begin,res.size()-begin);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout<<s.multiply("0","0")<<endl;
    cout<<13*25;
    return 0;
}