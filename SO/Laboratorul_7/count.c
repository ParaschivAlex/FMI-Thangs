#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <pthread.h>
#define MAX_RESOURCES 5

pthread_mutex_t mtx;///mutex-ul e declarat global pentru a fi accesibil tuturor firelor de executie
int available_resources=MAX_RESOURCES;///nr maxim de resurse dat

int decrease_count(int count)///cand un thread doreste sa obtina un numar de resurse acesta apeleaza decrease_count
{
    pthread_mutex_lock(&mtx);///blochez zona pentru a nu intra in executie mai mult de un singur thread

    if(available_resources<count)
    {
        pthread_mutex_unlock(&mtx);///deblochez zona ca sa obtin mai multe resurse
        return -1;
    }
    else
    {
        available_resources-=count;
    }

    pthread_mutex_unlock(&mtx);///deblochez zona daca am terminat pentru urmatorul thread

    return 0;
}

int increase_count(int count)///cand resursele nu-i mai sunt necesare apeleaza increase_count
{
    pthread_mutex_lock(&mtx);

    available_resources+=count;

    pthread_mutex_unlock(&mtx);

    return 0;
}

void * fct(void *v)///functie pentru thread-uri
{
    int count=rand()%(MAX_RESOURCES + 1);
    if(decrease_count(count)==0)
    {
        printf("Got %d resources %d remaining\n",count,available_resources);
        increase_count(count);
        printf("Released %d resources %d remaining\n",count,available_resources);
    }
    else
        printf("Nu s-au putut atinge %d resurse\n", count);
}

int main()
{
    pthread_t thr[7];///vector de 7 thread-uri (available_resources+2)
    int i,count;

    printf("MAX_RESOURCES=%d\n", available_resources);

    if(pthread_mutex_init(&mtx,NULL))///creez mutex-ul
    {
        perror(NULL);
        return errno;
    }

    for(i=0; i<7; i++)
    {
        if(pthread_create(&thr[i], NULL, fct, NULL))///creez un thread nou, initializand thr cu noul fir de executie lansat de functia si dand argumentul count
        {
            perror("Nu s-a putut crea thread-ul.\n");
            return errno;
        }
    }

    for(i=0; i<7; i++)
    {
        if(pthread_join(thr[i], NULL)) ///asteapta finalizarea executiei unui thread
        {
            perror("Eroare.\n");
            return errno;
        }
    }

    pthread_mutex_destroy(&mtx);///distrug mutex-ul pt ca nu mai este nevoie de el, eliberand resursele ocupate

    return 0;
}
