#include<iostream>
#include<limits>
using namespace std;
int main ()
{
	//Memory Size used by various Datatypes int,float,bool & char
	cout<<"size of int in bytes :"<<sizeof(int)<<endl;
	cout<<"size of float in bytes :"<<sizeof(float)<<endl;
	cout<<"size of bool in bytes:"<<sizeof(bool)<<endl;
	cout<<"size of char in bytes:"<<sizeof(char)<<endl;
	//Maximum and Minimum possible values of int
	cout<<"The Max value of int:";
	std::cout<<std::numeric_limits<int>::max();
	cout<<endl;
	cout<<"The Min value of int:";
	std::cout<<std::numeric_limits<int>::min();
	cout<<endl;
	//Maximum and Minimum possible values of float
	cout<<"The Max value of float:";
	std::cout<<std::numeric_limits<float>::max();
	cout<<endl;
	cout<<"The Min value of float:";
	std::cout<<std::numeric_limits<float>::min();
	cout<<endl;
	//Maximum and Minimum possible values of long int
	cout<<"The Max value of long int:";
	std::cout<<std::numeric_limits<long int>::max();
	cout<<endl;
	cout<<"The Min value of long int:";
	std::cout<<std::numeric_limits<long int>::min();
	cout<<endl;
	return 0;
}
	

