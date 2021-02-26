
#include <cstdlib>
#include <iostream>
#include <fstream>
// operatorul de citire >> din Baza, apelat in operatorul din clasa derivat D
using namespace std;

class B
{int a;
public: friend istream & operator >>(istream & i,B & ob);


};
class D: public B
{int c;
public: friend istream & operator >>(istream & i,D & d);

};

istream & operator >>(istream & i,B & ob)
{i>>ob.a; cout<<"B";return i;}

istream & operator >>(istream & i,D & d)
{ // i>>d.a; //este inaccesibil
    B &rb=d; i>>rb; // apelez operatorul de citire pentru baza printr-o referinta la baza
    i>>((B&) d); /*alta varianta - apelez operatorul de citire pentru baza convertind 
                 obiectul la baza (operatorul de conversie trebuie sa intoarca rezultatul prin referinta, 
                 altfel va intoarce o copie) */
    i>>d.c;
    cout<<"D"; return i;}

int main()
{
    D d;B b;
    cin>>b;cin>>d;
return 0;
}
