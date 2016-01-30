/*
liyi 2016-01-30

https://leetcode.com/problems/coin-change/

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
*/
#ifndef _COINCHANGE
#define _COINCHANGE

#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

template<class T> void display(vector<T> A) {
    for (T var : A) {
        cout << var << " ";
    }
    cout << endl;
}

class Solution {
 public:
    int coinChange(const vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, -1);
        dp[0] = 0;

        for (int i = 1; i <= amount ; i++) {
            for (int c: coins) {
                if (i == c) {
                    dp[i] = 1;
                } else if (i > c && dp[i-c] > 0) {
                    if (dp[i] > 0) {
                        dp[i] = dp[i] < (dp[i - c] + 1) ? dp[i] : dp[i - c] + 1;
                    } else {
                        dp[i] = dp[i - c] + 1;
                    }
                }
            }
        }
        //display(dp);
        return dp[amount];
    }
};


int main(int argc, char const *argv[]) {
    Solution s;
    vector<int> coins = {1,5,6,10};// { 186, 419, 83, 408 };
    int amount = 11;
    cout <<"counts: "<< s.coinChange(coins, amount) << endl;
    return 0;
}

/*
@11

coins:  - - - - - 5 6 - - - 10 11
amount: 0 1 2 3 4 5 6 7 8 9 10 11
dp:     0 - - - - 1 1 - - -  2  2

@6:  min{(dp[5]+dp[1]),(dp[6])}
@10: min{(dp[1])}


*/
/*
@11
coins:  - 1 - - -  5    6 - - - 10
amount: 0 1 2 3 4  5    6 7 8 9 10
dp:     0 1 2 3 4 {5,1}


dp[i]= iÔªÇ®×îÉÙµÄ×éºÏÊý
dp[i+1] = min:{1,c=i+1},{dp[i+1-c]+1,´æÔÚc<i+1&&dp[i+1-c]>=0},{-1;ËùÓÐc>i+1}
*/
#endif  //  _COINCHANGE
