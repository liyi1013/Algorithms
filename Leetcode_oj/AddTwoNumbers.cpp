#include<iostream>
using namespace std;

// * Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};


void disp(ListNode *head){
	while(head!=NULL){
		cout<<head->val<<" ";
		head=head->next;
	}
	cout<<endl;
}
 
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    	int d=0;
    	ListNode *res=new ListNode(0);
    	ListNode *head=res;
    	while(l1&&l2){
    		int added=l1->val+l2->val+d;
    		res->next=new ListNode(added%10);
    		d=added/10;
    		res=res->next;
            l1=l1->next;
            l2=l2->next;
    	}
    	while(l1){
    		int added=l1->val+d;
    		res->next=new ListNode(added%10);
    		d=added/10;
    		res=res->next;
            l1=l1->next;
    	}
    	while(l2){
    		int added=l2->val+d;
    		res->next=new ListNode(added%10);
    		d=added/10;
    		res=res->next;
            l2=l2->next;
    	}
    	if(d==1){
    		res->next=new ListNode(d);
    	}
        return head->next;
    }
};

int main(){
	ListNode l1(1),l12(2),l13(1),l14(1);
	l1.next=&l12;l12.next=&l13;l13.next=&l14;

	ListNode l2(1),l22(2),l23(1),l24(9);
	l2.next=&l22;l22.next=&l23;l23.next=&l24;

	disp(&l1);
    disp(&l2);
	Solution s;
	disp(s.addTwoNumbers(&l1,&l2));
	return 1;
}