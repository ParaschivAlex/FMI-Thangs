/**Executie: cc strrev.c -o strrev -pthread
Firele de executie(ale aceluiasi proces) impart resursele si vad modificarile
facute in spatiul procesului de oricare dintre ele, fara a fi nevoie de o structura
intermediara (ca la fork).**/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *strrev(char *str)
{
    char *sir_invers;
    int i, lg = strlen(str);
    sir_invers = malloc(lg + 1);
    for (i = 0; i < lg; i++)
        sir_invers[lg - 1 - i] = str[i];
    sir_invers[lg] = '\0';
    return sir_invers;
}

void *invers(void *v)
{
    char *sir =(char *) v;
    char *sir_invers = strrev(sir);
    return sir_invers;
}

int main(int argc, char *argv[])
{
    pthread_t *threaduri_create;
    char  *result;
    if (argc < 2)
    {
        puts("./rev sir1 sir2...");
        return -1;
    }
    threaduri_create = malloc((argc - 1) * sizeof(pthread_t));

    for (int i = 1; i < argc; i++)
    {
        pthread_create(&threaduri_create[i - 1], NULL, invers, argv[i]);///creez un thread nou, initializand fiecare thread cu noul fir de xecutie lansat de functia invers, ofering argumentul argv[i]
    }

    for (int i = 0; i < argc - 1; i++)
    {
        pthread_join(threaduri_create[i], &result);///asteapta finalizarea executiei unui thread(in mod implicit, nu poate fi alt thread)
        printf("%s\n", result);
        free(result);///dezaloc memoria
    }

    return 0;
}

