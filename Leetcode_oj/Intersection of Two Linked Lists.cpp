#include<iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
      int len_A=0;
      int len_B=0;
      ListNode a=headA;
      ListNode b=headB;
      while(a){
	  a=a.next;
	  ++len_A;
      }
      while(b){
	  b=b.next;
	  ++len_B;
      }
      int d=len_A-len_B;
      if(d>=0){
	for(int i=0;i<d;++i){
	    headA=headA->next;
	}
	while(headA && headB){
	    if(headA==headB){
		return headA;}
	    else{
		headA=headA->next;
		headB=headB->next;
	    }
	}
      }
      else{
	  for(int i=0;i<(-d);++i){
	      headB=headB->next;
	  }
	  while(headA && headB){
	      if(headA==headB){
		  return headA;}
	      else{
		  headA=headA->next;
		  headB=headB->next;
	      }
	  }
      }
      return headA;
    }
};

int main(){
  Solution s;
  s.getIntersectionNode();
}
