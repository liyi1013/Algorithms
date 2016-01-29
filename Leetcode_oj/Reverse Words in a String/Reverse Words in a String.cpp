#include<iostream>
#include<string>
#include<vector>
using namespace std;
void f(string &s){
	vector<string> vs; 
	string temp="";//=new string;
	int i=0;
	while(s[i]!='\0'){             //遍历直到结尾 
		if (s[i]==' '){            //如果遇到‘ ’（空格）
			if (!temp.empty())
				vs.push_back(temp);//将单词放入容器中
			++i;                   // 跳过空格 
			temp="";//new string;  //新建一个空字符串 
		}
		else{
			temp.push_back(s[i]); //将字母加到temp字符串后面 
			++i;
		}
	}
	if (!temp.empty())
		vs.push_back(temp);       //将最后单词放入容器中

	int len=vs.size();            //后续遍历容器，显示单词 
	string res="";
	for(int j=0;j<len;++j){
		res.append(vs[len-j-1]);
		if(j!=len-1)
			res.push_back(' ');
	}
	s=res;
}

int main(){
	string s;
	getline(cin,s);
	//string ss=
	f(s);
	cout<<endl<<s<<endl<<s.length()<<endl;
	
	string test="abc";
	cout<<test.length();
}
