#include<stdlib.h>
#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

/* 
Problem: Max Points on a Line 
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
http://oj.leetcode.com/problems/max-points-on-a-line/
*/

//Definition for a point.
 struct Point {
     int x;
     int y;
     Point() : x(0), y(0) {}
     Point(int a, int b) : x(a), y(b) {}
 };

class Solution {
public:
    int maxPoints(vector<Point> &points);
};
/////////////////////////////////////////////

int Solution::maxPoints(vector<Point> &points)
{
	const int n=points.size();
	//const int n=4;
	double M[n][n];
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(i==j) 
				M[i][j]=-2;
			else {
				if((points[j].x==points[i].x))
				M[i][j]=-1;
				else
				M[i][j]=double(points[j].y-points[i].y)/(points[j].x-points[i].x);}
		} 
	}
	
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<M[i][j]<<"  ";
		} 
		cout<<endl;
	}
	
	double C[n];C[0]=0;
	for(int i=1;i<n;i++)
	{   int c=0;
		for(int j=0;j<=i;j++)
		{	int temp=1;
			for(int k=0;k<n;k++)
			{
				if(M[i][j]==M[i][k]&&k!=j) temp++;
			} 
			if (temp>c) c=temp;
		} 
		C[i]=c;
	}
	
	int MN=0;
	for(int i=0;i<n;i++)
	{
		if(C[i]>MN)
			MN=C[i];
	} 
	cout<<endl<<"number of Max Points on a Line is "<<MN+1;
	return MN+1;
}

int main()
{
	//vector<Point> points;//(3,10),(0,2),(0,2),(3,10)
	//points.push_back(Point(0,0));points.push_back(Point(1,1));
	//points.push_back(Point(2,2));points.push_back(Point(1,2));points.push_back(Point(6,6));points.push_back(Point(6,12));
	
	vector<Point> points={(3,10),(0,2),(0,2),(3,10)};
	
	
	Solution s;
	s.maxPoints(points);
	
	return 0;
}
