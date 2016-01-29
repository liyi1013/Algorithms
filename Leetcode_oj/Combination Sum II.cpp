#include <iostream>
#include <vector>
#include <algorithm> 
#include <iostream>
using namespace std;

void display_vector(const vector<int>& v){
    cout<<"[ ";
    for (int j = 0; j < v.size(); ++j)
        {
            cout<<v[j]<< " ";
        }
    cout<<"]"<<endl;
}

void display_matrix(const vector<vector<int> >& m){
    for (int j = 0; j < m.size(); ++j)
        {
            display_vector(m[j]);
        }
}

class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int>& candidates, int target) {
    	vector<vector<int> > res;
    	if (candidates.size() <= 0 ){
			return res;
		}
        sort(candidates.begin(),candidates.end());
        if (target < candidates[0] ){
        	return res;
        }
        
        return combinationSum_in2(candidates,target);
    }

    vector<vector<int> > combinationSum_in2(vector<int>& cands, int target){
    	vector<vector<int> > res;
    	for (int i = 0; i < cands.size(); ++i)
    	{
            int target_d=target-cands[i];
    		
            if(target_d==0){
    			res.push_back({target});
                //if(i>0&&cands[i]==cands[i-1]){continue;}
    		}
    		else if (target_d>=cands[i])
    		{
    			vector<int>::iterator it = cands.begin();
				for (int k = 0; k <= i; ++k) ++it;
    			vector<int> cands_d(it,cands.end());
                
    			vector<vector<int> > res_d=combinationSum_in2(cands_d,target_d);
                
    			if (!res_d.empty()){
					for (int j = 0; j < res_d.size(); ++j){
						res_d[j].insert(res_d[j].begin(), cands[i]);
						res.push_back(res_d[j]);
					}
				}
			}
    	}
        sort(res.begin(),res.end());
        res.erase( unique(res.begin(), res.end() ), res.end() );
        //cout<<target<<" <-";display_matrix(res);cout<<endl;
    	return res;
    }
};

int main() {
	Solution s;
	vector<int> v={14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12};
    //int a,target;
    //cout<<"input target:";cin>>target;
    //cout<<"input candidates:";
    //while(cin>>a){
     //   v.push_back(a);
    //}

	vector<vector<int> > res=s.combinationSum2(v,27);
    
	cout<<"res= "<<endl;
    display_matrix(res);
    v={10,1,2,7,6,1,5};
    res=s.combinationSum2(v, 8);
    
    cout<<"res= "<<endl;
    display_matrix(res);
	return 0;
}
