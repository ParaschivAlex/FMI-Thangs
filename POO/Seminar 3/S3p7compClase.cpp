#include <cstdlib>
#include <iostream>
using namespace std;
// exemplu pentru compunere clasa sir si clasa Persoana care are data NumePrenume de tip sir 
class sir /* clasa asemanatoare cu string*/
{
public:
 sir(){}
 sir(const char *){}
 sir(const sir &){}
 sir operator= (sir){return * this;}

};
class Persoana
{sir NumePrenume;
 int varsta;
 public:
 Persoana(): varsta(0){}
 Persoana(sir np, int v):NumePrenume(np),varsta(v){}
 /* constr copiere dat de compilator apeleaza constr de copiere pt date mb iar varsta se copiaza bit cu bit */
 /* op = dat de compilator apeleaza op = pt date mb */
};

class Student
{ sir NumePrenume;
  float * medii;
  int nrMedii;
public:
  Student(sir np="",int nm=10 ): NumePrenume(np),nrMedii(nm) /* apel constructor de initializare din baza */
   {medii= new float [nm];}
  Student(const Student & s): NumePrenume(s.NumePrenume),nrMedii(s.nrMedii) /* apel constructor de copiere*/
   {medii=new float [nrMedii];
    for(int i=0;i<nrMedii;i++) medii[i]=s.medii[i];
   }
  Student operator = (Student s)
   {NumePrenume=s.NumePrenume;
	nrMedii=s.nrMedii;
	medii=new float [nrMedii];
    for(int i=0;i<nrMedii;i++) medii[i]=s.medii[i];
    return *this;
    }
};
int main()
{ Persoana X("Ion",10);
  Student Y("Ion", 3);
}

