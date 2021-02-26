/* clasa similara string pt problemele aparute la alocare dinamica*/
#include <iostream>
#include <string.h>
using namespace std;
/*
class sirs{char v[10];};
//clasa cu alocare statica -constructorul de copiere si operatorul de atribuire functioneaza corect
 // -copiere bit cu bit
*/
class sir
{char *p;
public:
 sir(const char * c=""); /* sau 1 constructor fara parametru  si 1 constructor cu parametru */
 sir(const sir& s);
// fara & -se apeleaza recursiv la infinit  constructorul de copiere !!
//fara const nu se poate apela pentru obiecte constante sau temporare (ex: cele intoarse prin valoare)
/* -operator e o functie cu simbol si forma de apel speciala -prefixat,infixat sau postfixat
     - trebuie pastrat numarul de operanzi
     - poate transmite parametrii prin valoare sau referinta si poate intoarce rezultatul prin valoare sau referinta
     - se pot supraincarca prin
        functii exterioare (nr parametrii =nr de operanzi) sau
        metode (primul operand este obiectul care apeleaza metoda si restul operanzilor =parametrii)
*/

friend  sir operator + (sir s1, sir s2);
// functie exterioara cu acces la datele private si protejate ale clasei
   //se declara dreptul de friend in clasa si se defineste in afara clasei
//sir & operator +(const sir & s2);  //nu pot exista ambii operatori -ambiguitate la apelul s1+s2
//primul operand=obiectul implicit, al doilea operand=parametrul

 sir operator=(sir s);
 ~sir();
 friend istream& operator>>(istream &i, sir& s);
 friend ostream& operator <<(ostream &o, const sir& s);

};
sir::sir(const char* c)
{ p=new char[strlen(c)+1];
  strcpy(p,c);
}
sir::sir(const sir& s)
{p=new char[strlen(s.p)+1];
 strcpy(p,s.p);
}
sir operator+(sir s1,sir s2)
{sir l;
 delete[]l.p;
 l.p=new char[strlen(s1.p)+strlen(s2.p)+1];
 strcpy(l.p,s1.p);
 strcpy(l.p, s2.p);
 return l;
}
/*
sir & sir::operator + (const sir & s2)
{sir *pl=new sir;
 delete [] pl->p;
 pl->p=new char[strlen(p)+strlen(s2.p)+1];
 strcpy(pl->p,p);
 strcpy(pl->p, s2.p);
 return *pl;
}*/
sir sir::operator=(sir s)
{/* daca s e transmis prin referinta -doar daca strcmp(s.p,p)!=0 sau this!=&s
 altfel la operatia s1=s1 se pierde adresa sirului de caractere
 operatia s1=s1 se poate face ca rezultat al unei operatii s1=min(s1,s2)
*/
delete[]p;
p=new char[strlen(s.p)+1];
strcpy(p,s.p);
return *this;
}
/*
sir& sir::operator+(sir &s) //mai eficient
{ sir *pl=new sir;
 pl->p=new char[strlen(p)+strlen(s.p)+1];
 strcpy(pl->p,p);
 strcat(pl->p,s.p);
 return *pl
}
*/
sir::~sir()
{ delete[]p;
}
istream& operator>>(istream& i, sir& s)
{ char v[100];
 i>>v;
 delete[]s.p;
 s.p=new char[strlen(v)+1];
 strcpy(s.p,v);
 return i;
}
ostream& operator<<(ostream& o, const sir& s)
{o<<s.p;
 return o;
}
int main()
{ sir s1,s2("ab"),s3(s2),s4=s2;
   s1=s2;
   s1=s2+s3;
   cin>>s1;
   cout<<s1;

    return 0;
}
