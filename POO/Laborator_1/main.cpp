/*
0).

#include <iostream>

using namespace std;

class Suma
{
    public:
    long long int a;
    long long int b;
};

int main()
{
    Suma x;
    cin>>x.a>>x.b;
    cout<<x.a+x.b;
    return 0;
}
*/

/*
0).

#include <iostream>

using namespace std;

int main()
{
    long long int a,b,c;
    cin>>a>>b;
    c=a+b;
    cout<<c;
    return 0;
}
*/




/** \brief
 *
 * \param
 * \param
 * \return
 *
 */

//1).
#include <iostream>

using namespace std;

bool perfect(long long int x)
{
    long long int s=0;
    for(long long int i=1;i<=x/2;i++)
        if (x%i==0)
            s+=i;
    if (s==x)
        return 1;
    return 0;
}

int main()
{
    long long a, b;
    cin>>a>>b;
    long long int s=0;
    for (long long int i=a; i<=b;i++)
        if (perfect(i)==1)
            s+=i;
    cout<<s;
    return 0;
}
*/

/*
#include <iostream>

using namespace std;

class Reteta
{
public:

};

class cerc: public Reteta
{
    public:
        int r;
        int h;


};

int main()
{
    int n, forme[101], suma[101];
    cin>>n; /// n forme de copt
    for (int i=1; i<=n; i++)

        return 0;
}
*/
