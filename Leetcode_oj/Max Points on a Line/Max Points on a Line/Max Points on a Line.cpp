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
	 if(points.empty())
		 return 0;
	 else
	 {
		 int n=points.size();

		 double **M=new double*[n];       //分配一个指针数组，将其首地址保存在b中                                                    
		 for(int i=0;i<n;i++)             //为指针数组的每个元素分配一个数组
			 M[i]=new double[n];


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

		 double *C=new double[n];C[0]=0;
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
		 cout<<MN+1;
		 for(int i=0;i<n;i++)
		 {
			 delete []M[i];
			 M[i]=NULL;
		 }
		 delete []M;
		 M=NULL;

		 delete []C;

		 return MN+1;
	 }
 }

int main()
{
	//vector<Point> points;//(3,10),(0,2),(0,2),(3,10)
	//points.push_back(Point(0,0));
	//points.push_back(Point(1,1));points.push_back(Point(1,-1));//points.push_back(Point(1,2));points.push_back(Point(9,9));
	
	vector<Point> points={(3,10),(0,2),(0,2),(3,10)};

	Solution s;
	s.maxPoints(points);
	
	int f;
	cin>>f;
	return 0;
}