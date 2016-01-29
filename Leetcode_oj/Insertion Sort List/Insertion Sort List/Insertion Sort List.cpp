/*
Definition for singly-linked list.
*/

#include<stdlib.h>
#include<iostream>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode *insertionSortList(ListNode *head);
};


ListNode * Solution::insertionSortList(ListNode *head)
{

	ListNode *h=head;
	if(h==NULL||h->next==NULL)
		return h;
	else	
	{
		int n=1;
		while (h->next!=NULL)
		{
			n++;
			h=h->next;
		}

		h=head;int ic=0;
		int *V=new int[n];
		while (h->next!=NULL)
		{
			V[ic]=h->val;
			h=h->next;
			ic++;
		};
		V[ic]=h->val;


		cout<<V[0]<<" "<<V[1]<<" ";

		for(int i=1;i<n;i++)
		{
			int k=V[i];
			int j=i-1;
			while(j>=0&&k<V[j])
			{
				V[j+1]=V[j];
				j--;
				V[j+1]=k;
			}
		}
		
		h=head;int j=0;
		while (h->next!=NULL)
		{
			h->val=V[j];
			j++;
			h=h->next;
		}
		h->val=V[j];

		return head;
	}
}

void main ()
{

	ListNode l1(15);
	ListNode l2(2);
	l1.next=&l2;

	ListNode *l=NULL;
	
	Solution s;
	l=s.insertionSortList(&l1);
	cout<<l->val<<" ";
	l=l->next;
	cout<<l->val<<endl;

	int i;
	cin>>i;

}