#include <unistd.h>
#include <stdio.h>
#include <pthread.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>

int a[100][100], b[100][100];
int n,m,p;

void * produs_matrici(void *v)
{
    int *elem=(int *)v;
    int *rez=(int*)malloc(sizeof(int));
    int i;
    for(i=1;i<=p;i++)
    {
        rez[0]+=a[elem[0]][i]*b[i][elem[1]];
    }
    return rez;
}

int main(int argc, char *argv[])
{
    pthread_t *thread=malloc((argc-1)*sizeof(pthread_t));///vector de thread-uri
    int i,j;
    int index=0;///index pt elemente

    printf("Matricea 1:\n");
    printf("Introduceti nr de linii al primei matrice: ");
    scanf("%d",&m);
    printf("Introduceti nr de coloane al primei matrice: ");
    scanf("%d",&p);
    for(i=1; i<=m; i++)
        for(j=1; j<=p; j++)
        {
            printf("a[%d][%d]= ",i,j);
            scanf("%d",&a[i][j]);
        }
    printf("\n");
    printf("Matricea 2:\n");
    printf("Introduceti nr de coloane al celei de-a doua matrice: ");
    scanf("%d",&n);
    for(i=1; i<=p; i++)
        for(j=1; j<=n; j++)
        {
            printf("b[%d][%d]= ",i,j);
            scanf("%d",&b[i][j]);
        }
    int c[m][n];

    for(i=1;i<=m;i++)
    {
        for(j=1;j<=n;j++)
        {
            int *v=(int*)malloc(2*sizeof(int));///vector alocat dinamic cu 2*sizeof(int) pentru a putea memora si linia si coloana curenta
            v[0]=i;
            v[1]=j;
            if(pthread_create(&thread[index], NULL, produs_matrici, v))
            {
                perror(NULL);
                return errno;
            }
            index++;///trecem la urmatorul element
        }
    }

    index=0;///luam elementele iar de la 0
    for(i=1;i<=m;i++)
    {
        for(j=1;j<=n;j++)
        {
            int *rezultat=(int*)malloc(sizeof(int));///alocam memorie pentru fiecare rezultat int c[i][j]
            if(pthread_join(thread[index],&rezultat))
            {
                perror(NULL);
                return errno;
            }
            c[i][j]= *rezultat;///c[i][j] ia valoarea rezultatului returnat de functia produs_matrici
            index++;///trecem la urmatorul element
        }
    }

    printf("\n");
    printf("Matricea rezultata din produsul celor 2 matrice este:\n");
    for(i=1;i<=m;i++)
    {
        for(j=1;j<=n;j++)
            printf("%d ",c[i][j]);
        printf("\n");
    }

    return 0;
}
