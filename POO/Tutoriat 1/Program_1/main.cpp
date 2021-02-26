#include <iostream>

using namespace std;

int main()
{
    /**int a=3;
    int *p=&a;*/

    //--------------------------------------------------------------------//

    /**int*v;
    *v=3;
    *(v+1)=5;
    *(v+2)=6;
    cout<<v[0]<<' '<<v[1]<<' '<<v[2];*/

    //--------------------------------------------------------------------//

    /**
    int*p= new int;//doar 4 octeti
    int *v=new int[50];//50 de blocuri de 4 octeti
    int *k=new int(50);//initializeaza cu 50
    cout<<p<<' '<<k<<' '<<v;
    */

    //--------------------------------------------------------------------//

    /**
    int nrlinii=3;
    int nrcoloane=3;
    int **m=new int*[nrlinii];//matrice alocata dinamic
    for (int i=0;i<nrlinii;++i)
        m[i]=new int[nrcoloane];
    cout<<m;
    ///Accesare m[i][j]=*(*(m+i)+j)
    */

    //--------------------------------------------------------------------//
    /**                                 STL                               */
    /**                   _size()=intoarce nr de elemente                 */
    //--------------------------------------------------------------------//

    /**

    Vector:   #include <vector>
              vector<int>v;  <==> int v[--]; <==> vector<int>v(5)

    _push_back(x); declarare metoda de adaugat
    v.push_back(3); accesare metoda, insereaza la sfarsitul lui v

    _popback(); declarare metoda de stergere de la final
    v.popback(); sterge ultima valoarea a lui v

    _erase(iterator 1, interator 2); iterator = element care pointeaza la o adresa de mem. din vect.

    vector<int>v(  5  ,  2 );
                  size, init

    v.erase(v.begin()+2,v.end()); sterge elementele de pe poz 2,3,4,5.
    v.begin() intoarce un vector catre pozitia 0



    {
    vector<int>::iterator it;
    for(it=v.begin();it<v.end();it++)
    }
    -----------SAU----------
    {
    for(auto it=v.begin();it<.....)
        cout<<*it;
    }


    #include<algorithm>
    sort(v.begin(),v.end()); sortare crescatoare

    bool cmp(int a, int b)
    {
    return a>b;   descrescator
    }
    sort(v.begin(),v.end(),cmp);

    */
    //--------------------------------------------------------------------//
    /**                              STRING                               */
    //--------------------------------------------------------------------//
    /**

    string//char[50];
    string a="abcdBabef";
    a.size();//a.length();

    int poz=a.find_first_of("ab",a.begin()+3);//5

    if(poz!=string::npos) ----> daca substringul a fost gasit
        {....}

    a.substr(3, 3); pozitia de inceput, nr de caractere
    |
    |-->"dBa"

    */
    //--------------------------------------------------------------------//
    /**                               MAP                                 */
    //--------------------------------------------------------------------//
    /**

    map <cheie, valoare>
    map <string, int> m;   ///// declarare

    m.insert({cheie,valoare}); // m.insert({"ab",3})
    cout<<m["ab"]; // 3

    m["cd"]=7;

    */
    //--------------------------------------------------------------------//
    /**                               PAIR                                */
    //--------------------------------------------------------------------//
    /**

    pair<string,int>p;

    p={"ab",3};
    p=make_pair("ab",3) --->cout<<p.first<<p.second;


    */
    return 0;
}
