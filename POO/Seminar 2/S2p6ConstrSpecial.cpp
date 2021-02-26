#include <iostream>
using namespace std;
//cazuri speciale pt apel constructori
class C{
public: C(int i=0){cout<<"constructor de initializare "<<endl;}
C(const C& c){cout<<"constructor de copiere "<<endl;}
	};

	void f1(C o){cout<<"transmitere parametru prin valoare"<<endl;}
	C f2(){cout<<"intoarcere rezultat prin valoare "<<endl;return 1;}
	void f3(const C & o){cout<<"transmitere parametru prin referinta "<<endl;}
    const C& f4(){cout<<"intoarcere rezultatprin referinta "<<endl;return 1;}
int main() {
	f1(1);/* se apeleaza constructorul de initializare -din int se construieste obiectul parametru */
	f2(); /* se apeleaza constructorul de initializare -din int se construieste obiectul parametru */
	f3(1);/* desi e transmitere prin ref -se apeleaza constructorul de initializare care din int creaza obiectul parametru */
	f4(); /* desi e intoarcere prin ref -se apeleaza constructorul de initializare care din int creaza obiectul parametru */
	return 0;
}
