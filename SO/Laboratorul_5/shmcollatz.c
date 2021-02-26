#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>

int main(int argc, char *argv[])
{
    char shm_name[]= "shmcollatz";///numele memoriei partajate
    int shm_fd;///este descriptorul pe care il folosim pentru manipularea obiectelor
    char *adresa_fisier=NULL;
    pid_t child;
    int n, v[101], i;

    shm_fd=shm_open(shm_name, O_CREAT|O_RDWR, S_IRUSR | S_IWUSR);///creez obiectul de memorie partajata. Daca exista, proprietarul are drepturide citire/scriere, altfel se creeaza un obiect cu aceste drepturi
    if(shm_fd<0)
    {
        perror(NULL);
        return errno;
    }

    size_t page_size=getpagesize();///functia returneaza nr de bytes al unei pagini, unde pagina este o dimensiune fixa, unitatea de masura folosita de mmap pt alocari de memorie sau pt file mapping
    size_t shm_size=page_size*argc;///fiecare copil va avea acces la cate o "pag" din memoria partajata
    if(ftruncate(shm_fd,shm_size)==-1)///ftruncate mareste sau micsoreaza MP in functie de dimensiunea pe care o dam
    {
        perror(NULL);
        shm_unlink(shm_name);///sterg memoria creata cu shm_open, in caz de eroare
        return errno;
    }

    for(i=1; i<argc; i++)
        v[i]=atoi(argv[i]);

    printf("Starting parent %d\n",getpid());

    for(i=1; i<argc; i++)
    {
        adresa_fisier=mmap(0,shm_size,PROT_WRITE,MAP_SHARED,shm_fd,(i-1)*page_size);///indica catre catre o parte din MP care incepe de la bite-ul (i-1)*page_size din zona de memorie aferenta descriptorului shm_fd
        if (adresa_fisier == MAP_FAILED)
        {
            perror(NULL);
            shm_unlink(shm_name);
            return errno;
        }
        child = fork();
        n = v[i];
        adresa_fisier+=sprintf(adresa_fisier, "%d: %d ", n, n);///incarc in zona de memorie nr din ipoteza collatz
        if(child == -1)
            return errno;
        else if(child == 0)
        {
            while(n > 1)
            {
                if(n%2==0)
                    n=n/2;
                else
                    n=3*n+1;
		adresa_fisier+=sprintf(adresa_fisier, "%d ", n);
            }
            printf("Done Parent %d Me %d\n",getppid(),getpid());
            return 1;
        }
        munmap(adresa_fisier, page_size);///nu mai am nevoie de zona de memorie incarcata
    }

    for(i=1; i<argc; i++)
        wait(NULL); ///parintele asteapta sa termine toti copiii

    for (i=1; i<argc; i++)
    {
        adresa_fisier=mmap(0, page_size, PROT_READ, MAP_SHARED, shm_fd, (i-1)*page_size);
		printf("%s\n", adresa_fisier);
		munmap(adresa_fisier, page_size);
    }

    printf("Done Parent %d Me %d\n",getppid(),getpid());

    shm_unlink(shm_name);

    return 0;
}
