#include<iostream>
#include<string>
#include<vector>
using namespace std;
void f(string &s){
	vector<string> vs; 
	string temp="";//=new string;
	int i=0;
	while(s[i]!='\0'){             //����ֱ����β 
		if (s[i]==' '){            //��������� �����ո�
			if (!temp.empty())
				vs.push_back(temp);//�����ʷ���������
			++i;                   // �����ո� 
			temp="";//new string;  //�½�һ�����ַ��� 
		}
		else{
			temp.push_back(s[i]); //����ĸ�ӵ�temp�ַ������� 
			++i;
		}
	}
	if (!temp.empty())
		vs.push_back(temp);       //����󵥴ʷ���������

	int len=vs.size();            //����������������ʾ���� 
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
