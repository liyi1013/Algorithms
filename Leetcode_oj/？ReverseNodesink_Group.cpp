#include <iostream>
using namespace std;

//* Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

void disp_listNode(ListNode *head){
	while(head!=NULL){
		cout<<head->val<<" ";
		head=head->next;
	}
	cout<<endl;
}
class Solution {
public:
	// 1->2->3->4->5->...
	// put 3 to head => 3->1->2->4->5->...
    ListNode *reverseKGroup(ListNode *head, int k) {
        if(k<=1||head==NULL){return head;}
        ListNode *h_temp=head;
        int num_node=0;
        while(h_temp!=NULL){
        	++num_node;
        	h_temp=h_temp->next;
        }
        cout<<num_node;
        if(num_node<k){return head;}


        ListNode *h=head;
        ListNode *current=head;
        ListNode *node=head->next;
        disp_listNode(h);
        //cout<<"h: "<<h->val<<". current:"<<current->val<<". node:"<<node->val<<endl;
        for(int i=1;i<k&&node!=NULL;++i){
        	current->next=node->next;
        	node->next=h;
        	h=node;
        	//current=current->next;
        	node=current->next;

        	//disp_listNode(h);
        	//cout<<"h: "<<h->val<<". current:"<<current->val<<". node:"<<node->val<<endl;
        }
        return h;
    }
};

int main(){
	Solution s;
	ListNode l1(1),l2(2),l3(3),l4(4),l5(5);
	l1.next=&l2;l2.next=&l3;l3.next=&l4;l4.next=&l5;
	//disp_listNode(&l1);
	ListNode *r=s.reverseKGroup(&l1,10);
	disp_listNode(r);
	int in;
	cin>>in;
}