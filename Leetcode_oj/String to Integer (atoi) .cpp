#pragma once
#include <iostream>
using namespace std;

int My_atoi(char* str);

int main(){
	cout << INT_MAX<<endl;
	cout << INT_MIN << endl;

	char a[] = " -2147483642   k";
	cout<<My_atoi(a)<<endl;
	return 0;
}


int My_atoi(char* str)
{
	int sign = 1;           // ����
	int current��number = 0;// ��ǰ����
	int i = 0;              // �ַ�����

	while (str[i] == ' ') { ++i; }  // �����ո�

	if (str[i]=='-')     { sign = -1; ++i; }  // �жϷ���
	else if(str[i]=='+') { ++i; }

	while (str[i] >= '0' && str[i] <= '9') {  // ��ʾ��������Ҫ�ӵ������
		int current_digit = str[i] - '0';
		if (current��number > INT_MAX / 10 || (current��number == INT_MAX / 10 && current_digit > 7))
		{
			if (sign == 1) { return INT_MAX; }
			else           { return INT_MIN; }
		}
		current��number = 10 * current��number + current_digit;
		++i;
		//cout << current��number << endl;
	}
	return current��number * sign;
}