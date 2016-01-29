#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
	vector<string> fullJustify(vector<string> &words, int L) {
		if (words.empty() || L < 1)
			return words;
		else
		{
			vector<string> s;
			while (!words.empty())
			{
				for (int i = 0; i < L / 2; i++){}
				string t;
				auto b = s.begin();
				do { t = t + *b; } while (t.length < 16);
			}
		}
	}
};