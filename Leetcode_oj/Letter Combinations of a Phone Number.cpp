#include<iostream>
#include<vector>
#include<string>
//#include "boost/lexical_cast.hpp" // 需要包含的头文件
using namespace std;

void disp(vector<string> &s){
    for(string ss : s){
        cout<<ss<<" ";
    }
    cout<<endl;
}

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        int length_digits=digits.size();
        if(length_digits<=1){
          res=num_let(digits);
        }
        else{
          vector<string> r=num_let(digits.substr(0,1));
          string sub_str=digits.substr(1);
          vector<string> temp_res=letterCombinations(sub_str);
          for(string s:r){
            for(string ss: temp_res){
              res.push_back(s+ss);
            }
          }
        }
        return res;
    }
    vector<string> num_let(string digit){
      int n=atoi(digit.c_str());
      //int n=boost::lexical_cast<int>(digit);
      switch (n) {
        case 2:
          return {"a","b","c"};
          break;
        case 3:
          return {"d","e","f"};
          break;
        case 4:
          return {"g","h","i"};
          break;
        case 5:
          return {"j","k","l"};
          break;
        case 6:
          return {"m","n","o"};
          break;
        case 7:
          return {"p","q","r","s"};
          break;
        case 8:
          return {"t","u","v"};
          break;
        case 9:
          return {"w","x","y","z"};
        default:
          return {""};
          break;
      }
    }

};

int main(){
    Solution s;
    vector<string> r1=s.letterCombinations("22");
    disp(r1);
    //vector<string> r=s.num_let();
    //disp(r);
    return 1;
}

