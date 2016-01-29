//http://oj.leetcode.com/problems/merge-intervals/
//Given a collection of intervals, merge all overlapping intervals.
//For example,
//Given[1, 3], [2, 6], [8, 10], [15, 18],
//return[1, 6], [8, 10], [15, 18].

#include<vector>
#include<iostream>
#include   <algorithm> 
using namespace std;

//* Definition for an interval.
struct Interval {
	int start;
	int end;
	Interval() : start(0), end(0) {}
	Interval(int s, int e) : start(s), end(e) {}
};

//�Զ���������
bool   lessmark(const   Interval&   s1, const   Interval&   s2)
{
	return   s1.start   <   s2.start;
}

class Solution {
public:
	vector<Interval> merge(vector<Interval> &intervals) {
		if (intervals.empty() || intervals.size()==1)
			return intervals;
		else
		{
			//  �ݹ��𲻵�������������á���Ե��������ȡ
			//	for (int i = 0; i < intervals.size()-1; i++)//ѭ���Ļ���Ҫ�ϲ�Ԫ�أ�x

			sort(intervals.begin(), intervals.end(), lessmark);   //��������

			//�����Ѿ���strat��С�ź���
			vector<Interval> d; int j = 0;
			d.push_back(intervals[0]);
			for (int i = 1; i < intervals.size(); i++)
			{
				if (d[j].end >= intervals[i].start)
				{
					if (d[j].end <= intervals[i].end)
					{
						d[j].end = intervals[i].end;
					}
				}
				else
				{
					d.push_back(intervals[i]);
					j++;
				}
			}
			intervals.clear();
			return d;
		}
	}

	//Interval merge2(Interval x, Interval y)
	//{
	//	Interval d(0,0);
	//	//СȡС����ȡ��
	//	x.start <= y.start ? d.start = x.start : d.start = y.start;
	//	x.end >= y.end ? d.end = x.end : d.end = y.end;
	//	return d;
	//}
};


void main()
{
	vector<Interval> X1 = { { 1, 3 } };
	vector<Interval> x2 = { { 1, 4 }, { 0 , 4 }, { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };

	Solution s;
	vector<Interval> d2=s.merge(x2);

	for each (Interval i in d2)
	{
		cout << i.start << " " << i.end << endl;
	}
}