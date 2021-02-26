#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <pthread.h>
#include <semaphore.h>

pthread_mutex_t mtx;///pentru contorizarea firelor aflate la bariera
sem_t sem;///pentru a astepta la bariera
int S,max_thr_number;

void init(int N)
{
    max_thr_number=N;
    S=0;
    if(sem_init(&sem, 0, S))///initializez semaforul cu valoarea lui S
    {
        perror(NULL);
        return errno;
    }
}

void barrier_point()
{
    int i,aux;
    pthread_mutex_lock(&mtx);
    S++;
    pthread_mutex_unlock(&mtx);
    aux=S;
    if(aux<max_thr_number)///scade valoarea cu o unitate,iar daca e 0, asteapta sa fie mai intai incrementata
    {
        if(sem_wait(&sem))
        {
            perror(NULL);
            return errno;
        }
    }
    else
    {
        for(i=0; i<max_thr_number; ++i)
            sem_post(&sem);///creste valoarea cu 1 si verifica daca sunt thread-uri blocate la semafor, eliberandu-l pe cel care asteapta de cel mai mult timp
    }
}

void * tfun(void *v)///functia executata de fiecare fir
{
    int *tid=(int *)v;

    printf("%d reached the barrier\n",*tid);
    barrier_point();
    printf("%d passed the barrier\n",*tid);

    free(tid);
    return NULL;
}

int main()
{
    pthread_t thr[10];///vector de thread-uri
    int N=5,i;
    init(N);

    if(pthread_mutex_init(&mtx,NULL))///creez mutex-ul
    {
        perror(NULL);
        return errno;
    }

    for(i=0; i<N; i++)
    {
        int *k=(int *)malloc(1);
        *k=i;
        if(pthread_create(&thr[i], NULL, tfun, k))
        {
            perror(NULL);
            return errno;
        }
    }

    for(i=0; i<N; i++)
    {
        if(pthread_join(thr[i], NULL))
        {
            perror(NULL);
            return errno;
        }
    }


    sem_destroy(&sem);///eliberez resursele
    pthread_mutex_destroy(&mtx);

    return 0;
}
